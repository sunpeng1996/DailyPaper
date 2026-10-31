---
title: Does the Citation Matter? Quality, Grounding, and Physician-Rubric Accuracy
  of Google's AI Overviews for Medical Information
title_zh: Google医疗类AI搜索概览的引用质量、事实对齐度与医生评分准确性评估
authors:
- Sam Agnoli
- Brigid Reilly
- Lily Barna
- Emőke-Ágnes Horvát
affiliations:
- Northwestern University
arxiv_id: '2610.39339'
url: https://arxiv.org/abs/2610.39339
pdf_url: https://arxiv.org/pdf/2610.39339
published: '2026-10-29'
collected: '2026-10-31'
category: Eval
direction: 生成式搜索结果可信度评测
tags:
- Generative Search
- RAG Evaluation
- Grounding
- Information Credibility
- Medical QA
- Search Audit
one_liner: 针对3611个医疗问题评测Google AI搜索概览的信源质量、事实接地与医疗准确性，披露其多项核心指标缺陷
practical_value: '- 做RAG驱动的生成式搜索/商品/文案推荐时，不能默认引用信源即内容准确，需额外增加陈述与信源的事实一致性校验，不能仅靠检索排序的信源质量兜底

  - 高风险场景（如电商医药类商品推荐、合规要求高的广告文案生成）需建立领域专家制定的专属评测标尺，比通用可信度指标有效性更高

  - 生成式结果的引用率、接地率与最终准确率无强相关，不能仅将接地率作为上线前的核心验收指标'
score: 7
source: arxiv-cs.IR
depth: abstract
---

## 动机
Google AI搜索概览（AIOs）为用户搜索首条结果，替代用户完成信源筛选，医疗场景下错误信息易造成严重危害，缺乏系统多维度量化评估。
## 方法
选取3611个医疗基准问题，对比AIO与传统搜索Top5结果的信源选择、可信度，校验AIO陈述与引用源的接地性，对照医生撰写的评分标尺评估准确性。
## 结果
96.4%的医疗搜索返回AIO，仅引用44.4%的传统Top5结果，更倾向商业医疗出版商而非权威学术/政府信源，6项可信度指标中4项低于传统结果；仅56.7%的引用陈述匹配源内容，20.8%的事实性声明无引用；对照医生标尺总得分仅38.2%（准确率54.2%、完备性21.6%），22.2%的AIO包含预设有害错误内容，且接地性与准确率无相关性
