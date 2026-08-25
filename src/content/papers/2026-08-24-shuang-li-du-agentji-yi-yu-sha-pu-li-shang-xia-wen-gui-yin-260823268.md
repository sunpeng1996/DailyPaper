---
title: Dual-Grained Agent Memory and Shapley Context Attribution for Multimodal Agentic
  Learner
title_zh: 双粒度Agent记忆与沙普利上下文归因的多模态智能学习框架
authors:
- Jieke Wang
- Tiancheng Shen
- Yibo Yang
- Ming-Hsuan Yang
affiliations:
- UC Merced
- Shanghai Jiao Tong University
arxiv_id: '2608.23268'
url: https://arxiv.org/abs/2608.23268
pdf_url: https://arxiv.org/pdf/2608.23268
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: Agent 双粒度记忆优化
tags:
- AgentMemory
- ShapleyValue
- MultimodalLLM
- GradientFree
- NonParametricMemory
one_liner: 为冻结多模态大模型配备梯度无关双粒度记忆与沙普利归因，显著提升推理性能
practical_value: '- 双粒度记忆架构可直接复用在电商导购Agent场景：实例级记忆存相似用户/商品应答case，schema级存通用导购/转化规则，兼顾个性化和普适性，无需微调大模型参数

  - 沙普利上下文归因思路可迁移到RAG召回排序：把召回的片段视为合作博弈玩家，通过子集测试计算每条内容的历史贡献权重，替代纯相似度排序，显著提升召回有效率

  - 在线增量分类器可用于推荐系统的标签体系构建：无需预定义固定类目，自动随业务数据扩展用户/商品兴趣标签空间，降低人工维护成本

  - 全流程梯度-free的设计可直接适配闭源API/端侧模型，适合快速上线业务Agent的记忆增强能力，降低落地成本'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有多模态大模型在科学/数学推理类任务上表现不佳，参数微调需要梯度权限，无法适配闭源或端侧大模型；单粒度Agent记忆要么只能存具体实例泛化性差，要么只存通用规则缺乏落地参考，同时多条召回记忆的信用分配没有合理的解决方案，无法优化排序权重。

### 方法关键点
- 受人类互补学习系统启发，设计双粒度无参数记忆：实例级样本记忆存储单个问题的推理策略和校验规则，类别级Schema记忆存储通用IF-THEN规则，中间用临时反射库隔离，避免样本细节污染Schema的泛化性
- 在线概念分类器自动增量扩展类目空间，无需预定义固定 taxonomy，适配未知的概念分布
- 沙普利上下文归因将召回的规则视为合作博弈的玩家，通过子集测试计算每条规则的边际贡献，作为检索时的加权项，解决多记忆的信用分配问题
- 整个流程完全梯度-free，无需更新大模型参数，支持闭源、端侧模型部署

### 关键结果
在MathVista、MMMU、MMMU-Pro三个多模态推理基准上，测试4个主流 backbone（Qwen3.5 27B/122B、GPT-5-Nano、Gemini-3-Flash），比无记忆基线平均涨点最高达12.5%（GPT-5-Nano），比SOTA记忆基线ViLoMem最高领先2.7个百分点；消融实验显示双粒度记忆和沙普利归因分别贡献了大部分性能增益。

### 最值得记住的话
Agent记忆的双粒度分离+历史效用加权检索，是无需微调就能稳定提升大模型任务性能的低成本落地方案。
