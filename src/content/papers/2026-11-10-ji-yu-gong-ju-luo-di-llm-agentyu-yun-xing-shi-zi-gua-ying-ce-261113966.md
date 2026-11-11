---
title: Controlled Knowledge Engineering for Taxonomy Induction with Tool-Grounded
  LLM Agents and Runtime-Adaptive Policies
title_zh: 基于工具落地LLM Agent与运行时自适应策略的分类体系自动构建方法
authors:
- Jonas Limniatis
- Bennet Schaarmann
- Georg Reuber
- Robert Stahlbock
affiliations:
- Lufthansa Technik
- Lufthansa Industry Solutions
- University of Hamburg Business School
- Nordakademie University of Applied Sciences
- FOM University of Applied Sciences
arxiv_id: '2611.13966'
url: https://arxiv.org/abs/2611.13966
pdf_url: https://arxiv.org/pdf/2611.13966
published: '2026-11-10'
collected: '2026-11-11'
category: Agent
direction: LLM Agent 分类体系自动构建优化
tags:
- LLM Agent
- Taxonomy Induction
- Tool Grounding
- Dynamic Policy
- Knowledge Engineering
one_liner: 提出工具落地LLM Agent框架TIGA，提升实体中心型分类体系构建的结构质量与语义一致性
practical_value: '- 电商商品类目自动构建可复用TIGA的工具调用约束设计，通过可执行的增/删/查/改工具操作替代自由文本生成，从执行层避免类目实体遗漏、幻觉、层级结构非法问题

  - 动态运行时策略机制可迁移到垂类类目构建场景：允许Agent在推理过程中迭代更新类目组织规则（如品类分层逻辑、命名规范），无需预先写死所有prompt约束，适配不同品类的个性化分类需求

  - 全局评审+有限次修订的设计可直接复用在类目质检流程：对已构建的完整类目做整体一致性校验，仅标记问题实体重入构建流程，平衡质检效果和计算成本

  - 记忆模块的滑动窗口+全量调用日志分离设计可降低Agent上下文开销：仅保留最近N次工具调用在活跃上下文，历史日志按需注入，在保障决策一致性的同时控制token消耗'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
分类体系（Taxonomy）是语义搜索、个性化推荐、电商商品类目管理、RAG的核心基础组件，传统人工构建成本高、扩展性差，现有LLM驱动的自动构建方案依赖自由文本生成，易出现实体遗漏/幻觉、层级关系非法、组织逻辑不一致等问题，无法保障输出结构的完整性与合法性。

### 方法关键点
- 将分类体系构建转化为显式状态上的迭代决策过程，状态包含当前未完成的分类结构、待处理实体集合、动态组织策略、工具调用记忆四部分
- 设计受限工具动作空间：仅允许Agent调用增/删实体、更新策略、查询子树四类可执行工具，所有操作直接修改显式状态，避免自由文本生成的结构错误
- 引入运行时自适应动态策略：Agent可在推理过程中迭代更新分类组织规则，无需预先指定所有约束；工具交互记忆记录历史调用的动作、决策理由、执行结果，保障跨步骤决策一致性
- 可选全局评审模块：所有实体处理完成后，评审Agent校验分类结构的实体覆盖率、策略合规性，最多支持3轮修订

### 关键实验结果
在WordNet、DBLP、TExEval-2、Google商品分类体系4个基准上测试，对比单轮生成（HF）、分层迭代生成（CoL）两类基线，TIGA在7/8的测试配置下取得最高F1，其中边级召回相对最优基线最高提升8.1pp，边级F1最高提升7.4pp；消融实验显示移除动态策略或记忆模块会导致F1下降3~6pp，全局评审对小体量分类体系收益明显，对大体量分类体系受限于修订轮次收益为负。

最值得记住的结论：结构化知识构建任务中，用工具调用约束LLM的输出空间、用显式状态替代隐式生成文本，能大幅提升输出结构的合法性与一致性，但需在质量收益和多轮交互带来的计算开销之间做权衡。
