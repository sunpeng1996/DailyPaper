---
title: Deeper Backpropagation or More Updates? Training Looped Language Models Across
  Budgets
title_zh: 不同训练预算下循环语言模型反向传播窗口的最优选择策略
authors:
- Jiarun Shen
- Xiao Li
affiliations:
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2610.38422'
url: https://arxiv.org/abs/2610.38422
pdf_url: https://arxiv.org/pdf/2610.38422
published: '2026-10-28'
collected: '2026-10-30'
category: Training
direction: 大模型训练 · 循环LM反向传播优化
tags:
- Looped LM
- Truncated BPTT
- Training Budget
- Training Efficiency
- Parcae
one_liner: 实证训练预算提升时短反向传播窗口的时间匹配优势持续衰减
practical_value: '- 训练业务侧循环结构垂直LM（如电商语义匹配模型、Agent推理小模型、生成式推荐Semantic ID模型）时，不要直接复用小预算下的短反向窗口最优结论，必须基于自身可用训练算力做ablation，以目标预算下的实测效果为准

  - 小训练预算场景（如快速迭代的业务小模型、ablation验证模型），优先选择更短的反向传播窗口，用节省的时间增加更新步数，相同训练时间内可获得比长窗口更低的Loss

  - 大算力预算场景（如训练生产级大参数量业务LM），优先选择更长的反向传播窗口，最终效果优于短窗口+更多更新步的方案，下游任务表现也更稳定'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
循环Transformer结构可在不增加参数量的前提下提升语言模型效果，但训练时循环深度会带来反向传播成本飙升，此前研究仅在固定预算下对比反向传播窗口的优劣，预算提升后最优窗口是否会发生变化无明确结论，该问题直接影响训练资源分配效率，对业务侧训垂直领域LM的ROI影响显著。

### 方法关键点
- 定义反向窗口为反向传播时保留梯度的最后N次循环迭代：窗口越短单步更新成本越低，可支持更多更新步；窗口越长单token学习效率越高
- 设计两组对照实验：同token量对比隔离单token效率差异，同训练时间对比评估两种策略的综合收益
- 测试K4（4步反向窗口）、K6、K8三种窗口，覆盖1×/2×/4×三种训练预算，全程控制随机种子、模型结构、前向循环次数完全一致

### 关键实验结果
基于FineWeb-Edu数据集，在144M、388M两种参数量的Parcae循环LM上测试：1×小预算下，同训练时间的K4+（短窗口+更多更新步）测试NLL比K8低0.0177 nats/token，优势明显；4×大预算下，K4+的优势收缩90%以上，144M模型场景下K8反超K4+ 0.003~0.006 nats/token；拆解发现预算提升时，额外更新步的收益衰减速度是单token效率收益衰减的3~8倍。

### 核心结论
循环语言模型的反向传播窗口最优选择完全依赖目标训练预算与资源约束，不能直接迁移小预算下的结论
