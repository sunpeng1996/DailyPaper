---
title: 'Credit Where It Matters: Dependency-Aware Policy Optimization for Terminal
  Agents'
title_zh: 面向终端Agent的依赖感知信用分配策略优化方法DepGPO
authors:
- Yu Li
- Guangfeng Cai
- Long-Fei Li
- Shuo Han
- Shengtian Yang
- Han Luo
- Kaibing Yang
- Lei Feng
affiliations:
- Southeast University
- Huawei Noah's Ark Lab
arxiv_id: '2610.03634'
url: https://arxiv.org/abs/2610.03634
pdf_url: https://arxiv.org/pdf/2610.03634
published: '2026-10-02'
collected: '2026-10-05'
category: Agent
direction: Agent RL训练 · 信用分配优化
tags:
- Reinforcement Learning
- Credit Assignment
- Terminal Agent
- Policy Optimization
- GRPO
one_liner: 基于命令读写依赖回溯实现更精准的多步终端Agent RL信用分配，提升任务表现与训练稳定性
practical_value: '- 电商导购/运营工具Agent多步RL训练可直接复用思路：基于工具调用的读写依赖（如搜品/加购/下单的链路依赖）重分配GRPO
  advantage，将奖励信号集中到影响最终转化的核心步骤

  - 对有明确最终校验规则的Agent任务（如客服工单解决率、投放素材过审率），可从校验点反向回溯操作依赖路径，无需额外标注过程奖励即可实现精准信用分配，大幅降低标注成本

  - 可在现有GRPO/DAPO训练框架上快速改造：仅新增依赖图构建、信用计算、advantage重分配三个模块，无需修改原有policy优化逻辑，落地成本极低'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有终端Agent的RL训练多采用GRPO等轨迹级信用分配，或基于状态匹配的步级分配，未显式追踪命令间的读写依赖，易将奖励信号分配给无关操作；且终端任务中61%的同任务轨迹组奖励全同导致advantage为0，稀疏锚点状态也限制了现有步级方法的效果，同时成功轨迹中仅18%~57%的操作真正和最终结果相关，亟需更精准的信用分配机制。

### 方法关键点
- 构建命令依赖有向无环图，包含文件读写边、标准输出复用边两类依赖
- 从任务校验器读取的资源集合E反向回溯，给写命令按最终影响E的代码行占比计算贡献分，读命令按最短依赖路径的衰减系数累加关联写命令的贡献分
- 聚合单步所有命令的信用值，归一化为步级权重，与原轨迹advantage相乘得到每步的最终advantage，保留原GRPO的clip优化逻辑不变

### 关键实验
用Qwen3.5-9B、Qwen3.6-27B在SETA、TMAX两个数据集训练，在Terminal-Bench 2.0/2.1上对比GRPO、DAPO、DPPO等6种基线，DepGPO在全部8个实验设置下pass@1均为最优，较最强基线提升3.22~10.03个百分点，较GRPO提升4.34~14.53个百分点，同时训练过程梯度更稳定，无后期性能退化问题。

**最值得记住的一句话**：对于有显式操作依赖、可回溯执行轨迹的多步Agent任务，基于执行依赖的信用分配可以在不增加标注成本的前提下，大幅提升RL训练的效果与稳定性。
