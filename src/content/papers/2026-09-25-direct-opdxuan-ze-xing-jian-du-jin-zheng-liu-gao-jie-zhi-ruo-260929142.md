---
title: 'Not Every Token Is Worth Distilling: Selective Supervision for Direct-OPD'
title_zh: Direct-OPD选择性监督：仅蒸馏高价值token的弱到强策略迁移方法
authors:
- Yibo Zhao
- Zixuan Yang
- Yunshi Lan
- Xiang Li
affiliations:
- East China Normal University
- Hugging Face
arxiv_id: '2609.29142'
url: https://arxiv.org/abs/2609.29142
pdf_url: https://arxiv.org/pdf/2609.29142
published: '2026-09-25'
collected: '2026-10-01'
category: Training
direction: LLM训练 · 策略蒸馏优化
tags:
- Direct-OPD
- Knowledge Distillation
- JSD
- Policy Transfer
- Weak-to-Strong
one_liner: 基于教师-参考模型JSD筛选高价值状态，用10%token提升Direct-OPD策略迁移精度
practical_value: '- 做LLM微调/蒸馏（如电商文案生成、Agent决策微调）时，可仅保留JSD top10%的高价值token训练，无需全token监督，在不损失效果甚至提升效果的前提下降低训练算力成本

  - 低JSD的监督信号不仅无价值还会导致模型退化，做RLHF、OPD类训练时务必过滤这类低divergence状态，避免性能下降

  - 该方法无额外前向传播开销，直接复用现有蒸馏流程中已计算的教师、参考模型概率即可实现，工程改造成本极低，可快速接入推荐、Agent等场景的LLM训练流程'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Direct-OPD可将小模型RL后的策略迁移至大模型，避免大模型直接跑RL的高昂成本，但它对所有token施加均等监督：其使用的log-ratio奖励仅衡量相对变化，哪怕教师和参考模型对学生候选token的概率质量极低、策略几乎无变化，奖励仍可能保持非零，引入大量无效甚至有害的监督信号，限制迁移效果。
### 方法关键点
- 理论证明：当教师与参考模型对学生候选token的总概率质量趋近于0时，JSD、双向KL都会趋近于0，但Direct-OPD的奖励与梯度保持不变，低JSD状态下教师行为几乎无变化，监督无价值
- 提出S²D-OPD：在学生top-K候选token集合基础上增加残差token（聚合剩余词表概率），计算教师与参考模型的JSD，按每个回复内的JSD排序，仅保留top 10%的高JSD状态做监督
- 无额外开销：直接复用Direct-OPD已计算的教师、参考模型概率，无需额外前向传播
### 关键结果
在AIME、HMMT数学推理基准测试，覆盖2组教师对、4个1.7B~8B参数量的学生模型：7/8的实验场景下S²D-OPD的held-out精度超过原生Direct-OPD，平均提升0.95个百分点（95% CI 0.40~1.54），训练速度无损失，后期训练稳定性更优。

**最值得记住的一句话**：策略蒸馏的效果由保留哪些状态决定，而非保留多少状态，低divergence监督不仅冗余甚至会损害模型性能。
