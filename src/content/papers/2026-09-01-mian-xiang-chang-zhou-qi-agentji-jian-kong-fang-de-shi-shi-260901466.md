---
title: 'Parsing the Stream: A Live Trace Model for Long-Horizon Agents and Their Observers'
title_zh: 面向长周期Agent及监控方的实时Trace增量折叠模型
authors:
- Egor Pakhomov
- Erik Nijkamp
affiliations:
- Salesforce AI Research
arxiv_id: '2609.01466'
url: https://arxiv.org/abs/2609.01466
pdf_url: https://arxiv.org/pdf/2609.01466
published: '2026-09-01'
collected: '2026-09-02'
category: Agent
direction: 长周期Agent · 上下文管理与可观测
tags:
- Long-Horizon Agent
- Trace Parsing
- Context Compression
- Observability
- Deterministic Fold
one_liner: 提出增量折叠的实时Trace模型，同时服务长周期Agent与监控方，降本5-7倍准确率大幅提升
practical_value: '- 长周期电商导购Agent、任务型Agent可复用该单源折叠架构，用同一份Trace数据同时支撑Agent上下文压缩与运营监控，避免双系统重复建设，降低维护成本

  - 上下文压缩优先采用带确定性统计的定制聚合方案而非通用summarization，针对业务任务保留所需明确统计量（如用户累计浏览商品数、加购金额等），避免静默截断导致任务失败，实测长链路任务成功率可从27%提升至100%

  - 工程落地可复用论文给出的11条Trace折叠要求，尤其注意「聚合必须明确标注覆盖范围」「禁止静默截断」「按来源而非值去重」三个高频坑点，避免上线后出现无告警的逻辑错误'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
长周期Agent运行过程中持续生成的Trace规模会快速超出两个核心消费方的承载能力：人类监控方读取全量原始Trace回答运营问题准确率低、token成本极高；Agent自身的上下文窗口容量有限，塞入全量Trace会导致调用成本暴涨、长链路任务成功率暴跌。当前业界普遍采用可观测工具+上下文管理两套独立系统处理，重复建设成本高、数据一致性难以保障。

### 方法关键点
- 四层核心架构：1）仅追加的类型化事件账本，支持字节偏移断点续传，自动去重避免token统计虚高；2）单趟增量折叠将事件流规约为带类型的运行状态RunState，采用聚合保留的驱逐策略，不会丢失关键统计量；3）带生命周期的版本化派生节点，支持事后回溯修正不篡改历史；4）面向不同消费方的编译视图，人类监控页面与Agent上下文视图同源，保证数据一致。
- 配套两个确定性评估基准：COMPREHEND监控问答基准（自动生成问题、精确判分）、CONTINUE长链路任务基准（控制注入错误、对比不同上下文策略的效果）。

### 关键结果
监控侧：对比读取全量原始Trace，编译视图输入token量减少14~15倍，成本降低5~7倍，回答监控问题准确率从0.48提升至0.85~0.87；
Agent侧：120步长链路累积任务中，全上下文prompt成功率仅27%（8/30），基于折叠视图的上下文成功率达100%（30/30），单跑成本从$7.13降至$1.59。

### 最值得记住的结论
长周期Agent上下文管理的核心不是尽可能多保留历史，而是明确保留任务所需的关键统计量，确定性聚合的效果远好于无差别的历史保留或通用压缩。
