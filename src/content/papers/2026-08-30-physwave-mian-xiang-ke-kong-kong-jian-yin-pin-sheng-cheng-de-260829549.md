---
title: 'PhysWave: Physics-Guided Latent Diffusion Models for Controllable Spatial
  Audio Generation'
title_zh: PhysWave：面向可控空间音频生成的物理引导潜扩散模型
authors:
- Lingfeng Yao
- Chenpei Huang
- Xingke Yang
- Ziye Geng
- Changqing Luo
- Hao Wang
- Jiang Liu
- Miao Pan
affiliations:
- University of Houston
- Stevens Institute of Technology
- Waseda University
arxiv_id: '2608.29549'
url: https://arxiv.org/abs/2608.29549
pdf_url: https://arxiv.org/pdf/2608.29549
published: '2026-08-30'
collected: '2026-09-06'
category: Other
direction: 生成式空间音频 · 物理先验引导扩散
tags:
- Diffusion Model
- Spatial Audio
- Physics Prior
- Controllable Generation
- Generative AI
one_liner: 引入可微分声学先验训练潜扩散模型，实现文本与轨迹统一控制的高质量空间音频生成
practical_value: '- 生成类任务可引入领域可微分物理先验，无需标注大量规则对齐数据即可提升生成结果的合理性，可复用在电商AR/VR场景的空间内容生成链路

  - 多模态控制信号（自然语言描述+数值参数）可通过统一表示层融合，平衡普通用户易用性与专业用户控制精度，可迁移至多模态内容生成的交互逻辑设计

  - 训练阶段注入的约束先验可复用于推理阶段做零样本效果优化，降低定制化场景下的微调成本，适合电商内容生成的多场景快速适配需求'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有文本转一阶Ambisonics（FOA）空间音频方法纯数据驱动，易违反声源方向、距离的声学规则，且文本描述与参数控制分离，用户需在易用性和精度间取舍，同时缺少大规模带声源轨迹的FOA数据集支撑动态生成。
### 方法关键点
1. PhysWave物理引导潜扩散模型通过共享航点-文本表示统一自然语言与轨迹控制输入
2. 训练阶段加入两个可微分声学先验：球谐方向一致性、平方反比距离一致性，约束生成结果符合物理规则
3. 构建含30万条片段的多类别、带声源轨迹的FOA数据集支撑动态生成
### 关键结果
声学先验使生成FOA音频空间一致性显著提升的同时保持音质达同期最优水平，且物理先验可直接用于推理阶段，实现免训练的空间效果优化
