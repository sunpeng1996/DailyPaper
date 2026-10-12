---
title: 'LapMerge: Differentiable Exact-Budget Token Merging in Linear Time'
title_zh: LapMerge：线性时间可微的精确预算Token合并算子
authors:
- Magdalena Trędowicz
- Aleksandra Nowak
- Tomasz Steifer
- Łukasz Struski
- Szymon Płotka
- Jacek Tabor
affiliations:
- Jagiellonian University in Kraków
- Institute of Fundamental Technological Research, Polish Academy of Sciences
- Centre for Credible AI, Warsaw University of Technology
arxiv_id: '2610.13858'
url: https://arxiv.org/abs/2610.13858
pdf_url: https://arxiv.org/pdf/2610.13858
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: 长序列Token压缩 · 高效推理优化
tags:
- Token Merging
- Efficient LLM
- Long Sequence Modeling
- Differentiable Operator
- Vision-Language Model
one_liner: 提出线性时间可微的有序序列Token合并算子，兼顾精确预算、可微性与高效性，性能优于现有Token缩减方案
practical_value: '- 电商多模态检索/商品详情理解场景，可将LapMerge作为前置Token缩减模块，对长序列商品图文Token做高效压缩，相同预算下精度更高且速度提升25~51倍，大幅降低推理成本

  - 长用户行为序列的召回/排序场景，可复用其拉普拉斯核局部聚合逻辑，对有序行为Token做端到端可微压缩，保留分散的弱用户兴趣信号，避免硬截断/剪枝的信息损失

  - 多模态Agent长上下文理解模块，可直接用score-routed LapMerge替换现有硬Token选择逻辑，无需重训原有VLM即可提升POPE hallucination指标1.58%（10%预算下），零成本升级管线'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有长序列Token压缩方案存在明显缺陷：剪枝会直接丢弃信息，对分散的弱信号敏感；而现有合并方法依赖M×N的Token交互，复杂度随序列长度上升过快，无法同时兼顾精确输出预算、端到端可微、线性计算成本三个核心需求，长序列场景下推理/训练成本过高。

### 方法关键点
- 引入拉普拉斯核为每个有序Token分配质量权重，将累计密度划分为N个等质量段，每段聚合为一个输出Token，无全局Token交互，前后向传播复杂度均为O(M+N)
- 支持精确控制输出Token数量，无需修改算子参数即可调整压缩比例，学习到的质量权重可直接作为Token重要性的可解释路由图
- 提供两种部署模式：标准LapMerge作为可训练组件端到端训练，score-routed LapMerge可直接替换现有Token选择模块，无需重训原有模型

### 关键结果
- 算力测试：在10^7级Token序列下，相比TokenLearner、PatchMerger等池化器速度最高提升2个数量级，M=2^20、N=M/16时纯PyTorch实现仍比现有方案快25~51倍
- 多模态VLM场景：替换Qwen2.5-VL-7B的VisionSelector硬选择模块，无额外训练下POPE F1在10%、30%预算下分别提升1.58、0.45，超越所有同期剪枝/合并基线
- 长序列LRA基准：10%预算下在4/5任务上取得最优精度，甚至超过全序列训练的Transformer模型，Text、Retrieval、Image任务分别领先最强基线2.0、0.8、4.7个百分点

最值得记住的结论：当Token序列存在时空局部性时，基于有序质量划分的局部合并相比全局交互或硬剪枝，可在大幅降低计算成本的同时保留更完整的序列信息，是长序列处理的高性价比方案
