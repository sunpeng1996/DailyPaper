---
title: 'CAPQ-FAST: Content-Adaptive Perceived Quality Assessment for Faster Audiovisual
  Playback'
title_zh: CAPQ-FAST：面向倍速音视频播放的内容自适应感知质量评估模型
authors:
- Jiarun Song
- Yuxin Song
- Fuzheng Yang
- Weisi Lin
arxiv_id: '2609.03498'
url: https://arxiv.org/abs/2609.03498
pdf_url: https://arxiv.org/pdf/2609.03498
published: '2026-09-03'
collected: '2026-09-06'
category: RecSys
direction: 音视频推荐 · 倍速播放QoE优化
tags:
- QoE
- Playback Speed
- Content Adaptive
- Perceived Quality
- Audiovisual Recommendation
one_liner: 提出分模态建模的倍速音视频感知质量统一预测模型，支撑自适应播放控制与个性化推荐
practical_value: '- 做音视频类内容（如直播带货回放、商品讲解短视频）的倍速推荐时，可参考分模态特征（视频TI、语音WPM、音乐BPM）做差异化播放速度预设，提升用户观看时长

  - 针对不同内容类型的用户倍速行为数据，可结合该模型的感知质量得分优化内容排序策略，优先推荐适配用户常用倍速的内容

  - 做音视频内容的个性化体验优化时，可复用该文的主观实验设计范式，快速获取不同用户群体的感知质量阈值'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
当前音视频平台倍速播放已成为主流用户行为，但不同模态内容（视频、语音、音乐）在倍速下的可理解性、信息完整性要求差异显著，现有研究对不同倍速下的用户感知质量刻画不足，无法支撑自适应的播放控制与内容推荐。
### 方法关键点
1. 开展多组主观实验，分析视频、语音、音乐三类内容的播放速度与感知质量的关联关系；
2. 提取各模态专属时序特征：视频用Temporal Information (TI)、语音用Words Per Minute (WPM)、音乐用Beats Per Minute (BPM)；
3. 分别训练三类内容的倍速感知质量预测模型，融合得到统一的CAPQ-FAST自适应评估模型。
### 关键结果
实验验证该模型可有效预测不同播放速度下的用户感知质量，可支撑平台优化自适应播放控制、个性化推荐策略，提升用户体验适配性。
