---
title: 'The Intruder Threshold: A Spectral Law for LoRA Fine-Tuning'
title_zh: 入侵者阈值：LoRA微调的谱定律
authors:
- Peng Xie
affiliations:
- Technical University of Munich
arxiv_id: '2607.23711'
url: https://arxiv.org/abs/2607.23711
pdf_url: https://arxiv.org/pdf/2607.23711
published: '2026-07-26'
collected: '2026-07-28'
category: Training
direction: 大模型高效训练 · LoRA遗忘抑制
tags:
- LoRA
- Catastrophic Forgetting
- Spectral Analysis
- PEFT
- Fine-Tuning
one_liner: 提出仅基于预训练权重谱的LoRA每层入侵者临界阈值，无拟合参数可降低灾难性遗忘
practical_value: '- 业务侧LoRA微调（如电商文案Agent、垂域推荐大模型）时，可先对每层预训练权重做SVD计算阈值，提前识别易遗忘层，降低调参成本

  - 可复用spike-budget规则，无需验证集扫参，直接按每层阈值限制LoRA alpha，可降低62%遗忘且不损失任务效果

  - 接入第三方LoRA适配器时，可快速扫描其入侵者占比，提前预判通用能力遗忘风险，避免上线故障

  - 全微调/LoRA选型可参考谱阈值：若LoRA更新强度可控制在阈值以下，优先选LoRA，兼顾高效与通用能力保留'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
LoRA微调产生的与预训练奇异向量几乎正交的入侵者维度是灾难性遗忘的核心诱因，但此前无分层定量预测入侵者出现时机的理论，只能事后调参验证，效率低且风险不可控。
### 方法关键点
- 基于矩形尖峰变形变换，仅用预训练权重W的谱计算每层临界更新强度$s^*=\bar{\theta}/(\gamma\sigma_1(BA))$，无拟合参数
- 设计低复杂度核心矩阵，精确计算更新后权重的奇异系统及与预训练基的重叠，无需大矩阵SVD，支持万级层快速扫描
- 提出无投影的spike-budget规则，通过限制每层LoRA alpha使其更新强度低于阈值，从根源抑制入侵者生成
### 关键结果
实验覆盖7类模型（Transformer、SSM、MoE、编解码）、18个适配器、9840层扫描，82%的层阈值预测误差在2倍以内，部署时区分是否存在入侵者的AUC达0.89；spike-budget规则在最脆弱模型上降低62%遗忘且不损失任务性能；全微调的更新强度比所有层阈值低100-200倍，解释了其几乎无入侵者的现象。
### 核心结论
LoRA的灾难性遗忘核心是更新强度超过了每层的谱阈值，而非更新幅度本身，阈值可仅通过预训练权重的SVD提前计算，无需任何训练数据
