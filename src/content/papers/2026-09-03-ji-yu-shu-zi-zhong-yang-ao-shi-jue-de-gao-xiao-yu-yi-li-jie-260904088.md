---
title: Efficient Semantic Understanding from Digital Foveation
title_zh: 基于数字中央凹视觉的高效语义理解方法
authors:
- Caterina Caccavella
- Vittorio Fra
- Andreas Ziegler
- Giulia D'Angelo
- Yulia Sandamirskaya
affiliations:
- Zurich University of Applied Sciences (ZHAW)
- ETH Zürich
- Politecnico di Torino
- University of Tübingen
- Czech Technical University
arxiv_id: '2609.04088'
url: https://arxiv.org/abs/2609.04088
pdf_url: https://arxiv.org/pdf/2609.04088
published: '2026-09-03'
collected: '2026-09-05'
category: Other
direction: 主动视觉 · 高效语义分割优化
tags:
- Active Vision
- Foveated Vision
- Semantic Segmentation
- Computational Efficiency
- Saliency Detection
one_liner: 提出基于生物中央凹视觉的轻量主动视觉管线，用远低于基线的算力实现接近全稠密处理的语义理解效果
practical_value: '- 电商商品图像/短视频语义理解场景可借鉴选择性算力分配策略：仅对商品主体等显著性高的核心区域做高分辨率处理，边缘区域用低分辨率计算，大幅降低推理成本

  - 多模态推荐的图像特征提取模块可复用「高分辨率核心区特征+低分辨率上下文特征」的融合架构，平衡特征精度与推理延迟

  - 搜索推荐的全链路资源调度可参考该思路：对高价值请求/高置信度候选集分配更多计算资源，低优先级场景简化计算链路，实现全局性价比最优'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
传统稠密语义分割对全图均匀分配算力，不区分任务相关性与场景复杂度，存在大量资源冗余，受生物视觉中央凹感知机制启发，探索稀疏观测下的高效语义理解路径。
### 方法关键点
提出轻量主动视觉管线，融合显著性驱动的注视点选择、高分辨率中央凹观测、低分辨率上下文信息、语义积累、自适应计算模块；采用对象级评价指标替代传统像素级指标，更适配稀疏观测场景的效果衡量。
### 关键结果
在ADE20K-Object数据集上：
1. 单次中央凹观测仅消耗4.7%的基线算力，即可达到95.9%的基线Top-1精度、96.9%的基线Top-3精度
2. 场景级语义积累仅用58.6%的基线算力，即可恢复90.6%的基线对象召回率
