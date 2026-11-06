---
title: 'Archetypal contexts in the neurons of language models: an architecture for
  intelligence?'
title_zh: 大语言模型神经元中的原型上下文：智能的底层架构探究
authors:
- David Nordfors
affiliations:
- archetypes.ai
arxiv_id: '2611.07234'
url: https://arxiv.org/abs/2611.07234
pdf_url: https://arxiv.org/pdf/2611.07234
published: '2026-11-04'
collected: '2026-11-06'
category: LLM
direction: LLM可解释性 · 神经元功能分层
tags:
- LLM Interpretability
- Neuron Activation
- Archetypal Context
- Self-organization
- Knowledge Representation
one_liner: 发现LLM预训练自发形成三层神经元结构，原型、主题、语言信息分离且跨域复用
practical_value: '- 领域LLM对齐时可复用通用原型层能力，仅微调主题层神经元适配电商/广告领域知识，降低微调成本的同时避免破坏通用推理能力

  - 跨语言推荐/多语种Agent研发时，可直接复用核心原型层逻辑，仅适配外层语言神经元，无需重新训练跨语言通用规则

  - 冷启动推荐场景可基于原型结构设计Prompt，触发LLM跨域模式匹配能力，提升新类目/新用户场景下的推荐准确性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM可解释性研究多聚焦具体领域概念的神经元表征，尚未揭示LLM跨域类比推理的底层机制，而类比能力是LLM智能性的核心来源，厘清其知识存储结构可有效指导模型训练、对齐与定向编辑。
### 方法关键点
- 覆盖Qwen3/3.5/3.8、OLMo-2、Phi-3/4等11个模型家族的30款0.6B~32B参数LLM，定位FFN层神经元的功能属性
- 采用神经心理学双分离实验范式：定向沉默特定功能神经元集，对比模型模式识别、主题认知能力的变化
- 跟踪预训练全流程的神经元功能分布，验证结构的自组织特性
### 关键结果
- 所有测试LLM均自发形成三层三明治结构：输入输出侧外层存储语言信息、中间层存储主题信息、核心层存储通用原型（如临界点、赢家通吃等跨域关系模式）
- 沉默某原型对应的4%左右神经元，模型失去该模式识别能力但保留主题认知，模式识别准确率下降超90%；沉默等量随机神经元无显著影响
- 原型层神经元无语言属性，跨中英日等多语言识别同一模式的一致率超95%；小模型与大模型的原型能力无显著差异，模型尺寸提升主要增加主题知识储量
### 核心结论
大语言模型的通用智能核心是预训练自发形成的跨域通用关系原型集，模型能力差异主要来自主题知识的储量而非原型能力
