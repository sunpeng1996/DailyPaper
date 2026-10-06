---
title: 'PACMI: Provenance-Aware Cascading Memory Invalidation for Long-Term LLM Agents'
title_zh: PACMI：面向长期LLM Agent的起源感知级联记忆失效框架
authors:
- Yiqi Wang
- Jiaqi Liu
- Jiaqi Zhang
- Zhangkai Wu
- Yiqun Duan
- Mingkai Zheng
- Taotao Cai
affiliations:
- University of Southern Queensland
- Southern University of Science and Technology
- Jiangsu University
- The University of Sydney
- Uploading Inc.
arxiv_id: '2610.05732'
url: https://arxiv.org/abs/2610.05732
pdf_url: https://arxiv.org/pdf/2610.05732
published: '2026-10-05'
collected: '2026-10-06'
category: Agent
direction: Agent 长期记忆失效管理
tags:
- LLM-Agent
- Long-Term-Memory
- Provenance-Graph
- Memory-Invalidation
- Benchmark
one_liner: 提出起源感知级联记忆失效框架，配套多领域诊断基准，解决LLM Agent过时记忆误用问题
practical_value: '- 电商智能导购、个性化推荐Agent可直接复用四状态有效性格设计，区分`active/needs-verification/historical-only/superseded`四类记忆，既避免用过时的用户偏好、库存、地址信息生成错误推荐/回答，也保留历史记忆支持订单溯源、用户行为分析

  - 记忆更新时借鉴级联传播逻辑，例如用户修改收货地址后，自动将关联的配送时效预估、周边本地生活推荐等依赖记忆标记为待验证，无需全量重刷记忆库即可降低错误率

  - 复用前提检查模块设计，当用户Query包含过时假设（如用户问「之前加购的悉尼酒店有优惠吗」但已改行程去墨尔本），先主动纠正前提再回答，降低客诉提升体验

  - 生产级长期记忆系统必须避免原地改写记忆，非破坏性更新可避免历史查询类需求的准确率崩塌，比如用户要查去年的订单地址时不会被新地址覆盖'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM Agent长期记忆方案仅优化存储、检索逻辑，未解决新证据到来后的过时记忆问题：过时记忆语义仍可能与Query高度相关被误召回，同时不能直接删除（需保留作为历史证据），现有方案既无法追踪依赖关系更新下游衍生记忆，也无法兼顾当前决策正确性和历史信息留存。

### 方法关键点
- 构建记忆起源图，用带类型的依赖边（supports/used-by等）关联记忆节点，新证据到来时先判定其与候选记忆的关系（update/contradict等），仅标记直接冲突/更新的记忆作为失效起点
- 设计四状态有效性格：`active < needs-verification < historical-only < superseded`，按依赖边类型级联传播有效性状态，全程非破坏性更新，保留原始记忆文本
- 检索时按Query类型添加状态偏置：当前类Query优先召回active/needs-verification记忆，历史类Query优先召回historical-only/superseded记忆；新增前提检查模块，识别Query包含的过时假设，提前注入纠正信息到生成上下文

### 关键结果
基于自建的5领域（个人档案、偏好、金融推荐等）100案例、300Query诊断基准，对比Vector RAG、A-MEM-style等6种基线：
- PACMI最终准确率达0.99，较最强基线A-MEM-style的0.90提升9个百分点，配对McNemar检验p=2.56×10⁻⁶，差异显著
- 前提检查模块在控制分布下precision、recall、F1均为1.00；移除前提检查后最终准确率降至0.83，移除历史保留后历史Query准确率降至0.36
- 级联传播可将记忆状态正确率提升37%，但在当前小记忆库规模下最终准确率提升未达0.05显著性阈值

长期记忆管理的核心不是删除过时信息，而是在正确的上下文场景下使用正确的信息，非破坏性更新+依赖追踪比单纯的语义检索更能避免过时记忆误用。
