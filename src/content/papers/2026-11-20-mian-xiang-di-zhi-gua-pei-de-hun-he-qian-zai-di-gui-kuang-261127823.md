---
title: Mixture of Latent Recursions for Low-Rank Adaptation
title_zh: 面向低秩适配的混合潜在递归框架MoLR
authors:
- Weixun Luo
- Ye Mao
- Ranran Huang
- Junpeng Jing
- Krystian Mikolajczyk
affiliations:
- Imperial College London
arxiv_id: '2611.27823'
url: https://arxiv.org/abs/2611.27823
pdf_url: https://arxiv.org/pdf/2611.27823
published: '2026-11-20'
collected: '2026-11-23'
category: Training
direction: 参数高效微调 · LoRA 自适应递归优化
tags:
- LoRA
- PEFT
- Adaptive Routing
- Conditional Computation
- Low-Rank Adaptation
one_liner: 提出参数开销与LoRA相当的混合潜在递归框架，大幅提升多场景低秩适配效果
practical_value: '- 做LLM4Rec、电商广告文案生成等业务微调时，可直接替换原有LoRA为MoLR，在参数增量可忽略的前提下提升下游任务效果

  - 推理侧对 latency 敏感的推荐/搜索场景，可动态调整MoLR的推理最大递归深度，实现性能与推理速度的灵活tradeoff，无需重新训练

  - 现有其他LoRA变体（如DoRA、VeRA）可直接叠加MoLR的自适应递归模块，仅增加极少参数即可获得稳定效果提升

  - 阈值驱动的token级动态路由思路可迁移到推荐系统的语义处理场景，对核心语义token分配更多计算资源'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LoRA变体提升表达能力的方式普遍依赖增加可训练参数，无法实现表达能力提升与参数开销的解耦，如何在不显著增加参数的前提下增强LoRA的表达能力是参数高效微调领域的核心痛点。

### 方法关键点
- 在LoRA的上下投影之间引入共享参数的潜在递归模块，通过迭代优化低维潜在表征提升表达能力，最大递归深度增加不会带来参数增长
- 设计轻量阈值驱动的token级路由，独立判断每个token是否需要继续递归优化，避免序列级路由带来的信息泄露问题
- 采用动态阈值调整策略实现递归深度的负载均衡，无需引入辅助损失即可保证不同深度的递归模块都得到充分训练
- 新增参数仅包含r维路由权重和r×r的共享潜在变换矩阵，参数开销与标准LoRA几乎一致

### 关键实验
在NLU（GLUE基准）、自然语言推理（MMLU、GSM8K等7个任务）、图像分类7个数据集上对比LoRA、DoRA、AdaLoRA、TopLoRA等7种主流LoRA变体，参数规模相当的前提下：RoBERTa-B上GLUE平均精度提升1.86个百分点，LLaMA-3.2-3B上7类推理任务平均精度提升2个百分点，CLIP-ViT-B上7类图像分类任务平均精度提升3.71个百分点；训练时间仅比LoRA增加13%，推理延迟仅高0.51ms。

### 核心结论
低秩潜在空间可作为可复用的计算工作区，迭代潜在优化是除提升秩之外的另一条高效提升低秩适配能力的核心路径。
