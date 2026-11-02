---
title: MUON-RT Reusing the Teacher's Trajectory for Momentum-Free Muon for LLM Self-Distillation
title_zh: MUON-RT：复用教师轨迹的无动量大模型自蒸馏优化器
authors:
- Aryan Das
- Vinay Kumar Verma
- Aakansha Mishra
affiliations:
- IIT Kanpur
- Amazon
arxiv_id: '2610.41104'
url: https://arxiv.org/abs/2610.41104
pdf_url: https://arxiv.org/pdf/2610.41104
published: '2026-10-30'
collected: '2026-11-02'
category: Training
direction: 大模型自蒸馏 · 训练显存优化
tags:
- Self-Distillation
- Muon Optimizer
- Memory Efficiency
- EMA
- LLM Fine-Tuning
one_liner: 复用EMA教师与学生的权重差值替代Muon动量缓冲区，同时提升自蒸馏精度并降低显存占用
practical_value: '- 做电商/Agent垂直域LLM自蒸馏微调（比如工具调用、商品文案生成能力训练）时，可直接替换原有AdamW/Muon优化器，无需改动训练逻辑，即可降低27%~42%持久显存占用，同时获得精度提升

  - 所有已维护参数对齐EMA教师的场景（比如推荐系统用户兴趣模型自蒸馏、RAG微调、半监督学习），均可复用teacher-student权重差值替代优化器动量缓冲区，无需额外存储成本

  - 可直接复用「梯度/教师分支分别处理、正交化后再用小系数α=0.1混合」的trick，避免历史梯度滞后于动态蒸馏目标的问题，效果优于预正交混合策略'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
EMA教师引导的自蒸馏（SDFT/SDPO）是LLM增量微调、缓解灾难性遗忘的主流方案，可用于Agent能力迭代、垂直域模型适配等场景，但现有优化器额外占用大量持久显存：AdamW需为每个参数存储2个动量缓冲区，Muon需存储1个动量缓冲区，7B模型自蒸馏时AdamW就需要129GB GPU显存，大模型训练硬件门槛极高。而自蒸馏流程本身已维护EMA教师的权重副本，其轨迹天然包含历史更新的动量信息，存在复用降本空间。

### 方法关键点
- 理论证明EMA教师与学生的权重差值是指数加权的历史更新方向累积，等效于动量信息，可直接替代Muon的动量缓冲区
- 梯度分支单独做Newton-Schulz正交化，教师分支先去除与学生权重平行的径向分量，再做谱归一化，两个分支完成正交化后再用固定系数α（实验最优为0.1）混合
- 仅保留1个小向量用于幂迭代热启动，无其他额外持久状态，临时张量随用随释放

### 关键实验
在Qwen2.5-7B-Instruct上做SDFT训练，对比AdamW平均精度高2.6个点，持久显存低42%；对比带动量的Muon平均精度高5.4个点，持久显存低27%。在Olmo-3-7B-Instruct上做SDPO训练，对比AdamW平均精度高2.0个点。10T参数规模下可省40%持久显存，优化器步长仅占训练总步长的2%，额外计算开销可忽略。

> 值得记住的一句话：只要训练流程中已维护参数对齐的EMA教师模型，就可以复用其轨迹信息替代优化器动量，无额外显存成本即可同时提升训练效率与效果
