---
title: 'AURORA-LM: Autoencoding Unified Representation for Continuous-Latent Diffusion
  Language Modeling'
title_zh: AURORA-LM：面向连续隐空间扩散语言建模的自编码统一表征
authors:
- Jiajun Liang
- Yucheng Liao
- Yukang Cao
- Jiazhe Wei
- Ken Li
- Wende Tan
- Jiankun Zhang
- ZY Cui
- Jingkang Yang
- Liucheng Guo
affiliations:
- PRLab, Nanjing University
- S-Lab, Nanyang Technological University
- Imperial College London
arxiv_id: '2608.02602'
url: https://arxiv.org/abs/2608.02602
pdf_url: https://arxiv.org/pdf/2608.02602
published: '2026-08-03'
collected: '2026-08-04'
category: LLM
direction: 扩散语言建模 · 连续隐空间表征构建
tags:
- DiffusionLM
- ContinuousLatent
- FlowMatching
- Autoencoder
- TextGeneration
one_liner: 提出表征与生成建模解耦的连续隐空间扩散语言模型，性能优于同类型公开基准
practical_value: '- 生成式推荐的商品文案、推荐理由生成场景，可复用高低维解耦设计：仅对噪声输入通路做低秩压缩，保留全维干净隐变量用于解码，平衡生成质量与推理效率；

  - 多模态电商内容生成场景，可借鉴Query-based编解码器的因果前缀对齐设计，保证生成序列的上下文一致性，避免内容前后矛盾；

  - Agent会话/工具调用回复生成模块，可引入self-trajectory consistency训练trick，有效降低扩散采样步数，满足线上低延迟推理要求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有连续扩散语言模型存在两类设计缺陷：要么继承的嵌入空间未针对生成与解码联合优化，要么为降低扩散学习难度压缩自编码隐变量，导致token级生成保真度受损，亟需同时兼顾生成可行性与文本还原精度的建模方案。
### 方法关键点
- 表征与生成建模完全解耦：先训练Query-based编解码器得到高容量、前缀对齐的连续文本隐序列，冻结编解码器后单独训练扩散模型拟合隐变量分布，避免表征压缩损失解码精度；
- Block-causal扩散Transformer架构：块间遵循左到右因果生成逻辑，块内所有位置并行去噪，仅对噪声输入通路做低秩投影，保留全维干净隐变量作为预测目标；
- 训练优化策略：针对宽隐变量校准噪声层级分布，加大高噪声状态的训练权重，引入自轨迹一致性损失对齐去噪轨迹相邻状态的预测结果，大幅减少采样步数需求。
### 关键结果
在OpenWebText自由生成、XSum条件摘要任务上对比Diffusion-LM、Cola-DLM等所有公开连续/扩散语言模型基准，130M参数版本取得最优性能；1B参数版本在9个通用语言基准上超越更大参数量的公开隐扩散语言模型，OpenWebText MAUVE最高达0.82，XSum ROUGE-1相对提升2~3个百分点。

最值得记住的结论：无需为适配生成模型简化表征，保留高容量可解码隐变量、针对性优化扩散模型设计，反而能同时获得更高的生成质量与还原保真度
