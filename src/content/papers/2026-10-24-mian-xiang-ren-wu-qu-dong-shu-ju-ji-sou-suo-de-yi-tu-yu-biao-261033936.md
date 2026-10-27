---
title: Bridging Search Intent and Tabular Data in Dataset Search
title_zh: 面向任务驱动数据集搜索的意图与表格数据桥接方法
authors:
- Wenjing Lin
- Madelon Hulsebos
affiliations:
- University of California, Berkeley
- Centrum Wiskunde & Informatica
arxiv_id: '2610.33936'
url: https://arxiv.org/abs/2610.33936
pdf_url: https://arxiv.org/pdf/2610.33936
published: '2026-10-24'
collected: '2026-10-27'
category: RecSys
direction: 表格数据集检索 · 意图对齐
tags:
- Table Retrieval
- Query Expansion
- Dense Retrieval
- NL2SQL
- LLM4IR
one_liner: 提出HySE假设Schema嵌入与FlexPrune元数据过滤组件，提升任务驱动的表格数据集检索效果
practical_value: '- 可复用HySE的查询增强思路：电商商品/内容检索中，用户模糊查询（如“买亲子露营装备”）可让LLM生成符合查询意图的假设商品属性列表/类目结构，和原查询嵌入融合后做召回，解决用户查询和商品标题/属性的语义gap，不需要额外领域训练数据

  - 可复用FlexPrune的NL过滤方案：电商筛选场景中，用户自然语言筛选条件（如“要月销过万的纯棉短袖”）可直接转SQL谓词对接商品元数据索引，替代固定筛选面板，降低用户操作成本

  - 表格序列化技巧：表格类数据（如商家资质、商品参数表）转Markdown格式（表头+样例行）后再做embedding，检索效果更优，可直接复用在商品属性检索、商家信息检索场景

  - 冷启动检索方案：新领域/垂直场景的检索系统冷启动时，用HySE类的查询增强方法，效果甚至优于用少量域内数据微调的Dense Retriever，可节省标注和训练成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有数据集搜索系统高度依赖关键词匹配，仅在用户知晓目标数据集元数据关键词时有效；但多数数据分析师仅清楚分析任务目标，不了解目标表结构，检索效率极低，数据科学家平均要花25%的时间查找数据集，亟需支持任务驱动的自然语言数据集检索能力。

### 方法关键点
-  HySE（假设Schema嵌入）：受HyDE启发，输入用户自然语言任务查询时，用LLM生成2个符合任务需求的假设表格Schema（含表名、列名、2条样例行），将假设Schema的平均嵌入与原查询嵌入以λ=0.5加权融合后做ANN召回，桥接用户意图和表格Schema的语义gap
- FlexPrune：将用户自然语言表达的元数据筛选条件自动转SQL谓词，对接混合元数据索引（融合结构化元数据和表格嵌入）做过滤，支持任意自定义元数据字段的筛选，不需要固定筛选面板
- 构建KAGGLEDS数据集：含6503个真实Kaggle表格，配套自然语言任务查询、关键词查询、元数据查询，是首个任务驱动的表格检索公开基准

### 关键实验
在KAGGLEDS测试集上，HySE的Recall@10达0.609，比语义任务检索基线高2pp，比域内微调的DTR高3.9pp；在16.9万表规模的NQ-Tables公开数据集上，HySE的Recall@10达0.837，比微调的DTR-large高5.8pp，Recall@30高6pp；HySE+FlexPrune的两级流水线，比“语义检索+标签过滤”的基线Recall@10高6pp，达0.704。

零训练的查询增强方案在跨域、冷启动检索场景下的效果，可能超过域内微调的专用检索模型，工程落地成本极低。
