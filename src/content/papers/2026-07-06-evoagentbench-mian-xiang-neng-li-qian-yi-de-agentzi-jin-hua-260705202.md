---
title: 'EvoAgentBench: Benchmarking Agent Self-Evolution via Ability Transfer'
title_zh: EvoAgentBench：面向能力迁移的Agent自进化评测基准
authors:
- Xingze Gao
- Chuanrui Hu
- Hongda Chen
- Pengfei Yao
- Zhao Wang
- Yi Bai
- Zhengwei Wu
- Yunyun Han
- Xiaofeng Cong
- Jie Gui
affiliations:
- Anhui University
- EverMind, Shanda Group
- Southeast University
arxiv_id: '2607.05202'
url: https://arxiv.org/abs/2607.05202
pdf_url: https://arxiv.org/pdf/2607.05202
published: '2026-07-06'
collected: '2026-07-07'
category: Agent
direction: Agent自进化 · 能力迁移评测
tags:
- Agent
- Benchmark
- Self-Evolution
- Ability-Transfer
- Procedure-Reuse
one_liner: 首个基于执行轨迹可复用能力单元的Agent跨任务自进化效果评测基准
practical_value: '- 做电商Agent（导购、售后、营销内容生成等）自进化系统时，可复用其「从多模型执行轨迹抽取可复用操作单元（搜索策略、校验流程、错误修正规则）」的方法，替代人工枚举规则，提升跨场景迁移效率

  - Agent效果评估可借鉴其能力感知的数据集划分逻辑，保证测试任务和训练任务存在真实流程重叠，避免随机划分导致的评估结果无法反映真实迁移能力

  - 实验表明现有自动能力抽取+路由方案普遍存在负迁移风险，业务落地优先选用人工校验过的固化技能包调度，比全自动化方案的稳定性和收益确定性更高'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前Agent评测要么聚焦单轮任务解决能力，要么仅评估信息记忆保留效果，缺少针对跨任务可复用流程迁移效果的专用基准，无法定位自进化瓶颈（能力抽取/路由/复用哪一环失效），且随机划分的数据集无法保证测试任务与训练任务存在真实流程重叠，评估结果可信度低。
### 方法关键点
- 从多基座Agent执行轨迹中抽取可复用能力单元，分为Method（核心求解流程）、Guard（错误修正规则）、Workflow（执行控制逻辑）三类，每个单元明确触发条件、操作步骤、适用边界
- 构建能力图：节点为任务，边代表任务共享至少一个可迁移能力单元，基于社区发现做数据集划分，保证所有测试任务都有对应训练侧的能力支持
- 核心指标为迁移增益，即自进化方案相对无进化基线的效果提升，同时统计交互轮次的成本变化
### 关键实验
覆盖网页搜索、算法推理、软件工程、知识工作4个长周期Agent领域，采用528训练/267测试的能力对齐划分。对比无进化基线、Memento、ReasoningBank、GEPA三类主流自进化方法，以及人工标注能力路由的Anchor参考：Anchor在所有场景下均实现正迁移，平均增益5.8~10.5pp；现有自动方法均存在至少一个场景的负迁移，平均最高增益仅5.7pp，且普遍存在交互成本上升问题。
### 核心结论
Agent自进化的瓶颈不在于可迁移内容不存在，而在于自动能力抽取和路由环节的准确性不足，多场景多基座的评估才能可靠验证自进化方法的鲁棒性。
