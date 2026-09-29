---
title: Improving Test-Time Scaling with Adaptive Looped Transformers
title_zh: 基于自适应循环Transformer的测试时推理性能优化
authors:
- Yichen You
- Tianyu Fu
- Aosong Feng
- Xingtai Lv
- Xuefei Ning
- Ning Ding
- Yu Wang
affiliations:
- Tsinghua University
- Yale University
arxiv_id: '2609.35748'
url: https://arxiv.org/abs/2609.35748
pdf_url: https://arxiv.org/pdf/2609.35748
published: '2026-09-27'
collected: '2026-09-29'
category: LLM
direction: 大模型推理优化 · 自适应循环Transformer
tags:
- Looped Transformers
- Test-Time Scaling
- Adaptive Computation
- LLM Inference
- SFT
one_liner: 提出TaH2自适应循环Transformer训练框架，用前瞻深度监督提升测试时算力效率与精度
practical_value: '- 电商搜索/推荐场景的query改写、商品文案生成等推理任务，可引入自适应迭代机制：仅对歧义大、复杂度高的query/候选分配更多迭代算力，既提升效果又控制推理成本

  - Agent多轮工具调用/规划场景，可复用前瞻深度监督思路：在线判断当前轮次推理是否还能带来收益，自动停止无价值的迭代，降低端到端延迟

  - 大模型垂直领域微调阶段可复用token-level加权损失设计：对高价值样本/难例分配更高的损失权重，用同等微调成本获得更高的下游任务效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有循环Transformer通过参数复用实现了较高的参数效率，但测试时随输出长度增长的算力-精度缩放表现未被充分研究；现有固定深度循环模型对所有token分配相同迭代次数，超50%的token无法从额外迭代中收益甚至效果下降，已有的自适应退出方案存在训练推理不匹配问题，同等算力下效果不如非循环基线。

### 方法关键点
- 架构包含共享Transformer backbone、输入注入更新器、token级迭代决策器三个模块，新增参数量小于3%
- 采用前瞻深度监督：训练时通过无梯度前瞻迭代计算每个token继续迭代的收益，动态生成在线标签，联合训练backbone和决策器，避免训练推理 mismatch
- 引入停止权重加权的多轮预测结果融合，以及代价敏感的决策器损失，提升迭代决策精度
- 推理时支持最大迭代深度动态配置，通过阈值控制退出时机

### 关键实验
基于Qwen3 1.7B/4B/8B backbone在数学、代码、QA、工具调用4类数据集评测，对比非循环基线、Ouro、Huginn等循环方案：AIME基准上精度-算力斜率较基线提升53%；同等测试时算力下精度超基线3.4个点；最大迭代深度从2提升到8时，增益从2.8个点增长到3.9个点，无性能 plateau。

### 核心结论
循环Transformer的性能瓶颈不在于迭代机制本身，而在于能否自适应地把算力分配给真正能从迭代中收益的token。
