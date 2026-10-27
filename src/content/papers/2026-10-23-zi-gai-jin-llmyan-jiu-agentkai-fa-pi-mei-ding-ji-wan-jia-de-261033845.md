---
title: 'Build, Don''t Play: Self-Improving LLM Research Agents Develop a Hearthstone
  Battlegrounds AI That Rivals Top Players'
title_zh: 自改进LLM研究Agent开发媲美顶级玩家的炉石酒馆战棋AI
authors:
- Changlian Ma
- Limin Wang
affiliations:
- 南京大学
- 上海AI实验室
arxiv_id: '2610.33845'
url: https://arxiv.org/abs/2610.33845
pdf_url: https://arxiv.org/pdf/2610.33845
published: '2026-10-23'
collected: '2026-10-27'
category: Agent
direction: Agent 自改进闭环系统设计
tags:
- LLM-Agent
- Self-Improvement
- PPO
- Reinforcement-Learning
- Game-AI
one_liner: 提出AUTOTAVERN自改进LLM研究Agent系统，20天打造超顶级人类水平的炉石战棋AI
practical_value: '- 多角色Agent分工+带版本校验的共享记忆架构，可直接迁移到推荐/广告策略自动化迭代场景，替代人工完成规则修复、特征调优、对手建模等重复工作

  - 五级验证门+真实环境反馈闭环设计，可解决仿真与真实环境的proxy drift问题，借鉴到推荐系统离线仿真到线上放量的校验流程，避免离线涨点线上掉点

  - 基于真实分布校准的训练环境/对手库相比纯自学习增益更高，可迁移到电商流量分配、竞价策略训练场景，用真实用户/竞品分布校准训练环境，提升策略线上效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM研究Agent多局限于基准任务验证，无法端到端解决带部分可观测、高随机性、规则复杂的真实场景问题，且普遍存在仿真优化与真实表现脱节的proxy drift、研究过程错误结论反复出现等痛点，亟需一套带真实反馈的自改进Agent系统。

### 方法关键点
- 多角色分工Agent架构：6个专有LLM Agent（研究牵头、环境、训练、对手建模、评估、部署）通过带版本的结构化研究记忆协作，无直接通信
- 五级验证门机制：代码构建、模型版本绑定、同环境对比、未见种子重校验、真实环境验证，过滤错误结论和漂移模型
- 三层闭环迭代：分钟级PPO策略训练，小时级迭代环境/模型/评估体系，天级真实天梯数据反馈修复仿真、输入编码、对手模型偏差
- 自研高保真仿真环境TAVERNGYM，基于真实天梯数据校准对手库，训练18M参数量Transformer决策模型TAVERNAGENT

### 关键结果
20天迭代23个Agent版本，仅需418条人工干预；TAVERNAGENT天梯评分从6000涨到约15000，最近20场平均排名1.6、夺冠率80%，优于服务器TOP10玩家的平均2.34、59%夺冠率；TAVERNBENCH基准上决策准确率91%，单决策耗时0.03s，远优于GPT-6 Astra的63%准确率、2.4s耗时，1s实时要求下通用LLM准确率几乎为0。

**最值得记住的一句话**：LLM agents build far better than they play（LLM Agent的核心价值是构建专用系统，而非直接执行任务）。
