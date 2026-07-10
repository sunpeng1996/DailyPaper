---
title: 'Linear Attention Architectures: Mechanisms, Trade-offs, and Cross-Layer Routing'
title_zh: 线性注意力架构：机制、权衡对比与跨层路由方案研究
authors:
- Tommaso Cerruti
- Tim Rieder
- George Rowlands
- Lingfeng Jin
- Imanol Schlag
affiliations:
- ETH Zurich, D-INFK
- ETH AI Center, ETH Zurich
arxiv_id: '2607.07953'
url: https://arxiv.org/abs/2607.07953
pdf_url: https://arxiv.org/pdf/2607.07953
published: '2026-07-07'
collected: '2026-07-10'
category: LLM
direction: LLM架构·线性注意力效率优化
tags:
- Linear Attention
- DeltaNet
- Cross-layer Routing
- Long Context
- Training Efficiency
one_liner: 统一表征4种DeltaNet系列线性注意力架构，提出跨层值路由CLVR实现线性时间下效果小幅提升
practical_value: '- 长上下文推荐/Agent场景可直接复用选型结论：效果优先选Kimi Delta Attention+Muon+线性-软max混合栈，吞吐量优先选纯Gated
  DeltaNet+AdamW，32k序列下迭代时间仅为软max的28.5%

  - 线性注意力架构上可叠加CLVR跨层通路：将下层写值通过零初始化投影注入共享残差流，几乎不增加推理开销，最高可降低验证损失0.012，无需修改原有核心逻辑

  - 调参可直接参考优化器匹配规则：线性注意力搭配AdamW选更高学习率（~1e-3），搭配Muon选更低学习率（~3e-4），减少调参成本'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
软max注意力的序列长度平方复杂度严重限制长上下文LLM的训练推理效率，现有DeltaNet系列线性注意力变体缺乏统一对比框架，深层信息稀释问题也缺乏适配线性结构的轻量解决方案，无法指导业务场景下的架构选型。

### 方法关键点
- 将软max注意力、DeltaNet、Gated DeltaNet、Kimi Delta Attention、Gated DeltaNet-2统一到相同的循环内存表征框架下，明确各架构在表达性、内存衰减、读写控制、吞吐量、实现复杂度上的差异
- 提出两种轻量跨层路由方案：CLER将下层写误差注入上层值目标，CLVR将下层写值通过零初始化投影注入共享残差流，两者均保留线性时间复杂度
- 实验统一控制数据、硬件、参数量变量，对比纯线性栈、线性+软max混合栈的效果与效率表现

### 关键实验结果
基于FineWeb-Edu数据集训练350M参数模型15B tokens：Kimi Delta Attention+Muon混合栈取得最低验证损失2.273，比同规模软max注意力+Muon低0.076；纯Gated DeltaNet+AdamW取得最高训练吞吐量，是软max的1.22倍；序列长度32k时，纯Gated DeltaNet迭代时间仅为软max的28.5%；CLVR对比基线最高降低验证损失0.012，无明显下游任务退化。

**最值得记住的一句话**：线性注意力没有绝对最优方案，需要根据损失、吞吐量、上下文长度的业务优先级，匹配架构、栈结构、优化器和学习率的组合。
