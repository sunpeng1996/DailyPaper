---
title: 'World from Motion: Generative Dynamic Gaussian Reconstruction from Monocular
  Video'
title_zh: World from Motion：基于单目视频的生成式动态高斯重建
authors:
- Liyuan Zhu
- Shengyu Huang
- Amrita Mazumdar
- Tianye Li
- Zan Gojcic
- Gordon Wetzstein
- Iro Armeni
- Shalini De Mello
- Alex Trevithick
affiliations:
- Stanford University
- NVIDIA
arxiv_id: '2607.01202'
url: https://arxiv.org/abs/2607.01202
pdf_url: https://arxiv.org/pdf/2607.01202
published: '2026-07-01'
collected: '2026-07-03'
category: Other
direction: 4D动态场景重建 · 3D高斯生成
tags:
- 3DGS
- 4D_Reconstruction
- Monocular_Video
- Generative_Model
- Novel_View_Synthesis
one_liner: 提出从单目视频生成可渲染动态3D高斯表征的方法，达4D重建SOTA，可泛化至复杂真实视频
practical_value: '- 电商AR商品展示、3D内容生产场景可复用该管线，仅用单目商品动态视频即可生成高质量可渲染3DGS，大幅降低3D建模成本

  - 训练阶段引入带模拟缺陷的样本做监督的思路，可迁移到生成式推荐、多模态生成任务的降噪、补全模块优化

  - 测试时将生成结果蒸馏为统一表征的方案，可参考用于多模态生成内容的一致性对齐，提升输出稳定性'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
单目4D重建是AR/VR、机器人仿真、3D内容生产的核心技术，但现有单目重建方案普遍存在渲染伪影、区域缺失问题，无法直接生成一致、高质量的动态3D表征。
### 方法关键点
1 构建对齐的多视角视频对+动态3DGS数据集，模拟单目重建的典型缺陷构造训练样本；
2 以编码了外观、几何、3D场景运动的像素对齐稠密渲染结果为条件，输入视频模型修正初始重建伪影、补全缺失区域；
3 测试阶段将模型生成的新观测区域、运动信息蒸馏为单个一致的高质量动态3DGS。
### 关键结果
在4D重建任务上达到SOTA，可无缝泛化至存在大视角变化、动态运动的户外真实视频，同时提升新视角合成效果与底层3D运动估计精度。
