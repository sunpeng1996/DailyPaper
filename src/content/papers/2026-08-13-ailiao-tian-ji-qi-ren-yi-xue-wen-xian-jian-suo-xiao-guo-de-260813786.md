---
title: Do AI chatbots find what experts would? Effects of model, user role, and sample
  size on study retrieval for medical questions
title_zh: AI聊天机器人医学文献检索效果的影响因素：模型、用户角色与样本量
authors:
- Qingfang Liu
- Qiao Jin
- Joe D. Menke
- Thorsten Kahnt
- Zhiyong Lu
affiliations:
- National Institute on Drug Abuse Intramural Research Program, National Institutes
  of Health
- National Library of Medicine, National Institutes of Health
- School of Information Sciences, University of Illinois Urbana-Champaign
arxiv_id: '2608.13786'
url: https://arxiv.org/abs/2608.13786
pdf_url: https://arxiv.org/pdf/2608.13786
published: '2026-08-13'
collected: '2026-08-17'
category: Eval
direction: LLM检索效果评估 · 影响因子分析
tags:
- LLM Evaluation
- Information Retrieval
- Citation Retrieval
- User Role Modeling
- Recall Analysis
one_liner: 对比3款主流LLM在三类用户角色下的医学文献检索表现，明确模型、角色、样本量对召回的影响
practical_value: '- 搭建面向多角色用户的RAG/检索Agent时，可针对性优化prompt角色设定，给高专业属性角色设置更高的召回目标，匹配用户对专业内容的需求

  - 检索排序模型可引入内容样本规模（电商场景对应商品销量、评价数、内容互动量等）作为强特征，符合LLM天然对高置信度大样本内容的偏好，提升用户感知相关性

  - 多LLM选型做检索Agent时，可参考本文的控制变量对比范式，针对业务场景做分层召回效果评测，筛选适配的基座模型'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有针对LLM回答专业问题时的检索效果研究多聚焦引用造假问题，缺少对检索内容质量、选择驱动因素的量化评估，尤其缺乏对新一代强推理能力模型的验证。
**方法关键点**：选取Claude Sonnet 5、Gemini 3.1 Pro、ChatGPT GPT-5.5三款通用LLM，基于2026年Cochrane系统评价数据库的20个临床问题，模拟患者、临床医生、证据合成研究者三类用户角色发起查询，每个模型-角色组合重复4次，共收集720条响应，以Cochrane官方纳入/排除研究集作为金标准评测。
**关键结果**：平均召回39.2%±29.8%的纳入研究，仅引用5.0%±9.4%的排除研究；ChatGPT召回率显著优于Claude、Gemini（63.1% vs 37.0% vs 17.3%，p=2e-5）；研究者角色召回率高于临床医生、患者角色（42.8% vs 38.6% vs 36.1%，p=2e-5）；控制发表年份、引用量、开放获取状态后，log样本量每提升1单位，检索odds ratio提升1.80（95%CI 1.37-2.36，p=2.34e-5），是唯一独立显著预测因子，LLM存在大样本研究的检索偏好。
