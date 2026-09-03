---
title: 'SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models'
title_zh: SolarWM：面向长时序视频世界模型的开放数据与可扩展训练框架
authors:
- Junchao Huang
- Guian Fang
- Shengju Qian
- Xianghao Kong
- Zhuoran Zhao
- Wei Huang
- Yihua Du
- Zixin Zhang
- Justin Cui
- Yuchao Gu
affiliations:
- CUHK-SZ
- SLAI
- NUS
- CUHK
- HKUST
arxiv_id: '2609.02886'
url: https://arxiv.org/abs/2609.02886
pdf_url: https://arxiv.org/pdf/2609.02886
published: '2026-09-01'
collected: '2026-09-03'
category: Other
direction: 长时序视频世界模型 · 开源训练底座
tags:
- World Model
- Video Generation
- Open Dataset
- Multi-source Processing
- Long-Horizon
one_liner: 开源143万片段数据集+多backbone兼容的长时序视频世界模型训练框架
practical_value: '- 多源异构数据统一格式化的工程方案可复用，解决推荐系统多来源物料（短视频、图文、直播）的特征对齐、混合训练问题

  - 三阶段训练范式可迁移到长序列用户行为建模、跨域推荐模型训练，降低不同域数据分布差异带来的性能损失

  - 短序列训练支撑长时序推理的思路，可优化电商Agent用户全购物旅程预判、长周期交互内容生成的训练成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
多源异构数据特征不一致、不同视频生成backbone适配成本高，导致长时序视频世界模型训练结果难复现、泛化性差。
### 方法关键点
1. 搭建可重配置多源数据引擎，将10个数据集的143万条视频片段转换为统一帧对齐格式，覆盖视觉、相机参数、字幕、质量元数据等维度，解耦源数据处理与混合构造；
2. 提出backbone原生适配框架，统一训练推理接口，在保留各模型原生表示与目标的前提下，完成Wan2.2、LTX-2.5、MiniMax-H3等4个5B-33B参数版本的实例化；
3. 采用三阶段训练范式：双向适配→教师强制自回归初始化→分布匹配蒸馏。
### 关键结果
仅用5秒短序列训练即可支撑数分钟到数小时级的实时交互推理，全套数据集、pipeline、训练配方、权重、框架全部开源。
