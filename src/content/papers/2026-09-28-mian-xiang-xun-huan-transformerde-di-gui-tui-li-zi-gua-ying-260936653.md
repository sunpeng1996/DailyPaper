---
title: Scheduling Recursive Reasoning in Looped Transformers
title_zh: 面向循环Transformer的递归推理自适应调度方法
authors:
- Boyuan Wang
- Chengyao Yu
- Jiaxi Ren
- Hongxin Wei
- Bingyi Jing
- Yuxin Tao
affiliations:
- Southern University of Science and Technology
- The Chinese University of Hong Kong, Shenzhen
- Shenzhen Loop Area Institute
arxiv_id: '2609.36653'
url: https://arxiv.org/abs/2609.36653
pdf_url: https://arxiv.org/pdf/2609.36653
published: '2026-09-28'
collected: '2026-10-01'
category: LLM
direction: LLM推理优化 · 循环Transformer自适应调度
tags:
- Looped Transformer
- Recursive Reasoning
- Adaptive Scheduling
- Inference Optimization
- TAPS
one_liner: 推出轨迹自适应调度器TAPS，无需重训即可提升循环Transformer推理精度与速度
practical_value: '- 做Agent多步思考、生成式推荐多轮结果refine、RAG多轮召回这类业务时，可直接复用TAPS的步长调度逻辑，无需修改模型权重，仅通过隐状态更新轨迹统计量动态调整步长，即可在不损失精度的前提下提升推理效率

  - 微调带循环推理逻辑的业务模型（比如用户意图推理、商品多属性匹配模型）时，可复用论文的训练协同优化loss，添加「波动超过进度的惩罚项」正则，让模型动态更适配自适应调度，进一步提升推理速度

  - 对现有开源LLM的中间层循环、全模型循环等递归推理场景，可将TAPS封装为推理侧通用插件，兼容自适应退出、并行推理等现有策略，实测同精度下最高可获1.56x速度提升'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有循环Transformer类递归推理模型均采用固定单位步长更新隐状态，更新持续正向时步长偏保守会浪费算力，更新波动大时步长过激进又会导致结果偏移，额外循环的收益被严重限制；且推理时无法获取最终任务损失信号，难以动态调整步长，亟需不依赖标签的自适应调度方案。

### 方法关键点
- 理论推导证实终端损失对循环更新步长的敏感性可精确分解为持续进度项和中心波动项，步长调整只需平衡这两个可从推理轨迹直接观测的统计量，无需下游任务标签
- 轨迹自适应进度-波动调度器TAPS通过EMA追踪历史更新的一阶矩（表征持续进度）和二阶矩（表征波动幅度），动态计算每步缩放系数η：进度占优时放大步长加速收敛，波动占优时缩小步长保证稳定性，全程无需重训模型
- 支持训练-推理协同优化，训练时在loss中添加「波动超过进度」的惩罚项，引导模型学习更稳定的循环动态，进一步放大自适应调度的收益

### 关键结果
在Sudoku、Maze结构化推理任务，Ouro、Huginn、Qwen3等循环LLM的MMLU、GSM8K等通用推理任务上测试，对比固定单位步长baseline：仅推理侧接入TAPS，Sudoku精度从89.67%提升至90.19%，推理速度最高1.042x；加入训练协同优化后，Maze精度从78.80%提升至79.90%，同精度下推理速度最高达1.56x；可适配自适应退出、分层循环、并行推理等所有主流循环推理策略，在Qwen3-4B的中间层循环场景下平均精度额外提升0.15个百分点。

最值得记住的一句话：循环推理的优化维度除了架构设计和迭代次数外，更新步长是第三个独立控制轴，无需重训的轨迹自适应调度可同时实现精度与推理速度的双重提升。
