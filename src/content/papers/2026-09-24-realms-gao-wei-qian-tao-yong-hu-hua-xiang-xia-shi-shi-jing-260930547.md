---
title: 'REALMS: An AI-Assistant Conversational System for Real-Time Exact Audience
  Sizing over High-Dimensional Nested Profiles'
title_zh: REALMS：高维嵌套用户画像下实时精准人群计算对话式AI助手
authors:
- Haixu Ma
- Aditya Bansal
- Shubham Lohiya
- Sumit Ranjan
affiliations:
- Adobe Inc.
arxiv_id: '2609.30547'
url: https://arxiv.org/abs/2609.30547
pdf_url: https://arxiv.org/pdf/2609.30547
published: '2026-09-24'
collected: '2026-09-28'
category: Agent
direction: Agent 营销人群量级查询优化
tags:
- NL2SQL
- KG-RAG
- Conversational Agent
- Audience Sizing
- Enterprise Analytics
one_liner: 提出融合语义检索、KG-RAG和NL2SQL的对话系统，实现高维嵌套画像下秒级精准人群量级计算
practical_value: '- 可复用分桶式属性检索设计：对高维schema按语义分桶后独立建向量索引，并行召回各桶top-k属性，解决大schema下检索结果偏聚单一品类的问题，提升召回覆盖率

  - KG-RAG构建技巧：将历史查询、schema属性、SQL模板、算子关联为知识图谱，比纯语义RAG的NL2SQL执行准确率提升22pct，适合业务侧结构化查询生成场景

  - 架构可直接复用：离线层做嵌套数据压平、属性embedding预计算、索引构建，在线链路仅做轻量检索+生成，兼顾跨客户通用性和低延迟，适合企业级分析类Agent部署

  - 生产落地优化点：SQL生成后增加合规校验+自纠正环节，过滤PII属性、语法/逻辑错误，降低生产故障和合规风险'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统人群量级计算依赖抽样、预计算或预测模型，高维嵌套用户画像下误差不可控、端到端延迟达数小时，无法支撑营销人员迭代式人群规划需求；现有NL2SQL方案适配企业级复杂异构schema定制成本高，泛化性差，难以落地到生产环境。

### 方法关键点
1. 离线预处理：将嵌套用户画像压平为列式存储，为每个属性生成语义描述并计算embedding，按语义分桶（人口属性、行为属性、交易属性等）独立建向量索引；同时构建历史查询-SQL知识图谱，关联语义、结构、执行关系
2. 在线检索：对用户query做分桶并行ANN检索，从每个语义桶召回top-k相关属性，避免单语义类结果偏聚，保障属性覆盖度
3. 结构化查询生成：通过KG-RAG召回结构+语义双匹配的历史查询样例，结合通用模板做in-context learning生成SQL，经校验合规后执行，返回结果同时附带自然语言逻辑解释

### 关键实验
基于600条真实+生成的企业级人群查询（覆盖计数、top-k、占比三类场景）评测：属性检索Recall@5达94%，Exact Match@5达93%；端到端SQL执行匹配准确率90%，LLM评判语义匹配率95%；负载30RPM时无请求失败，中位数延迟8.3秒，60RPM时中位数延迟10秒，故障率不到2%。ablation实验显示去掉KG-RAG准确率下降22pct，去掉schema检索准确率下降33pct。

### 核心结论
面向企业级结构化分析的LLM Agent，核心是将语义检索作为LLM和底层数据的中间层，用离线标准化+在线轻量生成的架构平衡通用性、准确率和延迟
