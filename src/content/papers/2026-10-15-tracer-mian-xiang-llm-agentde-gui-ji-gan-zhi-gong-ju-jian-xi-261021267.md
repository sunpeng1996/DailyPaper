---
title: 'TRACER: Trajectory-Aware Tool Retrieval for LLM Agents'
title_zh: TRACER：面向LLM Agent的轨迹感知工具检索系统
authors:
- Tanish Kher
- Sarvesh DK
- Abedelkadir Asi
- Sparsha Chennarayapatna Sundaresh
- Dezhi Hong
affiliations:
- Microsoft
- University of California, Berkeley
arxiv_id: '2610.21267'
url: https://arxiv.org/abs/2610.21267
pdf_url: https://arxiv.org/pdf/2610.21267
published: '2026-10-15'
collected: '2026-10-16'
category: Agent
direction: Agent 工具检索性能优化
tags:
- LLM-Agent
- Tool-Retrieval
- Trie-Index
- Empirical-Prior
- Contextual-Prior
one_liner: 基于历史工具调用序列构建trie索引，融合双先验实现低token成本的高准确率Agent工具检索
practical_value: '- 电商客服、运营类Agent的工具调用场景可直接复用TRACER的trie索引架构，基于历史成功调用轨迹做前缀匹配，仅给LLM返回top-k工具，最高可降80%单步推理token成本

  - 工具排序环节可复用双先验融合方案：将历史同前缀下工具转移频率作为经验先验，当前会话与同转移历史场景的语义相似度作为上下文先验，用可学习权重混合，比纯向量检索准确率提升30pct以上

  - 针对跨场景通用高频工具（如查用户、查订单等无固定前缀工具），可复用TRACER+G思路，固定将3个全局最高频工具加入候选集，避免召回遗漏

  - 冷启动阶段无足够历史轨迹时，直接采用论文的vector search fallback方案，无需额外开发冷启动逻辑，待轨迹积累后自动切换为trie检索'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM Agent执行多步工具调用时，全量加载大工具注册表会导致token成本陡增，还会因上下文信息过载降低工具选择准确率；现有基于工具描述的向量检索方案忽略了工具调用的序列依赖性，易混淆语义相似的工具，无法适配百级以上工具库的落地场景。
### 方法关键点
- 构建工具调用序列trie索引：将历史成功轨迹的所有前缀作为trie节点，每个边存储两类信息：该转移的历史出现频率（经验先验）、该转移对应所有会话的平均语义嵌入（上下文先验）
- 双先验加权排序：每步根据当前状态特征，用可学习权重混合经验先验、当前会话与边嵌入的余弦相似度得到的上下文先验，排序后取top-k工具返回给LLM
- 异常兜底与扩展：遇到未见过的前缀或得分分布过于平坦时，自动降级为全局工具描述向量检索；支持新增全局高频工具集G扩展候选集，覆盖无固定前缀的通用工具
### 关键结果
实验覆盖零售、电信、银行等6个环境，工具库规模最大128个，对比全量工具加载、纯向量检索等baseline，测试4款主流LLM：
- 零售+电信混合环境下，相比GPT-5.4全量加载工具，工具选择准确率高4.7pct，单步token减少80%；端到端任务成功率与全量加载持平，单步token减少61%
- 24个模型-环境组合中，21个准确率超过全量加载基线，平均提升6-10pct

**最值得记住的一句话：Agent工具检索本质是序列预测问题，而非独立的语义匹配问题，利用历史调用序列的结构化信息可同时实现降本提效**
