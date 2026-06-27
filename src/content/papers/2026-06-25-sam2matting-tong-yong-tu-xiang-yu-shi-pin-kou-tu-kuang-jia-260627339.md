---
title: 'SAM2Matting: Generalized Image and Video Matting'
title_zh: SAM2Matting：通用图像与视频抠图框架
authors:
- Ruiqi Shen
- Guangquan Jie
- Chang Liu
- Henghui Ding
affiliations:
- Fudan University
- Shanghai University of Finance and Economics
arxiv_id: '2606.27339'
url: https://arxiv.org/abs/2606.27339
pdf_url: https://arxiv.org/pdf/2606.27339
published: '2026-06-25'
collected: '2026-06-27'
category: Other
direction: 多模态 · 通用图像视频抠图
tags:
- SAM2
- Video Matting
- Image Matting
- VOS
- Foundation Model
- Cross Domain
one_liner: 仅用图像数据训练的tracker-to-matting框架，实现跨场景SOTA图像与视频抠图
practical_value: '- 电商商品图/直播短视频自动化抠图场景可直接复用该框架，无需额外标注视频抠图数据，大幅降低数据采集标注成本

  - 任务解耦架构可迁移至多模态内容生产链路，通用基础模型+轻量任务头的组合同时兼顾泛化性与细粒度效果

  - 多模态推荐/搜索链路中可集成该工具作为视觉预处理模块，提取商品/人物前景特征，提升后续跨模态匹配准确率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视频抠图方法依赖标注成本高、场景覆盖窄的专属视频数据集，域外泛化能力弱；同时存在高层时序跟踪的语义理解需求与低层细粒度抠图的像素精度需求的天然矛盾，跟踪鲁棒性难以保障。

### 方法关键点
提出tracker-to-matting范式的SAM2Matting框架，对任务做解耦设计：基于SAM2/SAM3等成熟VOS基础跟踪器保障时序一致性，新增区域提议桥接层+专属轻量抠图头，负责输出像素级alpha matte实现高精度抠图，全程仅使用图像数据训练，无需视频标注。

### 关键结果
仅用图像训练即取得视频抠图任务SOTA表现，支持多类型prompt输入，时序稳定性优异，在以人为中心和开放野外场景下均具备强泛化能力。
