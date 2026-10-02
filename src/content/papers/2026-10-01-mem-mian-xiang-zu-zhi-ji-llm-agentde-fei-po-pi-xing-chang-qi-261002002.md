---
title: 'Mem++: Non-Destructive Memory for Long-Term Organizational LLM Agents'
title_zh: Mem++：面向组织级LLM Agent的非破坏性长期记忆框架
authors:
- Ahmad Yehia
- Aly O. Abdelkareem
- Islam Ahmed
- Hesham Omran
- Khaled Alashmouny
- Christian Claudel
- Abduallah Mohamed
affiliations:
- The University of Texas at Austin
- AIDAChip Inc.
arxiv_id: '2610.02002'
url: https://arxiv.org/abs/2610.02002
pdf_url: https://arxiv.org/pdf/2610.02002
published: '2026-10-01'
collected: '2026-10-02'
category: Agent
direction: Agent 长期记忆架构优化
tags:
- LLM Agent
- Long-term Memory
- Non-destructive Memory
- RAG
- Temporal Retrieval
one_liner: 提出写时不蒸馏、读时选版本的非破坏性组织级记忆框架，性能超现有基线
practical_value: '- 电商运营/客服Agent可复用该非破坏性记忆架构存储不同时期的促销规则、售后政策，全量保留原始文档+时间戳，读时按查询时间过滤有效版本，避免旧规则丢失无法追溯

  - 检索阶段可借鉴 lexical+tag+vector 加权RRF融合+3个最新时间槽位预留的技巧，无需额外LLM调用即可提升时序相关查询的准确率，工程落地成本低

  - 对于需要多角色协作、决策追溯的企业级Agent场景，优先选择写时仅生成embedding不调用LLM的全量存储方案，比写时提取事实的结构化记忆方案成本更低、泛用性更强'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent记忆系统大多针对单会话场景设计，写时会做蒸馏、事实提取或直接覆盖旧版本，无法适配组织级多作者、多版本文档的时序查询需求；若需要查询某一历史节点的有效规则，现有方案要么丢失原始上下文，要么无法准确匹配对应时间范围的有效版本。

### 方法关键点
- 写路径全量存储原始文档，仅生成embedding建立索引，不调用任何生成模型，采用仅追加不删除的设计，每条记录携带时间、作者、状态标记
- 读路径先按查询的as-of时间过滤有效记录，再融合lexical、tag、semantic三个索引的排序结果，用加权RRF做融合，预留3个槽位给最新时间匹配的记录
- 可选合并算子仅对相似文档组做冲突/重述/区分判断，标记旧版本为已替代但不删除，默认关闭不影响基础性能

### 关键实验
在OrgMemBench组织级记忆基准上，搭配gpt-4.1-mini时Mem++得分57.6，超过最强基线RAG 2.6分，比其他记忆系统高8.0~13.1分；在LoCoMo会话记忆基准上平均LLM-judge得分81.5，比Nemori高2.1分；在LongMemEvalS长上下文基准上平均得分74.7，超过Full Context 9.1分。

### 核心结论
对于多版本时序记忆场景，写时不蒸馏、全量保留原始文档、读时再做选择的非破坏性记忆架构，综合性价比远超写时提取事实的结构化记忆方案。
