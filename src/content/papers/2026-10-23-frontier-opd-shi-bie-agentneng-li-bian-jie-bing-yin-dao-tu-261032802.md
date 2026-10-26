---
title: 'Frontier-OPD: Discovering the Edge of Agent Capability and Teaching Agents
  to Go Beyond'
title_zh: Frontier-OPD：识别Agent能力边界并引导突破的在路蒸馏框架
authors:
- Zheng Jiang
- Yiming Chen
- Houde Qian
- Ling Li
- Chaoyang Li
- Lifeng Sun
affiliations:
- Tsinghua University
arxiv_id: '2610.32802'
url: https://arxiv.org/abs/2610.32802
pdf_url: https://arxiv.org/pdf/2610.32802
published: '2026-10-23'
collected: '2026-10-26'
category: Agent
direction: Agent 多轮交互知识蒸馏优化
tags:
- On-Policy-Distillation
- Multi-Turn-Agent
- Knowledge-Distillation
- Agent-Optimization
- Teacher-Student-Framework
one_liner: 提出基于学习前沿的在路蒸馏方法，精准筛选教师干预点，提升多轮Agent自主性能
practical_value: '- 电商导购Agent、多轮搜索交互Agent的蒸馏场景下，可复用轨迹平衡的分歧聚合方法，优先选择学生未掌握、但经短指导即可自主承接后续步骤的节点做教师干预，大幅降低无效标注/调用大模型的成本

  - 干预有效性验证可直接复用匹配窗口对比法：给教师干预后的序列和原始序列分配相同长度的评估窗口，对比师生一致性，仅保留能提升后续学生自主表现的干预数据加入训练，避免负向迁移

  - 算力预算有限的小尺寸Agent落地场景，可优先把资源投到学习前沿节点的靶向干预上，相比全量OPD能更快达到目标性能，ROI更高'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多轮Agent的On-Policy蒸馏（OPD）普遍存在教师干预选择盲目的问题：要么在学生已经完全掌握的决策节点浪费计算和标注资源，要么干预后学生无法承接后续交互步骤，导致指导完全无效，小尺寸落地型Agent的蒸馏效率低、性能提升天花板明显。

### 方法关键点
- 构建共享状态轨迹图，将不同轨迹中「观测+可用动作」一致的节点聚合，采用轨迹平衡的师生对数概率差打分，筛选高分歧的学习前沿候选干预点，避免重复采样同一状态浪费预算
- 对每个候选点执行1步教师干预，再让学生自主执行3步，对比「干预+后续序列」与原始等长序列的师生一致性，仅保留一致性不降低的干预数据加入蒸馏训练池
- 每轮蒸馏后重新采样学生轨迹更新学习前沿边界，动态适配学生能力的变化

### 关键实验结果
在ALFWorld、WebShop、ScienceWorld三个多轮Agent基准测试，以Qwen3-32B/8B-RL为教师蒸馏Qwen3-1.7B/4B学生：
- 对比普通OPD、FutureBridge-OPD等6种基线，在所有任务上均取得最优性能，1.7B学生在ScienceWorld上成功率从基线最高的10.2%提升至14.5%，WebShop上成功率从57.7%提升至58.3%
- ALFWorld场景下，尽管单步训练耗时比普通OPD高96%，但达到55%目标成功率的总耗时比普通OPD低38%

> 最值得记住的结论：Agent蒸馏的核心不是给越多教师指导越好，而是精准找到学生「跳一跳够得到」的学习前沿节点，用最少的干预带来最大的性能提升。
