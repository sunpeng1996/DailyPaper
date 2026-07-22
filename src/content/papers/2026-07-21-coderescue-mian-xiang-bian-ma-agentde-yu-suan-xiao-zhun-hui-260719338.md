---
title: 'CodeRescue: Budget-Calibrated Recovery Routing for Coding Agents'
title_zh: CodeRescue：面向编码Agent的预算校准恢复路由框架
authors:
- Qijia He
- Jiayi Cheng
- Chenqian Le
- Rui Wang
- Xunmei Liu
- Yixian Chen
- Jie Mei
- Zhihao Wang
- Xupeng Chen
- Yuhuan Chen
affiliations:
- University of Washington
- New York University
- ByteDance
- Amazon
arxiv_id: '2607.19338'
url: https://arxiv.org/abs/2607.19338
pdf_url: https://arxiv.org/pdf/2607.19338
published: '2026-07-21'
collected: '2026-07-22'
category: Agent
direction: Agent 成本可控失败恢复路由优化
tags:
- Agent Routing
- Conformal Risk Control
- Cost Optimization
- LLM Inference
- Coding Agent
one_liner: 提出编码Agent失败后预算校准恢复路由机制，保证解决率的同时大幅降低推理成本
practical_value: '- 多步Agent失败后路由设计：可复用「修复/重跑/升模」三类动作框架，替代传统直接升模的二选一级联策略，充分挖掘小模型潜力降低推理成本

  - 动态预算适配方案：可直接复用Conformal Risk Control层实现单路由模型多预算点部署，无需针对不同成本要求重新训练模型，大幅降低上线迭代成本

  - 路由模型训练trick：输入加入任务难度、所属类目等元数据前缀，用「最便宜成功动作」做监督标签，比零样本Prompt路由效果提升30%以上'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有成本感知LLM推理系统多采用二值级联策略：先调用小模型生成，失败后直接升级大模型，忽略了可执行环境下失败反馈的价值——编码、工具调用等Agent场景中，失败的错误日志本身会把模糊任务转化为明确的修复问题，小模型二次尝试的性价比远高于直接升模，同时不同业务线的成本-效果权衡要求差异大，现有方案无法在不重新训练的前提下适配动态预算。
### 方法关键点
- 定义三类异质恢复动作：reflect（小模型基于错误反馈局部修复）、replan（小模型丢弃原有方案重新生成）、escalate（转发给大模型解决），覆盖不同失败场景的最优选择
- 路由模型基于离线执行回滚数据训练，标签为每个失败案例的最便宜成功动作，输入包含任务内容、执行结果、错误日志+任务难度/类目等元数据，用小参数LM微调输出三类动作的归一化得分
- 上层叠加Conformal Risk Control（CRC）校准层，通过调整成本惩罚系数λ，在不用重训路由模型的前提下生成不同预算的工作点，提供边际期望成本的统计保证
### 关键结果
在5个编码基准共2.73万问题上测试，对比固定动作、零样本prompt路由、二值级联基线：最优CRC校准点解决率超过始终升模策略（71.7% vs 68.6%），仅消耗其35%的平均恢复成本；无约束路由模型解决率达81.7%，远高于固定升模的68.6%，且平均成本更低。
### 核心启示
Agent失败后不要直接切换大模型，先基于错误反馈评估小模型二次尝试的性价比，配合CRC校准层可灵活适配不同成本预算要求，实现成本和效果的最优平衡
