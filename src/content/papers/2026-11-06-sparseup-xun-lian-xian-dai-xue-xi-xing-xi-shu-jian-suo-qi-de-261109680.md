---
title: 'SPARSEUP: Towards Better Recipes for Training Modern Learned Sparse Retrievers'
title_zh: SPARSEUP：训练现代学习型稀疏检索器的优化方案
authors:
- Thibault Formal
- Pierre Erbacher
- Cosimo Rulli
affiliations:
- Linkup, Paris
arxiv_id: '2611.09680'
url: https://arxiv.org/abs/2611.09680
pdf_url: https://arxiv.org/pdf/2611.09680
published: '2026-11-06'
collected: '2026-11-09'
category: RecSys
direction: 稀疏召回 · 学习型稀疏检索器训练
tags:
- Sparse Retrieval
- Learned Sparse Retriever
- Splade
- Information Retrieval
- Recall
- BEIR
one_liner: 通过三项低成本训练优化，实现150M参数下公开词表稀疏检索器Beir-13 SOTA
practical_value: '- 训练Splade类稀疏召回模型时可直接复用logit shifting技巧：取小样本统计的logit分布99.9百分位作为偏移值θ，大幅提升训练稳定性，解决ModernBERT、RoBERTa等现代骨干训练稀疏模型不收敛的问题

  - 新增per-position fan-out控制（推荐f取8~12），比单纯增加FLOPS正则更易管控稀疏度，同时检索效果损失更小，适合电商搜索、推荐首召等对延迟要求高的场景

  - 针对字节级BPE的词表冗余问题，可直接复用无参数的vocabulary folding策略，训练、推理阶段均生效，无需额外预训练即可提升大小写、前后缀变体的词匹配准确率

  - 若业务需要极低延迟召回，可在训练阶段就固定top-k稀疏度：k=64时比无约束训练后推理剪枝的效果高4个点nDCG，适合大流量的搜索suggestion、商品召回场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
学习型稀疏检索兼具精准 lexical 匹配能力与高检索效率，在稀有词匹配场景表现优于稠密检索，但训练收敛条件苛刻，难以适配ModernBERT等现代编码器，效果长期落后于稠密、晚交互模型，亟需可落地的训练优化方案。

### 方法关键点
- **Logit Shifting**：激活前对logit减去偏移量θ（取小样本统计的logit分布99.9百分位值），解决现代编码器初始logit右移导致的梯度弱、训练不稳定问题，RoBERTa等此前难收敛的骨干也可正常训练
- **Per-position Fan-out控制**：每个输入token位置仅保留得分最高的f个（推荐取8~12）词表维度激活，比FLOPS正则或后剪枝更易平衡稀疏度与检索效果，降低优化负担
- **Vocabulary Folding**：无参数合并BPE词表中同一单词的大小写、带/不带空格前缀的变体，训练推理均生效，无需额外预训练即可解决跨形态词匹配失效问题，词表维度从约50k压缩至34k

### 关键实验
在Beir-13数据集测评，150M参数以下公开词表稀疏检索器中，SPARSEUP达到56.4 nDCG@10，较此前SOTA提升1.8；与同数据同骨干的稠密模型DenseOn仅差1.5个点，推理延迟低于1ms/query；去污染Beir测评中与稠密模型效果基本持平，在BRIGHT-Pro、FreshStack等垂直领域数据集上效果超过稠密模型。

### 核心结论
学习型稀疏检索的训练瓶颈主要来自初始化分布偏差、词表冗余、无约束激活，三项零/低成本优化即可让稀疏检索效果追平稠密检索，同时保持低延迟优势。
