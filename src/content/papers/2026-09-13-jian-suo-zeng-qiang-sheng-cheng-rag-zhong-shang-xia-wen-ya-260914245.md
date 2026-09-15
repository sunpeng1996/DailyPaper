---
title: The Attribution-Compression Frontier in Retrieval-Augmented Generation
title_zh: 检索增强生成（RAG）中上下文压缩与归因的性能边界研究
authors:
- Deepanshu Mody
affiliations:
- New York University
arxiv_id: '2609.14245'
url: https://arxiv.org/abs/2609.14245
pdf_url: https://arxiv.org/pdf/2609.14245
published: '2026-09-13'
collected: '2026-09-15'
category: RAG
direction: RAG 上下文压缩 归因保真度评估
tags:
- RAG
- Context Compression
- Citation Attribution
- NLI
- Evaluation
one_liner: 量化5类RAG上下文压缩方案的归因保真度差距，绘制归因-压缩性能权衡边界
practical_value: '- 业务RAG（商品问答、客服Agent、种草文案生成）的引用校验不能仅核对压缩后上下文，必须回查原始数据源，避免「归因洗白」导致的虚假回答风险

  - 选型RAG压缩方案时优先选保留source ID映射的extractive类压缩，抽象压缩/无映射的token pruning（如默认配置LLMLingua）的真实归因精度仅0.1左右

  - 统计压缩率时采用实际压缩比而非标称预算，抽象压缩（如RECOMP）的实际压缩率可能比标称低30倍以上，避免成本核算失真

  - 评估RAG全链路成本时需纳入归因校验的token开销，该部分消耗可能与生成环节相当'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RAG上下文压缩可大幅降低大模型输入成本，但现有评估仅关注答案质量，忽略引用的真实可溯源性，抽象压缩可能切断输出与原始数据源的关联，导致看似引用正确、实则无对应原始证据的「归因洗白」问题，在电商商品介绍、客服回答等场景易引发合规风险。

### 方法关键点
- 固定生成器为Qwen2.5-7B-Instruct，统一采用ALCE风格带引用提示词，对比6类压缩方案：无压缩、重排序、提取式选句、RECOMP抽象压缩、LLMLingua-2 token剪枝、ECR（提取-聚类-重写）压缩
- 设计双维度归因评估：emitted精度（校验引用与压缩后上下文的一致性）、grounded精度（校验引用与原始数据源的一致性），两者差值为归因洗白的量化指标
- 实现3种校验模式：仅校验压缩后上下文、仅校验声明的源ID、自动溯源无声明压缩单元后校验

### 关键结果
在ASQA（944个事实类问题）、QASPER（976个科研论文问题）上测试，标称压缩率0.25时：
- RECOMP的emitted精度达0.86，但grounded精度仅0.12，两者差值0.74；LLMLingua-2的对应差值为0.43
- 提取式选句的grounded精度稳定在0.43~0.49，仅比无压缩的0.51低约15%，答案EM下降不到30%
- 抽象压缩的实际压缩率仅为标称的1/32左右，存在严重预算虚标

**最值得记住的一句话**：RAG压缩的引用可信度不能只看和压缩后文本的一致性，必须锚定原始数据源，没有源映射的压缩方案本质上是牺牲归因保真度换成本降低。
