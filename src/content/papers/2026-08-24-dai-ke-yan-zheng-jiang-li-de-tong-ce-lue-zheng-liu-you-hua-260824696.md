---
title: On-policy Distillation with Verifiable Reward
title_zh: 带可验证奖励的同策略蒸馏优化方法OPDVR
authors:
- Wenze Lin
- Jiale Zhao
- Xitai Jiang
- Songde Rao
- Yining Li
- Shenzhi Wang
- Bingxiang He
- Gao Huang
affiliations:
- Tsinghua University
- Beihang University
- Peking University
arxiv_id: '2608.24696'
url: https://arxiv.org/abs/2608.24696
pdf_url: https://arxiv.org/pdf/2608.24696
published: '2026-08-24'
collected: '2026-08-26'
category: Training
direction: 大模型后训练 · 蒸馏与RL融合优化
tags:
- On-policy Distillation
- RLVR
- ReLU Gating
- GRPO
- LLM Post-training
one_liner: 通过无额外超参数的ReLU门控融合同策略蒸馏与可验证奖励RL，效果优于标准蒸馏方案
practical_value: '- 做LLM类业务（推荐Agent、电商导购、生成式推荐文案）的大模型蒸馏小模型时，可直接复用ReLU门控机制，无需额外调参，还能突破老师模型性能上限

  - 业务场景做RLHF对齐时，可将规则化业务校验（比如推荐合规性、文案正确性）作为可验证奖励，用OPDVR无缝融合蒸馏稠密信号与任务正确性约束，省去多目标权重调参成本

  - 用GRPO做推荐/Agent策略优化的场景，可直接套用GRPD设计，融合token级蒸馏指导与组相对优势信号，比单独用GRPO或OPD获得更稳定的效果提升'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
RLVR（带可验证奖励的强化学习）与On-policy Distillation（OPD）是当前LLM后训练的两大主流范式：RLVR基于任务结果提供明确奖励，但信号稀疏导致信用分配困难；OPD通过老师模型提供token级稠密监督，但仅拟合老师输出分布、不校验生成轨迹正确性，学生性能被老师上限限制。现有两者结合方法依赖加权求和或启发式切换，引入大量额外超参数，调参成本高且鲁棒性差。
### 方法关键点
- 从RLVR视角重构采样token OPD的隐式奖励，发现其奖励符号由师生概率比决定，与轨迹正确性无关，存在正确轨迹token被惩罚、错误轨迹token被奖励的冲突问题
- 引入无额外超参数的ReLU门控机制：正确轨迹仅保留老师置信度高于学生的token做正向奖励，错误轨迹仅保留学生置信度高于老师的token做负向惩罚，既保证奖励符号完全对齐轨迹正确性，又保留老师的分布指导
- 可无缝兼容任意策略梯度算法，结合GRPO得到GRPD变种，用组相对优势替代二元正确性信号，进一步降低训练方差、提升稳定性
### 关键结果
在6个数学推理基准上测试：同架构蒸馏（Qwen3-4B←Qwen3-4B-RL）下OPDVR平均准确率49.1，较采样token OPD提升1.3，在AIME24上甚至超过老师模型；跨架构蒸馏（Qwen3-1.7B←Qwen3-4B-RL）下OPDVR平均准确率22.8，较采样token OPD提升1.9；GRPD变种平均准确率49.4，较GRPO提升4.6、较OPD提升1.0。
> 值得记住：蒸馏信号的方向永远要优先服从任务正确性，而非盲目拟合老师分布
