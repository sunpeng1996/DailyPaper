---
title: 'CARDEA: Auditable Reasoning Grounded in Spatial Evidence for End-to-End Coronary
  Angiography Interpretation'
title_zh: CARDEA：基于空间证据可审计推理的端到端冠脉造影解读模型
authors:
- Jia-Jen Lee
- Shih-Yen Hou
- Kee Koon Ng
- Wei-Chun Wang
- Shih-Sheng Chang
affiliations:
- China Medical University Hospital
- China Medical University
arxiv_id: '2609.06931'
url: https://arxiv.org/abs/2609.06931
pdf_url: https://arxiv.org/pdf/2609.06931
published: '2026-09-06'
collected: '2026-09-13'
category: Other
direction: 多模态大模型 医疗影像可解释推理
tags:
- LVLM
- Multimodal Reasoning
- Reinforcement Learning
- Chain-of-Thought
- Auditable AI
one_liner: 提出三阶段训练大视觉语言模型，实现带可审计空间证据的端到端冠脉造影全流程解读
practical_value: '- 三阶段（特征对齐→自蒸馏冷启动→可验证奖励RL）训练范式可复用至垂域多模态推荐模型训练，降低标注成本

  - Chain-of-Box可解释思路可迁移至多模态推荐/搜索的结果归因，向用户/运营透出决策依据，提升信任

  - 基于可验证闭环奖励的RL优化方法可用于提升垂域大模型的零样本泛化能力，减少下游任务适配成本'
score: 3
source: huggingface-daily
depth: abstract
---

### 动机
冠脉造影（CAG）是冠心病诊断金标准，但人工解读一致性差，现有AI系统决策过程不可审计、开放评估能力不足，难以获得临床信任。
### 方法关键点
仅基于公开数据集和封闭任务分三阶段训练统一大视觉语言模型CARDEA：1. 视觉特征对齐；2. 自蒸馏Chain-of-Box（CoB）冷启动；3. 带可验证奖励的强化学习（RLVR），鼓励推理轨迹用bounding box锚定空间证据。训练未引入报告生成标注，零样本评估开放报告生成能力。
### 关键结果
域偏移下主导分类准确率达0.91，与专用分类器持平；复杂度评估准确率0.90，达到介入心脏病医生水平；RLVR将零样本报告生成的血管严重度macro-F1从基线0.513提升至0.686，是常值基线（0.312）的2倍以上。
