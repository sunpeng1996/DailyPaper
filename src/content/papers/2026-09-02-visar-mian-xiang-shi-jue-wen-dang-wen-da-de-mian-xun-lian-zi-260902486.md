---
title: 'ViSAR: Training-Free Adaptive-$k$ Retrieval for Visual Document Question Answering'
title_zh: ViSAR：面向视觉文档问答的免训练自适应k值检索方法
authors:
- Adrien Mialland
- Marc Plantevit
- Julien Gallois
- Céline Robardet
affiliations:
- INSA Lyon, CNRS, LIRIS UMR 5205
- EPITA Research Laboratory (LRE)
- Lowit
arxiv_id: '2609.02486'
url: https://arxiv.org/abs/2609.02486
pdf_url: https://arxiv.org/pdf/2609.02486
published: '2026-09-02'
collected: '2026-09-03'
category: RAG
direction: RAG检索优化 · 自适应k值
tags:
- RAG
- Adaptive Retrieval
- DocVQA
- LVLM
- Training-Free
one_liner: 免训练视觉文档RAG自适应检索方法，降延迟最高58.7%同时保持或提升答案准确率
practical_value: '- 现有多模态RAG系统可直接复用自适应k检索逻辑，替代固定top-k策略，无需额外训练就能在召回精度和推理延迟间做动态平衡，适配电商商品说明书、票据、用户评价等问答场景

  - 可借鉴查询-页、页-页三层交互加权思路优化现有ColBERT/ColPali等多向量检索的排序效果，无需微调编码器即可提升召回F1

  - 可利用页间相似度矩阵稀疏度作为RAG回答置信度的无监督信号，无需额外标注即可识别低置信度回答，触发人工干预或二次检索，适合电商客服Agent的容错机制设计'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有DocVQA的RAG流程普遍采用固定top-k检索文档页，无法适配查询复杂度：检索页数过多会升高LVLM推理延迟、引入无关上下文降低准确率，页数过少则会遗漏关键证据；现有自适应k方法多针对纯文本场景、需要额外训练，无法直接适配多模态视觉文档检索需求。

### 方法关键点
- 完全免训练：直接在晚交互编码器的embedding空间计算，无需微调编码器或LVLM，可适配任意多向量多模态检索器
- 三层交互加权：依次计算查询-页、页-查询、页-页的语义激活权重，构造查询感知的页间相似度矩阵，突出查询相关语义
- 自适应k值选择：基于页自相似度排序，构造最小化候选集相干性、最大化无关页泄露惩罚的成本函数J(k)，自动选择最优检索页数k*
- 工程优化：过滤权重全0的无效页、分块计算相似度矩阵，降低内存占用和计算开销

### 关键实验
基于MMLongBench、LongDocURL两个多页文档问答数据集，对比固定top-k、Largest-Gap、Score-Cluster等基线，适配ColPali、ColQwen2.5等多个视觉编码器和LVLM：
1. 端到端RAG延迟最高降低58.7%（MMLongBench，max-k=10），LongDocURL场景延迟降低38.5%
2. 回答准确率对比固定top-k保持或提升，跨60组配置中24组提升、36组持平，无显著下降
3. 页间相似度矩阵稀疏度与回答准确率正相关，稀疏度越高的查询回答准确率平均高15%以上

### 核心结论
晚交互多向量检索的语义结构本身就包含自适应检索所需的全部信息，无需额外训练就能实现精度和延迟的双重优化
