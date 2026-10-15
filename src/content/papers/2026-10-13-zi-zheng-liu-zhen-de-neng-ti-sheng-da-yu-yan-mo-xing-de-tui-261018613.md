---
title: Does self-distillation improve reasoning?
title_zh: 自蒸馏真的能提升大语言模型的推理能力吗？
authors:
- Jason Ken Adhinarta
- Raina Wu
- Ashutosh Sharma
- Avinash Balakrishnan
- Rameswar Panda
- Polina Golland
- Yoon Kim
- Zhang-Wei Hong
affiliations:
- Massachusetts Institute of Technology
- MIT-IBM Computing Research Lab
arxiv_id: '2610.18613'
url: https://arxiv.org/abs/2610.18613
pdf_url: https://arxiv.org/pdf/2610.18613
published: '2026-10-13'
collected: '2026-10-15'
category: Training
direction: 大模型推理优化 · 自蒸馏效果验证
tags:
- Self-Distillation
- Reasoning
- GRPO
- SDPO
- OPSD
- Policy Gradient
one_liner: 系统验证现有自蒸馏方法的推理增益不泛化且并非来自特权信息
practical_value: '- 做Agent/导购机器人的推理微调时，优先选择GRPO等策略梯度方法而非纯自蒸馏，保障跨场景泛化性，避免线上OOD场景性能暴跌

  - 若用自蒸馏做知识迁移，需做消融实验区分增益是来自特权信息还是行为模式（如思维链格式对齐），避免无效调优

  - 微调效果评估必须加入完全OOD的测试集，不要复用训练集的问题/案例做评测，避免把过拟合当成性能提升'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
自蒸馏被视作比RLVR（可验证奖励强化学习）样本效率更高的推理微调方法，宣称能利用特权信息（如参考答案、执行反馈）提供更稠密的训练信号，但此前工作未严格验证其增益的泛化性，也未明确增益是否真的来自特权信息，存在落地风险。
### 方法关键点
- 复现SDPO、OPSD两种主流自蒸馏方法，对比基线为GRPO（策略梯度方法）、SFT
- 覆盖代码、科学推理、工具使用、数学推理4类推理任务，测试模型包括Qwen3（1.7B~14B）、OLMo-3-7B
- 新增梯度对齐度指标，计算自蒸馏梯度与OOD场景下策略梯度的余弦相似度，判断更新方向是否利于泛化
### 关键实验结果
- 代码任务：SDPO在训练见过的问题上精度比GRPO高2.8%，但完全OOD测试集低4.5%，解多样性下降超30%
- 科学/工具任务：SDPO域内精度与GRPO相当，但OOD精度平均下降12.2分，GRPO OOD精度基本无损失
- 数学任务：OPSD的推理增益90%以上来自思维模式迁移，特权参考信息的贡献不到1%
- 梯度对齐：自蒸馏梯度与OOD策略梯度的余弦相似度平均为-0.16，远低于GRPO的正对齐（平均+0.2）
### 核心结论
仅依赖自蒸馏目标的现有方法无法有效利用特权信息提升推理的泛化能力，做推理微调优先选择策略梯度类方法
