---
title: 'AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics'
title_zh: AgenticRoboRL：将编码Agent后训练方法引入智能体机器人规划器优化
authors:
- Xinxin Liu
- Bingxin Xu
- Wenrui Bao
- Ming Li
- Wentao Bao
- Chen Chen
- Yuzhang Shang
affiliations:
- University of Central Florida
- University of Southern California
- Michigan State University
arxiv_id: '2610.28589'
url: https://arxiv.org/abs/2610.28589
pdf_url: https://arxiv.org/pdf/2610.28589
published: '2026-10-19'
collected: '2026-10-22'
category: Agent
direction: Agent 规划器跨执行器后训练优化
tags:
- Agent
- Post-Training
- SFT
- Reinforcement Learning
- Adapter
- Robotics
one_liner: 提出适配多机器人执行器的规划器后训练框架，SFT结合多轮RL大幅提升开源模型任务成功率
practical_value: '- 多场景Agent训练可引入业务专属Adapter，无需改动底层执行逻辑，大幅降低跨业务线的训练适配成本

  - Agent核心能力优化可采用SFT+多轮RL的训练范式，无需依赖外部记忆即可逼近闭源大模型效果，适合低延迟业务场景

  - 跨执行机制的统一RL训练管道设计，可迁移至多业务线共享Agent底座的训练场景，适配搜索/推荐/广告不同的调用逻辑'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前智能体机器人系统依赖闭源大模型作为规划器，优化方向集中在执行器迭代、外部记忆引入，未针对规划器自身能力做增强；编码Agent领域已验证后训练的效果增益，但无法直接适配机器人领域VLA技能调用、控制代码生成等多元执行机制。
### 方法关键点
1. 提出AgenticRoboRL跨执行器的机器人规划器后训练框架，采用SFT+多轮RL的训练范式
2. 引入执行器专属Adapter，关联规划器交互记录与任务结果，在固定执行组件的前提下实现统一RL训练管道
### 关键结果
在LIBERO-PRO基准上，9B参数开源规划器无外部记忆的任务成功率从18.1%提升至71.0%，接近带外部记忆的Codex（GPT-5.5）72.1%的水平
