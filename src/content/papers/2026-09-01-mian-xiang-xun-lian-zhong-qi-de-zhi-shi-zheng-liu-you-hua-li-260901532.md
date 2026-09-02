---
title: Knowledge Distillation During Mid-Training Favors Reasoning over Factual Recall
title_zh: 面向训练中期的知识蒸馏优化：平衡推理能力与事实召回
authors:
- Jacqueline He
- Howard Yen
- Shuyue Stella Li
- Margaret Li
- Hanqing Zeng
- Yinglong Xia
- Benyu Zhang
- Zhuokai Zhao
- Qiang Zhang
- Pang Wei Koh
affiliations:
- Meta AI
- University of Washington
- Princeton University
arxiv_id: '2609.01532'
url: https://arxiv.org/abs/2609.01532
pdf_url: https://arxiv.org/pdf/2609.01532
published: '2026-09-01'
collected: '2026-09-02'
category: Training
direction: 大模型训练 · 知识蒸馏优化
tags:
- Knowledge Distillation
- Mid-Training
- LLM Training
- Reasoning
- Factual Recall
one_liner: 提出Switch Distillation缓解LLM训练中期蒸馏的推理与事实召回权衡
practical_value: '- 电商垂域LLM、生成式推荐模型的中期训练/微调阶段，可直接复用Switch Distillation思路，仅在teacher预测熵低的token位置做蒸馏，其余位置用原始CE损失，平衡推理能力（如复杂需求理解、导购路径规划）与事实准确性（如商品参数、价格、活动规则记忆），避免蒸馏导致事实类内容记错

  - 做垂域小模型蒸馏时，无需在所有token上做蒸馏，用teacher熵做轻量路由信号，几乎不增加额外计算量，还能避免全量蒸馏带来的事实召回下降问题，适合低成本快速落地

  - 若业务场景优先提升模型推理能力（如Agent做多轮用户需求拆解、个性化推荐理由生成），可调整路由阈值q，提升低熵token的蒸馏占比，在可控的事实召回损失下最大化推理能力增益'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM训练已普遍引入预训练与对齐之间的中期训练阶段，基于小体量高质量语料进一步提升推理、事实、指令遵循等能力。但传统知识蒸馏在该阶段存在显著的推理-事实召回权衡：蒸馏提升推理能力的同时会大幅减慢事实知识学习速度，现有蒸馏方法均针对预训练/对齐阶段设计，缺乏适配中期训练的优化方案，无法同时满足两类能力提升需求。

### 方法关键点
- 归因权衡根源：teacher模型在推理类（数学、指令）数据上预测熵更低、监督质量更高，学生在预训练阶段已掌握大部分低熵事实，中期训练待学习的事实集中在teacher高熵区间，全量蒸馏会弱化这部分事实的监督信号
- 提出Switch Distillation：逐token计算teacher预测熵，每步选取batch内熵最低的q% token做reverse KL蒸馏，其余token采用常规交叉熵损失；路由信号复用KD已计算的teacher logits，几乎无额外计算开销

### 关键结果
实验基于OLMo-2 1B学生模型、7B/13B Instruct teacher模型，对比NTP、正向/反向KD、TRKD等基线：
- 中期训练后，推理性能较NTP提升71%，知识与常识性能提升19%，事实召回仅下降1pp
- 经过完整SFT、DPO、RLHF对齐流程后，推理性能仍较NTP高32%，知识性能高20%，事实召回差距完全消失

**核心结论**：知识蒸馏不是阶段无关的，中期训练阶段需基于teacher置信度动态路由损失，才能在提升推理的同时避免事实召回损失。
