---
title: 'Agent Self-Improvement with Frozen Weights: The Added Value and Limits of
  Failure Traces'
title_zh: 固定权重下Agent的自我优化：失败轨迹的增益价值与边界
authors:
- Arkid Mitra
affiliations:
- Hopit AI
arxiv_id: '2611.11342'
url: https://arxiv.org/abs/2611.11342
pdf_url: https://arxiv.org/pdf/2611.11342
published: '2026-11-08'
collected: '2026-11-10'
category: Agent
direction: Agent固定权重自优化 · 失败轨迹利用
tags:
- Agent_Self_Improvement
- Frozen_LLM
- Failure_Trace
- Harness_Optimization
- Prompt_Evolution
one_liner: 量化固定权重Agent通过失败轨迹优化外围提示的真实增益与适用边界
practical_value: '- 做电商客服、售后等业务Agent的harness优化时，必须设置无失败轨迹的搜索对照组，避免把随机搜索的增益错当成失败轨迹的价值，减少无效迭代

  - 优化得到的单条规则（比如售后地址变更流程）不要只在单决策点验证，必须做全会话、跨场景的泛化测试，避免全场景负向效果

  - 业务Agent的prompt对比不要仅和空prompt对齐，要加中性无规则prompt做对照组，排除加提示本身的正向干扰

  - 上线前必须做评测规则的盲审，比如电商售后会话的判分规则，至少抽样10%做盲审，避免规则缺陷导致的效果误判'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
目前大量落地的Agent采用小参数开源模型，权重固定不可微调，仅能优化外围harness（提示、规则、控制逻辑），但现有研究无法区分harness优化的增益是来自失败轨迹的有效学习，还是随机搜索、规则复述的效应，普遍高估失败轨迹的价值，也未明确其适用边界。

### 方法关键点
- 固定基座为Qwen3.5-9B，权重全程不更新，harness仅修改系统提示槽位的规则笔记
- 两组严格对照：实验组由大尺寸teacher模型读取Agent失败轨迹生成WHEN-THEN规则；对照组采用相同流程、预算，仅将失败轨迹替换为固定文本/官方文档，隔离搜索效应
- 新增严格的规则准入gate：只有随机实验验证单条规则增益>1%、无上下文负向（损失<1%的概率<10%）、无严重危害才准入，所有实验提前预注册
- 新增Benchmark盲审机制，提前冻结缺陷样本列表，避免评测规则干扰结果

### 关键实验
- 数据集：τ2-bench零售客服（2997个单决策点样本、114个全会话任务）、BFCL多轮工具调用基准
- 核心结果：单决策点场景下，带失败轨迹的规则比无轨迹搜索准确率高4.0pp，其中60%的增益来自无轨迹的搜索本身；全会话场景下，带失败轨迹的规则相对标准harness无显著增益（-1.3pp，置信区间跨0）；BFCL场景下所有从失败轨迹生成的规则均未通过准入gate，过审的无轨迹规则在holdout集无增益，中性提示反而比所有规则高4.5pp；BFCL有60.8%的样本存在评测缺陷。

### 核心结论
固定权重Agent的失败轨迹优化增益远低于预期，多数增益来自规则搜索而非失败经验，全场景泛化性极差，上线前必须做严格的对照和泛化验证。
