---
title: 'FICO: Find-Then-Compute for Corpus-Level Spreadsheet Question Answering'
title_zh: FICO：面向语料库级表格问答的先检索后计算框架
authors:
- Sandarsita Guntupalli
- Lu He
- Kang Li
affiliations:
- Carnegie Mellon University
- Atlassian
arxiv_id: '2610.03958'
url: https://arxiv.org/abs/2610.03958
pdf_url: https://arxiv.org/pdf/2610.03958
published: '2026-10-02'
collected: '2026-10-06'
category: Agent
direction: Agent 结构化数据问答架构优化
tags:
- Spreadsheet QA
- RAG
- Agent
- Text-to-SQL
- Table Retrieval
one_liner: 提出先检索后计算的语料库级表格问答框架FICO，大幅超越现有RAG类基线
practical_value: '- 做电商交易报表、用户行为表、商品库存表等结构化数据的问答Agent时，放弃传统片段式RAG，改用「检索选表→生成SQL全表计算」的架构，可大幅提升聚合类查询（如类目销量、复购率统计）的准确率

  - 表检索阶段可复用FICO的设计：先给每个表生成包含主题、列名、统计特征的文本摘要做粗排，再用列名+代表性值的schema签名做精排，召回率远高于直接嵌入表格片段

  - 生成SQL的prompt中加入列的数值范围、代表性样例、表行数等元信息，可降低约7个点的列选错、谓词写错概率，效果远优于仅提供列名

  - 若SQL执行返回空结果，可自动fallback到下一个候选表重试，能减少源选择错误带来的损失'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统RAG处理需要聚合、统计的表格类查询时，仅能获取截断的表格片段，缺少全量行数据支撑计算，准确率极低；语料库级表格问答还需解决多表源选择、近重复表消歧问题，现有方案未端到端打通检索与计算环节，存在明显性能瓶颈。

### 方法关键点
- 拆分Find与Compute两个独立阶段，解耦源选择与全表计算逻辑
- Find阶段：入库时将异构表格统一转为标准化SQLite库，自动识别表头、宽表转长表；LLM生成每个表的主题、列名、适用场景摘要，通过embedding粗召Top10候选，再用列名+代表性值的schema签名精排，空结果自动fallback到下一个候选表
- Compute阶段：prompt包含表行数、列类型、数值范围、3条样例行，调用Gemini 3 Flash生成只读SQL，最多2次错误重试，SQLite不支持的操作走pandas路径，执行结果标准化后输出

### 关键实验
- 测试集：DataBench（80个数据集、1810个查询）、MiMoTable（174个多sheet工作簿、508个英文查询）
- 核心结果：DataBench上FICO准确率达76.2%，比同源选择的强TableRAG风格基线高9.9个点，比前缀RAG高63.4个点；MiMoTable上准确率79.7%，比前缀RAG高57.5个点；给基线喂金标准表后准确率升至76.3%，证明源选择带来的性能损失约10个点。

### 核心结论
哪怕是最强的SQL生成器也无法弥补选错数据源的问题，源消歧是语料库级结构化数据问答的独立核心环节。
