---
title: A Verifier-Guided Explainable Reasoning Framework with Gold-Anchored QLoRA,
  Task-Aware Mixture-of-Experts, and Group-Relative RLVR
title_zh: 结合锚定QLoRA、任务感知MoE和分组RLVR的验证器引导可解释推理框架
authors:
- Thi Kim Trang Vo
- Nam Tien Le
- Thi Kim Nguyet Vo
- Minh Khang Tran
- Duy Phuong Tran
affiliations:
- University of Information Technology (UIT), Vietnam
- Ho Chi Minh City University of Technology (HCMUT), Vietnam
- Vietnam National University, Ho Chi Minh City, Vietnam
- University of Economics Ho Chi Minh City (UEH), Vietnam
arxiv_id: '2609.05221'
url: https://arxiv.org/abs/2609.05221
pdf_url: https://arxiv.org/pdf/2609.05221
published: '2026-09-04'
collected: '2026-09-07'
category: Reasoning
direction: LLM可解释推理 · 神经符号验证
tags:
- QLoRA
- MoE
- Reinforcement Learning
- Neuro-Symbolic
- Explainable AI
- Reasoning
one_liner: 提出验证器引导的神经符号推理框架，在准确率损失极小的前提下大幅提升推理可解释性
practical_value: '- QLoRA微调时可采用字段加权损失策略，对电商文案生成、商品属性预测等任务，给价格、规格、优惠等核心字段分配更高权重，避免关键信息输出错误

  - 任务感知轻量路由+外部符号验证的架构可复用在电商导购Agent中，将满减计算、凑单等数值类查询路由到计算器工具，逻辑类查询路由到规则引擎，无需改动大模型结构即可提升准确率

  - 多维度（正确性/一致性/可解释性）分组RL优化策略，可用于推荐理由生成、商品QA的SFT后优化，在不损失答案准确性的前提下提升推理透明度，方便用户理解和bad
  case排查'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM通过CoT、指令微调已具备较强多步推理能力，但生成的解释常存在不一致、无事实依据、难以验证的问题，现有推理优化方案多仅关注最终答案正确性，无法区分偶然正确的结果和逻辑严谨的推理过程，无法满足高可解释性要求场景的需求。
### 方法关键点
- 金标锚定QLoRA微调：对Qwen2.5-3B-Instruct做4bit NF4 QLoRA微调，训练时锁定权威答案字段，给答案、单位、前提字段分配更高损失权重，避免噪声监督覆盖正确标签
- 任务感知MoE路由：轻量路由器仅在验证阶段做任务分发，逻辑类问题路由到FOL/Z3符号验证器，物理类问题路由到公式/单位感知的数值求解器，不修改大模型本身结构
- 分组相对RLVR优化：设计P1（答案正确性）、P2（证据/单位一致性）、P3（推理深度）三维度奖励，基于GRPO的分组相对优势做策略优化，用冻结的SFT checkpoint做参考正则化避免模型漂移
- 推理策略：生成5条候选回复做无金标自一致性聚类选最优，物理类任务额外增加置信度≥0.98的符号校验做保守修正
### 关键实验
在EXACT 2026的逻辑+物理QA数据集（共2162条，8:2拆分）上测试，RLVR相比校准后的SFT baseline，P3（推理深度）从50.68%提升至72.20%，P1（答案准确率）仅从56.62%微降至55.94%；符号验证器仅干预15.69%的物理类查询，即可将物理类P1提升约9个百分点。
### 核心结论
RL优化中若组内候选的核心指标（如答案正确性）差异很小，优化会自动向有区分度的维度倾斜，可通过多维度奖励设计在几乎不损失核心指标的前提下针对性优化可解释性等次要目标。
