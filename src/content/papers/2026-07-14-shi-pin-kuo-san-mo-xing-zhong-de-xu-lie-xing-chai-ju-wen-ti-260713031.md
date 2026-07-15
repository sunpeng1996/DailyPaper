---
title: The Seriality Gap in Video Diffusion Models
title_zh: 视频扩散模型中的序列性差距问题研究
authors:
- Jorge Diaz Chao
- Konpat Preechakul
- Yuxi Liu
- Yutong Bai
arxiv_id: '2607.13031'
url: https://arxiv.org/abs/2607.13031
pdf_url: https://arxiv.org/pdf/2607.13031
published: '2026-07-14'
collected: '2026-07-15'
category: Other
direction: 视频扩散模型 · 序列推理能力优化
tags:
- Diffusion Model
- Video Generation
- Serial Reasoning
- Causal Chain
- Model Optimization
one_liner: 揭示视频扩散模型的序列性差距，证明去噪步骤无法新增串行计算能力并给出优化方向
practical_value: '- 电商商品短视频生成/动态效果预览场景，可优先采用自回归/分块生成、加深骨干网络的方案提升长序列因果逻辑一致性

  - 基于扩散的视频模拟类任务（如商品使用流程模拟、互动效果预览），避免盲目增加去噪步骤提升序列推理效果，优先优化骨干串行计算能力

  - 构建Agent动态环境感知/序列模拟模块时，长因果链确定性序列预测场景不建议优先选用扩散模型，可优先考虑自回归架构'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有标准双向视频扩散模型在多物体碰撞等长因果链序列预测任务上性能随因果链延长显著下降，过往常归因于视频长度，实际成因未明确。
### 方法关键点
1. 设计多球硬球动力学对照实验，分离因果链长度、视频长度两个干扰变量；
2. 对比验证自回归/分块生成、架构深度、去噪步数等变量对任务性能的影响；
3. 从理论层面证明确定性视频预测场景下，去噪步骤无法在骨干网络之外新增串行计算能力。
### 关键结果
1. 因果链每延长一段，标准双向视频扩散性能显著衰减，等长无交互单球对照场景无明显性能下降；
2. 提升有效串行计算的方案（自回归/分块生成、加深骨干架构）可带来超出常规的性能增益；
3. 序列性差距本质是任务所需串行计算量与扩散模型去噪循环不可扩展串行计算的结构不匹配。
