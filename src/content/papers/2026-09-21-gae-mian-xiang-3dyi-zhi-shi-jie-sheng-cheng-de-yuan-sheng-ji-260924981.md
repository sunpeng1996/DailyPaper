---
title: 'GAE: Learning a Geometry-Native Latent Space for 3D-Consistent World Generation'
title_zh: GAE：面向3D一致世界生成的原生几何隐空间学习方法
authors:
- Jiahao Lu
- Minghao Yin
- Wenbo Hu
- Hengyu Liu
- Wang Zhao
- Sai-Kit Yeung
- Ying Shan
- Yuan Liu
affiliations:
- The Hong Kong University of Science and Technology
- ARC Lab, Tencent IEG
- The University of Hong Kong
- The University of Texas at Austin
arxiv_id: '2609.24981'
url: https://arxiv.org/abs/2609.24981
pdf_url: https://arxiv.org/pdf/2609.24981
published: '2026-09-21'
collected: '2026-09-22'
category: Other
direction: 3D生成 · 统一几何隐空间构建
tags:
- GAE
- 3D Generation
- Latent Space
- Autoencoder
- World Model
one_liner: 提出原生几何自编码器GAE，构建感知与生成通用的3D一致隐空间
practical_value: '- 电商3D商品生成场景可借鉴统一隐空间思路，用单隐向量同时输出RGB、深度、相机参数，解决多模型生成结果不一致问题

  - 虚拟试穿/3D商品展示业务可参考几何特征重参数化为生成隐空间的范式，替代传统额外加几何约束的训练方案，降低3D一致性优化成本

  - 虚拟场景搭建业务可复用该隐空间作为3D重建（感知）和内容生成（创作）的统一接口，打通上下游链路'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视觉生成器仅能生成逼真帧，无法保证3D场景一致性，核心痛点是生成侧隐空间以外观为核心，与感知侧编码跨视角结构的几何语义空间存在断层。
### 方法关键点
1. 不额外新增几何输出头，而是将几何基础模型的特征重参数化为紧凑的原生几何隐空间，通过几何原生自编码器GAE实现，其隐向量可同时解码出外观、深度、相机参数、点云图四类输出
2. 基于该隐空间，仅用标准条件流即可支持多类3D生成任务
### 关键结果
固定生成器和训练协议的对照实验中，替换为GAE隐空间后：
- RealEstate10K、DL3DV数据集上FVD分别下降12.7%、23.1%
- RealEstate10K数据集上相机轨迹误差减半
