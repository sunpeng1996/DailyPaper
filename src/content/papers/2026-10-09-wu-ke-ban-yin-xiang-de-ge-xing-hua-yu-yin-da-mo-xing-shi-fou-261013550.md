---
title: 'Personalization Without Stereotyping: Do Speech LLMs Know When to Turn a Deaf
  Ear?'
title_zh: 无刻板印象的个性化：语音大模型是否知道何时该“充耳不闻”
authors:
- Kshitij Ambilduke
- Caroline Brun
- Thibaut Thonet
- Vassilina Nikoulina
- Marcely Zanon Boito
affiliations:
- Université Paris-Saclay, France
- NAVER LABS Europe, France
arxiv_id: '2610.13550'
url: https://arxiv.org/abs/2610.13550
pdf_url: https://arxiv.org/pdf/2610.13550
published: '2026-10-09'
collected: '2026-10-13'
category: Eval
direction: 语音LLM评测 · 个性化与偏见解耦
tags:
- Speech LLM
- Bias Evaluation
- Personalization
- Benchmark
- Demographic Robustness
one_liner: 提出BASIS-Bench基准，解耦语音LLM的个性化能力与刻板偏见，完成8款主流语音大模型评测
practical_value: '- 电商语音导购、智能客服类Agent选型时，可复用BASIS-Bench的三维度评测框架，提前验证模型对人口特征的使用边界，避免刻板印象引发用户投诉

  - 语音交互系统中若需输入显式用户人口标签，需配套新增偏见过滤模块，抵消显式标签对文本基座固有刻板关联的放大效应

  - 个性化策略设计需明确规则：仅在用户明确要求或场景强相关时调用人口特征，禁止无触发的人口特征关联推理'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
语音LLM可通过副语言线索实现更自然的个性化交互，但现有评测体系无法区分有益的个性化适配与有害的刻板偏见行为，缺少专门的基准解耦二者的边界。
### 方法关键点
提出BASIS-Bench评测基准，从三个独立维度完成评估：1）人口统计鲁棒性：衡量不同说话人群体在内容类任务的表现差异及模型的人口分类能力；2）刻板偏见：衡量模型感知到人口线索后是否会触发无提示的刻板行为；3）个性化：衡量模型在收到明确要求时，能否根据人口特征定制响应。
### 关键结果
对8款最新语音LLM的评测显示，多数模型可正确识别人口线索，但无法将其转化为合理的个性化响应；显式人口标签可提升个性化表现，但会同步放大文本基座已有的刻板关联。
