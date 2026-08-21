---
title: 'Automated Summarization of Financial News Using Large Language Models and
  Retrieval-Augmented Generation: An Early Empirical Study (Fall 2023)'
title_zh: 基于大语言模型与RAG的财经新闻自动摘要早期实证研究
authors:
- Pranav Chandaliya
affiliations:
- George Washington University
arxiv_id: '2608.19526'
url: https://arxiv.org/abs/2608.19526
pdf_url: https://arxiv.org/pdf/2608.19526
published: '2026-08-20'
collected: '2026-08-21'
category: LLM
direction: 大模型文本摘要 · RAG应用失效分析
tags:
- LLM
- RAG
- Summarization
- FAISS
- Financial NLP
one_liner: 对比Summarize Chains与RAG的财经新闻摘要效果，披露小模型下RAG的失效模式
practical_value: '- 结构化数值数据（如电商商品价格、销量、用户行为数值）转自然语言叙事的模板方法可直接复用，解决LLM无法处理表格的问题，适配生成式商品文案、用户画像生成场景

  - 小参数开源模型做长文本生成任务时，优先测试Summarize Chains类串行拼接方案，不要盲目上RAG：大k值下RAG会导致输出重复、事实幻觉，可减少业务侧试错成本

  - 多源异质数据（如电商商品详情、用户评价、交易数据、舆情数据）的摘要Pipeline架构可直接复用，适配电商商品/活动摘要、商家经营报告自动生成场景'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
金融分析师与投资者每日需处理海量财经新闻，人工梳理效率极低，漏看关键信息会直接影响投资决策，现有自动化摘要方案可靠性不足。
### 方法关键点
1. 搭建多源数据Pipeline，拉取新闻、公司背景、股价三类数据，开发模板将股价数值表转换为自然语言叙事，解决LLM无法直接处理表格的问题
2. 对比Summarize Chains、基于FAISS的RAG两种摘要方案，在Falcon-7B-Instruct、DistilBART-CNN、BART-Large三个开源模型及GPT-3（text-davinci-003）上开展测试
### 关键结果
- Falcon-7B搭配Summarize Chains效果最优，新闻事件覆盖准确连贯
- RAG在k值较大时会导致Falcon输出严重重复、BART-Large出现事实幻觉
- 两类LLM摘要方案的ROUGE-1指标均优于Lead-3基线
