---
title: 'The Life Cycle of a Massive Activation: Stochastic Birth, Weight-Decay-Driven
  Growth, and Competitive Consolidation'
title_zh: Transformer大规模激活生命周期：随机诞生、权重衰减调控与竞争固化
authors:
- S. Aaron McClendon
- Jorge Gallego-Feliciano
- Antonios Saravanos
affiliations:
- Aimpoint Digital Labs
- Mistral AI
- New York University
arxiv_id: '2610.00423'
url: https://arxiv.org/abs/2610.00423
pdf_url: https://arxiv.org/pdf/2610.00423
published: '2026-10-04'
collected: '2026-10-12'
category: Training
direction: Transformer训练 · 大规模激活动态机制
tags:
- Massive Activations
- Weight Decay
- AdamW
- Transformer Training
- Activation Quantization
one_liner: 揭示Transformer大规模激活完整生命周期 明确权重衰减为其规模调控核心训练杠杆
practical_value: '- 做电商垂域LLM微调/低精度部署时，可通过调整训练阶段的权重衰减系数λ，控制激活离群值的峰值幅度与出现时机，降低量化损失、提升推理速度，实测峰值幅度与λ^(-1/2)正相关可直接复用

  - 针对LLM推理性能优化时，无需针对性抑制单个离群激活通道：这类通道是训练种子随机决定的冗余集体，抑制单个会自动在其他通道重建，应从sink token的整体RMS规模入手调控

  - 用AdamW训练生成式推荐/Agent调度小模型时，注意其二阶矩预条件会天然维持大激活通道存在，若对低精度部署有强要求，可适当调高λ或换用无偏优化器规避离群值'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Transformer中的大规模激活（残差流中幅度远超均值的离群坐标）是低精度训练/推理的核心障碍，与attention sink直接相关，但此前研究未明确其规模调控机制、完整生命周期演化规律，也未解释为何特定通道会成为离群载体。
### 方法关键点
- 结合两组实验：自训练51M/203M/380M decoder-only Transformer的全训练轨迹密集采样，与Pythia系列70M~6.9B公开模型的多种子checkpoint分析
- 设计可控扰动实验：权重衰减开/关对照、单通道消融、激活幅度匹配对照，分离通道身份与集体规模的效应
- 建立AdamW预条件增长与权重衰减的平衡模型，解释大规模激活的上升与峰值规律
### 关键结果数字
- 权重衰减系数λ与大规模激活峰值出现时间呈对数线性相关（corr=-0.985），峰值幅度近似服从λ^(-1/2)缩放
- 梯度衰减由sink token的整体RMS决定，单个最大激活通道消融仅改变整体RMS约5%
- 离群通道身份由训练种子随机决定，训练早期（4k~5k步）就锁定，全训练周期中top3通道占sink token平方范数的比例从0.55升至0.99，形成冗余集体
- AdamW二阶矩预条件是维持大激活通道存在的核心，原始维持力比权重衰减低2个数量级，不足以单独维持

大规模激活不是Transformer架构固有的特权坐标，而是训练过程中随机选择、集体实现的梯度调控机制，权重衰减是训练期调控其规模的核心杠杆。
