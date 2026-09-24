---
title: 'Learning from Failures: Heterogeneous Graph Memory for Small Language Model
  Tool-Using Agents'
title_zh: 面向小语言模型工具调用Agent的失败感知异构图记忆框架
authors:
- Jiaxing Li
- Lei Song
- Rui Dong
- Youyong Kong
affiliations:
- 东南大学计算机科学与工程学院
arxiv_id: '2609.28003'
url: https://arxiv.org/abs/2609.28003
pdf_url: https://arxiv.org/pdf/2609.28003
published: '2026-09-23'
collected: '2026-09-24'
category: Agent
direction: Agent工具调用 · 异构图失败感知记忆
tags:
- Agent
- SLM
- Tool Use
- Heterogeneous Graph
- Memory Augmentation
one_liner: 提出失败感知异构图记忆框架FRESH，无需微调即可大幅提升小语言模型工具调用Agent的可靠性
practical_value: '- 电商客服/运营Agent可直接复用失败经验结构化思路：将历史工单的成败操作、前置校验条件、修复路径存储为异构图，无需微调LLM即可降低误退款、误改订单等违规操作概率

  - 可复用Do/Avoid/Check/Repair四分类记忆提示模板：检索到的经验压缩为结构化指令，比全量回放历史轨迹节省token，且小模型更容易理解执行

  - 风险操作拦截机制可直接迁移：对涉及状态变更的操作（退款、改价、发券等），增加前置校验门，匹配历史失败案例的前置条件，直接拦截/修正不合规操作，避免不可逆业务损失

  - 小模型Agent落地参考方案：不需要大量微调数据，仅靠结构化历史经验即可提升小模型任务成功率，适合端侧/低算力场景的Agent部署'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
小语言模型（SLM）推理部署成本低，适合大规模/端侧Agent落地，但在长周期有状态的工具调用场景（如电商订单处理、票务改签）中，易出现漏读必要观测、重复无效调用、前置条件未满足就执行写操作等结构性错误，可能引发政策违规、不可逆资产损失。现有微调方案需大量标注数据和算力，平文本记忆无法保留失败的因果上下文和安全约束，易重复触发同类错误。

### 方法关键点
- 异构图经验建模：将历史成败轨迹拆解为任务、工具、操作、观测、错误、修复方案、前置条件等多类型节点，通过带语义的边（calls/requires/fails_because/fixed_by等）关联依赖，明确区分可复用的正确操作与需规避的失败模式
- 异构GNN检索器：基于轨迹反馈自动标注正负样本，训练检索模型为新任务召回相关经验，压缩为Do/Avoid/Check/Repair四类结构化提示，比全量轨迹回放更省token
- 风险操作校验门：对涉及状态变更的操作，结合历史前置条件、实时观测、领域规则做校验，输出允许/修正/拦截/转人工四类决策，避免违规操作
- 全程不微调SLM参数，经验图可独立迭代更新

### 关键实验
在τ-bench（航空、零售域工具调用）和AppWorld（多应用长周期API调用）上测试，对比无记忆、Vector-RAG、Mem0、H-EPM等7个基线，覆盖3个不同量级的开源SLM：
- τ-bench上相对无记忆基线平均提升10.8%~53.2%，其中Llama3.2-1B零售域pass4指标提升100%
- AppWorld挑战测试集PR达0.146，比最优基线提升26.9%，同时执行步骤更少
- 消融实验显示，失败记忆模块和风险校验门分别带来10%以上的性能增益

### 核心结论
无需微调SLM，仅通过结构化存储和检索历史成败经验，就能同时提升工具调用Agent的成功率和安全性，对小模型Agent规模化落地价值极高。
