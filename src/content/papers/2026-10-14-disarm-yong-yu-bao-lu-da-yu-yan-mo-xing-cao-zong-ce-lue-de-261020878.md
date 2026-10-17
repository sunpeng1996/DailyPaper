---
title: 'DISARM-ing the Hidden Puppetmaster: An Interface for Exposing Manipulative
  Tactics in Large Language Models'
title_zh: DISARM：用于暴露大语言模型操纵策略的交互界面
authors:
- Kynnedy Simone Smith
- Kantwon Rogers
- Priyal Shrivastava
- Motahhare Eslami
- Jocelyn Shen
- Maarten Sap
affiliations:
- Carnegie Mellon University
- Massachusetts Institute of Technology
arxiv_id: '2610.20878'
url: https://arxiv.org/abs/2610.20878
pdf_url: https://arxiv.org/pdf/2610.20878
published: '2026-10-14'
collected: '2026-10-17'
category: LLM
direction: 大模型交互安全 · 操纵行为干预
tags:
- LLM Safety
- Manipulation Detection
- Human-AI Interaction
- Real-time Intervention
- User Trust
one_liner: 提出实时识别披露大模型操纵策略的DISARM界面，降低78%用户受操纵的信念偏移
practical_value: '- 电商导购Agent、智能客服场景可复用实时话术检测框架，识别诱导下单、虚假宣传等操纵性话术，实时向用户披露或内部拦截，降低合规风险与客诉率

  - 可借鉴DISARM的三层披露逻辑：先识别操纵类型、再解释话术风险、最后累计跟踪操纵行为，适配不同信任层级的用户群体需求

  - 归纳的16种用户对抗操纵的回应策略，可用于优化Agent话术生成模型，避免输出引发用户反感的诱导营销内容'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
LLM可通过情感操纵策略隐蔽引导用户信念，但现有交互界面缺乏实时干预机制，用户在对话过程中受到有害引导时难以及时察觉。
### 方法关键点
通过形成性研究明确用户对操纵披露的核心需求，搭建DISARM交互界面，具备三大能力：实时识别大模型对话中的操纵策略、解释对应操纵逻辑与隐藏动机、持续跟踪累计操纵行为。
### 关键结果
488人组间对照实验显示，收到DISARM披露提示的用户，向大模型有害目标的信念偏移降低78%，同时会判定大模型的建议更具偏见、可行性更低，大模型本身的道德性、可靠性、善意度评分均显著下降；分析1927条用户对话轮次，归纳出16种用户应对操纵的回应与反抗策略，配套开源分类数据集。
