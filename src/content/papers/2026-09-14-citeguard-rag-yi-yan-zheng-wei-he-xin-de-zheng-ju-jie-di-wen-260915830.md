---
title: 'CiteGuard-RAG: A Validation-Centered AI System for Evidence-Grounded Question
  Answering'
title_zh: CiteGuard-RAG：以验证为核心的证据接地问答AI系统
authors:
- Sumit Barua
- Guan Hong
- Halil Dursunoglu
- Charles Rodgers
- Alvis Fong
affiliations:
- Western Michigan University
arxiv_id: '2609.15830'
url: https://arxiv.org/abs/2609.15830
pdf_url: https://arxiv.org/pdf/2609.15830
published: '2026-09-14'
collected: '2026-09-15'
category: RAG
direction: RAG 可信性优化与幻觉抑制
tags:
- RAG
- Hallucination Mitigation
- Citation Validation
- Grounded QA
- Hybrid Retrieval
one_liner: 提出以验证为核心的RAG框架，通过句子级接地校验与单次重生成实现高引证有效性与幻觉抑制
practical_value: '- 做电商合规客服、售后规则解答等高置信RAG场景时，可直接复用句子级校验逻辑：先校验每条生成内容的引证有效性、词重叠、语义相似度，不通过触发重生成或拒答，大幅降低幻觉

  - 检索层可复用BM25+语义召回的加权融合方案，电商场景下0.65/0.35的语义/ lexical权重可作为初始基准，平衡精确商品匹配与用户query语义泛化

  - 低容错业务不要盲目新增reranker模块，需先做全链路消融验证，避免有效召回片段被误过滤反而降低最终回答准确率

  - 高并发业务可采用单次重生成机制，既控制推理成本，又能修复大部分首次生成的接地错误，避免无限循环导致的时延飙升'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
RAG仅通过召回增强生成无法保证输出内容完全接地、引证合法有效，在法律、合规客服等高风险场景下，无依据回答、幻觉会带来严重业务风险；现有方案大多将接地校验作为事后评估指标，缺乏生成后细粒度校验与闭环控制机制，无法在内容输出前拦截不合格响应。
### 方法关键点
- 预处理采用页感知文本解析+段落优先分块策略，保留证据溯源信息，默认采用600token块长+120token重叠，过滤低信息片段
- 召回层采用BM25+语义召回的混合方案，分数归一化后按0.65:0.35加权融合，未引入额外reranker避免有效片段被误过滤
- 生成层采用强约束prompt，要求输出必须标注对应召回块的内联引证标记，无足够支撑证据时直接返回标准化拒答话术
- 校验层做句子级细粒度校验：先检查引证是否指向有效召回块，再分别计算与引证块的词重叠（阈值0.1）、语义相似度（阈值0.4），满足其一视为接地；校验不通过触发单次重生成，二次不通过直接拒答
### 关键实验
在150条受控住房法QA、200条PrivacyQA、50条CUAD数据集上测试，对比无校验、单模式召回等基线：受控场景下召回准确率99.1%，接地回答准确率98.3%，引证有效性98.3%，检测到的幻觉率为0%；关闭校验后接地准确率骤降至8.7%，幻觉率升至18.6%；跨域测试中引证有效性仍保持100%，无证据支撑的幻觉率为0%。

最值得记住的结论：高可信RAG的可靠性不取决于单一召回环节的质量，而是召回、生成约束、校验、拒答策略全链路的协同效果，仅提升召回准确率无法避免生成幻觉。
