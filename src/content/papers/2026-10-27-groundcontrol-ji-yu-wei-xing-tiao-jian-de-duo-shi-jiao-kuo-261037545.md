---
title: 'GroundControl: Satellite-Conditioned Multi-View Diffusion for Reconstruction-Free
  Novel View Synthesis'
title_zh: GroundControl：基于卫星条件的多视角扩散无重建新视角合成
authors:
- Akshay Krishnan
- Matias Turkulainen
- Jamie Wynn
- Zawar Qureshi
- Mohamed Sayed
- Guillermo Garcia-Hernando
- Sara Vicente
- James Hays
- Michael Firman
- Daniyar Turmukhambetov
affiliations:
- Niantic Spatial
- Georgia Institute of Technology
- Aalto University
arxiv_id: '2610.37545'
url: https://arxiv.org/abs/2610.37545
pdf_url: https://arxiv.org/pdf/2610.37545
published: '2026-10-27'
collected: '2026-10-29'
category: Other
direction: 多视角生成 · 扩散模型条件优化
tags:
- Diffusion Model
- Novel View Synthesis
- Cross-Attention
- Multi-View Generation
- Conditional Generation
one_liner: 引入卫星图像作为交叉注意力条件约束多视角扩散，无需3D重建即可解决场景外插的布局幻觉问题
practical_value: '- 电商3D商品展示、虚拟逛店场景可借鉴双视角条件约束思路，用少量实拍图+俯视图生成任意视角内容，大幅降低3D建模成本

  - 户外AR广告、街景广告投放场景可复用卫星+街景双条件生成方案，确保生成广告内容与真实空间布局完全匹配

  - 条件生成任务可复用「预训练模型保留+交叉注意力条件注入」架构，无需全量重训即可引入额外约束，降低训练成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有基于稀疏输入的多视角扩散模型做新视角合成时，外插超出输入视角范围的场景会产生不符合真实物理结构的空间布局幻觉，依赖3D重建的优化方案成本极高，无法落地大规模户外场景生成需求。
### 方法关键点
1. 引入卫星图像作为额外空间布局先验，设计交叉注意力模块同时注入卫星图像约束、街景输入图像特征到预训练多视角扩散模型，完全保留原有预训练生成先验
2. 无需3D场景重建，仅依赖带位姿的街景、卫星图像即可完成推理
### 关键结果
在户外公开数据集上效果全面优于仅卫星条件、仅街景条件的基线模型，尤其是目标视角与输入视角重叠度极低的困难场景下优势尤为突出
