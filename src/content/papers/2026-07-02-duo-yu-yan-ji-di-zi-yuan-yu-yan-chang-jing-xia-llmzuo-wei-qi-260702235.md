---
title: Challenges and Recommendations for LLMs-as-a-Judge in Multilingual Settings
  and Low-Resource Languages
title_zh: 多语言及低资源语言场景下LLM作为评判器的挑战与实践建议
authors:
- A. Seza Doğruöz
- Xixian Liao
- Verena Blaschke
- Jakob Prange
- Senyu Li
- David Ifeoluwa Adelani
affiliations:
- Universiteit Gent
- Barcelona Supercomputing Center
- LMU Munich
- Mila - Quebec AI Institute
- McGill University
arxiv_id: '2607.02235'
url: https://arxiv.org/abs/2607.02235
pdf_url: https://arxiv.org/pdf/2607.02235
published: '2026-07-02'
collected: '2026-07-03'
category: Eval
direction: LLM评估 · 多语言低资源场景实践
tags:
- LLM-as-a-Judge
- Multilingual Evaluation
- Low-resource NLP
- Evaluation Paradigm
- LLM Evaluation
one_liner: 调研多语言低资源场景LLM-as-a-Judge现状，输出可落地的评估优化指引
practical_value: '- 跨境多语言电商的生成式文案、推荐理由、多语言Query改写效果评估，不要直接复用单语言LLM-as-a-Judge方案，必须补充少量小语种人工标注校验偏差

  - 多语言场景下做LLM效果评估，避免仅采用单款评判模型，至少选用2-3款不同基座的LLM做交叉校验，降低结果不一致性

  - 低资源小语种业务评估可先将待评估内容翻译为英语，再用成熟的英语LLM-as-a-Judge评估，同时补充小语种人工评估子集做结果校准'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM-as-a-Judge已成为NLG任务主流评估范式，与人工判断相关性高且成本远低于纯人工评估，但现有实践大多针对英语场景，拓展至多语言尤其是低资源语言时，存在LLM小语种能力不足、缺乏有效人工校验等问题，行业无统一实践规范。

### 方法关键点
调研ACL Anthology中650篇提及LLM-as-a-Judge的论文，仅筛选出33篇聚焦多语言/低资源场景的工作，对其评估流程、结果一致性、校验逻辑做深度系统性分析。

### 关键结果数字
现有多语言场景LLM-as-a-Judge评估存在三类核心问题：评估结果一致性差、普遍过度信任LLM评判结果、90%+研究仅依赖单款评判模型，基于分析结论输出了适配多语言低资源场景的全流程评估实践建议。
