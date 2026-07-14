---
title: Boolean queries are all you need?
title_zh: 布尔查询足以支撑智能搜索代理？
authors:
- Charles L. A. Clarke
- Mark D. Smucker
affiliations:
- University of Waterloo, Canada
arxiv_id: '2607.11362'
url: https://arxiv.org/abs/2607.11362
pdf_url: https://arxiv.org/pdf/2607.11362
published: '2026-07-13'
collected: '2026-07-14'
category: Agent
direction: 智能搜索代理 · 布尔查询检索
tags:
- Agentic Search
- Boolean Retrieval
- LLM4IR
- RAG
- Query Generation
one_liner: LLM驱动布尔查询的智能搜索代理，无需训练与全局统计，性能超过多数一阶召回器
practical_value: '- 可复用LLM自动生成布尔查询的逻辑，替代电商搜索中人工配置的query改写/扩展规则，尤其适合属性、类目等需要精确匹配的检索场景，降低规则维护成本

  - 最短子串排序（SSR）无需全局IDF统计、词权重与监督训练，可直接用于冷启动商品库的检索场景，无需等待语料统计数据产出即可快速上线

  - 搜索代理的多轮交互框架可直接迁移到商品导购Agent、RAG问答系统，通过限制单query模型调用次数、去重已判断文档的机制控制推理成本

  - 检索效果评估阶段可借鉴UMBRELA工具补全未标注相关文档，大幅降低电商大规模query测试集的人工标注成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
布尔查询曾是传统检索的核心方案，能实现精确匹配，但普通用户难以构造有效查询，逐步被关键词检索、稠密语义检索替代；而LLM不存在人类的查询构造能力障碍，探索用LLM驱动的布尔查询代理能否实现高性能检索，免去传统检索所需的监督训练、全局统计、词权重计算等前置成本。
### 方法关键点
- 检索层采用**最短子串排序（SSR）**：将语料视为连续字符串，匹配布尔查询的最短子串，文档得分由匹配子串的数量和长度共同决定（短匹配权重更高），无需全局统计，支持动态索引更新。
- 搜索代理Vole交互逻辑：底层LLM（GPT-5.5）可选3种动作（发起新布尔查询、拉取已有查询的下一条结果、拉取全文档），每轮返回文档relevance打分，限制单topic最多100次模型调用、最多50份文档判断，自动去重已判断文档降低成本。
- 排序与评估逻辑：代理发现的文档先按LLM判断的relevance等级排序，再按发现顺序排序，未标注文档用UMBRELA工具（GPT-4o）补全标注后计算指标。
### 关键结果
基于TREC 2024 RAG Track的86个标准主题、MS MARCO V2.1去重片段集测试，Vole的NDCG@10达0.6863，超过多数稠密、稀疏、学习型稀疏一阶召回器，仅低于带LLM重排的赛道top方案；单topic平均模型调用不到74次，远低于赛道top3方案的194次调用成本。

**最值得记住的结论**：LLM不存在人类构造布尔查询的能力障碍，简单的模式匹配足以支撑高性能智能搜索，无需复杂的语义匹配模型和训练流程。
