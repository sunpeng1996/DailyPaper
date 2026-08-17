---
title: 'Information Satisfaction: A Reader-Centered Axis for Summarization Evaluation'
title_zh: 信息满意度：以读者为核心的摘要评估维度
authors:
- Isabel Cachola
- William Walden
- Reno Kriz
- Mark Dredze
affiliations:
- St. Edward’s University
- Johns Hopkins University
- Johns Hopkins University Human Language Technology Center of Excellence
arxiv_id: '2608.14457'
url: https://arxiv.org/abs/2608.14457
pdf_url: https://arxiv.org/pdf/2608.14457
published: '2026-08-14'
collected: '2026-08-17'
category: Eval
direction: LLM评估 · 用户中心摘要效果评测
tags:
- summarization_evaluation
- LLM-as-judge
- user_persona
- information_satisfaction
- human_evaluation
one_liner: 验证传统及LLM-as-judge摘要评估指标均无法匹配基于用户画像的信息满意度人工判断
practical_value: '- 做用户定向内容生成/摘要类业务（如商品详情页智能摘要、搜索结果个性化摘要）时，不要仅依赖ROUGE、BERTScore或通用LLM-as-judge评估，需加入用户画像维度的信息满意度校准

  - 电商场景下用户角色（如宝妈/数码发烧友）比单次query更稳定，可复用user persona作为个性化生成效果的评估核心信号，降低对query完备性的依赖

  - 落地LLM生成效果评估前，先做信息扰动测试验证指标敏感度，避免选用无法区分内容差异的无效评估指标'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有摘要评估指标仅关注通用质量或单一属性，无法衡量摘要对个体用户的实用价值；聚焦query的评估受限于用户query表述不全，无法覆盖差异化信息需求，而用户背景/角色（persona）更稳定，可作为评估的核心补充信号。
### 方法关键点
1. 对主流摘要评估指标（含SOTA LLM-as-judge）做信息扰动测试，验证其对信息差异、用户persona差异的敏感度
2. 开展专家人工评估，基于指定用户背景和使用场景，衡量用户对摘要的信息满意度偏好
### 关键结果
所有主流传统指标、LLM-as-judge指标均未通过基础信息内容扰动测试；两类指标与基于用户persona的信息满意度人工判断的一致性极差，完全无法替代人工评估用户真实需求的满足度
