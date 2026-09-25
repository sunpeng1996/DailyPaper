---
title: 'GRASP: Generating, Revising, and Assessing for Strategic Planning with Agentic
  AI'
title_zh: GRASP：面向智能体AI的多阶段策略规划框架
authors:
- Arunabh Srivastava
- Mohammad A.
- Khojastepour
- Srimat Chakradhar
- Sennur Ulukus
affiliations:
- University of Maryland, College Park
- NEC Laboratories America, Inc.
arxiv_id: '2609.30147'
url: https://arxiv.org/abs/2609.30147
pdf_url: https://arxiv.org/pdf/2609.30147
published: '2026-09-24'
collected: '2026-09-25'
category: Agent
direction: Agent 复杂任务多阶段规划
tags:
- LLM Agent
- Strategic Planning
- Multi-stage Pipeline
- Context Isolation
- Constraint Regularization
one_liner: 将规划拆分为生成-修订-评估三个上下文隔离模块，大幅提升复杂任务规划精度
practical_value: '- 做电商大促多目标运营规划、跨场景推荐策略编排时，可直接复用三阶段拆分逻辑：先拉全局约束（库存/预算/合规）生成通用执行框架，再并行探索不同策略路径，最后独立评估选优，避免单条路径误差累积

  - 多任务Agent场景（如同时处理推荐排序+素材生成+库存校验）可复用上下文隔离设计，避免跨任务上下文污染，用小模型即可达到接近大模型的效果，论文中GPT-4o-mini版GRASP比GPT-4o单阶段规划精度高11.3%，成本还低5%

  - 做Agent规划风控与可解释性优化时，可复用GenPlan的硬约束+软规则双正则设计，硬约束（广告合规、价格门槛）直接剪枝无效路径，软规则（用户体验、流量分配规则）优化生成质量，从源头降低幻觉风险'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM Agent处理复杂多步任务时，随任务复杂度升高会出现注意力疲劳、约束冲突、幻觉等「指令诅咒」问题，单阶段规划的误差会级联放大，多任务场景下性能直接崩溃，现有规划框架要么缺乏结构化约束，要么无法隔离上下文避免误差传染。

### 方法关键点
- 全流程拆分为3个上下文完全隔离的模块，杜绝跨模块误差传递：
  1. GenPlan：不感知具体任务实例，仅从任务描述抽取硬约束、软规则，迭代生成全局宏观规划蓝图，作为所有后续路径的刚性框架
  2. RevPlan：基于具体任务实例生成2-4个并行策略路径，每个路径在独立上下文窗口内生成实例化步骤，再与GenPlan全局框架合并，避免路径间污染
  3. VerPlan：独立评估所有候选计划，基于约束满足度、可行性打分，选取得分最高的计划作为最终输出

### 关键实验
在4类基准数据集测试：Natural Plan日历调度任务比直接LLM规划精度高12.4%，ZebraLogic逻辑推理高30.8%；多任务场景下完全消除性能衰减，双任务场景比直接规划最高高16.7%，GPT-4o-mini版GRASP比GPT-5-mini直接规划高14.5%；消融实验证明缺少GenPlan全局约束时，RevPlan局部探索会导致性能暴跌至10.9%；成本方面，GPT-4o-mini版GRASP仅为GPT-4o基线的0.95倍成本，还能获得11.3%的精度提升。

### 核心结论
复杂任务Agent规划的核心不是提升单步推理能力，而是通过模块化拆分和上下文隔离切断误差级联，用全局约束锚定局部探索边界，小模型也能超过更强的单阶段大模型
