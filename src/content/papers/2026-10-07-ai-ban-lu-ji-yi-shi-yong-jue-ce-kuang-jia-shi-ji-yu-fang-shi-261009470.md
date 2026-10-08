---
title: 'Before Bringing It Up: When and How AI Companions Should Use Memor'
title_zh: AI 伴侣记忆使用决策框架：时机与方式的设计与评估
authors:
- Zihan Guo
- Roxy He
- Junwei Quan
affiliations:
- University of Toronto
arxiv_id: '2610.09470'
url: https://arxiv.org/abs/2610.09470
pdf_url: https://arxiv.org/pdf/2610.09470
published: '2026-10-07'
collected: '2026-10-08'
category: Agent
direction: AI 伴侣 · 记忆使用决策优化
tags:
- AI_Companion
- Memory_Management
- LLM_Agent
- Prompt_Engineering
- LLM_Evaluation
one_liner: 基于用户访谈提出Reconsider记忆校验流程，优化AI伴侣记忆使用的场景适配性
practical_value: '- 电商AI导购、个性化客服Agent可复用Reconsider的5步校验逻辑，避免在用户开心场景提过往负面消费记录、过时偏好，降低用户反感

  - 个性化推荐系统记忆模块可参考4种处理模式，区分记忆的隐式应用（过滤用户明确拒绝的品类）、显式提及（「您上次要的XX到货了」）、询问权限、直接忽略，避免过度个性化

  - LLM评估对比时要注意同家族偏好偏差，跨模型评估尽量采用盲测、多评委、组内对比的方式，降低评估偏差'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前AI伴侣记忆系统仅关注记忆准确性和召回率，忽略场景适配性：准确记忆可能在错误时机、错误场景提及引发用户反感；同时用户对记忆的权限控制需求是分层的，现有系统未区分存储权限、使用权限、显式提及权限的差异，易出现过度回忆或该用记忆不用的问题。

### 方法关键点
- 基于14位AI伴侣用户的两轮访谈，提炼出8个记忆使用设计原则，覆盖场景适配、边界尊重、权限分层、时效性校验、有限推理等维度
- 提出Reconsider单轮模型无关prompt流程，对每条候选记忆执行5步有序非补偿校验：有效性校验→边界与权限校验→边际价值校验→当前场景合理性校验→适用范围校验
- 校验通过的记忆对应4种处理模式：直接忽略、隐式影响回复、显式提及、先询问用户再使用，目标是筛选满足交互需求的最小必要记忆集

### 关键实验
- 基于访谈真实场景构造80个测试用例，覆盖5种主流LLM（GPT、Claude、Gemini、Grok、DeepSeek），生成400组同模型盲测对比对，采用2个LLM评委做盲评
- 整体净胜率：评委1为+15pp，评委2为+23pp；其中DeepSeek、Gemini的效果显著提升，95%置信区间不含0，GPT、Claude的效果受评委偏好影响无明确结论
- Reconsider生成的回复平均比基线短21%

### 核心结论
记住准确的事实不代表它适合出现在当前交互中，记忆系统需要同时评估「必要的连续性」和「适当的克制」
