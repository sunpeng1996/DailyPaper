---
title: Rhetorical-Role-Aware Retrieval-Augmented Generation for Legal Question Answering
  over Indian Supreme Court Judgments
title_zh: 面向印度最高法院判决问答的修辞角色感知检索增强生成方法
authors:
- Sayed Ayaan Ahmed Sha
- Sangeetha Sivanesan
- Anand Kumar Madasamy
- Navya Binu
affiliations:
- National Institute of Technology, Tiruchirappalli
- National Institute of Karnataka, Surathkal
arxiv_id: '2608.06828'
url: https://arxiv.org/abs/2608.06828
pdf_url: https://arxiv.org/pdf/2608.06828
published: '2026-08-07'
collected: '2026-08-10'
category: RAG
direction: 垂直领域RAG · 结构化文档检索优化
tags:
- RAG
- Chunking
- Cross-Encoder Reranking
- Query Rewriting
- Domain-Specific LLM
one_liner: 提出融合修辞分块、融合检索、交叉编码器重排的法律领域专属RAG问答框架
practical_value: '- 处理结构化长文档时，可参考按领域修辞角色分块的思路，替代通用滑动窗口提升召回相关性，适配电商商品详情、商家资质等RAG场景

  - 多轮对话类RAG系统可复用「对话历史+query分类+query改写」的意图识别链路，降低多轮上下文理解偏差，适配电商客服、导购Agent场景

  - 检索链路可采用「混合检索+Cross Encoder重排」的融合方案，在可控成本下提升检索精准度，适配商品、内容、服务类召回排序需求'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
垂直领域长结构化文档的RAG问答面临文档结构复杂、专业术语密集、相关信息分散、多轮对话意图易偏差的问题，通用RAG方案召回准确率低、回答相关性差，无法满足高可靠性要求的领域场景需求。
### 方法关键点
1. 分块层采用领域专属的基于修辞角色的分块策略，同时保留法官姓名等强业务属性的文档结构特征，避免重要信息丢失；
2. 检索层采用融合式检索+Cross Encoder重排的链路，显著提升召回结果的相关度；
3. 多轮对话模块结合历史聊天记录，新增Query分类与改写能力，精准捕捉连续查询的用户意图。
### 关键结果
基于DeepEval框架评估，在contextual recall、answer relevancy等核心指标上表现优异，验证了领域定制化优化对高上下文依赖的垂直领域问答任务的显著增益。
