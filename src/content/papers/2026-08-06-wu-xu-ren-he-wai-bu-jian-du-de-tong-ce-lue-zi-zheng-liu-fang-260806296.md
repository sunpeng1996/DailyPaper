---
title: On-Policy Self-Distillation without Any Supervision
title_zh: 无需任何外部监督的同策略自蒸馏方法U-OPSD
authors:
- Yijiang Li
- Bingyang Wang
- Yijun Liang
- Yunjie Tian
- Di Fu
- Nuno Vasconcelos
affiliations:
- UC San Diego
- Georgia Institute of Technology
- University of Maryland, College Park
- ByteDance
arxiv_id: '2608.06296'
url: https://arxiv.org/abs/2608.06296
pdf_url: https://arxiv.org/pdf/2608.06296
published: '2026-08-06'
collected: '2026-08-07'
category: Training
direction: 大模型训练 · 无监督自蒸馏
tags:
- Self-Distillation
- On-Policy Training
- Unsupervised Learning
- LLM Post-training
- Majority Voting
one_liner: 提出无监督同策略自蒸馏U-OPSD，基于模型自生成多数投票伪标签追平甚至超越有监督基线
practical_value: '- 搜索推荐的Query理解、用户意图推理等垂直场景，可复用U-OPSD逻辑，用模型多轮输出多数投票构造伪标签，无需标注即可提升小模型推理能力，降低标注成本

  - 做LLM4Rec推理优化时，可借鉴其训练目标设计：仅对和共识不一致的生成轨迹做前缀KL蒸馏，聚焦模型易错点训练，比全量样本训练效率更高，节省训练资源

  - 工程实现上，可复用其top-k截断的分布蒸馏优化，无需计算全词表KL散度，在损失精度极小的前提下大幅降低蒸馏计算开销，适配线上低资源小模型迭代

  - 电商Agent的任务规划、工具调用等可萃取标准化结果的场景，可直接套用该自蒸馏流程实现无监督迭代，无需人工标注正负样'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有同策略自蒸馏（OPSD）依赖外部监督（真值标签、大模型指导、环境反馈），无法在无标注场景落地，限制了大模型在标注成本高、数据稀缺的垂直领域的后训练优化空间。

### 方法关键点
- 采样阶段：对每个无标注问题采样G条独立生成轨迹，提取每条的最终答案做标准化
- 投票阶段：对有效答案做多数投票得到伪答案，投票占比超过阈值τ时进入蒸馏流程，否则跳过
- 蒸馏阶段：选最短的共识轨迹作为伪解决方案作为老师的上下文输入，对所有和伪答案不一致的错误生成轨迹的前缀做token级KL散度蒸馏，仅修正模型确定错误的位置
- 训练天然聚焦模型能力边界：仅在模型能形成稳定共识但仍存在错误输出的样本上训练，自动形成课程学习

### 关键结果
在5个数学推理基准（AIME24/25、HMMT25、MATH500、AMC23）上测试不同规模的Qwen3模型：非思考模式下4B/8B模型比基线提升8.5%/10.7%，比有监督OPSD平均高3.2%/2.3%；思考模式下和有监督OPSD性能持平，比GRPO高0.9%/1.1%；30B MoE指令微调模型也可直接复用该方法，比基线提升1.7个点。

**最值得记住的一句话**：在模型有能力形成稳定共识但仍有提升空间的场景下，自蒸馏的核心约束不是标注数据，而是挖掘并修正模型自身不一致性的机制，无需外部监督即可实现性能提升。
