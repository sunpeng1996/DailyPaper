---
title: Geometry-Aligned Semantic Matching for Cross-Modal Planar Image Registration
title_zh: 面向跨模态平面图像配准的几何对齐语义匹配算法
authors:
- Zhiwei Wang
- Defeng He
- Yuxing Li
- Meilu Zhu
- Edmund Y. Lam
arxiv_id: '2610.03167'
url: https://arxiv.org/abs/2610.03167
pdf_url: https://arxiv.org/pdf/2610.03167
published: '2026-10-02'
collected: '2026-10-05'
category: Other
direction: 跨模态图像配准 · 基础模型特征融合
tags:
- Cross-Modal-Matching
- Image-Registration
- Foundation-Model
- DINOv3
- Feature-Fusion
one_liner: 提出CDPM跨模态图像配准框架，融合DINO语义与CNN细节特征，精度更高且算力消耗更低
practical_value: 主要是学术贡献，面向CV跨模态图像配准场景，电商/广告/推荐/Agent业务领域可迁移价值极低
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有跨模态图像匹配方案存在两个核心缺陷：语义表征仅保证跨模态一致性，特征相似度无法对应几何位置关系；细粒度CNN特征具备局部细节，但缺乏全局跨模态语义引导，匹配稳定性差。
### 方法关键点
1. 提出CDPM框架，先用几何一致的跨模态patch对渐进式适配DINOv3，让特征相似度直接反映真实跨模态空间对应关系
2. 构建DINO为核心的特征金字塔，多尺度DINO表征维持稳定跨模态匹配，轻量CNN分支补充结构细节实现精准局部精调
### 关键结果
在VIS-IR数据集上对比RoMa，AUC@3/5/10/20分别提升7.36、13.40、13.75、10.42个百分点，mACE从5.83降至2.78像素；性能全面优于RoMa v2的同时FLOPs降低45.6%
