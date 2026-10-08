---
title: 'Nobody Truly Agrees on Sentiment: Humans, Bespoke Tools, and LLMs Struggle
  with Social Media Texts'
title_zh: 社交媒体文本情感分析一致性对比：人类、定制工具与LLM均有分歧
authors:
- Himarsha R. Jayanetti
- Sivakanesan Dhanushkanda
- Shuai Hao
- Michael L. Nelson
- Michele C. Weigle
affiliations:
- Old Dominion University, Virginia, USA
arxiv_id: '2610.10318'
url: https://arxiv.org/abs/2610.10318
pdf_url: https://arxiv.org/pdf/2610.10318
published: '2026-10-07'
collected: '2026-10-08'
category: Eval
direction: 情感分析工具评测 · 标注一致性
tags:
- Sentiment Analysis
- LLM Evaluation
- Annotation Consistency
- Social Media NLP
- RoBERTa
one_liner: 对比人类、定制情感工具、LLM在推特情感分析的标注一致性，给出工具选型与标注优化方向
practical_value: '- 做电商评论、社媒投放舆情的情感分析时，优先选用垂直领域微调的小模型，效果优于通用LLM，推理成本也更低

  - 情感标注任务优先采用二分类（负/非负、正/非正）替代三分类，可大幅提升标注一致性、降低标签噪声，适用于用户反馈分层、商品评价筛选等场景

  - 构建情感分析金标准标签时必须保留多人复核流程，不要盲目信任单一标注结果或通用工具输出，避免因情感主观性引发业务决策偏差'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
社媒是实时公众舆情的核心来源，但现有情感分析工具的应用普遍缺乏对其局限性的认知，情感标注的主观性问题长期被忽略。
### 方法关键点
选取100条推特样本，以6名人类标注者为基准，对比3款定制情感工具（TextBlob、VADER、Twitter-roBERTa-base）、3款通用LLM（Qwen3-32B、GPT-OSS-120B、Llama-4-17B）的标注一致性，用Cohen's kappa（ pairwise 对比）、Fleiss' kappa（多标注者对比）两个指标量化一致性。
### 关键结果
1. 即使是人类标注者，一致性仅为fair级别，印证情感分析的强主观性；
2. 二分类（负/非负、正/非正）场景下所有主体的一致性均显著高于三分类场景；
3. Twitter-roBERTa-base和人类标注的对齐度最高，优于其他定制工具和通用LLM，尤其在负/非负分类上表现突出；
4. 通用LLM之间一致性达到substantial级别，和人类对齐度为moderate到substantial，在正/非正分类上表现更优。
