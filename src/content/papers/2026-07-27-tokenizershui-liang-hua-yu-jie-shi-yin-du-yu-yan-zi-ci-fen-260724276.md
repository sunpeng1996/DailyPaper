---
title: 'The Tokenizer Tax: Quantifying and Explaining the Cross-Lingual Cost of Subword
  Tokenization for Indian Languages'
title_zh: Tokenizer税：量化与解释印度语言子词分词的跨语言代价
authors:
- Priyansh Srivastava
affiliations:
- Sirena Ai, India
arxiv_id: '2607.24276'
url: https://arxiv.org/abs/2607.24276
pdf_url: https://arxiv.org/pdf/2607.24276
published: '2026-07-27'
collected: '2026-07-28'
category: LLM
direction: 多语言LLM 子词分词公平性优化
tags:
- Tokenizer
- Multilingual LLM
- BPE
- Cross-lingual NLP
- Fairness
one_liner: 量化主流分词器对印度语言的额外分词开销，揭示成因并验证可通过多语言分词器大幅缓解
practical_value: '- 布局东南亚、南亚等多语言市场的电商/广告Agent/推荐业务，优先选用o200k_base、XLM-R等多语言分词器，可大幅降低小语种token开销，提升上下文窗口利用率

  - 核算多语言LLM调用成本时，需按不同语言的分词倍率做预算，避免按英语token数预估导致的上下文溢出、成本超支问题

  - 针对特定小语种垂直业务场景，可基于业务语料补充训练BPE合并规则，进一步降低本地语言分词税，优化推理速度与成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
主流LLM子词分词器多基于英语语料训练，非英语语言存在被忽视的分词效率损失，直接影响多语言应用的上下文利用率、调用成本与实际效果。
### 方法关键点
基于FLORES-200平行语料，量化6种主流分词器在14种语言的分词生育率（单位语义内容对应的token数量），定位分词税的核心成因是BPE合并失败。
### 关键结果
- cl100k_base（GPT-3.5/4所用）下印度语言平均分词税为英语的8.0x，马拉雅拉姆语最高达13.0x，对应有效上下文窗口仅为英语用户的12%
- BPE合并失败率与分词税的皮尔逊相关系数r=0.89，为核心影响因子
- XLM-R、o200k_base等多语言分词器可降低73%的平均印度语言分词税
- 分词生育率与下游阅读理解效果的相关性本质由语料资源丰富度决定，与分词行为无直接因果
