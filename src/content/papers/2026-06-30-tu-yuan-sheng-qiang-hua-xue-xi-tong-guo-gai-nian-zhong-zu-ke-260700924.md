---
title: Graph-Native Reinforcement Learning Enables Traceable Scientific Hypothesis
  Generation through Conceptual Recombination
title_zh: 图原生强化学习通过概念重组实现可追溯科学假设生成
authors:
- Subhadeep Pal
- Shashwat Sourav
- Tirthankar Ghosal
- Markus J. Buehler
affiliations:
- Massachusetts Institute of Technology
- Washington University in St. Louis
- Oak Ridge National Laboratory
- Lawrence Berkeley National Laboratory
arxiv_id: '2607.00924'
url: https://arxiv.org/abs/2607.00924
pdf_url: https://arxiv.org/pdf/2607.00924
published: '2026-06-30'
collected: '2026-07-05'
category: Reasoning
direction: 可追溯推理 · 图原生强化学习
tags:
- Reinforcement Learning
- Graph Reasoning
- GRPO
- Traceable Generation
- Concept Recombination
one_liner: 提出经GRPO微调的图原生推理模型Graph-PRefLexOR，大幅提升开放域生成的推理可追溯性与效果
practical_value: '- 可借鉴GRPO微调+显式推理阶段拆分的思路，优化电商Agent多步决策链路的可解释性，方便快速排查选品、广告投放等场景的bad
  case

  - 图原生结构打通神经生成与符号关系的设计，可复用在推荐系统用户-物品交互建模中，提升召回、排序结果的因果可解释性

  - 有限语义空间内做概念重组的生成逻辑，可迁移到电商商品文案、营销话术生成场景，在控制内容合规性的同时提升多样性'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM处理开放域生成任务时输出流畅但推理路径不可追溯，无法验证结果的因果合理性，难以满足对推理严谨性要求高的领域需求。
### 方法关键点
提出Graph-PRefLexOR图原生推理模型族，采用GRPO微调，将推理拆分为机制探索、图构建、模式提取、假设合成4个显式阶段，打通神经语言生成与符号关系结构的链路，支持因果关系的构建、校验与复用。
### 关键结果
在100个材料科学开放问题上，较基线模型效果提升40~65%，其中推理可追溯性增益最高；语义多样性达基线的2~3倍，结构化推理与最终输出的一致性显著更强；测试阶段增加算力投入时，资源优先用于有限语义空间内的长距离概念重组，而非无意义的语义覆盖扩张。
