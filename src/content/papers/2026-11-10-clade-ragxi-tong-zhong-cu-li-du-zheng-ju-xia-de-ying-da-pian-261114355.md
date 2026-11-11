---
title: 'CLADE: Category-Level Answering from Deficient Evidence in Retrieval-Augmented
  Language Models'
title_zh: CLADE：RAG系统中粗粒度证据下的应答偏差与修复方法
authors:
- S M Rayeed
- Charles V. Stewart
- Yao Ma
affiliations:
- Rensselaer Polytechnic Institute
arxiv_id: '2611.14355'
url: https://arxiv.org/abs/2611.14355
pdf_url: https://arxiv.org/pdf/2611.14355
published: '2026-11-10'
collected: '2026-11-11'
category: RAG
direction: RAG系统优化 · 证据粒度与拒答机制
tags:
- RAG
- Abstention
- Ontology
- Evidence Granularity
- LLM
one_liner: 揭示RAG系统粗粒度证据触发的盲目猜测现象，验证领域本体的修复效果
practical_value: '- 电商商品问答/客服RAG场景新增证据粒度校验：若检索内容仅提及商品上层类目（如用户问某款笔记本适用场景，检索结果只提轻薄本通用属性），不要直接应答，触发商品类目树匹配，避免模型无依据猜测

  - RAG拒答模块优化：放弃仅二分类（上下文足够/不足）的设计，新增「可解决不足」分类，绑定领域类目/标签体系做补全，效果远优于仅通过prompt要求模型拒答

  - 复用现有业务类目体系：电商现成的商品类目树、品类属性体系可直接替代论文中的本体，候选排序优先采用销量/点击量的popularity prior，准确率高于LLM直接选择'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有RAG系统的上下文充分性判断仅做二分类，忽略了「检索内容准确但粒度粗于问题要求」的中间场景：这类内容可排除大量错误答案，但无法直接给出细粒度结果，属于可解决的信息不足。现有框架会直接触发模型猜测或拒答，严重降低回答准确率，缺乏针对性的处理机制。
### 方法关键点
- 将检索段落按证据粒度分为三类：`named`（明确提及目标细粒度实体）、`family-only`（仅提及实体的2级以内上层类目）、`silent`（无相关信息）
- 设计反事实对比实验：通过替换细粒度实体为上层类目、删除相关句子，隔离验证类目提及对模型拒答行为的影响
- 提出基于领域本体的修复链路：从段落中提取匹配的上层类目，通过本体扩展为候选实体集，再在候选集中做答案选择
### 关键结果
在生物医学PrimeKG（1800个药物-疾病事实）、生态GloBI（23694个物种交互事实）数据集上测试Qwen2.5、OLMo2、Granite等7-14B模型：
- `family-only`段落相比无信息段落，模型拒答率下降13.8个百分点，回答准确率从84-95%降至45-59%
- 常规优化手段（置信度过滤、增大模型规模、新增拒答指令）均无法解决该偏差
- 给定正确上层类目时，本体扩展候选集包含正确答案的比例达98.5%，端到端修复后准确率从10%提升至26.8%，基于实体流行度的排序效果优于LLM直接选择
### 核心结论
RAG系统的上下文不足不能仅做二分类，粗粒度可解决的不足应触发符号知识库匹配流程，而非依赖LLM自行猜测或拒答
