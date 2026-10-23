---
title: 'Working Through Representation: Malleable Workspaces for Human-Agent Knowledge
  Work'
title_zh: 面向人-Agent知识协作的可塑工作空间：基于动态表征的交互模型
authors:
- Nan Chen
- Long Ling
- Luna K. Qiu
- Zilong Wang
- Yuqing Yang
affiliations:
- Microsoft Research Asia
- Tongji University
- CataX AI
arxiv_id: '2610.30893'
url: https://arxiv.org/abs/2610.30893
pdf_url: https://arxiv.org/pdf/2610.30893
published: '2026-10-22'
collected: '2026-10-23'
category: Agent
direction: 人-Agent协作 · 动态工作表征交互设计
tags:
- Human-Agent Collaboration
- Knowledge Work
- Work Representation
- Interactive System
- Longitudinal Study
one_liner: 提出可塑工作空间概念模型，通过动态工作表征中介人-Agent多轮知识协作过程
practical_value: '- 电商运营/内容创作场景可复用该框架：将多轮Agent对话中的商品卖点、用户评论、营销素材拆解为独立单元并构建语义关联，避免重复整理上下文，提升营销文案、商品详情页的制作效率。

  - 多Agent推荐系统可参考R1-R2-R3三层交互逻辑：用Work Representation存储用户意图、候选Item、召回规则的关联关系，Agent基于表征自动补全上下文，执行后自动更新表征并同步到外部RAG知识库、召回规则库等工作环境。

  - 人-Agent交互产品迭代可参考能力优先级：优先实现「Agent输出本地嵌入表征」能力，再逐步支持「表征自动重组」「外部环境变更」，降低用户跨会话的上下文搬运成本，平衡开发成本与用户收益。'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有基于对话的人-Agent交互存在四大结构错配：单元错配（无法自定义操作对话片段的粒度）、关系错配（不保留内容间的语义/证据关联）、状态错配（无法显式表达当前工作的进展状态）、进度错配（多轮会话内容分散，后续动作需手动重构上下文），难以支撑复杂多步知识工作的持续性协作。

### 方法关键点
- 提出可塑工作空间概念模型，核心由动态Work Representation、Work Environment、人类引导三个组件构成，定义三层交互逻辑：R1（表征grounding指导人/Agent动作）、R2（选择性解释外部信息更新表征）、R3（基于表征的动作反哺修改外部Work Environment）。
- 基于模型分析2022-2026年CHI/UIST/CSCW等顶会的58篇论文共61个实现案例，归纳当前人-Agent系统的表征设计、动作支撑能力的分布规律。
- 实现原型系统MalleableSpace，支持可视化画布编辑多模态单元与关联、Agent基于表征自动获取上下文、表征动态更新、对接外部自定义Agent。

### 关键实验结果
- 3个月纵向用户研究招募7名资深Agent用户，共创建43个工作空间，单空间最大单元数629，覆盖文献调研、软件开发、演示文稿制作等场景。
- 跨案例分析显示：现有系统90%+支持Agent输出本地嵌入表征，仅不到20%支持表征自动重组，仅15%支持基于表征修改外部Work Environment。

### 核心结论
人-Agent协作的核心不是优化对话效率，而是构建可动态迭代的共享工作表征，让人的判断和Agent的执行能力形成持续闭环。
