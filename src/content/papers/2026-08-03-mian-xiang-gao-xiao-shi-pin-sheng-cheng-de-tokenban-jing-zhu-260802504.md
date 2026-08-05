---
title: Token Radius Attention for Efficient Video Generation
title_zh: 面向高效视频生成的Token半径注意力机制
authors:
- Jiayu Chen
- Zhikun Jiang
- Maoliang Li
- Jiayi Luo
- Jiawei Yang
- Zihao Zheng
- Hengyi Zhang
- Guojie Luo
- Xiang Chen
affiliations:
- Peking University
- Beihang University
- Zhongguancun Academy
arxiv_id: '2608.02504'
url: https://arxiv.org/abs/2608.02504
pdf_url: https://arxiv.org/pdf/2608.02504
published: '2026-08-03'
collected: '2026-08-05'
category: Multimodal
direction: 多模态生成 · 稀疏注意力优化
tags:
- Sparse Attention
- Video Diffusion
- Transformer
- Inference Optimization
- Training-Free
one_liner: 提出免训练Token级稀疏注意力框架TRA，为视频扩散Transformer实现低损耗推理提速
practical_value: '- 电商商品短视频生成场景可直接复用TRA框架，无需重训现有视频扩散模型，仅替换attention模块即可降低推理成本35%+，适合大规模商拍视频批量生成

  - 搜推长序列用户建模场景可迁移熵→预算的token级计算分配思路：根据query/用户行为序列的注意力熵动态分配交互预算，无需全量attention即可降低长序列推理延时

  - 大模型推理工程可直接复用两个fused kernel设计：熵提取与softmax融合、半径掩码构造kernel，能将辅助计算开销降低10×以上

  - 多模态推荐的跨模态attention优化可借鉴半径稀疏模式：针对图文交互的空间局部性，构造结构化稀疏掩码，在不损失召回/排序效果的前提下降本提速'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
视频扩散Transformer（VDiT）是当前高保真视频生成的主流架构，但其3D稠密自注意力为O(N²)复杂度，随视频分辨率、时长增长算力成本线性飙升，已成为大规模落地的核心推理瓶颈。现有头/块级稀疏注意力方案为同组内所有query分配统一计算预算，既浪费算力在注意力分布高度集中的query，又会漏掉分布分散query的关键交互，导致生成质量明显下降。
### 方法关键点
- 基于两个核心观测：不同query的保留密度与注意力熵呈强对数线性关系（R²>0.94），高权重key天然形成以query为中心的圆形邻域，注意力得分随空间距离指数衰减
- 采用免训练的熵→预算→半径 pipeline：先根据query注意力熵计算专属token预算，再映射为带时间衰减的空间半径，生成结构化稀疏掩码，无需显式对key排序
- 配套工程优化：融合熵提取与softmax的CUDA kernel、warm-up阶段熵全局复用、块稀疏掩码自动构造，额外开销可忽略，兼容FlashInfer等主流推理引擎
### 关键实验
覆盖Wan2.1、Wan2.2、HunyuanVideo共7种文本/图像转视频配置（参数规模1.3B-14B，720P分辨率），对比SVG、SVG2、Radial等免训练稀疏注意力基线：仅保留9%-19%的注意力交互，实现1.56×-2.05×端到端提速，VBench评分与全稠密attention几乎持平，PSNR比基线最高高出10dB。

**最值得记住的结论**：Token级自适应稀疏注意力不需要额外训练或参数，仅利用注意力本身的统计规律就能实现质量与效率的极佳平衡。
