---
title: 'ZipTok3D: High-Fidelity 3D Tokenization with Compact Token Prefixes'
title_zh: ZipTok3D：基于紧凑Token前缀的高保真3D Token化方法
authors:
- Mingda Lin
- Weijie Wang
- Zeyu Zhang
- Bowen Cui
- Yefei He
- Haoyu Zhao
- Yuanyu He
- Donny Y. Chen
- Feng Chen
- Bohan Zhuang
affiliations:
- Zhejiang University
- Monash University
- University of Adelaide
arxiv_id: '2609.01740'
url: https://arxiv.org/abs/2609.01740
pdf_url: https://arxiv.org/pdf/2609.01740
published: '2026-08-31'
collected: '2026-09-04'
category: Multimodal
direction: 3D表示学习 · 高保真紧凑Token化
tags:
- 3D Tokenization
- Representation Learning
- Nested Dropout
- Iterative Decoding
- Transformer
one_liner: 提出ZipTok3D 3D tokenizer，通过嵌套dropout与迭代解码实现极短token序列下的高保真3D重建
practical_value: '- 电商3D商品建模场景可复用嵌套dropout训练思路，优先将核心结构信息编码到前缀token，大幅降低3D内容存储与传输成本

  - 生成式3D内容推荐pipeline可接入该tokenizer，极短token序列能显著降低下游3D生成/检索的推理时延，适配端侧3D内容展示需求

  - 多模态检索场景可借鉴前缀渐进式编码思路，实现不同算力约束下的多粒度内容召回，平衡精度与计算开销'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有3D tokenizer要么基于空间区域组织隐表示，要么采用固定大小全局token集，在极低token预算下重建质量骤降，无法兼顾隐序列长度与几何保真度，制约3D生成下游任务的效率。
### 方法关键点
1. 嵌套dropout训练机制：编码后随机截断隐序列，要求每个保留前缀都可重建完整物体，强制核心几何信息优先编码到前缀token
2. 迭代解码架构：解码器复用参数共享的Transformer块，无需单独生成采样阶段即可从短前缀恢复细粒度几何
### 关键结果
相同token维度下，ShapeNet数据集上仅用1个token就达到32-token COD-VAE基线相当的重建质量，序列缩短32×；TRELLIS数据集上仅用4个token达到基线效果，序列缩短8×。
