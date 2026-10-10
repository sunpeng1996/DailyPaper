---
title: 'LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation'
title_zh: LEGO：无需升维的外视角到第一视角视频生成方法
authors:
- Suhwan Cho
- Yonwoo Choi
- Soongjin Kim
- Jicheol Park
- Taegyu Lim
affiliations:
- GenGenAI
arxiv_id: '2610.12442'
url: https://arxiv.org/abs/2610.12442
pdf_url: https://arxiv.org/pdf/2610.12442
published: '2026-10-08'
collected: '2026-10-10'
category: Other
direction: 跨视角视频生成 · 扩散模型优化
tags:
- Video Generation
- Diffusion Model
- View Synthesis
- Transformer
- Cross-View Alignment
one_liner: 提出无深度、点云依赖的视图合成器驱动扩散的跨视角视频生成方案，超SOTA且跨数据集免重训泛化
practical_value: '- 扩散模型条件输入设计可借鉴「优先保结构对齐而非输入清晰度」思路，生成式推荐/商品文案/图生成任务中，不用过度优化条件输入的细节，利用扩散自身去噪能力补全细节，降低预处理成本

  - 基于概率映射置信度引导扩散早期去噪步布局生成的方案，可迁移到电商多模态生成（如商品展示视频、定制化营销素材）的布局约束优化，提升生成内容的合规性与匹配度

  - 用Transformer内部隐式学习跨域对应关系、省去显式对齐的设计思路，可迁移到跨域/跨模态推荐的表征对齐任务，降低特征映射的误差累积'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
外视角转第一视角视频生成属于高难度新视图合成任务，两类视角重叠度低、目标视图大部分内容不可见；现有SOTA依赖显式深度估计、点云升维重渲染流程，深度误差会直接传导为生成内容错位，泛化性差。

### 方法关键点
1. 提出lifting-free方案，用微调的LVSM-style Transformer作为视图合成器，无需深度、点云、重投影，内部隐式学习跨视角对应关系，输出概率映射的结构化条件；
2. 基于概率映射的区域置信度，掩码低置信度区域，同时引导扩散模型早期去噪步优先生成高置信度布局；
3. 利用扩散模型去噪训练擅长补全细节的特性，抵消视图合成器输出纹理模糊的缺陷，实现结构供给与细节生成的分工配合。

### 关键结果
性能全面超越基于显式重建的SOTA pipeline，无需重训即可直接泛化到其他数据集。
