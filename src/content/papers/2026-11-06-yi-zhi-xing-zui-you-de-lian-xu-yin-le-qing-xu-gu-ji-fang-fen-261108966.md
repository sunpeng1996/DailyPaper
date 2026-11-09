---
title: 'Concordance-Optimal Continuous Music Emotion Estimation: Variance Decomposition,
  Dual-Branch Temporal Fusion, and Conformal Prediction Intervals'
title_zh: 一致性最优的连续音乐情绪估计：方差分解、双分支融合与共形预测区间
authors:
- Mohammad Faraz Akhtar
- Aditya Parashar
- Ayush Jain
- Madhur Gupta
- Ritesh Kumar
- Soubhik Chakraborty
affiliations:
- Birla Institute of Technology, Mesra, Ranchi, India
arxiv_id: '2611.08966'
url: https://arxiv.org/abs/2611.08966
pdf_url: https://arxiv.org/pdf/2611.08966
published: '2026-11-06'
collected: '2026-11-09'
category: Other
direction: 音乐情绪识别 · 多模态时序融合
tags:
- Multimodal
- Temporal Convolutional Network
- Conformal Prediction
- Emotion Recognition
- Cross-Modal Attention
one_liner: 通过方差分解优化损失，提出双分支多模态模型，大幅提升歌曲内情绪动态追踪效果
practical_value: '- 损失优化可复用：需同时优化全局排序与细粒度动态拟合的任务，可借鉴方差分解+λ参数权衡两类目标的方案，适配短视频情绪时序预测、商品评价情感动态建模等场景

  - 多模态融合架构可迁移：双分支时序卷积+跨模态注意力的融合结构，可用于音视频多模态内容特征提取场景，支撑短视频/直播推荐的内容标签生成

  - 鲁棒性评估方法可借鉴：部分模态失效的效果降幅验证逻辑，可用于多模态推荐系统的故障容错能力评估'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有音乐情绪识别的池化帧级相关指标被歌曲间差异主导，无法区分模型是追踪情绪动态还是仅按歌曲平均水平排序；MSE损失易导致方差压缩，无法有效优化歌曲内情绪动态的拟合效果。
### 方法关键点
1. 将标注方差分解为歌曲间、歌曲内两类，采用窗口化Lin's CCC作为歌曲内拟合目标，通过单参数λ权衡MSE（歌曲间排序目标）与CCC损失的权重
2. 提出双分支多模态模型MMAS，融合冻结的MERT预训练音频embedding与自动转录的10维符号特征，通过带跨模态注意力的时序卷积网络融合，支持多数据集无领域条件联合训练
3. 引入split-conformal区间输出预测置信度
### 关键结果
λ从0调至1时，歌曲内Arousal相关系数从0.204升至0.368；MMAS在DEAM/PMEmo数据集上池化Arousal/Valence相关系数最高达0.801/0.746，歌曲内Arousal相关系数较岭回归基线提升近2倍，共形预测区间覆盖率最高达93.7%
