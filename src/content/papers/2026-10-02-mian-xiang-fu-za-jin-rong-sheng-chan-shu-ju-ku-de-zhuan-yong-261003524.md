---
title: 'From Benchmarks to Production: A Text-to-SQL System for Complex Financial
  Data'
title_zh: 面向复杂金融生产数据库的专用Text-to-SQL系统FLINT
authors:
- Arijit Sehanobish
- Bruno Gomes Coelho
- Guillaume Michel
- Sophia Zhi
- Valerie Faucon-Morin
- Kristen Howell
affiliations:
- Kensho Technologies
arxiv_id: '2610.03524'
url: https://arxiv.org/abs/2610.03524
pdf_url: https://arxiv.org/pdf/2610.03524
published: '2026-10-02'
collected: '2026-10-05'
category: Agent
direction: Agent 垂直域结构化数据查询优化
tags:
- Text-to-SQL
- Agent
- Production System
- Domain Adaptation
- Schema Linking
one_liner: 提出融合Lookup Agent、专家模板检索、外键链剪枝的专用Text-to-SQL系统，精度较SOTA基线高20%以上
practical_value: '- 垂直域结构化查询场景（如电商商家后台取数、运营多表分析工具）优先解决值映射问题：76-96%的错误来自错误的参考表过滤ID，可复用Lookup
  Agent架构，将自然语言概念动态映射到库内枚举ID/外键值，避免依赖LLM幻觉生成ID

  - 小样本模板检索无需堆量级：仅需15-30个覆盖核心查询模式的专家标注样例，就能通过embedding检索提供足够的结构模板参考，配置成本仅1-3人周，远好于无针对性的大量低质量样例

  - 三级评估管道可直接复用：AST规范化→列对齐比较→LLM Judge的流程，解决相同语义SQL写法差异导致的评估误差，适合内部BI/取数工具的效果评测

  - 并行化Agent流水线可降低latency：无数据依赖的Lookup、模板检索、实体链接、Schema Linking步骤并行执行，兼顾效果的同时把端到端latency控制在10-20s，符合生产级要求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有通用Text-to-SQL系统在Spider、BIRD等学术基准上精度可达70-85%，但迁移到金融等生产场景的归一化数据库时精度不足50%：这类库为优化存储效率，将指标、维度、实体等概念编码为无可读性的整数外键，单条简单查询平均需要5-6次多表关联，通用方案无法解决自然语言到不透明ID的映射问题，其中76-96%的错误都是过滤ID错误。

### 方法关键点
- 并行流水线架构：无依赖的Lookup Agent、相似查询检索、实体链接、Schema Linking步骤并行执行，后续接SQL生成、执行反射串行步骤，控制端到端延迟
- Lookup Agent：分两步映射自然语言概念到参考表过滤条件，先匹配相关参考表，再查询拉取候选值由LLM选对应ID，金融指标场景通过SME curated缩编候选集保证98%召回
- 专家模板检索：维护仅15-30个覆盖核心查询模式的专家标注query bank，通过embedding检索Top3相似样例，提供关联结构模板与SQL样例
- 外键链Schema Linking：不依赖表名列名相似度，通过遍历外键链剪枝大schema为相关子集，自动识别关联所需的中间桥接表

### 关键实验
在两个生产金融数据集（共359个专家标注问题，平均单条查询需5-6次关联，最多13次关联）上，FLINT在Financials数据集精度68.8%，Transactions数据集精度65.2%，比最优基线（ReFoRCE）分别高22.2、18.1个百分点，端到端延迟仅10-20s，比多Agent基线快5倍。

### 核心结论
学术Text-to-SQL基准到生产部署的差距核心不是SQL生成能力，而是领域知识的注入：知道要关联哪些表、值的含义是什么、用户问题的隐含意图。
