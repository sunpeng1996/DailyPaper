---
title: 'Let Me Clarify: Interactive Modeling of Soft Attributes'
title_zh: 《让我澄清：软属性的交互式建模》
authors:
- Steffen Holter
- Rita Sevastjanova
- Michaela Benk
- Mennatallah El-Assady
affiliations:
- ETH Zurich, Switzerland
- University of Zurich, Switzerland
arxiv_id: '2610.20227'
url: https://arxiv.org/abs/2610.20227
pdf_url: https://arxiv.org/pdf/2610.20227
published: '2026-10-14'
collected: '2026-10-17'
category: RecSys
direction: 交互式偏好建模 · 软属性量化
tags:
- Soft Attribute
- Preference Elicitation
- Interactive System
- User Modeling
- Interpretability
one_liner: 提出软属性软度量化方法，构建AttriFy交互系统将用户模糊偏好转化为可执行属性函数
practical_value: '- 电商推荐中用户模糊偏好（如“好看”“性价比高”）可复用软属性量化方法，判断是否需要发起多轮澄清交互明确真实需求，减少语义歧义

  - 可借鉴AttriFy“软度评估→澄清交互→生成可执行规则”工作流，搭建用户可干预的偏好建模链路，提升推荐可解释性与用户满意度

  - Agent导购场景可复用软属性度量作为交互触发阈值，仅当用户输入歧义度高于阈值时发起追问，避免过度打扰用户'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
用户表达偏好时常用“有趣”“原创”等语义模糊的软属性，现有基于隐式表征的偏好建模方法无法透明展示属性的解释逻辑，限制用户可控性与模型可解释性，难以落地到实际业务的偏好提取场景。
### 方法关键点
1. 形式化定义软属性的“软度”为单条描述允许的有效解释多样性，设计可落地的量化指标评估软度；
2. 搭建AttriFy混合主动系统，基于软度阈值引导澄清交互，将用户的模糊描述转化为可在文本语料上执行的Python函数；
3. 配套交互仪表盘支持用户对生成的属性函数进行查看、接受、拒绝、精细化调整操作，保证属性匹配用户真实意图。
### 关键结果
32名被试的组内探索性实验表明，软度引导的澄清方案相较普通LLM baseline，在可解释属性构建的用户满意度、属性语义匹配度上均有显著提升。
