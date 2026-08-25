---
title: 'ToSCA: Leveraging Hierarchical Reinforcement Learning on Temporal and Strategic
  Abstractions of Conversational Agents'
title_zh: ToSCA：基于层次强化学习的对话Agent时序与策略抽象框架
authors:
- Xiaoyu Wang
- Qingqing Gu
- Yue Zhao
- Teng Chen
- Yuqi Cao
- Xiaokai Chen
- Hongyan Li
- Luo Ji
affiliations:
- Geely AI Lab
- Beijing Institute of Technology
- Peking University
arxiv_id: '2608.21969'
url: https://arxiv.org/abs/2608.21969
pdf_url: https://arxiv.org/pdf/2608.21969
published: '2026-08-22'
collected: '2026-08-25'
category: Agent
direction: 对话Agent · 层次强化学习优化
tags:
- Hierarchical RL
- Conversational Agent
- PPO
- DQN
- Reward Engineering
one_liner: 提出双层HRL对话框架ToSCA，用显式策略引导token生成，缓解RLHF奖励稀疏问题
practical_value: '- 电商客服/导购Agent可直接复用双层HRL架构：上层用DQN做话术策略分类（如问候/答疑/促单/安抚），下层用PPO做token级生成，比单级RLHF训练效率高，策略可解释性强便于业务调试

  - 奖励设计可直接迁移：除业务侧用户满意度外，叠加token级KL penalty避免生成偏离业务规范，加内在动机奖励（策略与生成内容的匹配度）缓解多轮对话奖励稀疏问题

  - 上层策略选择可采用选择题式prompt设计，无需额外新增模型价值头，直接复用LLM logit输出策略选项，工程实现成本极低，适合快速落地'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有对话Agent的RLHF方法多为token级，存在奖励稀疏、计算开销高的问题，多轮对话场景下需等整句生成完成才能获得反馈，探索效率极低；此前分层RL方案要么上层为不可解释的隐式意图空间，要么仅做策略规划不联动token生成，策略与回复的对齐度差。
### 方法关键点
- 双层MDP架构：上层（utterance级）用DQN训练策略选择器，输出显式可解释的文本策略（如提问/告知/指令/承诺）；下层（token级）用PPO训练生成器，以上层策略为prompt输入生成回复，两者共享预训练LLM backbone
- 双粒度奖励机制：上层奖励为LLM-as-Judge输出的用户满意度分（0-5分）；下层奖励叠加满意度分、KL penalty（约束生成不偏离SFT基准模型）、内在动机奖励（策略与生成内容的匹配度对数似然），大幅缓解奖励稀疏
- 训练逻辑：先由上层从对话上下文选择最优策略，下层基于策略生成回复，交替训练上下层模块，理论证明可收敛
### 关键结果
在DailyDialog（日常对话）、ESConv（情感支持对话）、EmpatheticDialogues（OOD测试）3个数据集上对比SFT、PPO、ArCher等10+基线：DailyDialog上策略选择Acc达63.64%（超SFT 3.45个百分点），Rouge-L达35.22%（超SFT 16.7个百分点）；OOD测试下Bleu-2较次优基线高16.9%。
### 核心洞见
显式可解释的策略分层设计，是大幅降低对话Agent RLHF训练成本、提升业务可控性的最优路径之一
