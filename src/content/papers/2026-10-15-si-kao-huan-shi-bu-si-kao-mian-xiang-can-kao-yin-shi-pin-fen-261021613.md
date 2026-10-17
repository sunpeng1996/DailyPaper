---
title: 'To Think or Not to Think: Pre-Decisional Reasoning Budgets for Referring Audio-Visual
  Segmentation'
title_zh: 思考还是不思考：面向参考音视频分割的预决策推理预算机制
authors:
- Haojie Hu
- Senda Chen
- Ying Shen
- Lin Zhang
affiliations:
- Tongji University
- IEIT SYSTEMS (Beijing) Co., Ltd.
arxiv_id: '2610.21613'
url: https://arxiv.org/abs/2610.21613
pdf_url: https://arxiv.org/pdf/2610.21613
published: '2026-10-15'
collected: '2026-10-17'
category: Reasoning
direction: 多模态推理 · 自适应CoT优化
tags:
- Chain-of-Thought
- Adaptive Reasoning
- Multimodal LLM
- Routing
- Efficiency Optimization
one_liner: 发现多模态推理过度思考陷阱，基于预生成启动态实现自适应CoT路由降本提效
practical_value: '- 做Agent推理路由时，可复用预生成启动态作为特征训练轻量线性探针，比文本特征、不确定性代理信号的路由准确率更高，无额外多轮推理开销

  - 业务场景中可抛弃「CoT越长效果越好」的固有认知，对简单query跳过长推理步骤，可减少60%左右token消耗同时保留96%以上性能，平衡推理成本和效果

  - 做生成式推荐/多模态商品理解的自适应推理时，可参考五折交叉验证构造反事实推理预算标签的方案，标注不同query的最优推理长度，降低标注成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有多模态系统普遍默认越长的CoT推理对下游任务效果越好，但在参考音视频分割（Ref-AVS）任务中存在「过度思考陷阱」：简单query使用长推理会出现短语、定位漂移导致效果下降，仅歧义query能从多步推理中获益，亟需低成本自适应推理机制。
### 方法关键点
1. 采用五折out-of-fold协议构造反事实推理预算标签，将自适应推理转化为预决策表示问题；
2. 基于第一个token生成前的generation-onset状态训练线性探针，预测是否需要额外推理；
3. 复用onset状态做单前向传播路由，无需额外推理开销。
### 关键结果数字
线性探针二分类推理需求准确率达70.1%，优于文本特征、不确定性代理信号；路由方案减少60%自回归token消耗，同时保留约96%的全量长推理性能，效果优于下游置信度路由，性能接近Short-then-Decide方案但token消耗低得多。
