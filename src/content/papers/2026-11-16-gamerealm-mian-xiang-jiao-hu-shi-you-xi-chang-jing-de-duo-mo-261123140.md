---
title: 'GameRealm: Grounding Visual Learning in Interactive Games'
title_zh: GameRealm：面向交互式游戏场景的多模态视觉学习数据集
authors:
- Weiguang Zhao
- Yifan Wang
- Ni Yang
- Yating Wang
- Xingyu Miao
- Yankai Jiang
- Mulin Yu
- Tao Lu
- Haoyu Guo
- Junting Dong
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Shanghai Jiao Tong University
- Zhejiang University
arxiv_id: '2611.23140'
url: https://arxiv.org/abs/2611.23140
pdf_url: https://arxiv.org/pdf/2611.23140
published: '2026-11-16'
collected: '2026-11-19'
category: Multimodal
direction: 多模态数据集 · 视觉基础模型训练
tags:
- Multimodal Dataset
- Visual Foundation Model
- Game Synthetic Data
- Data Collection Pipeline
- Geometric Learning
one_liner: 发布含1.2亿帧1000小时游戏素材的多模态标注数据集GameRealm，赋能视觉基础模型性能提升
practical_value: '- 游戏引擎生成的合成数据可作为多模态模型训练的低成本标注数据源，电商场景可复用该思路生成虚拟商品、3D展示场景的标注数据，大幅降低真实标注成本

  - 人机结合的统一数据采集pipeline可直接复用：电商商品多视角拍摄、交互行为数据采集可结合人工操作+Agent自动探索，提升数据采集效率与场景覆盖度

  - 多模态标注（含深度、相机参数、控制信号等）的数据集构建思路，可迁移至AR/VR电商导购场景的多模态推荐模型训练'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视觉基础模型训练受数据集碎片化、标注质量不稳定、多模态监督信号不足限制，真实场景大规模精准标注成本极高，无法满足模型对几何、交互信息的学习需求。
### 方法关键点
1. 构建GameRealm大规模多模态游戏数据集，覆盖1.2亿RGB帧、1000小时全视角游戏素材，提供度量深度、相机参数、同步音频、控制输入、3D点轨迹等原生多模态监督信号，支持单目/双目/多视角/全景多种视图配置
2. 研发统一数据采集pipeline，结合人工操作交互与Agent自动探索，可适配多类游戏环境实现规模化数据获取
### 关键结果
多任务实验验证，基于GameRealm预训练的视觉基础模型，在视觉生成、几何学习两类任务上均获得一致性性能提升
