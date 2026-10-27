---
title: 'LoopFold: Parallelizing Recurrent Depth in Looped Transformers'
title_zh: LoopFold：循环Transformer的循环深度并行化方法
authors:
- Feichen Song
- Boyi Zeng
- Yiqin Hao
- Shixiang Song
- He Li
- Yizhou Yang
- Zitong Wang
- Yifan Liu
- Ziwei He
- Zhouhan Lin
affiliations:
- Shanghai Jiao Tong University
- Sun Yat-sen University
- Shanghai Innovation Institute
arxiv_id: '2610.35556'
url: https://arxiv.org/abs/2610.35556
pdf_url: https://arxiv.org/pdf/2610.35556
published: '2026-10-26'
collected: '2026-10-27'
category: LLM
direction: 大语言模型 · 循环Transformer推理加速
tags:
- Looped-Transformers
- Decoding-Optimization
- Parallel-Inference
- KV-Cache
- Low-Latency
one_liner: 通过轻量预测校正机制并行化循环Transformer多步深度计算，降解码延迟同时提升模型精度
practical_value: '- 业务中使用循环Transformer做电商Agent推理、生成式推荐文案生成时，可直接复用LoopFold的预测-校正并行架构，在不损失效果的前提下降低大深度迭代的解码延迟，提升用户交互体验

  - KV缓存优化策略可直接迁移到所有多轮迭代Transformer的推理场景：复用首轮KV+仅更新最近64个token位置，可降低28.6%的KV存储开销，精度损失控制在可接受范围

  - 仅用最终预测损失联合优化全模块的训练方案，不需要额外构造监督信号，落地成本极低，适合业务场景快速迭代适配'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
循环Transformer通过复用同一块主干多次迭代提升固定参数量下的模型效果，但迭代的串行依赖导致深度越大解码延迟越高，现有并行方案（如PLT）深度加大后精度边际收益快速衰减，难以同时兼顾效果和latency。

### 方法关键点
- 轻量预测器：基于首轮迭代的隐状态变化量，线性外推后续多步迭代的输入，让多步迭代可并行批处理
- 校正模块：每轮并行计算后，用已完成的前序迭代真实结果，通过线性映射修正后续迭代的输出误差
- 训练策略：所有模块仅用最终的下一词预测损失联合训练，预测/校正层初始化为单位矩阵，收敛难度低
- KV缓存优化：提供两种缓存复用策略，将多轮独立KV缓存从7倍降至5倍，仅损失极小精度

### 关键实验
用1.4B参数LLaMA风格模型在Pile数据集训练，对比vanilla循环Transformer、PLT、Hidden Decoding等基线：
- 深度D=9时，比9轮vanilla循环模型解码延迟降低46%，8项零样本任务平均精度提升2.2个百分点到56.38%
- 相同训练算力、相同解码延迟下，PPL和零样本精度均优于所有基线
- 批量解码时吞吐量稳定为vanilla模型的1.6倍以上

### 核心结论
循环深度和串行解码深度不需要强绑定，额外的迭代计算可以通过预测校正转移到并行维度，在不增加延迟的前提下提升模型效果。
