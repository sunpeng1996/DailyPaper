---
title: Embedding Prediction Helps Image Generation
title_zh: 嵌入预测优化扩散Transformer图像生成性能
authors:
- Sihan Xu
- Ji Xie
- Zilin Wang
- Hui Shen
- Stella X. Yu
affiliations:
- University of Michigan
- Carnegie Mellon University
arxiv_id: '2610.02203'
url: https://arxiv.org/abs/2610.02203
pdf_url: https://arxiv.org/pdf/2610.02203
published: '2026-10-01'
collected: '2026-10-03'
category: Other
direction: 扩散Transformer 动态生成条件优化
tags:
- Diffusion Transformer
- Embedding Prediction
- Image Generation
- Dynamic Conditioning
- Compute Efficiency
one_liner: 提出NEPA动态嵌入预测框架，为扩散Transformer每步提供自适应条件，降训练算力同时提生成效果
practical_value: '- 电商AIGC商品图/营销文案生成场景，可借鉴动态条件更新思路，每步根据当前生成状态重新计算condition embedding，替代固定prompt
  embedding，提升生成内容和业务需求的匹配度

  - 算力受限的生成类业务优化，可参考「预训练嵌入预测模块+轻量生成器」的架构拆分思路，在推理开销增加可控的前提下，大幅降低整体训练算力成本

  - LLM4Rec/生成式推荐的序列生成场景，可复用NEPA的自回归连续嵌入预测思路，为动态推荐提示生成、多轮交互推荐的条件建模提供新路径'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
扩散Transformer生成过程中，class/text条件嵌入仅计算1次，所有去噪步复用固定条件，无法适配不同噪声阶段的生成需求，且现有SOTA方案训练算力成本极高。

### 方法关键点
1. 提出Next-Embedding Predictive Autoregression（NEPA）模块，基于输入条件和带噪图像，自回归预测对应干净图像的连续嵌入序列
2. 设计Multi-Embedding Prediction实现一次前向生成全部目标嵌入，每步去噪前重新计算动态嵌入作为DiT生成器的条件，适配当前噪声状态

### 关键结果
在ImageNet 256×256分类条件生成任务上，NEPA-DiT-XL仅用REPA 1/3的训练算力，即可达到FID 1.32的优异生成效果
