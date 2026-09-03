---
title: 'PragAlign: Feedback-Guided Pragmatic Alignment for Controlled Synthetic Dialogue
  Generation'
title_zh: PragAlign：反馈引导的可控合成对话语用对齐框架
authors:
- Smitha Muthya Sudheendra
- Jaideep Srivastava
affiliations:
- University of Minnesota, Twin Cities
arxiv_id: '2609.02480'
url: https://arxiv.org/abs/2609.02480
pdf_url: https://arxiv.org/pdf/2609.02480
published: '2026-09-02'
collected: '2026-09-03'
category: Agent
direction: Agent 合成对话生成 · 闭环反馈优化
tags:
- Synthetic Dialogue
- LLM Agent
- Iterative Refinement
- Controllable Generation
- LLM-as-Judge
one_liner: 通过反馈引导的生成-评估-修订闭环，实现服务场景高约束满足度的可控合成对话生成
practical_value: '- 电商客服/导购对话Agent缺训练数据时，可复用该框架，按业务需求自定义意图、情绪、风格约束，生成标注对话数据，大幅降低人工标注成本

  - 做多约束LLM生成任务（如营销文案生成、客服话术生成）时，可借鉴维度拆分评估方案，分别对意图合规、情绪匹配、通顺度等设置阈值，避免单一综合分掩盖核心约束缺失问题

  - LLM生成的最后一公里优化无需盲目增加重试次数，结构化维度级反馈比单纯重复生成可多提升3~5pct的全约束满足率，收益集中在情绪匹配这类难对齐维度，可针对性分配迭代预算

  - 注意LLM-as-Judge评估结果和人类感知存在偏差，尤其是情绪类主观维度，上线前必须做人类标注校验，避免自动评估过拟合到显式标记而非上下文合理性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
服务场景下真实用户-客服对话涉及隐私、获取成本高，现有合成对话生成方法难以同时满足意图准确、情绪匹配、流程连贯等多约束，容易出现某一核心维度不达标但整体得分偏高的问题，亟需可量化约束满足度的可控生成框架。

### 方法关键点
- 输入为结构化目标表征：包含服务场景上下文、目标意图集合、目标情绪集合、大五人格风格控制向量、生成超参数
- 采用生成-评估-修订闭环：先用LLM生成初始对话，再用LLM-as-Judge从意图对齐、情绪对齐、连贯性、通顺度4个维度分别打0~1分，输出维度级反馈，不满足阈值则进入修订，最多支持3轮修订
- 验收规则同时要求综合分≥0.8，且各维度分不低于阈值（意图≥0.8、情绪≥0.7、连贯性≥0.8、通顺度≥0.8），避免单一分数掩盖核心约束缺失

### 关键实验
基于800条匹配的对话规格数据集（覆盖10个服务领域，含电商配送、订阅服务等），对比one-shot生成、无反馈重复生成等基线：
- PragAlign自动接受率达99.50%，显著高于one-shot的72.25%，也比无反馈重复生成的95.88%高3.62pct
- 优化收益集中在情绪对齐维度，210条进入修订的对话情绪对齐分平均提升0.34
- 1200条对话的人类评估显示，意图识别率99.7%、对话流程认可度97.7%，但情绪适配性认可度仅79.1%，存在自动评估与人类感知的明显偏差

### 核心结论
结构化反馈的核心价值不是提升生成内容的平均质量，而是解决最后一公里的多约束同时满足问题，尤其对情绪这类难对齐的维度优化效果最显著。
