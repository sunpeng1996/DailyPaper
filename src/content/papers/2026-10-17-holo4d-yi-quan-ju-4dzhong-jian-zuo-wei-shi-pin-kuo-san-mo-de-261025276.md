---
title: 'Holo4D: Holistic 4D Reconstruction as Geometric Control for Video Diffusion'
title_zh: Holo4D：以全局4D重建作为视频扩散模型的几何控制框架
authors:
- Yushi Lan
- Zeren Jiang
- Koichi Namekata
- Xingang Pan
- Chuanxia Zheng
- Andrea Vedaldi
affiliations:
- University of Oxford
- Nanyang Technological University
arxiv_id: '2610.25276'
url: https://arxiv.org/abs/2610.25276
pdf_url: https://arxiv.org/pdf/2610.25276
published: '2026-10-17'
collected: '2026-10-31'
category: Other
direction: 视频扩散 · 新视角视频生成
tags:
- Video Diffusion
- 4D Reconstruction
- Novel View Synthesis
- Geometric Control
- Generative AI
one_liner: 提出基于4D重建几何引导的视频重拍框架，无需重训预训练视频扩散即可实现可控新视角视频合成
practical_value: '- 电商商品短视频生产场景可直接复用该框架：基于单条实拍商品视频生成任意运镜的新视角展示素材，大幅降低多视角拍摄成本

  - 短视频生成类Agent可集成该几何控制模块，解决现有扩散生成视频普遍存在的视角漂移、空间几何不一致的痛点

  - 虚拟直播间/数字人带货内容生产场景中，可兼容不同精度的4D重建器，无需重训扩散基座即可快速迭代生成效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
从新相机轨迹合成单目视频需同时保留原场景的几何结构与运动信息，且合理补全新出现的可见区域。传统4D重建方案仅能还原观测区域结构，原生视频扩散模型生成的内容易出现几何不一致、视角漂移问题。
### 方法关键点
1. 搭建Holo4D视频重拍框架，将前馈4D重建器输出的3D轨迹作为全局源视图4D支架
2. 将3D轨迹投影到目标视角，编码几何信息与源视图外观特征，引导预训练视频扩散模型生成
3. 无需重训视频扩散基座，可兼容任意4D重建器，可随重建技术迭代自动提升生成效果
### 关键结果
实验验证基于轨迹的条件控制可显著提升新视角视频的相机控制精度与几何一致性，生成内容既完整保留原场景运动与结构，未观测区域的生成自然度也达到主流SOTA水平。
