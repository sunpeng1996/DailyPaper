---
title: 'PIVOT: Progressive Intervention via Online Teacher Correction'
title_zh: PIVOT：基于在线教师校正的渐进式干预LLM训练框架
authors:
- Zhihao Yang
- Boyuan Zheng
- Puhui Tan
- Yukun Chen
- Kuan Zhang
- Longze Chen
- Jiaming Li
- Renke Shan
- Lu Wang
- Xianpei Han
affiliations:
- 中国科学院大学
- 清华大学
- 中国科学院软件研究所中文信息处理实验室
arxiv_id: '2610.40576'
url: https://arxiv.org/abs/2610.40576
pdf_url: https://arxiv.org/pdf/2610.40576
published: '2026-10-29'
collected: '2026-10-30'
category: Training
direction: LLM训练 · 教师辅助RLVR推理优化
tags:
- RLVR
- Teacher-guided Training
- GRPO
- Knowledge Distillation
- LLM Reasoning
one_liner: 结合轨迹层干预与token级监督的教师辅助RLVR框架，大幅提升硬推理任务性能
practical_value: '- 落地Agent多步决策、复杂Query理解、大模型选品推理等稀疏奖励任务时，可复用PIVOT混合训练范式：小模型作为学生，大模型作为在线教师，同时结合RL任务奖励与教师校正段的KL蒸馏损失，解决纯RL无有效学习信号的问题

  - 干预位置可直接复用trick：让学生先生成512token左右的推理前缀，再插入教师校正段，比直接给教师初始轨迹的学习效率高30%以上，同时预留足够的后续生成空间避免任务内容截断

  - 蒸馏损失选择策略：新任务冷启动、学生初始准确率<10%时用反向KL快速收敛到至少一种有效推理路径；学生效果达标后换正向KL提升泛化性，适配OOD场景

  - 资源分配优化：固定教师推理成本时，优先给更少的样本配更长的教师校正段，KL蒸馏仅取教师Top30 token，可在几乎无损效果的前提下降低30%以上的训练算力开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RLVR（基于可验证奖励的强化学习）是当前LLM推理能力对齐的主流范式，但在硬推理任务上受稀疏奖励瓶颈限制：当批次内所有采样轨迹全部失败时，奖励信号完全失效无法训练。单独使用教师轨迹干预或token级蒸馏均存在缺陷：前者教师轨迹与学生自身生成分布差异大，难以被学生学习；后者在学生错误轨迹上的教师监督信号多模态冲突，无法引导学生回归正确路径。

### 方法关键点
- 混合Rollout构造：每个Prompt采样6条纯学生生成轨迹+2条教师辅助轨迹，辅助轨迹中学生先生成前缀，教师输出校正段后学生继续生成至结束
- 多目标混合损失：用GRPO RL损失优化全轨迹的任务奖励，加仅作用于教师生成段的KL蒸馏损失，同时保留参考KL正则项避免学生分布漂移
- 可落地训练配方：干预位置选学生生成512token后，初始成功率低用反向KL、高用正向KL，固定教师token预算下优先更少的长段干预，KL蒸馏仅取教师Top30 token平衡效果与算力

### 关键实验
在SynLogic硬逻辑游戏、数学推理基准上测试，对比RL only、SFT+RL、KDRL等基线：硬逻辑游戏上mean avg@8从最优基线的19.5%提升至35.6%，接近翻倍；Math-ID硬数学任务准确率从基线最高22.09%提升至23.05%，在AIME、MATH500等OOD基准上也一致优于所有基线。

### 核心结论
教师指导的效果同时取决于引入的推理路径质量与路径上的监督设计，二者缺一不可；基于学生自身生成上下文的校正比直接提供教师完整轨迹更容易被学生学习。
