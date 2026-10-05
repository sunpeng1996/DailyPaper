---
title: Adaptive Sparsity Optimization with Learnable Soft Top-K and Per-Term Thresholding
  for Efficient Retrieval
title_zh: 基于可学习软Top-K与逐词阈值的自适应稀疏检索优化
authors:
- Wentai Xie
- Parker Carlson
- Shanxiu He
- Tao Yang
affiliations:
- University of California, Santa Barbara
arxiv_id: '2610.02572'
url: https://arxiv.org/abs/2610.02572
pdf_url: https://arxiv.org/pdf/2610.02572
published: '2026-10-01'
collected: '2026-10-05'
category: RecSys
direction: 稀疏召回 · 自适应稀疏化效率优化
tags:
- Sparse Retrieval
- Top-K Pruning
- Per-term Thresholding
- Retrieval Efficiency
- LLM4Rec
one_liner: 提出软Top-K与逐词阈值协同的自适应稀疏检索方案，降存储延迟且保留高相关性
practical_value: '- 电商搜索/推荐稀疏召回场景可直接复用STop软Top-K正则：给原始Query/商品标题中的词加惩罚豁免，避免核心意图词被误剪，在压缩向量长度的同时保证召回相关性

  - 替换现有全局阈值剪枝为PTT逐词阈值：为每个token学习独立的剪枝阈值，适配不同词的权重分布，解决大词汇量LLM生成稀疏向量的长尾低权重冗余问题，进一步提升稀疏度

  - 三正则组合（FLOPs+STop+PTT）可零成本迁移到现有LLM稀疏检索训练流程：无需修改模型结构，仅在损失函数中加入对应正则项，即可实现4倍左右的存储与延迟下降，相关性损失可控制在1%以内'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
基于大词汇量LLM的稀疏检索方法（如Lion-SP）生成的query、document向量过于稠密，倒排索引存储成本高、检索延迟大，现有剪枝方案要么是固定硬剪枝易误删核心语义词，要么全局阈值无法适配不同词的权重分布，难以在保证相关性的前提下大幅提升稀疏度。

### 方法关键点
提出AdaSparse自适应稀疏化框架，通过三类互补策略协同优化：
1. **STop可学习软Top-K**：为每个向量设置与输入长度正相关的软K值，用sigmoid门控给K位外的非原始文本词加L2惩罚，训练时不硬剪枝，通过梯度引导模型自主压低冗余词权重，原始文本词自动豁免惩罚避免误删核心意图。
2. **PTT逐词阈值**：为每个token分别学习query、文档侧的独立剪枝阈值，用带温度的sigmoid实现软剪枝，训练时梯度可导，推理时直接滤除低于阈值的低权重项。
3. 联合原有FLOPs正则，三类损失加权加入排序损失协同优化：FLOPs压制大权重噪声，STop控制向量整体长度，PTT清除长尾低权重冗余。

### 关键实验
在MS MARCO、13个BEIR零样本数据集上基于Lion-SP-1B backbone测试：
- 相比原生Lion-SP-1B，query长度降69%、文档长度降73.4%，MS MARCO MRR@10几乎无损，BEIR NDCG@10仅降0.74%；
- 检索延迟降低3.8倍，倒排索引存储降低4.2倍；
- 效果优于固定Top-K、质量比剪枝MRP、全局阈值HT等所有基线，同等稀疏度下相关性最高。

### 核心结论
大词汇量LLM稀疏检索的稀疏化优化，向量级软Top-K+词级独立阈值+全局FLOPs正则的协同策略远好于单一剪枝方法，可实现几乎无损的效率数倍提升。
