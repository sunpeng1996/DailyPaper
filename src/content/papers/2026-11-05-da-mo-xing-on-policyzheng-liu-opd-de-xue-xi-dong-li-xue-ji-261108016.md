---
title: Learning Dynamics of On-Policy Distillation
title_zh: 大模型On-Policy蒸馏（OPD）的学习动力学机制分析
authors:
- Guan Zhe Hong
- Sumeet Ramesh Motwani
- Liang Chen
- Yangchen Pan
- Junchi Yu
- Jialin Yu
- Philip Torr
- Yi Ren
affiliations:
- University of Oxford
- EPFL
- City University of Hong Kong
arxiv_id: '2611.08016'
url: https://arxiv.org/abs/2611.08016
pdf_url: https://arxiv.org/pdf/2611.08016
published: '2026-11-05'
collected: '2026-11-06'
category: Training
direction: 大模型训练 · On-Policy蒸馏机制
tags:
- On-Policy Distillation
- Learning Dynamics
- Knowledge Distillation
- LLM Post-training
- Failure Mode Analysis
one_liner: 拆解On-Policy蒸馏反馈循环机制，解释失效模式，验证离线预蒸馏可大幅提升OPD收益
practical_value: '- 做垂直场景Agent/生成式推荐蒸馏训练时，不要冷启动OPD：先做1-4轮离线蒸馏让学生适配教师输出分布，避免OPD阶段生成低质量轨迹导致训练退化

  - OPD训练可引入2项早期诊断指标：监控梯度一致性（coherence）和蒸馏信号可及性（accessibility），提前识别 stalled 训练，节省算力成本

  - 做业务场景定制蒸馏时，优先选择同规模RL微调教师而非单纯用更大的通用教师，避免梯度抵消导致无训练收益'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
On-Policy蒸馏（OPD）是当前大模型后训练的核心范式之一，结合稠密教师监督与学生自生成轨迹训练，可高效对齐模型的推理、生成能力，但训练过程的反馈循环机制不清晰，业界普遍面临大教师迁移效果差、训练loss下降但泛化退化等问题，缺乏可落地的诊断和优化方案。
### 方法关键点
- 拆解OPD反馈循环为两个核心阶段：**转换阶段**（蒸馏信号转为参数更新）、**广播阶段**（参数更新跨前缀改变预测、重塑rollout分布）
- 基于神经切线核提出动力学分析框架，定义转换效率的两个核心指标：`accessibility`（学生参数对蒸馏信号的响应度）、`coherence`（跨样本梯度的一致性）
- 将训练效果变化分解为**漂移**（固定前缀下预测优化）和**路由**（训练前缀分布变化）两个维度，解释局部训练loss下降但泛化效果变差的根本原因
### 关键实验
在Qwen-2.5、Llama-3.1系列模型的数学推理任务（AIME 2024/2025、MATH-500）上验证：
1. 7B模型OPD训练时，健康配对的梯度一致性是失效配对的2.75~3.24倍，转换增益高2.27~2.62倍
2. 充分离线蒸馏后，OPD在AIME任务的pass@32比纯离线蒸馏最高提升15pp，1.5B模型MATH pass@1从45.9%提升至56.2%
### 核心结论
OPD训练的收益核心不在于教师的绝对能力，而在于学生是否有足够的离线准备、教师的蒸馏信号与学生的参数空间是否匹配
