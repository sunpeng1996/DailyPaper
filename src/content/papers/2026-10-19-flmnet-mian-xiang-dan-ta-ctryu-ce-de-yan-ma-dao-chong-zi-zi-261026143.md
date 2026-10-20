---
title: 'FLMNet: Self-Ensemble Distillation from Masks to Seeds for Single-Tower CTR
  Prediction'
title_zh: FLMNet：面向单塔CTR预测的掩码到种子自集成蒸馏方法
authors:
- Yifan Wang
- Yifei Du
affiliations:
- National University of Singapore
- University of Science and Technology of China
arxiv_id: '2610.26143'
url: https://arxiv.org/abs/2610.26143
pdf_url: https://arxiv.org/pdf/2610.26143
published: '2026-10-19'
collected: '2026-10-20'
category: RecSys
direction: CTR预测 · 单塔自集成蒸馏
tags:
- CTR-Prediction
- Self-Ensemble-Distillation
- Single-Tower
- Regularization
- Knowledge-Distillation
one_liner: 推导自集成蒸馏无限掩码极限，设计无采样单塔FLMNet，结合跨种子蒸馏获CTR预测SOTA
practical_value: '- 可将自集成蒸馏的闭式正则化直接迁移到现有单塔CTR模型：只要满足门控读未掩码输入、输出层仿射、每层逐坐标缩放三个条件，即可无需多次dropout前向，仅单步前向计算logit方差加罚，在不增加训练耗时的前提下提升模型泛化性。

  - 跨种子蒸馏的轻量化集成方案可直接复用：仅训练3个同结构不同初始化的单塔，将其logit均值作为软目标蒸馏到单个学生塔，推理仍为单塔前向，可拿到50%以上的多塔集成收益，完全适配线上低延迟要求的电商/广告CTR排序场景。

  - 自蒸馏教师目标优化：优先选择logit空间平均的对数意见池作为教师，而非概率算术平均，匹配KL散度蒸馏的最优目标，可进一步提升自蒸馏效果。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有单塔CTR模型（如FinalNet、QNN）通过自集成蒸馏提升精度，但依赖多次随机dropout前向采样，训练成本高且生效机制不明确；线上大规模CTR推理要求严格的单塔单步前向延迟，无法部署多塔集成模型，亟需在不增加推理成本的前提下最大化自蒸馏与集成收益的方案。
### 方法关键点
- 理论推导无限掩码下自集成蒸馏的极限形式：等价于无掩码前向的标签损失 + logit在掩码下的Jensen gap正则项，仅需logit的均值和方差即可计算，无需采样。
- 设计满足三大条件的FLMNet单塔结构：门控仅读取未掩码输入embedding、输出层为仿射变换、每层逐坐标缩放表征，使logit均值等于无掩码前向输出，方差可通过闭式近似高效计算，训练全程无需dropout采样。
- 新增跨种子蒸馏阶段：训练K个不同初始化的FLMNet，将其logit均值作为软目标蒸馏到单个学生塔，吸收多初始化集成收益，推理仍为单塔前向。
### 关键实验结果
在Criteo、Avazu、KKBox等5个公开CTR基准上，对比17个SOTA基线（含QNN-α、FinalNet等），FLMNet-CF（带闭式正则）、FLMNet-KD（加跨种子蒸馏）包揽AUC、Logloss指标前两名；跨种子蒸馏可拿到3塔集成50%以上的收益，单步训练耗时与QNN-α接近。
### 核心结论
自集成蒸馏的核心是压制掩码噪声和种子噪声带来的过拟合，无采样闭式正则+跨种子蒸馏可在完全不增加推理成本的前提下，拿到接近多模型集成的CTR效果收益。
