---
title: Training User Simulators with Latent Intrinsic Feedback
title_zh: 基于隐式内在反馈的用户模拟器训练方法
authors:
- Tarek Naous
- Craig Boutilier
- Wei Xu
- Ofer Meshi
affiliations:
- Google Research
- Georgia Institute of Technology
arxiv_id: '2610.13617'
url: https://arxiv.org/abs/2610.13617
pdf_url: https://arxiv.org/pdf/2610.13617
published: '2026-10-09'
collected: '2026-10-12'
category: Agent
direction: Agent 仿真用户模拟器构建
tags:
- User Simulator
- Reinforcement Learning
- Multi-turn Conversation
- LLM Training
- Latent State
one_liner: 为用户模拟器加入隐式评估状态，提升仿真真实度同时降低RL训练算力超50%
practical_value: '- 对话式推荐、智能客服Agent训练可直接复用该方案：用带隐式评估的用户模拟器做RL训练，无需额外调用Judge LLM，降低训练算力50%以上，效果无损失

  - 仿真用户行为时可参考5维隐式评估状态（Internal_Thought/Rating/Instruction_Followed/Reaction/Feedback）的设计，捕捉用户未明确表达的不满，优化推荐/客服响应策略

  - 训练垂直领域用户模拟器时，可复用「人机交互日志+大模型标注隐式状态+全参数SFT」的流程，无需重新设计标注框架'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM助手多轮对话易丢失用户目标、响应不符合预期，传统用户模拟器仅能生成用户话术，RL训练需额外调用外部Judge LLM获取奖励，算力成本高且奖励与真实用户主观评估相关性弱；同时用户的不满往往不会明确表达，仅隐含在后续交互行为中，现有模拟器无法捕捉这类隐式反馈。

### 方法关键点
- 设计隐式评估状态（LES）：包含5个分量，分别为第一人称内部想法、1-5分满意度评分、指令遵循度（Yes/No/Partially）、反应类型（Critique/Praise/Neutral）、短反馈摘要
- 数据标注：基于WildChat人机交互数据集，调用Gemini3.1-Pro标注所有多轮对话的LES与用户初始意图
- 训练流程：对Gemma3/Qwen2.5系列基座模型做SFT，每轮先生成LES再输出下一轮用户话术；RL训练助手时直接取LES中的评分作为奖励，无需外部Judge

### 关键结果
- 对比同尺寸prompt基线：LES模拟器的评分与人类标注相关性最高提升0.08，仿真真实度（统计对齐分）最高提升0.35，PPL降低约75%
- 对比同尺寸无LES的SFT基线：LES模拟器仿真真实度平均提升2%，可额外输出可靠的评估信号
- RL训练场景下：用LES内置奖励的效果略优于外部Judge（任务满意度41.44% vs 41.08%），总训练FLOPs降低55%以上

> 带隐式内在评估的用户模拟器可同时兼顾仿真真实度与RL训练效率，是多轮对话Agent低成本训练的可行方案
