---
title: 'From SRA to Self-Flow: Data Augmentation or Self-Supervision?'
title_zh: 从SRA到Self-Flow：是数据增强还是自监督？
authors:
- Dengyang Jiang
- Mengmeng Wang
- Harry Yang
- Jingdong Wang
affiliations:
- The Hong Kong University of Science and Technology
- Zhejiang University of Technology
- Baidu Inc.
arxiv_id: '2607.02508'
url: https://arxiv.org/abs/2607.02508
pdf_url: https://arxiv.org/pdf/2607.02508
published: '2026-07-01'
collected: '2026-07-03'
category: Training
direction: 扩散Transformer训练优化
tags:
- Diffusion Transformer
- Data Augmentation
- Self-Supervision
- Attention Mechanism
- Training Optimization
one_liner: 揭示Self-Flow性能提升本质为噪声维度数据增强，提出注意力分离优化扩散Transformer训练
practical_value: '- 做电商广告素材、生成式推荐的Diffusion模型训练时，可直接复用双时间步+注意力分离的无标注数据增强trick，提升生成质量同时加速收敛

  - 针对自监督训练策略的性能归因，可参考本文变量控制思路（隔离注意力交互验证贡献来源），快速定位核心增益点，减少无效优化尝试

  - 多噪声水平输入训练场景下，无需强行引入跨噪声token交互，用注意力分离简化架构即可获得数据增益，降低工程实现复杂度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
扩散Transformer自对齐方法SRA、Self-Flow可无需外部预训练编码器提升生成质量，但Self-Flow的双时间步调度增益此前被错误归因于跨噪声level的token交互，底层机制未被验证。
### 方法关键点
提出Attention Separation机制，保持Self-Flow的双时间步输入不变的同时，阻断不同噪声level分配的token之间的注意力交互，隔离「跨噪声token交互」和「噪声维度数据增强」两个潜在增益因子做对照实验。
### 关键结果
1. 移除跨噪声token交互后模型性能无下降甚至有所提升，证明Self-Flow的性能提升核心来自噪声维度的数据增强，而非token交互；
2. Attention Separation本身可将单样本拆分为多个有效训练部分，实现训练数据扩增；
3. 结合自表示对齐、双时间步、注意力分离的方案在ImageNet上验证了有效性。
