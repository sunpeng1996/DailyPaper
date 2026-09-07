---
title: Necessary or Sufficient? Evaluating LLM Explanations With Behavioural Evidence
title_zh: 必要还是充分？基于行为证据的大模型解释评估
authors:
- Urja Pawar
- Rajitha Ramanayake
- Nabeel Kemal
- Ashwin Kandath
- Owen O'Neill
- Guillaume Bourgeon
- Houssem Chatbri
affiliations:
- BNY
arxiv_id: '2609.05385'
url: https://arxiv.org/abs/2609.05385
pdf_url: https://arxiv.org/pdf/2609.05385
published: '2026-09-04'
collected: '2026-09-07'
category: Eval
direction: LLM可解释性 · Agent工作流监管评估
tags:
- LLM Explainability
- Agent Oversight
- Black-box Evaluation
- Necessity Test
- Sufficiency Test
one_liner: 提出黑盒评估框架，量化验证Agent工作流中LLM决策解释的必要性与充分性可信度
practical_value: '- 落地Agent推荐/内容审核场景时，可复用必要性+充分性黑盒校验逻辑，快速排查LLM解释的虚假性，避免基于错误解释做故障归因

  - 电商个性化推荐场景如果引入LLM生成推荐理由，可参考该框架对Top影响因子做校验，提升理由可信度，降低用户投诉

  - 可直接复用该轻量评估框架，不需要模型白盒权限，即可对不同基座LLM的解释可靠性做横向对比选型'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
Agent工作流中LLM决策常附带解释用于系统监控、故障排查，但现有应用默认解释与实际决策行为一致，缺乏可落地的可靠性校验方法。
### 方法关键点
基于黑盒干预构造两个评估维度：必要性（修改因子是否会改变输出）、充分性（仅保留因子是否能维持原输出），分别计算对应得分，和LLM输出的Top3影响因子排序做相关性校验。
### 关键结果数字
在顾问推荐、prompt风险审核两个场景测试8款Claude/GPT/Gemini系列模型：顾问推荐场景下解释排序与必要性、充分性得分的平均Spearman相关仅为0.349、0.354，57%以上的案例存在未提及因子影响力高于排名最低的提及因子；prompt审核场景相关度为0.431、0.580，对应错误率为25.8%、8.9%。整体LLM给出的解释仅含部分有效信息，无法可靠对应实际决策影响因子。
