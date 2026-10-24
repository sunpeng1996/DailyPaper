---
title: A Unified Framework for Image-to-3D Part Generation via Variable Granularity
title_zh: 基于可变粒度的图像转3D部件生成统一框架
authors:
- Qiwen Gu
- Xin Zhou
- Xiwu Chen
- Zhongyang Zhu
- Zhuo Zhang
- Junqiao Zhao
affiliations:
- Tongji University
- Chongqing Afari Intelligent Drive Co., Ltd
- Huazhong University of Science and Technology
arxiv_id: '2610.31671'
url: https://arxiv.org/abs/2610.31671
pdf_url: https://arxiv.org/pdf/2610.31671
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: 多模态生成 · 可变粒度3D部件生成
tags:
- 3D Generation
- Variable Granularity
- Multimodal Input
- Geometric Guidance
- Cross-Modal Synergy
one_liner: 提出支持从稀疏点到密集掩码多粒度输入的统一图像转3D部件生成框架FlexPart，精度优于现有方案
practical_value: '- 电商3D商品素材生成场景可复用可变粒度条件控制思路，支持从粗到细的用户自定义3D部件编辑，降低素材制作门槛

  - 多模态异质输入的门控自适应调制方法可迁移至多模态生成式推荐场景，实现不同粒度用户交互信号的统一编码

  - 不对称几何引导的跨粒度表征对齐机制可借鉴到多粒度召回/排序任务中，提升不同粒度信号的表征一致性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有可控3D部件生成方案仅支持单一粒度控制输入，无法适配数字资产创作中不同精细度的操作需求，多模型对应多粒度输入的架构部署成本高。
### 方法关键点
1. 提出统一框架FlexPart，单模型兼容稀疏点、bounding box、密集掩码三类不同粒度的异质几何条件输入；
2. 设计门控自适应调制模块实现多源异质输入的无缝融合，充分挖掘跨模态协同效应；
3. 引入不对称几何引导机制，依托强空间先验对齐不同粒度的表征，提升几何一致性与跨任务协同效果。
### 关键结果
在PartVerseXL数据集掩码条件任务上，Part CD指标较TripoSG + SAM3D相对降低16.6%，较OmniPart相对降低10.5%，同时全网格生成质量保持业内竞争力水平
