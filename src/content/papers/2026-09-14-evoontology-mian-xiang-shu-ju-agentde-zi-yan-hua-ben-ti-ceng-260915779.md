---
title: 'EvoOntology: A Self-Evolving Ontology Layer for Data Agents'
title_zh: EvoOntology：面向数据Agent的自演化本体层框架
authors:
- Meiduo Chong
- Shaolei Zhang
- Ju Fan
- Xiaoyong Du
affiliations:
- Renmin University of China
arxiv_id: '2609.15779'
url: https://arxiv.org/abs/2609.15779
pdf_url: https://arxiv.org/pdf/2609.15779
published: '2026-09-14'
collected: '2026-09-15'
category: Agent
direction: 数据Agent · 自演化语义交互层
tags:
- DataAgent
- Ontology
- SelfEvolution
- MCP
- SemanticLayer
one_liner: 提出封装为MCP服务的自演化本体层，弥合数据Agent与异构数据的语义鸿沟
practical_value: '- 电商/广告多源数据Agent（运营取数、用户行为分析Agent等）可复用三层本体+MCP服务架构，替代静态语义prompt注入方案，避免context浪费，提升工具调用准确率

  - 自演化机制可直接迁移到业务Agent迭代：先通过builder Agent从历史任务初始化语义映射，再从执行轨迹归因缺陷，仅当候选优化在验证集达阈值才上线，降低人工维护语义规则成本

  - 业务Agent选型可参考结论：不同LLM backbone适配的本体层存在显著差异，针对部署的特定backbone做本体迭代的收益远高于通用本体跨模型迁移，不要盲目复用其他模型的语义层配置

  - 文本到SQL类业务场景（如电商自助分析Agent）优先优化Tool层暴露方式，贡献57%的性能增益，远高于Content和Schema层调整，投入产出比最高'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
数据Agent需要处理表格、数据库、文档等异构数据，但现有方案要么让Agent盲探原始数据源，效率低下易出错；要么依赖人工构建的静态语义层注入prompt，受context长度限制无法适配大规模数据，也不能随Agent行为和任务变化动态调整，存在明显的Agent-数据语义鸿沟。

### 方法关键点
- 本体层分为三层：Content层存储领域术语、数据映射、约束、证据组成的语义图；Schema层定义节点和边的类型规则；Tool层封装为MCP服务，提供browse（检索相关语义术语）、resolve（获取完整语义映射）两个工具，仅初始化时向prompt注入极简清单，详细内容按需调用获取，避免context浪费
- 初始化阶段由builder Agent从历史任务集挖掘候选语义概念，通过探针查询验证数据映射的有效性，生成初始本体
- 自演化循环：从Agent执行轨迹归因缺陷，针对性生成Content/Tool/Schema层的局部修改，仅当修改后在验证集上的性能提升超过阈值才更新本体，避免回归

### 关键实验
在DDR-Bench（10-K多源数据分析）、InsightBench（商业分析）、BIRD（文本到SQL）三个基准上，对比无本体的ReAct基线、静态语义层注入基线，覆盖6种主流LLM backbone：DDR-Bench上轨迹准确率平均提升17.8个百分点，最高达26.7；BIRD上SQL执行准确率平均提升7.4个百分点，执行效率提升8.6个百分点；静态语义层甚至会在部分模型上出现性能下降，最高降15个百分点。自演化阶段贡献约40%的总性能增益，其中Tool层优化贡献57%的演化收益。

**最值得记住的一句话：面向异构数据的Agent，可查询的动态自演化本体层的收益远高于静态语义prompt注入，且针对特定backbone的定制化迭代收益显著高于跨模型通用语义层。**
