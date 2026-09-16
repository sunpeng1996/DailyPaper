---
title: Training Specialist Models without Reasoning Trajectories for Domain Expert
  Distillation
title_zh: 无需推理轨迹标注的领域专家模型蒸馏训练方法
authors:
- Yilei Tu
- Zihao Li
- Shaoxiong Ji
- Jörg Tiedemann
- Fei Yuan
affiliations:
- University of British Columbia
- Shanghai Artificial Intelligence Laboratory
- University of Helsinki
- ELLIS Institute Finland
- University of Turku
arxiv_id: '2609.13770'
url: https://arxiv.org/abs/2609.13770
pdf_url: https://arxiv.org/pdf/2609.13770
published: '2026-09-11'
collected: '2026-09-16'
category: Training
direction: 领域大模型蒸馏 · 无推理轨迹标注训练
tags:
- Knowledge Distillation
- Domain Adaptation
- SFT
- Chain-of-Thought
- LoRA
one_liner: 揭示QA对训练的专家模型优化策略决定隐式推理轨迹分布，可控调控下游蒸馏模型的专精-泛化权衡
practical_value: '- 垂直领域小模型蒸馏可直接复用该范式，无需高价标注推理轨迹，仅用业务场景积累的QA对+控制专家模型漂移即可获得高质量蒸馏数据，大幅降低电商导购、推荐理由生成等场景的训练成本

  - 训练上游专家模型优先选择LST或带KL锚定的ASFT，相比全量微调可在保留领域性能的同时避免通用能力退化，适合电商多场景复用的小模型训练

  - 专家与下游蒸馏模型性能强相关（Spearman ρ=0.9573），仅优化上游专家的微调策略即可直接提升下游蒸馏模型效果，无需额外改动下游训练流程

  - 禁止使用后自洽生成的推理轨迹做蒸馏（Self-Rationalize基线在低资源语言场景性能下降超过70%），避免引入幻觉推理污染训练数据'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前领域专家蒸馏依赖教师生成的推理轨迹做监督，但垂直领域通常仅能获取QA对，无标注推理轨迹可用，不同专家模型优化策略对隐式推理轨迹分布的影响不明确，导致下游蒸馏效果不可控。
### 方法关键点
- 将蒸馏过程作为无偏探针：学生模型不继承专家参数或优化约束，仅学习专家生成的推理轨迹，隔离不同优化策略对轨迹分布的影响
- 对比三类隐式漂移控制方法：全量微调（FFT）、LoRA、层选择性微调（LST），以及基于KL锚定的ASFT显式漂移控制方法，验证漂移程度对专精-泛化权衡的影响
- 所有学生模型采用完全一致的全量微调配置，仅使用不同专家生成的、过滤后答案正确的推理轨迹训练，保证变量唯一
### 关键结果
在化学、物理、低资源多语言三个领域测试，对比自蒸馏、自洽推理基线，核心结论：
1. 专家与下游学生模型的性能秩相关系数达0.9573，p值0.0093，相关性极强
2. LST微调的专家蒸馏出的8B模型性能超过4倍参数的32B通用模型，领域内任务性能最高提升200%，通用能力仅下降不到1%
3. 全量微调专家领域内性能提升最高但通用能力下降超过60%，ASFT可通过调整λ系数连续调控专精-泛化的平衡
### 核心结论
无推理轨迹标注时，上游专家模型的微调漂移控制是决定下游蒸馏模型效果的核心变量，而非蒸馏流程本身
