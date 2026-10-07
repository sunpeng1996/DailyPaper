---
title: 'DiffGate: Difficulty-Gated Teacher Guidance for On-Policy Distillation'
title_zh: DiffGate：面向策略蒸馏的难度门控教师引导方法
authors:
- Karn Tiwari
- Varnith Chordia
- Prathosh A P
affiliations:
- Indian Institute of Science
- Snap Inc.
arxiv_id: '2610.04596'
url: https://arxiv.org/abs/2610.04596
pdf_url: https://arxiv.org/pdf/2610.04596
published: '2026-10-02'
collected: '2026-10-07'
category: Training
direction: 大模型训练 · 策略蒸馏与RL融合
tags:
- Knowledge Distillation
- On-Policy Distillation
- GRPO
- RLVR
- LLM Training
one_liner: 将难度门控的选择性教师指导融入GRPO，互补解决OPD与RLVR的监督盲区，提升小模型推理与代码性能
practical_value: '- 做垂直域小LLM蒸馏（如客服回复、商品文案生成、规则型导购Agent）时，可借鉴仅给失败轨迹加教师信号的设计，避免正确输出被教师风格带偏，降低蒸馏负向影响

  - 用GRPO做RLHF/RLAIF优化推荐/Agent策略时，可复用「难度门控+教师信号限幅」trick：全失败组给最大教师信号，随组正确率下降信号权重，既解决GRPO奖励稀疏问题，还能避免梯度爆炸

  - 计算资源有限、rollout组采样量小（如n=4）的场景下，DiffGate效果比纯GRPO更稳定，适合边缘端小模型的低成本训练落地'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有On-policy Distillation（OPD）是小模型蒸馏主流方案，能降低传统蒸馏的训推分布差，但监督是token级、不感知全序列正确性，易被风格差异误导；而基于可验证奖励的RL（RLVR，比如GRPO）能优化序列级正确性，但存在奖励稀疏、credit分配粗、全失败组无梯度的问题，二者盲区互补，直接简单融合易出现信号冲突、梯度不稳定问题。

### 方法关键点
- 仅对验证失败的轨迹施加教师指导，成功轨迹完全保留GRPO的优化方向，避免正确输出被教师修改
- 教师信号做限幅处理：用`2*tanh(Δ/2)`把教师-学生对数概率差限制在(-2,2)区间，防止大偏差主导梯度，稳定训练
- 加难度门控权重：按rollout组的求解率缩放教师信号强度，全失败组（p=0）权重最大，随求解率提升权重下降，精准补全GRPO无信号的盲区
- 最终token级优势由GRPO的序列级优势加门控限幅后的教师信号组成，用PPO裁剪代理目标优化

### 关键实验
用Qwen3-0.6B/1.7B/4B学生、Qwen3-8B/14B教师，在数学推理、代码生成任务上对比GRPO、OPD系列基线；代码任务上比纯GRPO提升avg@8 1.7~1.8点、pass@8 1.6~5.7点，数学任务上pass@8提升1.1~3.9点，OOD科学任务上比基线最高提升8.4个avg@8点。

**最值得记住的一句话**：教师信号的核心价值是补全RL奖励的盲区，而非全局对齐教师分布，仅在需要的地方、以合适的强度施加引导，才能同时保留蒸馏和RL的优势。
