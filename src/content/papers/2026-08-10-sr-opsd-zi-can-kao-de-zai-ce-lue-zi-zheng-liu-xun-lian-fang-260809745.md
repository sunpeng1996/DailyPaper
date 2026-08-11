---
title: 'SR-OPSD: Self-Referenced On-Policy Self-Distillation'
title_zh: SR-OPSD：自参考的在策略自蒸馏训练方法
authors:
- Zhuo Sun
- Entong Li
- Yanlong Zhao
- Xiaoyuan Cheng
- Wenxuan Yuan
- Kaiyu Li
- Che Liu
- Huihang Liu
- Harrison Bo Hua Zhu
- Li Zeng
affiliations:
- Shanghai University of Finance and Economics
- Imperial College London
- University of Science and Technology of China
- University College London
- Peking University
arxiv_id: '2608.09745'
url: https://arxiv.org/abs/2608.09745
pdf_url: https://arxiv.org/pdf/2608.09745
published: '2026-08-10'
collected: '2026-08-11'
category: Training
direction: 大语言模型在策略自蒸馏训练优化
tags:
- On-Policy Self-Distillation
- Rényi Divergence
- LLM Training
- RLHF
- Reference Anchoring
one_liner: 提出自参考在策略自蒸馏框架，通过参考锚定与Rényi投影提升OPSD性能与训练稳定性
practical_value: '- 做电商场景LLM微调（如商品文案生成、智能客服推理、个性化推荐理由生成）时，可引入初始SFT模型作为固定参考锚，通过调整α（建议0.7~0.9）平衡新任务适配和原始通用能力，避免训练过拟合或能力坍缩

  - 替换现有蒸馏的KL/JSD损失为Rényi散度，调整ρ（建议0.7~0.95）平滑极端token概率比，可有效提升用用户点击/转化等反馈信号做自蒸馏时的训练稳定性，减少调参成本

  - 对于需要多步推理的Agent场景（如复杂商品搭配推荐、售后问题自动解决），可直接复用SR-OPSD训练pipeline，相比GRPO/SDPO在相同训练成本下可提升3~8pp的任务准确率，且输出多样性更稳定'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有On-Policy Self-Distillation（OPSD）能将环境反馈转化为稠密token级监督，补充稀疏奖励RL的不足，但自教师策略和学生策略共同演化，固定KL/JSD投影目标容易导致训练不稳定、模式坍缩或基础能力退化，长期训练性能容易先升后降。

### 方法关键点
- 构造自参考蒸馏目标：将EMA更新的自教师策略和冻结的初始参考策略做几何插值，用α系数控制目标位置，α=1时退化为原始OPSD，α=0时回到初始策略
- 采用Rényi散度族统一投影几何，用ρ参数控制对token级概率比的敏感度：ρ→1时退化为KL散度，0<ρ<1时可以平滑极端概率比，避免梯度爆炸或模式坍缩
- 训练流程和现有OPSD完全兼容，仅需在损失计算层替换原有目标，无需额外数据或外部教师

### 关键实验
在SciKnowEval科学推理、数学推理、LiveCodeBench代码生成三个领域验证，对比GRPO、SDPO、OPSD等基线：
1. SciKnowEval上，Qwen3-8B模型15小时训练后5个领域平均准确率75.2%，超SDPO 2.8pp、超GRPO 6pp，长期训练无性能退化
2. 数学推理数据集上，平均Pass@64达78.4%，超GRPO 3.2pp、超SDPO 8pp
3. LiveCodeBench上，Qwen3-8B模型准确率达50.1%，超SDPO 1.3pp、超GRPO 8.9pp，模型越大增益越明显

### 最值得记住的一句话
自参考锚定的收益高度依赖投影几何的选择，仅添加参考锚定对KL/JSD目标无增益，必须搭配Rényi投影才能同时提升性能与训练稳定性
