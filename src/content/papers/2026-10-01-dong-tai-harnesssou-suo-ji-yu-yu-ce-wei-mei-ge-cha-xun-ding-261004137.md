---
title: 'Dynamic Harness Search: Building Multi-Agent Systems Per-Query via Prediction'
title_zh: 动态Harness搜索：基于预测为每个查询定制多智能体系统
authors:
- Som Sagar
- Shasha Li
- Hejie Cui
- Ransalu Senanayake
- Sercan Ö. Arık
affiliations:
- Google
- Arizona State University
arxiv_id: '2610.04137'
url: https://arxiv.org/abs/2610.04137
pdf_url: https://arxiv.org/pdf/2610.04137
published: '2026-10-01'
collected: '2026-10-06'
category: MultiAgent
direction: 多智能体系统 · 逐查询自适应工作流构建
tags:
- Multi-Agent
- MCTS
- Policy-Value Model
- Workflow Optimization
- LoRA
one_liner: 提出SHIFT框架，通过MCTS和本地小模型预测为每个查询生成最优多智能体工作流
practical_value: '- 电商客服/导购Agent场景可复用逐查询定制架构思路：简单咨询用单Agent降低算力成本，复杂多跳需求（如组合优惠计算、售后流程核验）自动扩容多角色Agent（规划、校验）提升准确率，无需固定套复杂工作流浪费资源

  - 成本敏感的Agent业务可直接复用其cost-aware utility函数设计：把token消耗、latency、工具调用次数加权计入奖励，训练value头选出准确率达标前提下成本最低的工作流，平衡体验和算力开销

  - 多Agent工作流调优可复用「小本地模型+LoRA训练+MCTS无执行搜索」架构：无需修改大执行模型（如Gemini、GPT-4）权重，训练成本低，推理时搜索
  overhead 不到1秒，落地门槛低

  - 工作流优化参考「结构+指令+工具联合调优」结论：不要单独调prompt或者单独开工具权限，三者联合调整能带来最高的准确率提升，比如给电商规划Agent加计算工具的同时配优惠核验指令，效果远好于单独优化单一模块'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多智能体系统多采用固定Harness（角色、指令、工具、通信结构的集合），简单查询算力浪费严重，复杂任务能力不足；而逐查询搜索最优Harness如果每次都执行候选方案，成本过高，人工定制又无法覆盖所有query场景。

### 方法关键点
- 核心为本地小模型Architect：采用Gemma 4 E2B作为backbone，仅训练LoRA适配器和policy-value两个头，无需执行候选Harness即可预测其效用，平衡准确率和执行成本
- 将Harness构建转化为MCTS搜索问题：以最小单Agent为初始节点，搜索空间覆盖新增Agent、新增指令、授权工具三类动作，MCTS全程仅调用Architect做推理，无执行开销
- 训练时结合执行后的真实效用（准确率扣减token、latency、工具/Agent数量惩罚），同时优化三类损失：policy拟合MCTS访问分布、value预测效用、排序损失区分同query下不同Harness的优劣
- 提供两种推理模式：SHIFT-search选访问量最高的Harness（准确率优先），SHIFT-value选效用预测最高的Harness（成本优先）

### 关键实验
在6类基准共9193个任务（数学、多跳QA、代码、表格处理、文档QA、通用助手）上，用Gemini 3.5 Flash作为执行器，对比17个baseline：SHIFT-search平均准确率79.9%，比最强基线Trace高7.2个百分点，长工具密集任务（OfficeQA、GAIA）上分别提升30、15个百分点；SHIFT-value平均准确率74.5%，超过所有基线，同时比最强基线节省32%的执行token；结构、指令、工具三者联合优化比仅调整其中一项最高提升9.1个百分点。

### 核心结论
没有通用最优的多智能体工作流，根据query复杂度动态调整架构，能在成本和准确率上同时超过固定工作流方案。
