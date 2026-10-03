---
title: On-Policy or Off-Policy Learning? A Systematic Study of Distillation Dynamics
title_zh: 强到弱蒸馏场景下On-Policy与Off-Policy学习的动态特性系统研究
authors:
- Julianna Piskorz
- Antonin Berthon
- Mihaela van der Schaar
affiliations:
- University of Cambridge
arxiv_id: '2609.35259'
url: https://arxiv.org/abs/2609.35259
pdf_url: https://arxiv.org/pdf/2609.35259
published: '2026-09-27'
collected: '2026-10-03'
category: Training
direction: 大语言模型蒸馏 · 训练策略对比
tags:
- Knowledge-Distillation
- On-Policy-Learning
- Off-Policy-Learning
- KL-Divergence
- LLM-Training
one_liner: 受控拆解蒸馏三要素作用，推翻On-Policy学习固有优势的通用结论
practical_value: '- 小模型蒸馏降本优先选Forward KL + Off-Policy方案：Forward KL对rollout数据来源鲁棒性极强，无需生成On-Policy数据即可达到与On-Policy相当的性能，大幅降低训练算力成本

  - 业务需泛化到更难场景（如复杂query理解、长推理链Agent任务）时，可在蒸馏阶段加入部分On-Policy数据，可带来10~15%的泛化性能提升

  - 控制灾难性遗忘和参数更新稀疏度优先调小学习率：效果远优于切换On-Policy策略，小学习率+Forward KL可在不损失分布内性能的前提下将遗忘降到最低

  - 需避免蒸馏时教师模型无关风格迁移（如保留学生原有话术风格），可选择Reverse KL + On-Policy组合抑制风格迁移'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
业界普遍认为On-Policy学习可减少灾难性遗忘、生成更稀疏参数更新、提升泛化能力，但过往SFT与RLVR的对比混杂了目标函数、监督信号等大量变量，无法孤立验证rollout策略的实际作用；而On-Policy训练需要持续生成数据，成本远高于Off-Policy，明确其真实价值对优化LLM训练流程、降低成本至关重要。
### 方法关键点
- 以强到弱蒸馏为受控测试环境，固定训练pipeline仅独立调整三类变量：rollout策略（On/Off-Policy、连续师生rollout光谱）、token级KL方向（Forward/Reverse）、学习率
- 覆盖Llama 3、Qwen2.5两个模型族，测试医疗、科学、算术三类推理任务，所有对比严格控制无关变量一致
- 评估维度覆盖分布内准确率、灾难性遗忘、参数更新稀疏度、跨难度泛化性能、后续RLVR适配性
### 关键结果
- On-Policy无通用优势：分布内最高准确率On-Policy为72%，Off-Policy为73%几乎持平；相同KL和学习率下，On-Policy未带来更少遗忘或更稀疏更新
- KL方向是性能核心影响因素：Forward KL准确率稳定在71%~73%，对rollout策略变化鲁棒性极强，性能波动仅5.2个百分点；Reverse KL性能波动大（35%~72%），仅在On-Policy rollout下能拿到较好性能
- 学习率是遗忘和稀疏度的唯一核心影响因素：学习率从1e-5升到5e-5时，OOD准确率下降11~14个百分点，参数更新稀疏度从85%~90%降到52%~60%，与rollout策略无关
- 特定场景On-Policy有优势：泛化到更难算术任务时，On-Policy比Off-Policy准确率高10~15%，且Reverse KL + On-Policy可抑制教师风格迁移
### 核心结论
不要为了追求On-Policy的宣称收益盲目增加训练成本，优先调优KL方向和学习率，仅在需要泛化到更难任务时才考虑引入On-Policy数据
