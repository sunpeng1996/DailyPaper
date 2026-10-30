---
title: 'Every Token Needs Its Own Teacher: Multi-teacher Adaptive On-policy Self-distillation'
title_zh: Token级多教师自适应在线自蒸馏算法MTA-OPSD
authors:
- Yifu Luo
- Chuang Ma
- Zeyu Chen
- Enkelejda Kasneci
- Qi Chen
- Gjergji Kasneci
affiliations:
- TU München
- Munich Center for Machine Learning
- relAI
- Kyoto University
- Aalto University
arxiv_id: '2610.40574'
url: https://arxiv.org/abs/2610.40574
pdf_url: https://arxiv.org/pdf/2610.40574
published: '2026-10-29'
collected: '2026-10-30'
category: Training
direction: LLM后训练 · 在线自蒸馏优化
tags:
- Self-Distillation
- On-Policy Training
- LLM Post-training
- Knowledge Distillation
- Reasoning
one_liner: 首次实现token级自适应在线自蒸馏，数学推理任务较基线最高提升5.9
practical_value: '- 做LLM驱动的电商个性化文案生成、Agent多轮推理/工具调用蒸馏时，可将原响应级蒸馏替换为token级自适应教师选择策略，能在不增加额外教师模型成本的前提下提升生成/推理准确率

  - 多教师池构造方法可直接复用：无需训练多个教师模型，仅通过对参考文本（如用户历史、商品属性、正确推理路径）做不同策略的截断，即可生成差异化的监督信号，落地成本极低

  - 两阶段token级教师选择逻辑（多数投票筛方向一致候选→选KL最大的教师提供强信号）可迁移到推荐系统的多目标蒸馏、多信号融合排序场景，解决不同监督信号在不同样本/位置适配性差的问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现存On-policy Self-distillation（OPSD）均为响应级自适应，要么全程使用全参考的固定教师，要么同一响应内所有token共享同一个自适应教师，无法匹配不同token的差异化学习需求，易出现师生分布不匹配、推理性能退化的问题。

### 方法关键点
- 通过教师干预预实验验证：同一响应内不同token的最优教师存在显著差异，且最优教师可通过多数投票+KL散度两步筛选识别
- 构造轻量多教师池：基于参考文本的3种截断策略（前缀、后缀、随机片段）+ 3种暴露比例（0.5、0.75、全量）生成7个候选教师，所有教师共享同一套模型参数，仅参考上下文不同
- 两阶段token级教师选择：每个token先通过多数投票筛选出与大部分教师信号方向一致的候选子集，再从子集中选择与学生KL距离最大的教师作为该token的监督源
- 训练目标为所有token与对应所选教师的KL散度之和

### 关键实验
基于Qwen3-1.7B/4B/8B模型在数学推理数据集DeepMath-103k上训练，对比OPSD、SDPO、Paint三类主流OPSD基线，在AMC23、AIME24、AIME25基准上，平均性能较基线上限分别提升+5.9、+1.5、+2.8个点，且在难度最高的AIME25数据集上增益最稳定。

### 核心结论
在线自蒸馏无需整句共享同一教师，每个token都可基于自身学习状态自适应选择最合适的监督信号，仅通过上下文截断生成多教师即可实现显著性能增益。
