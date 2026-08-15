---
title: 'AlayaWorld: Interactive Long-Horizon World Modeling - Full Technical Report
  (v1.1)'
title_zh: AlayaWorld v1.1：交互式长时序世界建模完整技术报告
authors:
- AlayaWorld Team
- Kaipeng Zhang
- Chuanhao Li
- Yifan Zhan
- Yongtao Ge
- Yuanyang Yin
- Jiaming Tan
- Kang He
- Liaoyuan Fan
- Mingliang Zhai
affiliations:
- Alaya Lab
arxiv_id: '2608.13492'
url: https://arxiv.org/abs/2608.13492
pdf_url: https://arxiv.org/pdf/2608.13492
published: '2026-08-13'
collected: '2026-08-15'
category: Other
direction: 长时序交互式世界建模 条件信号优化
tags:
- World Modeling
- Autoregressive Generation
- Causal VAE
- 3D Rendering
- Memory Optimization
one_liner: 对齐条件信号与生成内容的隐空间、时序结构，优化长时序世界建模的条件注入与存储模块
practical_value: '- 可借鉴条件信号与生成目标隐空间、时序结构对齐的设计思路，优化生成式推荐中用户行为序列、item特征的注入逻辑，降低训练推理分布差

  - hard memory dropout trick可迁移到序列推荐的用户历史记忆模块训练，直接丢弃而非置零无效记忆token，避免噪声干扰，提升模型泛化性

  - 训练推理统一VAE编解码协议的做法，可复用在电商商品图生成、推荐文案生成等所有基于VAE的生成任务中，减少分布偏移带来的效果损失'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有长时序交互式世界建模的多源条件信号经独立通路处理，与生成内容的隐表示、时序结构不匹配，存在训练-推理分布偏移，生成连贯性、可控性不足。
### 方法关键点
核心遵循「条件信号与生成内容在隐表示、时序结构上尽可能对齐」的原则，做两大架构升级：
1. 替换原深度扭曲空间存储模块为流式3D点缓存渲染器
2. 重构条件注入通路，将视觉条件编码至与生成视频一致的Causal VAE隐空间，对齐时序统计特征
具体包含6项落地修改：改用运动感知隐式条件替代静态帧条件、因果编码重渲染空间存储为连续序列、对齐像素空间时序存储窗口、采用直接丢弃记忆token的hard memory dropout、统一训练推理VAE编解码协议、移除相机AdaLN分支，视角控制完全通过重渲染空间条件实现。
### 关键结果
本技术报告未公开量化效果对比数据，已开源代码、演示视频供复现验证。
