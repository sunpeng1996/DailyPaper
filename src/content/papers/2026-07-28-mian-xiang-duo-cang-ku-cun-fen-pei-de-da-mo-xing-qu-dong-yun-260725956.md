---
title: Large Language Model for Operations Research Formulation Selection in Multi-Warehouse
  Inventory Allocation
title_zh: 面向多仓库存分配的大模型驱动运筹学公式选择方法
authors:
- Jintao Xu
- Yingzheng Ma
- Jiong Dong
- Yongzhi Qi
- Jianshen Zhang
affiliations:
- JD.com Supply Chain Tech Team
arxiv_id: '2607.25956'
url: https://arxiv.org/abs/2607.25956
pdf_url: https://arxiv.org/pdf/2607.25956
published: '2026-07-28'
collected: '2026-07-29'
category: Agent
direction: Agent 多专家路由与策略优化
tags:
- LLM
- Routing
- GRPO
- SFT
- Supply Chain Optimization
one_liner: 提出SFT+IPO+GRPO渐进训练框架，实现多仓库存分配的实例级OR公式自适应选择
practical_value: '- 多专家路由场景可复用渐进训练范式：先SFT对齐输出格式与领域知识，再IPO做 pairwise 偏好区分，最后GRPO用离线预计算的效果元数据做策略优化，适合推荐多召回源选择、广告多策略路由等场景，大幅降低在线训练成本

  - 可直接复用GRPO离线元数据设计：训练前提前跑完所有候选专家在历史样本上的效果（得分、排名、最优标识），训练时直接查表获得奖励，避免RL训练时反复调用下游模块，适合电商业务中重链路的策略选择场景

  - 小样本RL训练奖励设计参考：融合有效性校验（非法输出给负奖励）、效果归一化、排名奖励、长尾场景均衡惩罚，提升RL训练稳定性，缓解样本不平衡带来的长尾效果退化问题'
score: 10
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
多仓库存分配是电商供应链核心运营问题，传统统一采用固定MIP公式求解，但不同SKU实例的需求集中度、库存不平衡度、预测波动、服务约束差异极大，单一公式无法适配异构场景，往往导致分配效果次优，亟需实例级的OR公式自适应选择能力。

### 方法关键点
1. 构建4种互补MIP专家库：LB（字典序优先满足目标库存天数带）、SBD（加权平衡带内占比和偏差）、DM（最小化全局库存天数偏差）、RCB（按预测可靠性加权偏差），覆盖不同场景优先级需求
2. 渐进式 solver 引导训练流程：① 均衡采样SFT，让LLM学会结构化输出和实例特征-专家优先级匹配；② 用求解器评估的得分差构造带margin权重的IPO偏好对，过滤随机波动的弱对比对，提升专家区分度；③ GRPO阶段提前离线计算每个实例所有专家的得分、排名、最优标识等元数据，训练时直接查表给奖励，基于同组采样的相对比较更新策略
3. 奖励设计融合分配质量、排名反馈、最优专家激励、参考专家惩罚、输出有效性校验多个维度

### 关键实验结果
基于京东真实业务数据，基模型采用Qwen3-14B，对比SFT+IPO、固定LB专家、事后最优Oracle：HR@1从21.45%提升至50.42%，HR@2从70.47%提升至82.31%，分配准确率比现有基线高12.57pp，与Oracle的差距缩小到4.85pp。

### 核心启示
多专家路由的目标不是单纯提升分类准确率，而是最大化后端执行的实际业务效用，用下游真实效果做训练信号才能避免预测和业务收益脱节
