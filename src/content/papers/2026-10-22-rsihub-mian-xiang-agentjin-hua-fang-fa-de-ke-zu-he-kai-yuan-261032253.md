---
title: 'RSIHub: A Composable Framework for Agent-Evolution Methods'
title_zh: RSIHub：面向Agent进化方法的可组合开源框架
authors:
- Zimu Wang
- Xiaobo Wang
- Siyu Ye
- Jiaqi Li
- Silin Chen
- Yuling Shi
- Ruobing Wang
- Jingjing Zhang
- Chaofan Wang
- Kai Wu
affiliations:
- UC Berkeley
- 中国科学技术大学
- Douyin Group
- 上海交通大学
- 北京通用人工智能研究院
arxiv_id: '2610.32253'
url: https://arxiv.org/abs/2610.32253
pdf_url: https://arxiv.org/pdf/2610.32253
published: '2026-10-22'
collected: '2026-10-26'
category: Agent
direction: Agent进化 · 可组合框架
tags:
- Agent_Evolution
- Composable_Framework
- LLM_Agent
- Self_Improvement
- Reproducibility
one_liner: 提供可复用的Agent进化实验基础设施，统一不同进化方法的执行评估与溯源流程
practical_value: '- 搭建业务Agent（如电商导购Agent、推荐策略迭代Agent）的自进化链路时，可复用其Recipe+Operator解耦架构，将通用的执行、评估、快照、溯源能力下沉为公共服务，业务侧仅需实现定制化的进化策略算子，大幅减少重复开发量

  - 做Agent策略迭代的效果校验时，可参考其train/gate/sealed三数据集拆分机制，将进化反馈数据集、准入校验数据集、离线泛化评估数据集完全隔离，避免数据泄露导致的虚假效果提升，确保迭代收益真实可落地

  - 对比不同Agent进化策略（如不同Prompt优化方法、技能迭代方法）时，可复用其受保护运行时设计，将评估逻辑、指标计算完全与Agent可变范围隔离，确保不同策略的对比结果公平、可复现'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Agent进化方法依赖执行反馈迭代优化Prompt、技能、工具调用逻辑与编排策略，但现有实现均需重复搭建执行、评估、快照、溯源等基础实验设施，不同方法的横向对比需要对齐大量环境、配置、评估逻辑，研发成本极高，且易出现评估逻辑被篡改、结果不可复现、收益归因模糊等问题。
### 方法关键点
- 采用Recipe+Operator可组合架构：Recipe声明可变资源范围、各进化阶段的算子绑定关系、运行配置；Operator封装选择父版本、执行、分析、变异、准入等阶段的具体实现，新增进化方法仅需修改配置或新增算子，无需改动框架核心。
- 内置受保护运行时：评估逻辑、档案记录完全由框架管控，不在声明的可变范围内，每个候选版本的结果均绑定对应代码、配置、评估条件，彻底避免归因歧义。
- 支持两种运行模式：固定Recipe模式适用于验证已知进化策略，Agent驱动模式支持外层Agent动态调整进化策略，适配复杂自进化场景。
### 关键结果
在Terminal Bench 2与τ3 Banking两个基准上，基于MiniSWE、Codex两个种子Agent，固定模型与评估配置对比4种主流进化方法：最大整体pass@1提升达13.5个百分点；不同方法的排名随任务场景、种子Agent变化，优化收益不一定能迁移到未见过的密封数据集任务；框架自身额外开销仅占端到端运行时间的0.02%，无明显性能损耗。
### 核心结论
Agent进化无通用最优策略，效果高度依赖任务场景与初始基线，统一的可复现实验基础设施是高效迭代进化方法的核心前提
