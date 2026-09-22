---
title: 'AgentRouter: Heterogeneous Model Routing for Cost-Optimal Multi-Step Agentic
  Workflows'
title_zh: AgentRouter：面向成本最优多步Agent工作流的异构模型路由
authors:
- Rudrendu Kumar Paul
- Sourav Nandy
affiliations:
- Boston University
- University of Texas at Austin
arxiv_id: '2609.22951'
url: https://arxiv.org/abs/2609.22951
pdf_url: https://arxiv.org/pdf/2609.22951
published: '2026-09-19'
collected: '2026-09-22'
category: Agent
direction: Agent工作流优化 · 步级模型成本路由
tags:
- AgentInference
- ModelRouting
- CostOptimization
- LLMInference
- WorkflowOrchestration
one_liner: 12M参数轻量分类器实现Agent工作流步级路由，降本72%仅损失2.7%质量
practical_value: '- 搭建电商Agent系统（智能客服、商品分析、内容生成工作流）时可复用4档模型分级策略，优先将格式校验、结构化抽取、简单检索等低复杂度步骤路由到7B-13B小模型，可快速实现推理成本下降

  - 步级路由的5个输入特征（任务类型、推理深度、工具调用需求、输出格式、上下文占用率）无需复杂特征工程即可直接复用，快速搭建业务可用的路由baseline

  - 训练路由模型时可复用不对称损失设计，惩罚低配导致质量损失的权重高于过度高配的成本损失，兼顾降本与业务效果的硬性要求

  - 标注路由训练数据时采用依赖感知标注方案，以实际工作流前序步骤的输出质量为前提标注当前步的适配模型，避免孤立标注导致的路由效果偏差'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前企业级Agent系统全链路调用前沿LLM时，60%~80%推理预算浪费在小模型即可同等质量完成的简单子任务上；现有单轮路由方案忽略Agent工作流单条轨迹内的步骤复杂度差异与步间上下文依赖，要么降本幅度有限，要么质量损失过大，无法满足生产级成本-质量平衡要求。
### 方法关键点
- 将步级模型路由形式化为带端到端质量约束的序列分配问题，定义4档按能力/成本排序的模型梯队，核心目标是在质量不低于指定阈值的前提下最小化总推理成本
- 路由模块为仅12M参数的前馈分类器，A100上单步路由overhead <5ms，输入为5个可实时提取的特征：任务类型、推理深度、工具调用数量、输出格式约束、上下文窗口占用率
- 采用依赖感知标注策略：标注单步最低适配模型时，以前序步骤均用最低适配模型的输出作为上下文，避免孤立标注与实际工作流脱节；训练时加入不对称正则项，低配导致的质量损失惩罚权重高于高配的额外成本惩罚，优先保证效果
- 增加兜底机制：端到端质量不达标时用前沿模型重跑失败步骤，生产环境触发概率<4%
### 关键实验
基于5万标注步、6250条跨领域Agent轨迹训练，测试集包含2400条轨迹共18720个步决策：对比RouteLLM、FrugalGPT、DAAO等baseline，AgentRouter实现71.8%成本下降，仅保留97.3%的前沿模型全链路质量，降本幅度是单步RouteLLM的2.3倍、FrugalGPT的1.6倍；单步路由平均精度84.6%，极简难度步精度91.2%。
### 核心结论
单条Agent工作流内部的步骤复杂度差异足够大，细粒度步级路由可以用极低的overhead实现大幅降本且几乎不损失端到端效果。
