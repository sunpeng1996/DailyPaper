---
title: Harness Scaling for Generalizable Agentic Reinforcement Learning
title_zh: 基于执行框架缩放的通用智能体强化学习方法
authors:
- Fei Bai
- Huatong Song
- Chuan Hao
- Ran Tao
- Jian Yang
- Bryan Dai
- Wayne Xin Zhao
- Ji-Rong Wen
affiliations:
- Renmin University of China
- IQuest Research
- Beihang University
arxiv_id: '2610.29458'
url: https://arxiv.org/abs/2610.29458
pdf_url: https://arxiv.org/pdf/2610.29458
published: '2026-10-20'
collected: '2026-10-22'
category: Agent
direction: Agent 执行框架缩放与泛化优化
tags:
- Agentic RL
- Harness Scaling
- Generalization
- Reinforcement Learning
- Cross-Configuration Transfer
one_liner: 提出Harness Scaling新缩放维度，通过多样化执行框架训练提升Agent跨未知配置的泛化能力
practical_value: '- 训练电商/导购/运营类Agent时，可将系统Prompt、工具接口、上下文管理、执行流拆分为可变组件，用正交设计选少量组合训练，无需为每个业务场景单独适配，大幅降低多场景部署成本

  - 对接多平台第三方黑盒Agent接口/工具链时，无需在每个黑盒上单独做SFT/RL，仅需在自建的白盒多样化执行套件上做Harness Scaling训练，即可直接迁移到未知黑盒，效果优于单黑盒训练

  - 训练时优先给同一个任务分配2个结构近邻的执行配置，用局部可控变化+全局覆盖的策略，相同算力成本下可获得最优的跨配置泛化效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent RL通常在单一固定执行框架（Harness，包含Prompt、工具接口、上下文管理规则等）下训练，容易过拟合到特定配置，跨不同执行框架的迁移能力极差；而现有Agent缩放维度仅覆盖任务、环境两类，未覆盖执行方式的差异，无法解决跨配置泛化问题。

### 方法关键点
- 因子化Harness空间：将Harness拆分为系统Prompt、工具接口、Observation格式、上下文管理策略、执行工作流5个独立可变组件，每个组件设计3种变体，组合形成243种完整配置的空间
- 结构化训练集选择：用强度2正交设计构造仅含18个配置的训练子集，保证所有单组件变体、两两组件组合出现次数完全均衡，避免全空间训练的冗余
- 局部感知任务分配：每个任务随机采样1个锚点Harness，再搭配1个汉明距离最近的配置，用同一任务下的局部可控差异训练，兼顾全局空间覆盖

### 关键结果
在3个Agent基准上对比单Harness RL、黑盒SFT/RL等基线：
- 跨未知白盒Harness的Pass@1平均提升3.57~9.8个点，30B模型最高提升10.48点，原训练基准Harness的性能仅下降0.19点，几乎无损伤
- 迁移到Claude Code等未知黑盒Harness时，平均Pass@1比黑盒SFT高2.14~3.12个点，比黑盒RL高3.84~4.92个点

> 最值得记住的结论：Agent RL的缩放维度除了「解决什么任务、在什么环境运行」，还可以增加「用什么执行方式运行」，结构化的执行框架多样性训练比盲目堆配置、直接拟合黑盒的泛化效率高得多
