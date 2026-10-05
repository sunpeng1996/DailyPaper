---
title: 'Learning Style, Forgetting Semantics: A Case Study of SFT and RFT on Classification
  Tasks'
title_zh: 学习风格导致语义遗忘：分类任务下SFT与RFT的对比研究
authors:
- Haodong Liang
- Yanhao Jin
- Krishnakumar Balasubramanian
- Lifeng Lai
affiliations:
- University of California, Davis
arxiv_id: '2610.02437'
url: https://arxiv.org/abs/2610.02437
pdf_url: https://arxiv.org/pdf/2610.02437
published: '2026-10-01'
collected: '2026-10-05'
category: Training
direction: 大模型微调 · SFT/RFT遗忘机制对比
tags:
- SFT
- RFT
- Catastrophic Forgetting
- Fine-tuning
- Policy Gradient
one_liner: 从理论与实验层面证明SFT拟合教师风格偏好会引发语义遗忘，RFT可规避该问题
practical_value: '- 电商场景做商品分类、query意图识别等多任务微调时，若需保留旧任务语义能力，优先选择RFT替代纯SFT，可大幅降低遗忘风险

  - 若必须使用SFT微调，需对训练数据中不同语义类的回答风格做均衡处理，避免单类风格偏好过强，减少风格漂移引发的语义错误

  - 多序列任务微调可采用「风格中立SFT初始化+RFT微调新任务」的范式，在适配新任务的同时保留核心旧能力'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有经验观察显示，使用同样语义正确的标注数据微调时，SFT的灾难性遗忘程度显著高于RFT，但底层机制缺乏清晰解释，尤其是无法说明为何完全正确的标注也会导致模型丢失已掌握的语义能力，该研究针对这一核心问题展开理论与实验验证。
### 方法关键点
- 将模型输出拆分为**语义通道**和**风格通道**：同一语义类别的不同表达（如答案“4”的文字、数字、带前缀格式）归为同语义、不同风格
- 基于线性softmax策略推导SFT与RFT的更新分解，证明两者语义更新方向完全一致，仅风格更新逻辑存在差异
- 理论证明：从无风格偏好的初始化出发，RFT的精确策略梯度会始终保持风格通道对称无漂移，而SFT拟合非均匀教师风格偏好时会产生轴外风格漂移，进而偏移语义决策边界引发错误
### 关键结果
在8个序列分类任务的实验中：
1. 群体更新场景下，RFT的泛化误差和遗忘率始终为0，SFT在所有测试学习率下均出现正遗忘，最高可达0.16
2. 有限样本场景下，RFT的轴外参数能量比SFT低1~2个数量级，泛化误差比同学习率下的SFT低30%以上
### 核心结论
哪怕所有标注的语义完全正确，SFT拟合数据的风格偏好也会引发语义能力遗忘，RFT仅奖励语义正确性的机制可天然规避该问题
