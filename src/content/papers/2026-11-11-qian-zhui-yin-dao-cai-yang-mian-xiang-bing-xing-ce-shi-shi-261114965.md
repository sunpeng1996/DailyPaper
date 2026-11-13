---
title: 'Early Signals, Strong Decisions: Prefix-Guided Sampling for Parallel Test-Time
  Scaling'
title_zh: 前缀引导采样：面向并行测试时扩展的高效LLM推理优化方法
authors:
- Jie Ren
- Jonathan Rosenfeld
- Neil Thompson
affiliations:
- MIT CSAIL
- MIT FutureTech
arxiv_id: '2611.14965'
url: https://arxiv.org/abs/2611.14965
pdf_url: https://arxiv.org/pdf/2611.14965
published: '2026-11-11'
collected: '2026-11-13'
category: LLM
direction: LLM推理 · 测试时扩展效率优化
tags:
- Test-Time Scaling
- Prefix-Guided Sampling
- LLM Inference
- Confidence Score
- Parallel Reasoning
one_liner: 通过短前缀置信度筛选推理路径，在固定计算预算下提升LLM并行测试时扩展的性能与效率
practical_value: '- 落地Agent多路径推理、生成式推荐多候选采样场景时，可直接复用PreG框架：先生成占全长度20%的短前缀做置信度排序，仅保留Top
  30%候选补全，最高可节省80%token成本且效果无损失

  - 工程侧可直接适配现有推理引擎：PreG无需动态停止、跨路径比较逻辑，所有前缀生成可完全并行，实测端到端延迟降低30%，KV cache峰值占用下降约20%，适配高并发线上场景

  - 业务侧做候选筛选时可复用核心结论：决策边界附近的样本即使是弱置信信号，也能通过多路径聚合放大效果，无需等待全路径生成即可做早期过滤，降低不必要计算'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有并行测试时扩展（TTS）方法需生成完整推理路径后才做置信度评估，大量低质量路径的全量生成带来极高冗余计算，token浪费严重，推理成本随采样路径数线性上升，难以落地高并发线上业务。
### 方法关键点
- 理论证明多路径聚合对决策边界附近样本有信号放大效应，仅占全路径20%左右的短前缀的弱置信信号，足够通过聚合影响最终结果
- PreG框架分两步执行：第一步并行生成固定长度k的短前缀，用DeepConf、Self-Certainty等内部置信度排序；第二步仅选Top α比例的前缀补全到完整长度，再聚合输出结果
- 理论推导最优超参数规则：前缀长度k取搜索区间端点即可，过滤比例α建议取0.1~0.3，平衡路径数量和质量
### 关键实验
在Qwen3-8B、Llama-Nemotron-4B两个模型，AIME25等4个数学竞赛数据集、GPQA-D常识数据集上测试，对比Self-Consistency、PRM、各类早期停止基线：
- 固定token预算下，13/15的Qwen配置、14/15的Llama配置下PreG取得最优精度，在CMIMC数据集1000k token预算下，相对基线最高提升5.4%
- 达到相同精度时，27/60配置下可节省50%以上token，最高省80%；多GPU部署时端到端延迟降低30.6%，KV cache峰值占用从93.8%降至74.7%
### 核心结论
短前缀的弱置信信号经多路径聚合可发挥和全路径信号接近的效果，早期筛选是降低LLM推理成本的高性价比路径
