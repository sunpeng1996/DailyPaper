---
title: 'AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language
  Models'
title_zh: AutoScaffold：面向大语言模型强化学习的AI引导脚手架框架
authors:
- Zijian Zhang
- Rizhen Hu
- Jiangweizhi Peng
- Shiyang Li
- Sujay Bhatt
- Sihan Zeng
- Mingyi Hong
affiliations:
- University of Minnesota, Twin Cities
- JPMorgan AI Research
arxiv_id: '2611.14515'
url: https://arxiv.org/abs/2611.14515
pdf_url: https://arxiv.org/pdf/2611.14515
published: '2026-11-10'
collected: '2026-11-11'
category: Training
direction: LLM强化训练 · 自动自适应脚手架
tags:
- Reinforcement Learning
- LLM Training
- Scaffolding
- Teacher-Student
- RL Optimization
one_liner: 用冻结Teacher LLM自动生成自适应训练脚手架，提升RL训练LLM的无辅助任务性能
practical_value: '- 电商推荐场景做LLM4Rec的RL微调（如生成个性化推荐理由、营销文案）时，可直接复用该师生架构：用强Teacher LLM自动挖掘学生模型的Bad
  Case规律，生成针对性训练脚手架，无需人工跨场景写提示规则，降低微调成本

  - 训练时注入脚手架、推理时完全移除的设计，可迁移到所有对线上延迟有要求的推荐/搜索/Agent场景，既降低RL训练的冷启动难度，又不会增加推理阶段的计算开销

  - 类级脚手架按动态概率注入（而非全量注入）的技巧可直接复用，既避免学生模型对脚手架产生依赖，还可通过对比有/无脚手架的效果自动调整注入比例，适配训练不同阶段的模型能力'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有基于可验证奖励的LLM强化学习（RLVR）仅通过单值 reward 学习，大量轨迹中蕴含的失败原因、低效策略等信息被浪费；传统人工设计的训练脚手架存在定制成本高、无法自适应学生模型能力变化、跨域适配性差的问题，难以充分挖掘RL训练的性能潜力。
### 方法关键点
- 采用冻结Teacher LLM + 学生RL训练的双层架构，Teacher每K步读取学生训练轨迹，自动诊断能力瓶颈，生成两类脚手架：① 类级通用策略，共享给同类型所有任务；② 实例级提示，针对单个难例生成定制化hint
- 脚手架仅在训练阶段按动态概率注入训练Prompt，推理阶段完全移除，不影响线上性能；设置最大注入概率上限，避免学生模型依赖脚手架
- 新增类级脚手架验证环节：新策略先在留存任务上验证效果再部署，随着学生能力提升自动降低脚手架注入比例，逐步撤去支持
### 关键实验
在ALFWorld、搜索QA、数学推理、GPU核生成4个跨域任务测试，对比原生RL基线：ALFWorld成功率+7.2pt，搜索QA精确匹配+4.0pt，数学推理精度最高+2.0pt，GPU核生成通过率+3.0pt；数学域仅用1/3训练步数就超过人工设计脚手架的QuestA方法，效果优于所有依赖人工定制的脚手架方案。
### 核心结论
合适的训练阶段临时脚手架，能让学生模型在无辅助的推理阶段获得比直接RL训练更好的独立能力，且无需人工跨域定制规则
