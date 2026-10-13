---
title: 'GLIMPSE: Global-Local Indexing with Multi-Precision Spectral Encoding for
  Explorable Video World Models'
title_zh: GLIMPSE：面向可探索视频世界模型的多精度光谱编码全局局部索引
authors:
- Zhufeng Xu
- Henglei Lv
- Bailin Deng
- Yikang Ding
- Xiaoqiang Liu
- Guoxin Zhang
- Hongbo Fu
- Lin Gao
affiliations:
- Institute of Computing Technology, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Cardiff University
- Kling AI
- The Hong Kong University of Science and Technology
arxiv_id: '2610.13706'
url: https://arxiv.org/abs/2610.13706
pdf_url: https://arxiv.org/pdf/2610.13706
published: '2026-10-09'
collected: '2026-10-13'
category: Other
direction: 视频世界模型 · 记忆索引优化
tags:
- World Model
- Memory Indexing
- Spectral Encoding
- Video Generation
- Scene Consistency
one_liner: 提出带多精度坐标与光谱衰减的全局-局部记忆接口，提升可探索视频世界模型的场景一致性
practical_value: '- 多精度坐标+几何条件衰减的思路可迁移到推荐系统Semantic ID召回，降低向量检索中地址不准带来的匹配误差

  - 全局+局部双层记忆架构可复用给Agent场景记忆模块，局部存细粒度交互特征、全局存上下文语义，平衡精度与效率

  - 固定读取预算下的足迹引导检索策略可用于大模型长上下文检索场景，控制IO开销的同时提升召回相关性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
可探索视频世界模型在相机回扫已观测场景时，现有位置传输机制对深度、姿态估计误差敏感，易出现重影、结构重复等一致性问题，全精度位置编码会进一步放大投影不准确的负面影响。
### 方法关键点
1. 提出GLIMPSE全局-局部记忆接口，采用分带多精度坐标+几何感知光谱衰减，降低对投影地址误差的敏感度；
2. 双层记忆架构：局部Patch记忆存储视图专属外观特征，循环全局记忆提供全局场景上下文；
3. 足迹引导检索机制，在固定局部读取预算下筛选匹配的历史Patch，控制计算开销。
### 关键结果
相同检索与读取预算下，相比确定性位置传输方案，几何对应性、光度一致性均实现显著提升，支持最长721帧的自由场景连续探索生成。
