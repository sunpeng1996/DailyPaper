---
title: 'StarHarness: Evolving Harnesses with Stratified Search for Enterprise Environments'
title_zh: StarHarness：面向企业环境的分层搜索驱动Agent Harness演化框架
authors:
- Esakkivel Esakkiraja
- Denis Akhiyarov
- Vikas Yadav
- Sai Rajeswar
- Patrice Bechard
- Sridhar Nemala
- Sagar Davasam
affiliations:
- ServiceNow
- Mila
- Université de Montréal
arxiv_id: '2608.24804'
url: https://arxiv.org/abs/2608.24804
pdf_url: https://arxiv.org/pdf/2608.24804
published: '2026-08-25'
collected: '2026-08-26'
category: Agent
direction: Agent 企业场景Harness自动演化优化
tags:
- Agent
- Harness Optimization
- Stratified Search
- Cross-model Transfer
- Enterprise AI
one_liner: 提出分层搜索驱动的Agent Harness演化框架，固定模型权重即可大幅提升企业场景Agent性能
practical_value: '- 企业/电商Agent落地优先迭代Harness（提示词、工具接口、执行流程、子Agent结构），无需修改模型权重，收益比单纯Prompt优化高13~22pp，投入产出比远高于模型微调/换更大模型

  - 做Harness/提示词迭代时可复用任务拆分逻辑：按基线失败模式分层抽样，拆为提案器可见搜索集、隐藏选择集、留资验证集，避免过拟合到特定任务，保证泛化性

  - 多模型部署场景可复用同一套演化后的Harness，不需要为每个模型单独调优，最高可降低80%以上的多模型适配人力成本

  - Harness优化优先覆盖三个方向：修复工具接口适配问题、显式编码环境规则、沉淀可复用领域操作知识，可直接减少Agent无效推理和违规调用'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
企业场景工具增强Agent的性能高度依赖Harness（提示词、工具接口、执行策略、子Agent结构等）与环境的适配性，手动调优Harness人力成本极高，现有优化方法容易过拟合到特定任务，跨模型泛化性差，缺乏针对有状态企业场景的高效演化方案。

### 方法关键点
- 固定模型权重，仅对Harness的可编辑空间迭代优化，覆盖提示词、工具schema、参数预处理、子Agent结构、上下文管理、执行策略等维度
- 基于基线失败模式、任务得分、验证通过率三个维度对任务分层抽样，拆分为对提案器可见的搜索集、隐藏的选择集、完全留资的测试集，从机制上避免过拟合
- 支持爬山、树搜索两种演化策略，通过提案-验证-评估的自动迭代流程，仅保留能提升隐藏选择集性能的补丁，迭代过程全可回溯
- 设置严格guardrails禁止硬编码任务答案、访问隐藏真值等操作，保证演化出的能力是通用环境适配能力而非任务特解

### 关键实验
在ITBench SRE、EnterpriseOps-Gym ITSM、AutomationBench Finance三个企业级Agent基准上，对比默认Stirrup Harness、GEPA Prompt优化等baseline：
- 全基准性能比默认Harness提升20~35pp，每个环境仅需接受4~12次修改即可达成
- 演化后的Harness无需重新迭代即可跨GPT、Qwen模型家族迁移，最高可带来46.3pp的性能提升
- 同时推理成本降低17%~53%，交互轮次、工具调用次数、违规操作数均显著下降

### 核心结论
固定模型权重的Harness演化是比模型缩放、单纯Prompt优化性价比更高的企业Agent落地优化路径。
