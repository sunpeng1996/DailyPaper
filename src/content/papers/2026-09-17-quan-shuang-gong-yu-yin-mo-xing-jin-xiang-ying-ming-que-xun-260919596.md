---
title: Full-Duplex Speech Models Take the Floor When Asked, Not When Needed
title_zh: 全双工语音模型仅响应明确询问，不会基于内容需求主动发言
authors:
- Linkai Peng
- Baorian Nuchged
- Kaiqi Fu
- Yuyang Yao
affiliations:
- University of Connecticut
- The University of Texas at Austin
- X Square Robot
- The University of Oxford
arxiv_id: '2609.19596'
url: https://arxiv.org/abs/2609.19596
pdf_url: https://arxiv.org/pdf/2609.19596
published: '2026-09-17'
collected: '2026-09-18'
category: Agent
direction: 语音交互Agent 主动发言决策能力评估
tags:
- full-duplex-speech
- turn-taking
- spoken-dialogue
- agent-intervention
- evaluation
one_liner: 通过受控实验揭示现有全双工语音模型无法基于内容需求主动发言，仅对询问、停顿触发可靠响应
practical_value: '- 开发智能客服/导购语音Agent时，暂不依赖模型自动识别错误、风险内容主动打断，需额外开发规则类触发模块

  - 评估语音交互Agent主动响应能力时，可复用本文上下文匹配对照实验、10类轮次分配规则的评估框架

  - 语音Agent打断触发逻辑可优先基于用户明确称呼、语句停顿两类高可靠信号，降低误触率'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
全双工语音Agent支持边听边说的交互模式，可实现随时响应的体验，但现有模型是否能像人类一样基于内容需求（如纠正错误、风险预警）主动发言尚未被验证，传统评估未区分发言触发的原因与时机干扰。
### 方法关键点
构建同主题上下文匹配的英文独白数据集，仅调整触发语句变量；基于对话轮次分配规则定义10类触发场景；压缩词间停顿排除沉默带来的发言机会干扰，对5类主流全双工语音模型开展对照测评。
### 关键结果
- 询问、停顿两类触发的响应可靠性远高于错误事实、风险类内容触发
- Moshi、PersonaPlex对错误事实的主动反驳率仅14%~15%，风险场景主动预警率仅4%~7%，即使给出发言权限也无法填补内容驱动主动发言的能力缺口
