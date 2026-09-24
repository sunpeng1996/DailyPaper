---
title: 'GeoPair: Geometry-Preserving Cross-Layer Factorization for Training-Free Transformer
  Compression'
title_zh: GeoPair：保留几何特性的免训练Transformer跨层因子化压缩方法
authors:
- Baher Mohammad
- Ammar Ali
- Stamatios Lefkimmiatis
affiliations:
- MWS AI
- ITMO University
arxiv_id: '2609.25963'
url: https://arxiv.org/abs/2609.25963
pdf_url: https://arxiv.org/pdf/2609.25963
published: '2026-09-21'
collected: '2026-09-24'
category: LLM
direction: LLM免训练压缩 · 跨层参数共享
tags:
- Transformer Compression
- Training-Free
- Dictionary Learning
- Weight Factorization
- Model Optimization
one_liner: 提出免训练Transformer压缩框架，通过最优层配对与共享字典学习，高压缩比下保留90%+基线精度
practical_value: '- 电商/推荐场景中用于文案生成、个性化推荐理由生成的轻量化LLM，可直接复用GeoPair免训练压缩流程，无需大量标注数据微调，20%压缩比下精度损失<3%

  - 跨层参数配对可复用其提出的列空间对齐+Edmonds Blossom最优匹配策略，替代相邻层硬配对的启发式规则，相同精度下压缩比可提升10%以上

  - 稀疏系数优化可借鉴HTP+共轭梯度的实现方案，在保证压缩比的同时避免精度大幅下降，适合推荐系统低延迟LLM推理场景的性能优化'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Transformer后训练压缩方法要么独立优化单层，要么采用启发式相邻层分组，忽略各层激活的几何特性，高压缩比下精度损失严重，且大多需要后压缩微调，落地成本高，难以适配电商、推荐场景中快速迭代的轻量化LLM部署需求。

### 方法关键点
- 层配对阶段：提出白化空间Frobenius子矩阵距离度量层间结构相似度，通过Edmonds Blossom算法求解全局最优层匹配，替代相邻层硬分组启发式规则
- 共享字典学习：将双权重共享字典优化转化为广义Sylvester方程，通过广义特征值分解得到闭式解，保留各层独立的白化几何特性，无需协方差聚合
- 稀疏化阶段：集成Hard Thresholding Pursuit (HTP) 算法，在系数优化阶段引入ℓ0约束，进一步提升压缩比，同时保证收敛性

### 关键实验
在Llama3、Qwen3、Gemma3等1B-32B参数LLM，以及视频生成模型Wan2.2 5B上验证，对比Basis Sharing、SVDLLM、CoSpaDI等SOTA压缩方法：20%压缩比下，Llama3 8B平均精度恢复96.9%，仅比基线低2.19个百分点，视频生成CLIP分数仅下降0.01%；40%压缩比下精度仍恢复85%以上，大幅优于所有基线。

### 核心结论
免训练压缩的核心是保留各层激活的几何特性而非强制参数对齐，最优跨层结构匹配比启发式相邻层共享能带来翻倍的压缩收益。
