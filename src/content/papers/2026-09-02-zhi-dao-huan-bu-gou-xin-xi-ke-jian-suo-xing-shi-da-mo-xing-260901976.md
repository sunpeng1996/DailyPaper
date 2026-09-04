---
title: 'Knowing Is Not Enough: Information Retrievability as a Precondition to Effective
  LLM Oversight'
title_zh: 知道还不够：信息可检索性是大模型有效人工监督的前置条件
authors:
- Xinyu Fu
- Narayan Ramasubbu
- Dennis Galletta
affiliations:
- Georgia State University
- University of Pittsburgh
arxiv_id: '2609.01976'
url: https://arxiv.org/abs/2609.01976
pdf_url: https://arxiv.org/pdf/2609.01976
published: '2026-09-02'
collected: '2026-09-04'
category: LLM
direction: LLM人工监督 · 错误检出优化
tags:
- LLM Oversight
- Error Detection
- Retrievability
- Self-explanation
- Retrieval Cues
one_liner: 通过640名一线员工实验验证，自解释与检索提示可显著提升LLM输出人工校验的错误检出率
practical_value: '- 搭建LLM辅助客服/商品文案生成的人在回路审核链路时，可要求审核人员上岗前先自主生成校验规则解释，无需复杂培训即可提升错误检出率

  - 高频审核LLM生成的推荐话术、活动文案时，可在审核界面固定展示校验规则检索提示，有效缓解审核疲劳导致的错漏判

  - 落地面向一线运营/客服的LLM辅助工具时，轻量的自解释引导+日常检索提示的成本远低于重度培训，投入产出比更高'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
企业大规模将LLM落地到客服回复、内容生成等业务场景时，人在回路审核作为最后安全屏障常漏过LLM错误，现有研究多将漏判归因于审核者能力不足或参与度低，未关注审核时刻相关校验信息的可检索性影响。

### 方法关键点
面向640名客户-facing一线员工开展两组随机田野实验，测试两类轻量干预效果：1）上岗前要求审核者自主生成校验规则的自我解释；2）审核过程中插入可重新激活校验逻辑的检索提示。

### 关键结果
自生成解释可显著提升错误检出率，同时强化审核者对校验逻辑的长时记忆；配合检索提示可有效缓解长时间重复使用LLM后的审核疲劳，维持稳定的错误检出能力，两类干预均无需复杂培训即可快速落地。
