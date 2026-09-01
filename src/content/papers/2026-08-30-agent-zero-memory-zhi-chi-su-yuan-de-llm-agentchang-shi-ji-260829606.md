---
title: 'Agent Zero Memory: Provenance-Aware Long-Term Memory for LLM Agents'
title_zh: Agent Zero Memory：支持溯源的LLM Agent长时记忆系统
authors:
- Ming Wu
- Pengyuan Zhu
affiliations:
- Zero Labs
arxiv_id: '2608.29606'
url: https://arxiv.org/abs/2608.29606
pdf_url: https://arxiv.org/pdf/2608.29606
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: Agent 长时记忆系统优化
tags:
- AgentMemory
- LongTermMemory
- Provenance
- HybridRetrieval
- RAG
one_liner: 设计三套溯源感知的并行记忆系统，在长时记忆基准达SOTA，兼顾精度成本灵活性
practical_value: '- 电商客服Agent/用户长期偏好记忆可直接复用三层并行架构：事件时间线存用户交互时序（退换货/咨询历史）、实体关系图关联订单/商品/地址实体、分层文档库存固定用户偏好，解决单一向量库时序/多跳检索不准的问题

  - 检索链路可复用intent gate设计：前置轻量分类判断当前query是否需要调用记忆、需要调用哪类记忆，自包含query直接跳过检索，降低30%+无意义检索开销

  - 对可信度要求高的业务场景（订单咨询/权益查询）可复用citation lock机制：所有生成内容必须绑定已召回的溯源证据，无证据直接拒答，从结构上消除幻觉

  - 电商sku/订单号等需要精确匹配的场景可复用embedding+lexical混合检索+RRF融合方案，比单一检索渠道提升1.2~1.8个百分点的召回准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent长时记忆系统普遍采用单一存储结构（向量库/知识图谱/事实库），存在三大共性痛点：写入侧LLM事实提取成本随历史长度线性增长、读取侧无差别检索开销大、更新时覆盖旧数据无法溯源时序变更，无法同时满足时序推理、多跳关联、事实可信三类长时召回需求。

### 方法关键点
- 三层并行记忆架构：1）事件时间线存储所有交互的时序信息，支持知识变更溯源；2）实体-事件知识图谱关联跨会话的人/项目/事件，支持多跳检索；3）分层文档记忆库（HDM）存储固定可信事实，分三级摘要降低读取成本
- 检索链路：前置intent gate判断是否需要记忆，不需要直接透传无延迟；再通过source router选对应存储桶，最后三套记忆的Agent检索并行执行，每个检索都用embedding+lexical混合检索+Agent可控过滤器，结果融合后输出
- 溯源约束：所有记忆条目自带来源、时间戳、证据指针，所有生成内容必须绑定已打开的证据（citation lock），无证据直接拒答，从结构上消除幻觉

### 关键实验
在LongMemEval、LoCoMo两个公开长时记忆基准上测试，对比Mem0、Zep、Mastra等主流记忆系统，分别达到95.60%、93.60%的准确率，比之前最优系统提升0.73、1.10个百分点；8种不同量级LLM backbone测试下，准确率波动仅3.4个百分点，成本波动达30倍，最小成本仅为最优配置的1/20。

长时记忆系统的质量核心由检索和存储结构决定，而非大模型本身的参数能力，对检索架构和溯源机制的投入可在所有backbone上获得通用收益。
