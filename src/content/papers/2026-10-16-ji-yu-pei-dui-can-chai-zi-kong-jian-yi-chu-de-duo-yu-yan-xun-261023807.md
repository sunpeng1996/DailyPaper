---
title: 'Steering beyond Language: Improving Multilingual Training-Free Text Embeddings
  via Paired-Residual Subspace Removal'
title_zh: 基于配对残差子空间移除的多语言免训练文本嵌入优化
authors:
- Ailiang Lin
- Zhuoyun Li
- Yusong Wang
- Keyu Mao
- Kotaro Funakoshi
- Manabu Okumura
affiliations:
- Institute of Science Tokyo
- Tencent
arxiv_id: '2610.23807'
url: https://arxiv.org/abs/2610.23807
pdf_url: https://arxiv.org/pdf/2610.23807
published: '2026-10-16'
collected: '2026-10-19'
category: RAG
direction: 多语言文本嵌入 · 推理时干预
tags:
- Text Embedding
- Multilingual
- Training-Free
- Activation Steering
- Subspace Removal
- LLM
one_liner: 提出PRSR推理时激活干预方法，无需微调即可提升冻结LLM的多语言文本嵌入效果
practical_value: '- 跨境电商多语言检索场景可直接复用PRSR方案，无需微调LLM即可大幅提升跨语言商品/Query语义匹配准确率，降低多语言模型部署成本

  - 多语言推荐/Agent的RAG模块可通过百级平行句对估计语言敏感子空间，提升跨语言召回准确率，快速适配小语种业务需求

  - 推理时激活干预思路可迁移至单语言垂直场景，通过移除领域敏感子空间提升电商客服、美妆等垂类的嵌入语义区分度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有免训练文本嵌入方法大多针对英文优化，多语言场景下存在严重的语言聚类问题：相同语义的跨语言句子嵌入距离甚至超过同语言不同语义句子的距离，36.2%的场景下同语言负样本比翻译正样本和锚点的相似度更高，导致跨语言检索、推荐匹配效果极差，而微调多语言嵌入模型成本高、迭代慢。

### 方法关键点
- 提出Paired-Residual Subspace Removal (PRSR)方法，完全不需要微调LLM参数，仅在推理时对中间激活做干预
- 基于多语言平行句对构造配对残差：同一语义的多语言句子隐状态减去组均值，残差即可表征语言相关偏差
- 对残差做SVD分解得到各层低秩语言敏感子空间，推理时将当前层最后token隐状态在该子空间的投影移除，再输入后续层
- 子空间仅需构建一次即可复用，适配所有评估语言，包括未参与子空间训练的小语种

### 关键结果
实验覆盖18种语言的208个单语言MTEB/MMTEB任务，以及英语与200+语言的跨语言双文本挖掘任务，对比5种主流免训练嵌入基线（PromptEOL、Pretended CoT、ECHO等），跨3个LLM backbone（LLaMA-2-7B、Mistral-7B、Qwen3-8B）均稳定提升：单语言任务平均提升6~7.3个点，跨语言任务FLORES平均提升18.5~23.96个点，BUCC.v2最高提升55.25个点，未参与子空间构建的8种小语种也获得稳定增益。

**最值得记住的一句话**：冻结LLM的表示中语言相关信息可通过低秩子空间分离，推理时移除该部分即可大幅提升多语言语义对齐效果，无需任何参数微调。
