---
title: Detecting Inconsistencies in Model Specifications with LLM-as-Verifier Reasoning
title_zh: 基于LLM验证器推理的大模型行为规范不一致性检测方法
authors:
- Zichen Xie
- Mrigank Pawagi
- Lize Shao
- Yang Hu
- Wenxi Wang
affiliations:
- University of Virginia
- University of Pennsylvania
- The University of Texas at Austin
arxiv_id: '2610.01847'
url: https://arxiv.org/abs/2610.01847
pdf_url: https://arxiv.org/pdf/2610.01847
published: '2026-10-01'
collected: '2026-10-02'
category: LLM
direction: 大模型对齐 · 行为规范审计
tags:
- LLM Alignment
- Specification Auditing
- LLM-as-Judge
- Inconsistency Detection
- Reasoning
one_liner: 提出VERISPEC框架直接审计大模型自然语言行为规范的内部冲突，精度更高成本更低
practical_value: '- 迭代Agent行为规则、电商内容审核规范时，可复用VERISPEC的「上下文感知规则抽取+主题聚类+LLM验证器」pipeline，提前检测规范内部冲突，避免线上Agent/审核模型行为矛盾

  - 搭建LLM-as-Judge服务（如电商合规审核、推荐内容判优）时，可借鉴其结构化举证要求（必须提供冲突场景、规则适用依据、上下文无法消解证明），可大幅降低误判率，本文实验中精度从1.4%提升至38.5%

  - 处理长文档规则类审计需求时，不要直接喂全文档prompt，先按主题+权威等级聚类为小分析单元，能降低LLM长上下文遗漏错误，同时降低调用成本，本文单条有效冲突检测成本比基线低30%以上'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
大模型行为规范（如OpenAI Model Spec、Claude宪法）是对齐训练、推理约束、效果评估的核心依据，但规范迭代过程中容易出现多条独立合理的规则在特定场景下互斥的问题。现有方法要么将自然语言规范转成形式化语言丢失语义细节，要么通过模型行为测试间接推导，无法区分是模型能力缺陷还是规范本身存在问题，亟需能直接审计自然语言规范内部一致性的低成本方案。

### 方法关键点
- 上下文感知规则抽取：将无结构规范文本拆分为带权威等级、前置条件、后置要求、关联上下文的结构化规则，补全原有未标注的规则，共覆盖405条有效规则
- 图结构规则聚类：构建带语义边（同主题规则）和句法边（同章节/交叉引用规则）的规则图，按相同权威等级聚类为5~26条规则的分析单元，避免全量两两校验的算力浪费
- LLM-as-Verifier校验：要求LLM输出冲突必须同时提供3个证据：触发冲突的具体场景、两条规则均适用的依据、现有上下文无法消解冲突的证明，大幅减少误报

### 关键实验
在OpenAI公开的Model Spec上测试，对比5种基线方法，VERISPEC实现38.5%的最高精度，单条验证有效的冲突成本最低为11.12美元，共检测到5个真实不一致，均已被OpenAI官方接收进入内部讨论。

### 最值得记住的一句话
大模型对齐的前提是对齐依据本身无缺陷，对规范的前置审计是比事后模型行为评估成本更低、效率更高的对齐保障手段。
