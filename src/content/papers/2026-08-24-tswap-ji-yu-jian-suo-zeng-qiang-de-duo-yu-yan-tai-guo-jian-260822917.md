---
title: 'TSWAP: A Multilingual Retrieval-Augmented Thai Wellness Advisor'
title_zh: TSWAP：基于检索增强的多语言泰国健康养生咨询系统
authors:
- Pornthep Ukosaramig
- Kobkrit Viriyayudhakorn
affiliations:
- Digital Touch Point Co., Ltd.
- iApp Technology Co., Ltd.
arxiv_id: '2608.22917'
url: https://arxiv.org/abs/2608.22917
pdf_url: https://arxiv.org/pdf/2608.22917
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: Agent · 多语言RAG垂直领域落地
tags:
- RAG
- Multilingual
- Vertical Agent
- LLM Deployment
- Low-resource NLP
one_liner: 基于无微调开源LLM与混合RAG构建落地级多语言泰式健康咨询Agent，开源首个泰医检索基准
practical_value: '- 垂直领域RAG落地可复用「首句query分类强制检索」策略，针对短名词实体查询强制调用rag_search，避免auto tool
  choice模式下模型跳检索用参数记忆产生幻觉，可靠性更高

  - 非英语小语种RAG部署避坑：英语校准的4-bit AWQ量化会破坏泰语声调/元音标记，小语种场景优先用官方FP8量化checkpoint，可加简单规则后处理校验字符完整性

  - 多语言垂直Agent无需开发单语言微调/模板，采用「翻译后检索+多语言基座」即可零样本支持多语言，依赖bge-m3这类跨语言嵌入的冗余能力可大幅降低开发成本

  - 合规类场景安全层可轻量化实现：用「路由规则+系统prompt」即可覆盖大部分边界case，不需要额外训练安全分类器'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
泰国健康养生产业2023年规模达405亿美元，养生旅游支出123亿美元，但泰式传统医药、认证服务商信息高度分散，外国游客同时面临语言壁垒与服务商资质信任问题；现有泰语LLM无针对泰医领域的落地级多语言咨询方案，也无公开检索基准。

### 方法关键点
- 知识库：整合泰国卫生部官方泰医、认证服务商等8类共30.6K chunk结构化数据存入Milvus向量库，每篇草药条目带禁忌症、权威文献引用字段
- RAG pipeline：采用未微调的Qwen3.6-35B-A3B MoE模型，混合bge-m3稠密检索+BM25稀疏检索，RRF融合后经Qwen3-Reranker-8B重排取top3上下文
- 路由机制：首句query分类为5类，实体查询强制调用检索工具，避免auto模式下短查询跳检索产生幻觉
- 多语言：8语言零样本支持，采用先翻译为泰语再检索策略，模型自动以用户输入语言回复
- 安全层：系统prompt限定健康养生领域、不提供诊疗建议、紧急情况直接路由对应热线，无额外训练的安全分类器

### 关键结果
- 开源首个泰医健康检索基准含50条标注query，Recall@5达0.88
- 120人UAT测试整体满意度87.2%，泰医知识准确率90.2%，服务商信息信任度91.0%
- 259例生产QA重测通过率91.1%；无检索时模型生成的服务商推荐100%不可验证，无安全prompt时出现3/22安全违规（给出用药剂量、响应非合规请求）

### 核心结论
垂直领域低资源语言Agent落地，优先投资RAG grounding与规则路由，不需要额外微调基座LLM即可达到生产可用标准
