---
title: 'BooM-VVT: Boosting Mask-Free Video Virtual Try-On with Image-Level Pseudo
  Data'
title_zh: BooM-VVT：基于图像级伪数据的无掩码视频虚拟试穿优化
authors:
- Wei Zhang
- Xin Li
- Peishu Shi
- Jialin Gao
- Xuekang Peng
- Zhichao Lian
- Yeying Jin
affiliations:
- Nanjing University of Science and Technology
- University of Science and Technology of China
- National University of Singapore
- Meituan
arxiv_id: '2609.04120'
url: https://arxiv.org/abs/2609.04120
pdf_url: https://arxiv.org/pdf/2609.04120
published: '2026-09-03'
collected: '2026-09-05'
category: Multimodal
direction: 电商生成式内容 · 虚拟试穿
tags:
- Virtual Try-On
- Video Generation
- Pseudo Data
- E-commerce Content
- Multimodal Generation
one_liner: 提出无掩码视频虚拟试穿框架BooM-VVT，通过伪数据复用、采样优化提升复杂场景试穿效果
practical_value: '- 电商虚拟试穿场景可复用多阶段训练策略，用低成本图像级伪数据替代昂贵的视频级伪数据，大幅降低数据标注成本

  - 关键帧采样模块可借鉴服装敏感采样思路，聚焦服装关联的人体区域选帧，提升试穿生成的服装一致性

  - 开源多视图试穿数据集OmniView可直接用于训练电商场景下多视角、跨品类试穿模型，覆盖更多业务场景'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视频虚拟试穿（VVT）依赖掩码标注试穿区域，大动作、严重遮挡场景鲁棒性差；无掩码方案需构造视频级伪数据，成本极高；粗粒度关键帧采样+多视角试穿数据稀缺，导致服装一致性差、无法适配多样试穿任务。
### 方法关键点
1. 基于关键帧驱动范式搭建无掩码VVT框架BooM-VVT，采用多阶段训练策略，用低成本图像级伪数据完成无掩码定位学习，大幅降低视频伪数据需求；
2. 设计服装敏感关键帧采样策略，聚焦服装关联人体区域选帧，更好捕获服装外观；
3. 引入帧共享3D-RoPE建立关键帧与目标帧的时空对应关系，实现精准服装细节迁移；
4. 构建大规模多视角试穿数据集OmniView，覆盖复杂相机视角、多品类试穿场景。
### 关键结果
实验验证BooM-VVT在时序一致性、服装保真度上均优于现有SOTA方法，可适配大动作、遮挡、多视角、跨品类、分层试穿等复杂业务场景。
