---
title: 'Transferability for General Reasoning: An Automated Curriculum for Multi-Domain
  RLVR'
title_zh: 面向通用推理的可迁移性：多域RLVR自动课程学习方法
authors:
- Yongjin Yang
- Jiarui Liu
- Yinghui He
- Lechen Zhang
- Bernhard Schölkopf
- Zhijing Jin
affiliations:
- University of Toronto
- Carnegie Mellon University
- Princeton University
- University of Illinois Urbana-Champaign
- Max Planck Institute for Intelligent Systems
arxiv_id: '2606.25178'
url: https://arxiv.org/abs/2606.25178
pdf_url: https://arxiv.org/pdf/2606.25178
published: '2026-06-26'
collected: '2026-07-03'
category: Training
direction: LLM多域RL训练 · 自动课程设计
tags:
- Curriculum Learning
- RLVR
- GRPO
- Multi-Armed Bandit
- Cross-Domain Transfer
one_liner: 提出结合可学习性与梯度迁移性的多臂老虎机课程TAC，显著提升多域RLVR训练效果
practical_value: '- 多任务LLM微调（如同时优化推荐文案生成、query理解、商品属性抽取）场景可直接复用TAC框架，无需手动调任务采样权重，自动将训练资源向高迁移性任务倾斜，降低调参成本的同时提升全链路效果

  - 现有GRPO/RLHF训练流程可零成本集成迁移性计算逻辑：仅需复用训练产生的梯度做随机投影，无需额外标注、探针或rollout，整体开销<1%，工程落地门槛极低

  - 面对训练数据不平衡场景（如推荐场景点击数据远多于转化数据），TAC的迁移性信号可避免模型过度拟合高数据量但低迁移性的任务，有效提升小样本重要任务的效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多域RLVR是提升LLM通用能力的核心方案，但现有训练课程要么固定采样比例、要么仅基于单域可学习性自适应调度，完全忽略当前域的梯度更新对其他域的迁移增益，容易过度拟合高可学习性但窄适用的任务，浪费训练算力，整体性能提升受限。

### 方法关键点
- 多域采样建模为多臂老虎机问题，单域得分由β加权组合两部分信号：一是单域可学习性，即GRPO训练产生的平均绝对优势的z-score，反映当前域的学习空间；二是跨域迁移性，即当前域梯度与其他所有域梯度的余弦相似度均值，经min-max归一化后映射到[0,1]区间
- 迁移性信号无额外开销：对Transformer最后N层的梯度做TRAK风格随机降维投影，维护各域梯度的EMA状态，每Kc步计算一次跨域余弦相似度，整体wall-clock开销<1%
- 自适应更新机制：除更新当前采样域的Q值外，每Kc步用最新迁移性信号批量更新所有未采样域的得分，搭配UCB探索项避免低可学习性但高迁移性的域被饿死

### 关键实验
在覆盖数学、代码、逻辑、仿真、表格、STEM的6域推理套件上测试，对比随机采样、手动设计的Math-to-Others课程、仅用可学习性的SEC基线：Qwen3-1.7B上宏观准确率比最优基线高1.8pp（相对+5.6%），Llama3.2-3B上比最优基线高1.6pp（相对+5.4%）；在训练数据不平衡的场景下，仍比SEC基线高1.5pp，鲁棒性显著。

### 核心结论
最具可学习性的域往往不是迁移性最好的域，跨域梯度对齐信号是多任务训练课程设计的核心增益来源。
