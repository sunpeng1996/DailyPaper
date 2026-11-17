---
title: Adaptive-Elbow Graph Traversal for Schema Retrieval in Text-to-SQL
title_zh: 面向Text-to-SQL schema检索的自适应肘点图遍历方法ElbowHop
authors:
- Fabio Picariello
- Salvatore Cipolla
- Susanna Bonura
- Vito Morreale
affiliations:
- Engineering Ingegneria Informatica S.p.A.
arxiv_id: '2611.20979'
url: https://arxiv.org/abs/2611.20979
pdf_url: https://arxiv.org/pdf/2611.20979
published: '2026-11-16'
collected: '2026-11-17'
category: RAG
direction: RAG检索优化 · Text-to-SQL schema召回
tags:
- RAG
- Text-to-SQL
- Schema Retrieval
- Graph Traversal
- Adaptive Cutoff
one_liner: 提出结合自适应肘点截断与双向外键遍历的低开销Text-to-SQL表检索方法，大候选集精度较固定top-k翻倍
practical_value: '- RAG召回阶段可直接替换固定top-k为自适应肘点截断方案，仅需调整单参数α即可平衡召回率与精度，无需额外标注或模型重训，适配大候选池的电商商品、知识库检索场景

  - 对于存在明确关联关系的实体（如电商用户-订单-商品、内容-标签体系），可在语义召回后加1跳双向关联遍历，低成本补全语义相似度漏召的桥接实体，紧预算下桥接实体召回率最高可提升15pp

  - 多平滑窗口的肘点检测逻辑可开箱复用，通过相似度曲线形状自适应决定召回量，简单query少召减少下游噪声，复杂query多召保障覆盖，工程落地成本极低'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
基于LLM的Text-to-SQL系统性能上限由上游schema检索步骤决定：固定top-k的稠密检索存在两个核心缺陷，一是固定预算无法适配query复杂度，简单query引入过多噪声降低生成质量，复杂query漏召回必要表导致SQL完全错误；二是语义相似度无法捕获外键关联的桥接表，无法支撑多表join逻辑生成。而Agent式检索调用LLM成本高、延迟大，无法适配大规模生产场景，轻量本地检索的优化需求迫切。
### 方法关键点
1. 自适应肘点截断：对稠密检索得到的表相似度降序列表，用两个和候选池规模绑定的滑动窗口做平滑，计算每个点到序列首尾连线的距离，取最大距离点作为肘点，通过单参数α缩放肘点位置得到召回阈值，自适应决定每个query的召回数量。
2. 双向外键遍历：对语义召回的表集合做最多1跳的双向外键关联遍历，补全语义相似度无法命中的桥接表，遍历逻辑在内存中完成，单query开销仅几十毫秒。
3. 两个模块完全解耦，可根据业务场景单独落地。
### 关键结果
在3个不同规模的候选池上做预算匹配对比：74表候选池下相同召回率时精度较固定top-k提升44%，546表候选池下精度提升104%（翻倍）；1跳外键遍历在紧预算下桥接表召回率最多提升15个百分点，全检索链路p95延迟低于450ms，符合生产要求。
### 核心结论
低开销检索优化的核心是用数据自适应规则和固有结构信息补全语义检索的短板，无需引入额外大模型调用即可获得显著收益
