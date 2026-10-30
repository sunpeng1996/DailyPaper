---
title: What Hallucinations Have We Measured? Semantic Illusion, Confabulation, and
  Expressed Uncertainty
title_zh: 大语言模型幻觉分类框架：语义错觉、虚构与表达不确定性的区分
authors:
- Hazel H. Kim
- Jakub Binkowski
- Ekaterina Fadeeva
- Juan David Guerra
- Yijie Hao
- Zheng Yi Ho
- Baixiang Huang
- Buyun Liang
- Siyuan Liang
- Anh Tuan Luu
affiliations:
- University of Oxford
- ETH Zurich
- Meta (FAIR)
- MBZUAI
- Nanyang Technological University
arxiv_id: '2610.38520'
url: https://arxiv.org/abs/2610.38520
pdf_url: https://arxiv.org/pdf/2610.38520
published: '2026-10-28'
collected: '2026-10-30'
category: LLM
direction: 大语言模型 · 幻觉检测与缓解
tags:
- Hallucination
- LLM
- Uncertainty Estimation
- Semantic Illusion
- Confabulation
one_liner: 提出LLM错误三类划分框架与标注协议，明确不同幻觉类型的检测与缓解方法适配性
practical_value: '- 做Agent/RAG/GenRec系统的幻觉检测时，先做10次语义等价prompt重触发测试判定错误类型：如果是语义错觉(SI)，无需引入RAG/微调，改prompt/解码参数即可解决，大幅降低优化成本

  - 幻觉效果评估需拆分UNK(表达不确定性)、SI、CF三类指标，避免把识别到"I don''t know"的能力当成幻觉检测效果好，实际漏掉高风险的自信错误

  - 对虚构类(CF)错误，优先用latent信号做检测，配合RAG引入外部知识缓解，无需浪费精力做prompt调优，实验证明调优对CF缓解率仅0.7%~2.8%

  - 生成式推荐的商品/文案生成校验可复用该分类框架，区分错误是模型未学到商品知识(CF)还是prompt引导偏差(SI)，针对性优化迭代'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM幻觉是产业落地的核心安全障碍，但业界对幻觉的定义长期混乱，常将表达不确定性、可通过prompt修正的错误、确实缺乏知识的错误混为一谈，导致评估结果失真、缓解方法适配错误，浪费大量研发资源。

### 方法关键点
- 重新定义幻觉为**自信的错误回答**，明确表达不确定性(UNK，如主动回复"我不知道")不属于幻觉范畴
- 用重触发测试划分两类幻觉：语义错觉(SI，任意语义等价prompt/解码参数能召回正确答案，说明模型具备对应知识只是未正确调用)；虚构(CF，所有重触发都返回自信错误，说明知识缺失/不可访问)
- 提出仅需10个左右语义等价prompt的低成本标注协议，标签稳定性可达Cohen's κ≈0.8，可落地性强

### 关键实验
基于TriviaQA、SimpleQA闭箱QA数据集，在Llama 3.1 8B、Gemma 3 12B上测试14种2021~2025年的SOTA幻觉检测/缓解方法，核心结果：
1. 现有方法对SI的缓解率达28%~29%，对CF的缓解率仅0.7%~2.8%，仅引入外部知识的方法能将CF缓解率提升到约20%
2. 现有不确定性检测器对UNK的打分高于SI/CF，即把非幻觉的不确定回答判定为最高概率幻觉，且漏检50%的CF
3. 不同信号适配不同错误类型：verbal信号检测UNK最优，语义一致性信号缓解SI最优，latent信号检测/缓解CF最优

### 核心金句
在引入RAG/微调解决幻觉问题前，先做重触发测试区分错误类型，60%以上的非知识缺失类幻觉可通过低成本的prompt/解码优化解决
