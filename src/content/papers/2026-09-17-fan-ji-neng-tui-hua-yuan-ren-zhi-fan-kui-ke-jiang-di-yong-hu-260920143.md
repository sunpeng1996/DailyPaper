---
title: 'Designing Against Deskilling: Metacognitive Feedback Reduces Cognitive Offloading
  to LLM Assistants'
title_zh: 反技能退化：元认知反馈可降低用户对LLM助手的认知卸载
authors:
- Sebastian Maier
- Kai Schwabe
- Manuel Schneider
- Stefan Feuerriegel
affiliations:
- LMU Munich
- Munich Center for Machine Learning (MCML)
arxiv_id: '2609.20143'
url: https://arxiv.org/abs/2609.20143
pdf_url: https://arxiv.org/pdf/2609.20143
published: '2026-09-17'
collected: '2026-09-20'
category: LLM
direction: LLM用户交互 · 认知卸载干预
tags:
- LLM
- Cognitive Offloading
- Metacognitive Feedback
- Human-AI Interaction
- User Experiment
one_liner: 通过704人对照实验验证元认知反馈可降低LLM认知卸载并提升用户自主任务表现
practical_value: '- 设计商家/运营端AI辅助工具（如文案生成、选品Agent）时，可增加元认知反馈模块，明确告知过度依赖AI的能力退化风险，引导用户主动思考，避免长期使用后核心运营能力流失

  - 搭建C端导购/学习类AI产品时，可复用元认知反馈设计逻辑，平衡AI辅助效率和用户自主能力留存，提升长期用户粘性与产品价值

  - 做产品策略效果验证时，可参考该研究的2×2+空白对照组实验设计方法，量化不同干预策略的真实影响，减少主观判断偏差'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
用户向LLM进行认知卸载会大幅减少技能练习机会，带来长期技能退化风险，当前缺乏不限制AI使用权限前提下的有效干预方案。
### 方法关键点
设计两类干预策略：1）元认知反馈，明确告知用户认知卸载的负面影响；2）基于努力的奖励，激励用户减少LLM调用。开展704人预注册在线对照实验，任务为用户可自主选择是否调用LLM辅助完成分数运算练习，后续通过无辅助测试验证技能留存效果。
### 关键结果
- 元认知反馈可降低47%的答题卸载行为（OR = 0.47）
- 元认知反馈可提升51%的无辅助测试表现（OR = 1.51）
- 基于努力的奖励未观测到对两类结果的显著影响
