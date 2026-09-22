---
title: 'iSDFT: Information-Proximal Self-Distillation for Continual Learning in LLMs'
title_zh: iSDFT：面向大模型持续学习的信息近端自蒸馏方法
authors:
- Ahmed Khaled Khamis
- Xiaotong Ji
- Hassan Jaber
- Rasul Tutunov
- Matthieu Zimmer
- Jun Wang
- Haitham Bou-Ammar
affiliations:
- Georgia Tech
- Imperial College London
- Politecnico di Torino
- UCL Centre for AI
arxiv_id: '2609.24646'
url: https://arxiv.org/abs/2609.24646
pdf_url: https://arxiv.org/pdf/2609.24646
published: '2026-09-21'
collected: '2026-09-22'
category: Training
direction: 大模型持续学习 · 自蒸馏微调
tags:
- Continual Learning
- Self-distillation
- LLM Fine-tuning
- On-policy Learning
- Stability-plasticity
one_liner: 提出带信息预算约束的自蒸馏框架，在保留基础能力前提下提升持续学习的新技能获取效果
practical_value: '- 电商/导购Agent、推荐话术生成等领域LLM微调场景，可复用iSDFT的「信息预算+冻结基模型锚定」机制，学习领域新知识的同时避免语义匹配、通用推理等基础能力退化，减少微调负迁移

  - 自蒸馏目标构造trick可直接迁移：无需固定人工插值系数，通过KL I投影自动求解每个token的倾斜系数λ_t，适配不同token的学生-教师分布差异，比固定线性插值效果更稳定

  - 多任务持续学习场景（如分批次学习不同品类推荐话术、不同场景Agent工具调用能力）可复用ρ从0.25线性增长到1的调度策略，逐步提升教师权重，收敛更快、遗忘更少'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有on-policy自蒸馏微调（SDFT）解决了SFT的训练部署分布偏移问题，但每步强制学生完全拟合带演示的教师分布，无法控制每个状态下的知识传递强度，极易导致模型原有基础能力遗忘，陷入稳定性-可塑性困境，尤其在多任务持续学习、领域微调场景下，新技能学习与旧能力保留的平衡难以把控。
### 方法关键点
- 将教师视为带信息预算的知识源而非完全拟合目标，通过KL I投影构造信息近端目标：在满足指定教师信息约束的前提下，选择与当前学生分布最接近的目标分布，得到学生与教师几何插值的闭式解，每个token的插值系数λ_t由信息预算自动求解，无需人工设置固定插值参数。
- 新增冻结基模型的KL锚定项，解决局部保守更新导致的累计漂移问题，实现局部可塑性控制与长期能力保留的解耦。
- 信息预算γ_t设为ρ*KL(Tt||Pt)，ρ采用0.25到1的线性调度策略，自适应适配不同token的学生-教师分布差异，全局仅需控制ρ和锚定权重µ两个超参。
### 关键实验
跨4个异质LLM骨干（Qwen2.5-7B、Qwen3-1.7B等）、2个专项任务（工具使用、科学领域适配）测试，相比vanilla SDFT在7/8的模型-任务组合上取得提升，平均增益2.7个点；原有能力保留上，73%的评估结果与基模型差值在0.5分以内，比最强基线高21个百分点；在10个数学、编码、竞赛数学benchmark上均取得最大平均增益，其中MATH-500提升11.8分，AIME24提升9.6分。
### 核心结论
控制教师知识的注入时机与强度，而非强制完全拟合教师，能在高效获取新技能的同时更好保留模型原有通用能力。
