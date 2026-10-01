---
title: 'The Teacher Is a Direction, Not a Destination: Extrapolating RL-Induced Representation
  Residuals in On-Policy Distillation'
title_zh: On-policy蒸馏新方法RIDE：沿RL诱导表征残差方向外推超越教师
authors:
- Hao Li
- MeiJia Chen
- Weijie Ren
- Donghan Li
- Zijun Tian
- Jingchun Huang
- Naibo Wang
affiliations:
- University of Science and Technology of China
- Rutgers University
- Zhejiang University
- Independent Researcher
arxiv_id: '2609.36484'
url: https://arxiv.org/abs/2609.36484
pdf_url: https://arxiv.org/pdf/2609.36484
published: '2026-09-28'
collected: '2026-10-01'
category: Training
direction: LLM蒸馏 · 表征方向外推训练
tags:
- On-Policy Distillation
- Representation Learning
- Reinforcement Learning
- Knowledge Distillation
- LLM Training
one_liner: 提出RIDE蒸馏方法，在表征空间沿RL诱导残差方向外推，稳定实现学生模型超越RL教师
practical_value: '- 做电商客服Agent、推荐文案生成LLM轻量化蒸馏时，可复用RIDE的层间表征残差外推思路，替代传统输出层蒸馏，降低LM头衰减带来的信号损失，稳定提升小模型性能

  - 业务中如果要将RL微调后的大模型蒸馏到同初始化小模型，可直接复用λ=1.15~1.35的超参区间，无需大量调参即可获得超越教师模型的效果，训练稳定性远高于输出空间外推方法

  - 做用户偏好对齐的生成式推荐模型蒸馏时，可将RLHF后的表征残差作为方向信号，直接在每层表征层面做对齐，避免输出层采样噪声放大导致的训练崩溃，提升生成内容的偏好匹配度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统On-policy蒸馏（OPD）将教师模型作为学习终点，近年输出空间外推方法尝试让学生超越教师，但LM头会各向异性衰减RL带来的表征变化，且基于采样token对数概率比的外推会放大噪声，导致训练不稳定甚至性能退化，尤其当教师与基线差距较小时退化更严重。

### 方法关键点
- RIDE（RL-Induced Direction Extrapolation）利用预RL基线模型与RL训练后教师模型的层间隐状态差作为RL诱导残差，直接在表征空间沿该残差方向外推目标点
- 学生初始化自预RL基线，在学生生成的轨迹上，将每层隐状态回归到「教师隐状态 + (λ-1)*残差」的目标点，λ>1时目标点超出教师位置，实现沿RL优化方向的继续迭代
- 该目标等价于在二次惩罚约束下最大化与残差方向对齐的线性奖励，梯度为确定性值，无输出空间采样噪声放大问题

### 关键实验
在4组不同规模、架构的Base/RL教师对（1.5B~4B参数）上测试，对比OPD、OPRD、输出空间外推ExOPD等基线，RIDE在所有测试集上平均Avg@16比教师模型高0.32~1.08分，比ExOPD平均高9.1分，是唯一在所有测试对上均接近或超过教师模型的方法，λ在1.15~1.35区间效果最优，训练稳定性远高于ExOPD。

> 最值得记住的一句话：RL训练后的教师模型提供的是优化方向而非终点，在表征空间沿RL诱导残差外推比输出空间外推更稳定高效，可实现学生模型稳定超越教师
