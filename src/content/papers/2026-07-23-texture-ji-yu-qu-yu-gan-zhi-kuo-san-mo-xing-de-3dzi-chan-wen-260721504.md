---
title: 'Texture++: Elevating 3D Asset Texture Resolution with a Region-Aware Diffusion
  Model'
title_zh: Texture++：基于区域感知扩散模型的3D资产纹理分辨率提升
authors:
- Shuaiwei Wang
- Shi Li
- Jieting Xu
- Yuchi Huo
- Qi Wang
- Wenting Zheng
- Rengan Xie
affiliations:
- State Key Laboratory of CAD&CG, Zhejiang University
- North China Electric Power University
arxiv_id: '2607.21504'
url: https://arxiv.org/abs/2607.21504
pdf_url: https://arxiv.org/pdf/2607.21504
published: '2026-07-23'
collected: '2026-07-25'
category: Other
direction: 3D资产纹理超分 · 区域感知扩散模型
tags:
- Diffusion Model
- Super Resolution
- 3D Asset
- Texture Enhancement
- Region-Aware
one_liner: 提出区域感知扩散框架Texture++，通过多视图融合实现3D资产纹理超分，效果优于现有SOTA
practical_value: '- 电商3D商品库优化场景可复用自适应视图选择+四叉树区域组织方法，解决现有3D商品纹理模糊、跨视角展示不一致问题

  - 3D直播/虚拟试穿场景可借鉴掩码区域定向扩散超分思路，仅对纹理模糊区域做增强，大幅降低推理算力消耗

  - 存量低清3D资产翻新时可直接参考本框架pipeline，无需重新建模即可提升资产质量，降低3D内容生产成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有超分辨率模型多针对自然图像设计，未适配3D资产纹理优化需求，大量存量低分辨率纹理的3D资产无法被有效复用，影视、游戏、电商3D商品展示等领域均存在高清纹理生成的强需求。
### 方法关键点
1. 重构UV空间超分任务为「多渲染视图超分+结果合并」流程，设计自适应视图选择策略整合分散在UV纹理块中的信息，保证视图空间纹理完整连续；
2. 提出基于四叉树的纹理区域组织方法，合并多视角超分结果并生成待增强区域掩码，精准识别需要优化的纹理区域；
3. 设计面向掩码区域的扩散超分模型，增强指定区域纹理的同时保证与周边区域无缝融合，避免拼接痕迹。
### 关键结果
综合实验表明，本方法生成的纹理在细节还原度、跨区域连续性上均显著优于现有SOTA方法，生成效果更接近人工标注的高清真值。
