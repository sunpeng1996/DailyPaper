---
title: 'MAREval: A Multi-Agent Framework for Evaluating Natural Language Recommendation
  Explanations'
title_zh: MAREval：面向推荐自然语言解释的多智能体评估框架
authors:
- Reza Yousefi Maragheh
- Jayesh Uddhav Kudase
- Aysenur Inan
- Ramin Giahi
- Kai Zhao
- Parth Parikh
- Jianpeng Xu
- Jason Cho
- Evren Korpeoglu
- Sushant Kumar
affiliations:
- Walmart Global Tech
arxiv_id: '2610.36389'
url: https://arxiv.org/abs/2610.36389
pdf_url: https://arxiv.org/pdf/2610.36389
published: '2026-10-26'
collected: '2026-10-28'
category: Eval
direction: 多Agent 推荐解释自动评估
tags:
- Multi-Agent
- Recommendation Explanation
- LLM-as-Judge
- Automated Evaluation
- Chain of Debate
one_liner: 提出整合辩论链、上下文管控、蒙特卡洛采样的多Agent框架，提升推荐解释评估的人机对齐度与稳定性
practical_value: '- 可直接复用MAREval的4角色架构（Planner+Evaluator+Moderator+Arbitrator）做电商推荐文案、商品解释、标题的自动质检，替代部分人工标注，降低内容审核成本

  - Chain of Debate（CoD）prompt策略可迁移到所有多Agent协作任务，提前为各Agent同步角色与执行计划，能有效解决多Agent闲聊、prompt漂移的常见问题

  - 多轮Monte Carlo采样聚合的trick可直接用于所有LLM-as-Judge场景，仅需3-5次独立运行取平均，即可将结果稳定性提升15%以上，几乎无额外开发成本

  - 电商场景实测，经过该框架质检的推荐解释可直接带来ATC、GMV的正向提升，可快速上线A/B测试验证业务收益'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
推荐系统附带的自然语言解释直接影响用户信任与转化，现有评估方案中人工标注成本高、无法规模化，单Agent LLM评估存在prompt敏感、结果波动大问题，传统多Agent评估缺乏结构化协调易出现讨论漂移，难以满足工业生产的稳定性、对齐度要求。

### 方法关键点
- 4角色多Agent架构：Planner采用Chain of Debate（CoD）策略，提前为所有Agent生成同步的分轮执行计划，确保各角色逻辑协同，避免无意义闲聊
- Moderator每轮蒸馏评估者的共识与争议点，压缩冗余信息，防止prompt漂移
- Arbitrator聚合多轮讨论结果，搭配Monte Carlo采样多次独立运行的结果取平均，抵消LLM随机采样带来的结果方差

### 关键结果
在公开TopicalChat对话数据集、沃尔玛私有电商推荐解释数据集上对比6种基线方案：
- 电商数据集相关性评估Cohen's kappa达0.334，较次优基线ChatEval提升42%；措辞质量kappa达0.208，提升5%
- 评估结果平均标准差仅0.0197，较最优基线G-Eval降低15.2%，稳定性大幅提升
- 人工标注验证：硬约束通过率100%，软约束满足率98.6%，远高于G-Eval的91%、76.1%，达到生产上线标准
- 线上A/B测试：通过MAREval质检的解释带来ATC提升1.18%（p=0.05）、GMV提升1.36%（p<0.01）

### 核心记忆点
结构化多Agent协调搭配蒙特卡洛采样，是解决工业场景下LLM-as-Judge对齐度不足、稳定性不够的可行路径，可直接落地到生成式推荐的内容质检环节
