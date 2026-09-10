---
title: Guaranteeing Faithful Evidence Extraction in Speculative Retrieval-Augmented
  Generation
title_zh: 投机式检索增强生成（RAG）的忠实证据抽取保障方法
authors:
- Quentin Signé
- Mohand Boughanem
- Jose Moreno
- Thiziri Belkacem
affiliations:
- Université de Toulouse - IRIT UMR 5505
- Airbus Protect
arxiv_id: '2609.10046'
url: https://arxiv.org/abs/2609.10046
pdf_url: https://arxiv.org/pdf/2609.10046
published: '2026-09-09'
collected: '2026-09-10'
category: RAG
direction: 检索增强生成 · 证据保真约束解码
tags:
- RAG
- Constrained Decoding
- Faithfulness
- Speculative Decoding
- Question Answering
one_liner: 提出CHyD约束混合解码框架，为投机式RAG提供引用片段完全匹配原文的强保真保证
practical_value: '- 电商合规问答、商品参数咨询场景可直接复用CHyD的触发+约束解码逻辑，保证引用的规格、售后规则100%匹配官方文档，避免虚假宣传风险

  - 可借鉴EFA（Extraction Faithfulness Accuracy）指标，替代传统语义相似度指标，用于评估RAG系统引用内容的真实可信度

  - 强合规类推荐理由生成场景（如3C、医疗器材推荐）可复用双模式切换机制，自由生成话术+约束抽取官方参数，平衡流畅度与合规性

  - 工程上可复用上下文后缀树实现，高效计算约束解码模式下的合法token集合，避免全量扫描上下文，降低约束解码 overhead'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有投机式RAG优先优化推理效率，半抽取式QA仅通过软约束提升事实性，均无法保证输出中引用的片段完全与检索上下文 verbatim 匹配，在航空维修、医疗、电商合规等强监管场景下，内容偏差可能引发严重合规或安全风险，亟需可验证的抽取保真机制。
### 方法关键点
- 提出CHyD（Constrained Hybrid Decoding）框架，设置双解码模式：Standard模式支持自由生成文本，EEC（Extraction of Evidence from Context）模式强制输出检索上下文中的连续原文片段
- 用「[」作为EEC模式触发token，「]」作为退出触发token，模式切换逻辑完全模型无关，无需修改基座LLM结构
- EEC模式下通过上下文后缀树快速匹配合法后续token，对非法token的logits赋值为-∞，仅允许输出连续原文片段或退出符
### 关键实验
在医疗、航空、开放域共4个QA数据集上对比SEMQA、NEST等SOTA基线：CHyD的EFA稳定达到0.981~1.000，而基线SEMQA在技术领域EFA最低跌至0.371；MedMCQA数据集上EM值较SEMQA最高提升10.6pp，整体流畅度指标（ROUGE-L、BERTScore）与基线差距<2%，仅长上下文场景 latency 提升3~4倍，为合规场景可接受trade-off。
### 核心结论
强合规场景下，RAG的证据正确性优先级远高于生成流畅度与推理速度，解码层硬约束可在几乎不损失用户体验的前提下实现近100%的引用保真。
