---
title: 'When to Follow the Teacher: Advantage-Based On-Policy Distillation'
title_zh: 基于优势的在策略蒸馏方法：选择性遵循教师指导
authors:
- Mahdi Sabbaghi
- George Pappas
- Hamed Hassani
- Adel Javanmard
affiliations:
- University of Pennsylvania
- University of Southern California
arxiv_id: '2610.31563'
url: https://arxiv.org/abs/2610.31563
pdf_url: https://arxiv.org/pdf/2610.31563
published: '2026-10-22'
collected: '2026-10-23'
category: Training
direction: 大模型在策略蒸馏训练优化
tags:
- Knowledge Distillation
- On-Policy Training
- LLM Alignment
- Advantage Weighting
- Policy Optimization
one_liner: 提出优势加权在策略蒸馏算法，无需额外辅助信号即可多场景超越现有蒸馏/RL基线
practical_value: '- 电商/Agent场景下做大小模型蒸馏上线时，可复用AOPD思路：不对教师输出做全量模仿，仅给能提升学生最终业务指标（转化率、任务成功率）的教师动作加权，避免无效/有害模仿

  - 工程实现上AOPD的无偏估计器仅需现有学生采样轨迹和终端奖励，无需额外RM或反事实rollout，可无缝替换现有OPD训练流水线，新增计算量极低

  - 做自蒸馏（如用带ground truth的特权学生当教师优化业务模型）时，可复用重要性采样权重截断（c=4）技巧，大幅提升训练稳定性，且采样组大小G=4即可，降低训练成本

  - 同时用蒸馏和RL优化业务场景（如推荐文案生成、Agent决策）时，避免直接加权相加蒸馏和RL损失，用AOPD优势加权范式天然对齐两个目标，避免性能下降'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统在策略蒸馏（OPD）要求学生在轨迹每一步都完全模仿教师，默认教师所有指导都有益，但实际教师动作可能并不适配当前学生的能力，甚至会降低学生最终任务成功率；现有优化方法要么依赖额外的奖励模型、反事实采样，要么没有直接围绕教师动作对学生最终奖励的影响加权，存在优化错位。

### 方法关键点
- 以学生策略下的动作优势（即采取教师动作后学生完成任务的期望奖励减去学生自身动作的期望奖励）对教师动作加权，正优势动作增强，负优势动作抑制
- 推导出无偏重要性采样估计器，仅用学生的在策略轨迹和终端奖励即可计算目标，无需额外rollout、价值函数或外部奖励模型，保持OPD的采样效率
- 加入重要性权重截断（默认c=4）降低训练方差，同时保留单步更新奖励提升的理论保证

### 关键实验
在数学（Open-Thoughts、AIME24）、编码（TACO、HumanEval）、生物、医疗QA四类任务上分别测试外部教师蒸馏和自蒸馏设置：外部教师蒸馏时，AOPD在AIME24数据集上比OPD基线高2.9pp，AMC高3.3pp；自蒸馏时，Qwen3-8B在AIME24上比OPSD高10.4pp，Qwen2.5-7B在MedQA上比OPSD高2.7pp，全部优于GRPO、OPD/OPSD、KDRL等基线。

### 核心结论
有效的蒸馏应该优化学生的最终成功，而不是最大化与教师的一致性。
