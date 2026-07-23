---
title: 'Disentangling Curriculum Learning in NLP: Towards a Unifying Taxonomy'
title_zh: 拆解NLP领域课程学习：迈向统一分类体系
authors:
- Vanessa Toborek
- Florian Seiffarth
- Sebastian Müller
- Tamás Horváth
affiliations:
- University of Bonn
- Lamarr Institute
- Fraunhofer IAIS
arxiv_id: '2607.18984'
url: https://arxiv.org/abs/2607.18984
pdf_url: https://arxiv.org/pdf/2607.18984
published: '2026-07-21'
collected: '2026-07-23'
category: Training
direction: 课程学习 · 训练策略分类体系
tags:
- Curriculum Learning
- Training Strategy
- Difficulty Evaluation
- Scheduler Design
- NLP
one_liner: 将课程学习拆分为难度评估与调度模块，提出细粒度分类体系解决现有CL策略不可比问题
practical_value: '- 训练推荐/大模型时可将CL策略拆分为难度评估、调度两个独立模块调优，避免耦合导致的效果波动

  - 设计业务场景CL训练策略时，可参考文中难度归因、调度形式化定义对齐优化目标，降低无效调参成本

  - 对比不同CL方案效果时，可基于该分类体系定位差异来源，避免不同目标的CL方案无效对比'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
NLP领域课程学习（CL）发展十余年，缺乏针对特定问题选择难度函数与调度器的统一指导，现有策略混淆不同难度、调度概念，无法横向对比，阻碍经验沉淀。
### 方法关键点
1. 提出细粒度CL分类体系，将CL拆分为难度评估、训练调度两个独立模块；
2. 难度评估维度区分归因来源与任务依赖，明确难度是包含「实例难学原因假设」的视角化概念；
3. 首次基于期望训练贡献形式化CL调度器，引入保留机制、单调性属性支持不同实现的横向对比。
### 关键结果
对现有NLP CL工作的分析显示，过往研究普遍混淆不同难度、调度定义，在相同CL标签下追求不同目标，存在系统性不可比问题；该分类体系可支撑CL策略的设计、分析与对比，帮助拆解效果优化来源。
