---
title: Can Induced Emotion Bias LLM Behaviors in Sequential Decision Making?
title_zh: 诱导情绪是否会影响LLM在序列决策中的行为表现
authors:
- Minh Khoi Ho
- Zihao Zhu
- Runchuan Zhu
- Levina Li
- Zhiwen Fan
- Zhangyang Wang
- Junyuan Hong
arxiv_id: '2607.12631'
url: https://arxiv.org/abs/2607.12631
pdf_url: https://arxiv.org/pdf/2607.12631
published: '2026-07-14'
collected: '2026-07-15'
category: Agent
direction: Agent序列决策 · 情绪影响机制
tags:
- LLM
- Emotion Induction
- Sequential Decision Making
- Iowa Gambling Task
- Agent Behavior
one_liner: 通过爱荷华赌博任务验证诱导情绪对LLM序列决策的影响，揭示愤怒情绪的特定作用规律
practical_value: '- 搭建电商导购、客服类LLM Agent时，可前置用户情绪识别模块，当识别到用户愤怒时新增决策校验逻辑，避免Agent过早收敛导致服务效果下降

  - 开发基于LLM的序列决策类Agent（如广告投放优化、推荐冷启动探索Agent）时，可在prompt中加入情绪隔离提示，降低负面情绪对惩罚敏感度的影响

  - 评估LLM Agent鲁棒性时，可引入情绪诱导类测试用例，覆盖用户极端情绪场景下的决策稳定性校验'
score: 8
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM作为自主Agent在高风险场景落地规模持续提升，但上下文诱导情绪是否会调控其序列决策行为尚不明确，存在决策稳定性隐患。
### 方法关键点
采用心理学经典的爱荷华赌博任务（IGT）范式，结合想象式情绪诱导流程开展实验；首先完成范式可行性验证：确认LLM可从上下文感知区分度高的强情绪，且LLM Agent能以类人节奏从序列交互中学习决策规律。
### 关键结果
1. 整体层面与人类行为不同，诱导情绪不会显著平均偏移LLM Agent的决策动态；
2. 愤怒情绪存在条件效应：诱导愤怒会降低LLM Agent对错误决策惩罚的敏感度，且在任务早期会抑制探索行为，导致决策过早收敛到少量选项。
