---
title: 'Honeycomb: Constant-Size Scene Memory Representation for Video World Models'
title_zh: Honeycomb：面向视频世界模型的固定大小场景内存表示
authors:
- Jack Wei Lun Shi
- Kaichen Zhou
- Haoyu Chen
- Yufeng Weng
- Keane Ong
- Ruojin Cai
- Hang Hua
- Justin K. W. Yeoh
- Mengyu Wang
affiliations:
- Harvard University
- National University of Singapore
- MIT
- MIT-IBM Watson AI Lab
arxiv_id: '2609.37690'
url: https://arxiv.org/abs/2609.37690
pdf_url: https://arxiv.org/pdf/2609.37690
published: '2026-09-29'
collected: '2026-10-04'
category: Other
direction: 视频世界模型 · 固定大小场景内存优化
tags:
- VideoWorldModel
- MemoryOptimization
- LowRankRepresentation
- LongVideoGeneration
one_liner: 提出固定大小低秩场景内存HexMemory，解决长视频生成存储膨胀与重访一致性问题
practical_value: '- 固定大小低秩内存的设计思路可迁移到Agent长期交互记忆、推荐系统长周期用户行为建模模块，解决历史特征存储膨胀问题

  - 置信度加权池化加残差修正的多源时序特征融合方法，可复用到长短期用户兴趣融合、时序召回的特征更新流程

  - 仅处理新增数据块、避免全历史重计算的增量更新逻辑，可优化实时推荐的特征计算效率，降低线上推理开销'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
长时序视频生成需持久场景内存保障一致性，现有方案随生成时长累积RGB或隐特征，存储开销线性增长，重访旧场景时一致性表现差。
### 方法关键点
1. 提出固定大小HexMemory低秩表示，用6个固定维度的空间/时空平面存储场景特征，总存储全程恒定；
2. 前馈writer仅处理新生成片段的观测，将其映射为新平面特征；旧特征通过坐标变换保持维度后，经置信度加权池化+可学习残差修正与新特征融合；
3. reader从HexMemory读取隐变量作为后续生成条件，无需逐场景优化或全历史重复计算。
### 关键结果
在WorldScore、RealEstate10K数据集上取得优异视频生成质量，重访场景一致性显著优于基线，全程存储大小无增长。
