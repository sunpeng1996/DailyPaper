---
title: Auditing Post-Training Unlearning in Diffusion Language Models using Sparse
  Autoencoders
title_zh: 基于稀疏自编码器的扩散语言模型训练后去学习审计
authors:
- Yunha Seo
- Changhoon Kim
affiliations:
- Soongsil University
arxiv_id: '2611.27652'
url: https://arxiv.org/abs/2611.27652
pdf_url: https://arxiv.org/pdf/2611.27652
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: 扩散大语言模型 · 训练后去学习
tags:
- Diffusion Language Model
- Machine Unlearning
- Sparse Autoencoder
- LLaDA
- Privacy Protection
one_liner: 针对扩散语言模型训练后去学习空白，用稀疏自编码器对比静态与自适应特征抑制的遗忘-保留效果
practical_value: '- 业务侧若需对生成式推荐/Agent所用扩散LLM做敏感数据擦除，可复用本研究的稀疏自编码器特征定位方法，快速锁定待遗忘数据关联的隐层特征

  - 做LLM去学习工程实现时可优先验证静态特征抑制方案，本研究证明阶段自适应动态抑制无显著收益，可降低不必要的开发复杂度

  - 扩散LLM去学习的效果验证可直接复用WMDP基准和去噪状态回放的评估流程，减少自建评估体系的成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前机器去学习研究主要针对自回归LLM，面向扩散语言模型（DLM）的训练后去学习机制仍缺乏实证支撑，需明确跨去噪阶段的特征抑制策略对遗忘效果与保留能力的trade-off影响。

### 方法关键点
1. 以LLaDA-8B-Instruct为实验基底，采用WMDP作为预训练知识遗忘域基准
2. 用top-k稀疏自编码器定位待遗忘数据关联的隐层特征，结合去噪状态回放技术，对比静态特征抑制、阶段自适应特征抑制两种方案的表现

### 关键结果
待遗忘数据关联的特征在不同去噪阶段存在显著偏移，但仅跟踪该动态变化无法在测试操作点上可靠提升遗忘-保留trade-off，为DLM训练后去学习隐私机制的开发与评估提供了初始实证基础。
