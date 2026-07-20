---
title: 'Expanding the Lexicon of Ge''ez Based African Languages: A Comparative Study
  of Amharic and Tigrinya'
title_zh: 面向吉兹语系非洲语言的词汇扩展：阿姆哈拉语与提格里尼亚语对比研究
authors:
- Hailay Kidu Teklehaymanot
- Debela Desalegn Yadeta
- Wolfgang Nejdl
affiliations:
- L3S Research Center, Leibniz University Hannover, Germany
- Addis Ababa University, Ethiopia
arxiv_id: '2607.15209'
url: https://arxiv.org/abs/2607.15209
pdf_url: https://arxiv.org/pdf/2607.15209
published: '2026-07-16'
collected: '2026-07-20'
category: LLM
direction: 低资源多语言LLM词汇扩展优化
tags:
- Multilingual-LLM
- Low-resource-NLP
- Tokenizer
- XLM-R
- Vocabulary-Extension
one_liner: 针对低资源吉兹语系语言优化XLM-R词汇与训练策略，提升多语言下游任务表现
practical_value: '- 垂直领域/小语种LLM适配可复用该词汇扩展方案：训练专属SentencePiece分词器扩充基础模型词表，新增嵌入用原模型子词嵌入平均初始化，避免从零训练嵌入

  - 两阶段训练策略可直接复用：先在领域/语种语料上做扩展词表的持续MLM预训练，再下游微调，兼顾基础模型泛化性和领域适配效果

  - 跨境电商小语种站点的搜索/推荐/客服LLM适配可参考该方案，无需全量重训大模型即可大幅提升低资源语言任务性能，降低适配成本'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有多语言预训练模型以拉丁脚本为核心训练，在非拉丁低资源语言上OOV率高、子词碎片化严重，性能退化显著。
### 方法关键点
1. 针对阿姆哈拉语、提格里尼亚语两类高资源吉兹语系语言，训练专属SentencePiece分词器，为XLM-R扩展30000个吉兹语子词，新增嵌入用原XLM-R分词器对应子词嵌入平均初始化
2. 采用两阶段训练：先在专属语料上做扩展词汇的掩码语言建模持续预训练，再在QA、NER、情感分析任务上做有监督微调
### 关键结果
- 阿姆哈拉/提格里尼亚QA任务：EM 87.0、F1 90.0，较XLM-R分别提升21、12个点
- 情感分析任务：准确率80.0%，较XLM-R提升3个百分点
- 11种可做OOV分析的语言平均OOV实体识别准确率从81.4%提升至94.3%，效果可迁移到17种同语系未扩充词表的低资源非洲语言
