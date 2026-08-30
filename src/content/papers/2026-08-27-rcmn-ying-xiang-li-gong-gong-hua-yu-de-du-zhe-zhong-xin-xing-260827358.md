---
title: 'RCMN: Understanding Misleadingness in Influential Public Discourse'
title_zh: 《RCMN：影响力公共话语的读者中心型误导性理解框架》
authors:
- Peiling Yi
affiliations:
- Kingston University London, United Kingdom
- Faculty of Engineering, Computing and the Environment, Kingston University
- School of Computer Science and Mathematics, Kingston University
arxiv_id: '2608.27358'
url: https://arxiv.org/abs/2608.27358
pdf_url: https://arxiv.org/pdf/2608.27358
published: '2026-08-27'
collected: '2026-08-30'
category: Other
direction: 公共话语误导性检测 · 多维度评估框架
tags:
- Misinformation Detection
- Frame Analysis
- Dataset Construction
- Lightweight Representation
- LLM Evaluation
one_liner: 提出读者中心的公共话语误导性五维评估框架，配套证据锚定数据集并验证轻量表征的分析潜力
practical_value: '- 电商虚假种草、误导性营销内容识别可复用五维评估框架，从内容呈现、用户认知偏差、证据匹配度、情绪唤醒、传播意图维度建模违规内容

  - 大规模内容治理场景可先采用轻量claim+上下文表征做初步违规筛查，高风险内容再补充多维度证据做细粒度误导机制判定，平衡效率与准确率

  - 大模型生成电商营销文案的合规校验可参考该框架设计评估维度，对齐用户真实认知、匹配事实依据，减少误导性内容输出'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有公共话语误导性研究多聚焦内容造假本身，极少关注误导性的生成机制以及对读者认知的实际影响，缺乏可落地的系统性评估框架。
### 方法关键点
提出RCMN框架，从误导机制、读者预期解读、证据支持的合理解读、情绪唤醒度、传播意图5个维度量化误导性；基于框架构建证据锚定的影响力公共话语数据集；测试仅用轻量级claim+上下文表征、不依赖丰富多模态/证据信息时大模型的误导性识别能力。
### 关键结果
- 误导性类型远不止内容捏造，无依据推断、夸大、信息遗漏是最普遍的误导机制，普遍伴随高情绪唤醒与扭曲性传播意图
- 5款主流生成式大模型仅用轻量表征即可较好还原读者层面的认知偏差，但误导产生机制的识别难度显著更高
- 轻量表征可支撑规模化误导性筛查，细粒度机制识别仍需丰富上下文与证据锚定
