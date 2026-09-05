---
title: Zero-Shot Novel Depth Synthesis Using 3D Foundation Models Scene Representations
title_zh: 基于3D基础模型场景表征的零样本新视角深度合成
authors:
- Denis M. Akola
- David F. Fouhey
affiliations:
- New York University Tandon School of Engineering
- Courant Institute of Mathematical Sciences
arxiv_id: '2609.04174'
url: https://arxiv.org/abs/2609.04174
pdf_url: https://arxiv.org/pdf/2609.04174
published: '2026-09-03'
collected: '2026-09-05'
category: Other
direction: 3D视觉 · 零样本新视角深度合成
tags:
- 3D-FM
- Latent Diffusion
- Zero-Shot
- Depth Synthesis
- Scene Representation
one_liner: 利用3D基础模型内部表征结合潜扩散方法Z3D，实现零样本新视角真实深度图预测
practical_value: '- 本研究聚焦3D视觉方向，对通用搜索推荐、广告、Agent业务无直接可迁移价值

  - 若业务涉及AR试穿、3D商品建模、虚拟卖场场景，可复用3D基础模型内部表征解码隐式几何的思路，提升稀疏视角下3D重建效率

  - 可借鉴「预训练大模型通用表征+下游轻量扩散模块」的范式，降低特定场景3D内容生成的微调成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有NeRF、3D高斯溅射等神经场景表征方法仅支持已观测视图插值，无法在稀疏视角下推理遮挡区域的几何结构；此前3D基础模型（3DFM）学到的通用3D场景知识未被充分用于新视角深度合成任务。
### 方法关键点
1. 验证了可直接从3DFM的内部表征中解码得到场景隐藏表面的几何信息；
2. 提出Z3D方法，对3DFM输出的场景表征做潜扩散处理，零样本估计未观测视角的点图；
3. 无需针对特定场景微调，仅依赖预训练3DFM的通用知识即可推理。
### 关键结果
在多个公开数据集上，Z3D可生成符合几何一致性的高真实感新视角深度图，能合理推断被前景遮挡的区域几何。
