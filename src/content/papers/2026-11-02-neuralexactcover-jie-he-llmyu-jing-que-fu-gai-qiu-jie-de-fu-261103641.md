---
title: 'From Natural Language to Exact Cover: A Neuro-Symbolic Approach to Zebra Puzzles'
title_zh: NeuralExactCover：结合LLM与精确覆盖求解的神经符号逻辑推理框架
authors:
- Paulius Skaisgiris
- Thomas Pammer
- Veronika Semmelrock
- Mykyta Ielanskyi
- Maximilian Heisinger
- Erich Kobler
affiliations:
- TU Wien
- Johannes Kepler University Linz
- University of Klagenfurt
arxiv_id: '2611.03641'
url: https://arxiv.org/abs/2611.03641
pdf_url: https://arxiv.org/pdf/2611.03641
published: '2026-11-02'
collected: '2026-11-03'
category: Reasoning
direction: 神经符号推理 · LLM与符号求解器融合
tags:
- Neuro-Symbolic
- Logical Reasoning
- Tool Calling
- Constraint Satisfaction
- Exact Cover
one_liner: 结合LLM语义解析与精确覆盖求解器，构建带反馈迭代的高可靠神经符号逻辑推理框架
practical_value: '- 可复用「LLM工具调用转结构化约束+符号求解器反馈迭代」架构：适用于电商活动资源分配、优惠券发放等约束满足场景，将自然语言运营规则转成约束编码，用符号求解器保证结果合规，避免LLM幻觉。

  - 实体属性归一化trick：用字符串相似度匹配对齐LLM输出的实体和标准属性库，解决LLM拼写、表述不一致问题，可直接用于推荐/广告系统的query理解、实体链指模块。

  - 复杂约束任务拆解范式：将推理任务拆分为「语义理解转编码」和「符号求解」两部分，降低LLM直接推理的复杂度，可迁移到Agent的规划、调度类任务，提升可靠性。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
纯LLM在逻辑推理任务中存在幻觉、正确性无保障的问题，传统符号求解器（如SAT、CSP求解器）虽然能保证结果准确完备，但要求输入为高度专业化的形式化编码，无法直接处理自然语言需求，二者的能力断层限制了LLM在约束满足类决策场景的落地。

### 方法关键点
- 提出NeuralExactCover双模块框架：语言模块基于LLM工具调用能力，将自然语言描述的约束问题转成精确覆盖问题的结构化编码；符号推理模块基于MiniExact精确覆盖求解器，直接求解编码得到确定解。
- 设计迭代反馈机制：求解器返回过约束、欠约束、唯一解三种状态，指导LLM修正工具调用，直到得到合法唯一解或达到重试阈值。
- 发布ZebraExtreme数据集：在原有ZebraLogic基础上扩展超大规模谜题，最高支持8×10实体属性规模，覆盖1e18~1e50解空间的高难度任务。

### 关键结果
- 在ZebraLogic数据集上，基于Devstral-Small-2-24B的方法达到97.9%的谜题准确率，超过此前SOTA o3-mini的91.7%；基于gpt-oss-20B的方法在ZebraExtreme数据集上达到84.75%的谜题准确率，远超基线最高的40.5%。
- 求解速度比同类神经符号方法Logic.py快2倍，带反馈迭代的版本比单轮版本准确率平均提升3~5pct。

对可形式化的约束满足类任务，LLM作为语义翻译层+符号求解器作为推理引擎的混合架构，比纯LLM推理同时兼顾准确率、效率与可解释性。
