---
title: Do People Trust AI Assistants Even When They Are Consistently Wrong?
title_zh: 即便AI助理持续出错，人们仍会信任它吗？
authors:
- Cameron R. Jones
- Julia Wong
- Aaron S. Cohen
- James Woolley
- Benjamin K. Bergen
affiliations:
- Stony Brook University, Department of Psychology
- University of California San Diego, Department of Cognitive Science
arxiv_id: '2611.14833'
url: https://arxiv.org/abs/2611.14833
pdf_url: https://arxiv.org/pdf/2611.14833
published: '2026-11-10'
collected: '2026-11-13'
category: Eval
direction: LLM信任评估 · 人机交互
tags:
- LLM
- Trust
- Human-AI Interaction
- User Behavior
- Evaluation
one_liner: 通过4组对照实验揭示人类对LLM助手的信任校准规律，无反馈时全错LLM仍能说服近半数用户，信任度高于人类助手
practical_value: '- 电商导购Agent上线初期需严格保障前10-20次交互准确率，用户初始信任度极高，仅在出现明确错误时才会快速下跌，早期错误会直接流失用户

  - 推荐/导购类Agent必须配套错误结果的用户反馈入口+事后校验机制，无反馈场景下即便持续输出错误推荐仍会误导用户，极易引发合规/客诉风险

  - 同场景下用户对LLM助手的信任度天然高于人类客服（83% vs 65%），高准确率LLM承接高价值咨询场景的转化效果优于人工，可优先落地'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
用户越来越依赖对话式AI做消费、工作等各类决策，但多轮交互场景下人类对LLM准确率的信任校准机制未被量化，无真实反馈场景下的过度依赖风险不明确。
### 方法关键点
设计4组对照实验，控制AI助手准确率分为100%（有帮助）、0%（完全错误）、50%（混合）三类，变量包含是否提供模型准确率的外部反馈，同时对比人类助手与LLM助手的信任差异。
### 关键结果数字
1. 有外部反馈时，用户对有帮助/无帮助LLM的信任率为67%/21%；无反馈时，持续全错的LLM仍有48%概率说服用户，反而高于对正确LLM的38%信任率
2. 用户对LLM的初始信任度极高，仅在出现明确错误证据时信任度才会下降
3. 用户对LLM助手的信任度显著高于人类助手（83% vs 65%），优秀历史记录对LLM信任的增益远高于人类
