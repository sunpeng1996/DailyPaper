---
title: Why This and Not That? A Collaborative Reflection Approach for Understanding
  Thought Coverage in Decision Making Support Dialog
title_zh: 决策支持对话中理解用户思考覆盖度的协作式反思方法
authors:
- Morita Tarvirdians
- Hayley Hung
- Catharine Oertel
affiliations:
- TU Delft
arxiv_id: '2608.17054'
url: https://arxiv.org/abs/2608.17054
pdf_url: https://arxiv.org/pdf/2608.17054
published: '2026-08-17'
collected: '2026-08-19'
category: Agent
direction: Agent 决策支持对话策略优化
tags:
- Conversational Agent
- Dialog Policy
- User Intent
- Human-AI Collaboration
- Decision Support
one_liner: 提出协作式反思框架，实证刻画对话代理与用户间的解释鸿沟，给出9类用户解释分类
practical_value: '- 做电商导购、消费决策助手等用户引导类Agent时，不要仅基于对话行为观测做单向策略跳转，可将观测结果显性告知用户，获取解释后再调整方向，避免误判意图

  - 可复用论文的9类用户解释taxonomy作为意图分类标签体系，训练小模型自动识别用户解释类型，优化对话策略的个性化适配

  - 对于需要深度交互的决策支持Agent，可借鉴「观测-确认-解释-决策」四步交互框架，在降低误判率的同时提升用户信任感'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有决策支持对话Agent仅基于观测到的用户行为模式推断用户状态、制定对话策略，但同一行为模式可能对应完全不同的用户原因（比如用户持续聚焦某话题既可能是刻意优先关注，也可能是回避其他话题），单向策略容易出现误判，甚至强化用户认知盲区，而用户行为观测与真实原因间的「解释鸿沟」此前缺乏系统性实证研究。

### 方法关键点
- 改造反思支持Agent ReflectiMate，将原本静默执行的策略决策节点改为协作式反思时刻：Agent显性告知用户观测到的思考覆盖度偏差，依次确认用户是否识别该模式、询问模式成因、让用户自主选择后续对话方向
- 设计三类思想分类框架：internal（感受、价值观）、external（现实约束、他人意见）、experiential（过往经验），通过广度（想法数）和深度（单想法扩展数）计算各分类的覆盖度指标Sk
- 采用归纳式定性编码构建用户解释分类体系，用多开源LLM做交叉编码验证可靠性

### 关键实验结果
62名用户参与实验，覆盖13类生活决策场景，共采集232个协作式反思时刻：
1. 归纳出9类用户解释分类，同一观测状态最多对应8种不同解释，解释鸿沟普遍存在
2. 用户选择与Agent默认策略的对齐率仅45.3%，但74.4%的用户选择仍会转向未充分探索的思考维度，分歧主要在转向的具体方向而非是否拓展思考

### 核心结论
对话策略的输入信号存在固有歧义，结构化的人机交互交换可以获取双方单独都无法获得的信息
