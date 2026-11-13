---
title: 'SimRec: Learning to Search, Ask, and Recommend from Simulated Interaction'
title_zh: SimRec：基于模拟交互端到端训练工具增强推荐Agent的框架
authors:
- Yaxin Zhang
- Xingyu Wu
- Yuchen Yan
- Yuqin Dai
- Hong Zhao
- Lixing Shen
- Zhan Chen
- Jian Shao
- Yongliang Shen
affiliations:
- Zhejiang University
- Tsinghua University
- Hikvision Research Institute
arxiv_id: '2611.15426'
url: https://arxiv.org/abs/2611.15426
pdf_url: https://arxiv.org/pdf/2611.15426
published: '2026-11-11'
collected: '2026-11-13'
category: Agent
direction: Agent 多轮推荐交互策略优化
tags:
- RecAgent
- GRPO
- User Simulation
- Reinforcement Learning
- Multi-turn Recommendation
one_liner: 通过任务锚定用户模拟与GRPO强化学习端到端优化推荐Agent全交互策略
practical_value: '- 训练多轮交互推荐Agent时，可复用任务锚定用户模拟器设计：仅基于当前任务需求生成反馈，不泄露目标item，避免模拟漂移，支持外接LLM或自博弈两种模式，大幅降低真实用户交互的训练成本

  - 大商品库稀疏reward场景下可参考轨迹级奖励设计：除最终命中奖励外，增加检索质量、有效工具调用、格式合规的中间奖励，配合训练阶段目标注入机制，解决正样本稀疏无法训练的问题

  - 小参数量LLM落地推荐Agent时，可尝试用GRPO做全交互策略端到端优化，无需拆分查询改写、排序等模块单独训练，实测4B模型优化后效果超过更大参数量的无训练基座Agent'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM推荐Agent多依赖人工设计固定工作流，训练也仅优化查询改写、排序等孤立模块，未从全交互链路优化策略，导致Agent很少验证候选、无法从被拒推荐中恢复，增大基座参数量也无法弥补流程缺陷；同时真实用户交互训练成本高、命中信号稀疏，难以支撑RL规模训练。

### 方法关键点
- 任务锚定用户模拟器：仅基于当前任务需求而非用户画像/目标item生成反馈，支持外接LLM或同参数自博弈两种模式，避免信息泄露与交互漂移
- 工具增强动作空间：开放商品检索、商品详情查询、用户偏好查询三类工具，无固定工作流，由Agent自主决策调用时机
- 任务对齐的GRPO优化：轨迹级奖励融合最终命中、检索质量、有效工具调用、格式合规四类指标，增加交互冗余惩罚；训练阶段对未检索到目标的轨迹随机注入目标item，解决大库下信号稀疏问题，推理时关闭注入。

### 关键实验
在ESCI、Amazon C4两个电商数据集上测试，对比检索基线、无训练推荐Agent、单模块训练基线及不同参数量LLM基座：Qwen3-4B基座用SimRec优化后，ESCI上NDCG@100从32.23%提升到35.42%，Amazon C4上从22.94%提升到24.72%，效果超过更大参数量的无训练GLM-5.1、Kimi-K2.6等基座；优化后Agent从被拒推荐中的恢复率是基线的2倍以上。

最值得记住的一句话：给推荐Agent配工具只是第一步，从全交互链路端到端学习工具调用、推荐、修正的完整策略，比单纯增大基座参数字效更高
