---
title: 'Toward a Gricean Retreat: Probing LLMs for Knowledge Boundaries and Referent
  Specificity'
title_zh: 面向Gricean退避：探测大语言模型的知识边界与指代特异性
authors:
- Dananjay Srinivas
- Saksham Khatwani
- Maria Pacheco
affiliations:
- University of Colorado, Boulder
arxiv_id: '2608.13484'
url: https://arxiv.org/abs/2608.13484
pdf_url: https://arxiv.org/pdf/2608.13484
published: '2026-08-13'
collected: '2026-08-14'
category: LLM
direction: 大模型对齐 · 知识边界与幻觉控制
tags:
- Hallucination
- Knowledge Boundary
- Probing
- Gricean Alignment
- LLM Alignment
one_liner: 发现LLM激活已编码知识边界与指代特异性信号，但生成时未耦合两类信号导致幻觉
practical_value: '- 电商Agent生成商品/品牌介绍时，可复用中间层激活探针识别长尾冷门实体是否在知识边界内，避免编造不存在的参数/资质信息，降低合规风险

  - 可基于指代特异性探针做生成前置校准，对知识边界外的实体强制输出高层级通用表述，相比事后RAG校验/重生成延迟更低，适合实时推荐话术、搜索补全场景

  - 利用LLM天然偏好具体输出的bias，在搜索Query推荐、商品文案生成场景优先触发该偏好提升内容相关性，同时对未知Query fallback到通用suggestion降低错误率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM面对知识边界外的实体时，易生成看似合理的虚假信息而非输出更安全的通用表述，现有幻觉控制方案多为事后校验修正，成本高且是全有或全无的abstain策略，无法平衡信息密度与真实性。人类遵循Grice合作原则，对不确定的实体会自动执行「Gricean退避」，降低表述特异性以保障真实性，目前尚不清楚LLM是否具备该能力的内部基础。
### 方法关键点
- 基于T-REx数据集构建测试基准，覆盖人物、企业、产品、技能4个领域的8类Wikidata关系，构造真实实体/合成实体（模拟未知实体）对，生成3种不同长度的上下文prompt，同时为每个目标实体生成10个不同特异性层级的通用替代表述。
- 用线性探针分别探测两类信号：实体末尾token的激活（识别实体是否在知识边界内）、生成位置前最后一个token的激活（预测即将生成的指代特异性）。
- 采用LLM-as-judge标注生成结果的entailment真实性与特异性，对比不同模型规模、不同解码策略下的生成行为。
### 关键结果
- 知识边界探测AUROC随模型规模提升，2B以上模型可达>90%，最优信号出现在模型中间层附近。
- 指代特异性预测AUROC在模型深层可达>0.9，argmax解码的预测准确率显著高于多分类采样。
- 无论实体是否在知识边界内，模型90%以上的情况优先生成具体指代，即使存在正确的通用替代选项，未知实体场景下该偏好导致85%以上的生成属于不符合要求的幻觉。

> 最值得记住的结论：LLM本身已经具备执行Gricean退避所需的全部内部信号，仅缺耦合两类信号的生成策略，无需大规模重训即可通过轻量对齐实现幻觉的前置控制。
