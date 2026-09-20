---
title: Accelerating Visual Policy Learning with Sampling-Based Model Predictive Control
title_zh: 采用采样式模型预测控制加速视觉策略学习
authors:
- Yilang Liu
- Haoxiang You
- Qian Wang
- Daniel Rakita
- Ian Abraham
arxiv_id: '2609.20575'
url: https://arxiv.org/abs/2609.20575
pdf_url: https://arxiv.org/pdf/2609.20575
published: '2026-09-17'
collected: '2026-09-20'
category: Other
direction: 机器人视觉策略学习 · 训练效率优化
tags:
- Reinforcement Learning
- Model Predictive Control
- Policy Learning
- Visual Perception
- Zero-Shot Transfer
one_liner: 提出采样引导策略搜索SGPS，结合采样MPC与一阶策略优化降低视觉策略训练成本并规避局部最优
practical_value: '- 复杂决策类任务训练可借鉴「采样生成指导信号+交替短视程梯度更新」范式，缓解局部最优问题，提升RL类排序/多轮推荐任务训练效率

  - 多模态感知任务训练可参考「感知渲染/梯度计算解耦」设计，降低图文/视频等大输入场景下的GPU显存占用

  - 落地部署可参考「仿真训练蒸馏+零样本迁移」pipeline，降低真实业务场景适配的标注与调优成本'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
机器人运动/操作类视觉策略训练计算与GPU显存成本高；一阶策略梯度（FoPG）虽通过可微仿真降本，但局部优化易陷入非预期接触模式，现有方案多依赖特权状态的教师模型，流程繁琐。
### 方法关键点
1. 提出SGPS，结合采样式MPC的循环动作目标精修与一阶策略优化：行为克隆基于采样动作初始化策略，训练阶段交替执行采样精修、扰动初始态/随机动力学下的短视程FoPG更新
2. 视觉训练采用解耦FoPG设计，将渲染排除在计算图外，无需状态策略教师即可直接从深度观测学习
### 关键结果
- 单GPU即可完成Unitree Go2、G1机器人的行走、越障、推箱、双臂搬运等策略训练
- 蒸馏后策略可零样本迁移到真实Go2机器人，自主完成小跑、爬行、跨栏、行为切换等任务
