---
title: 'WARP: Weight-Space Analysis for Recovering Training Data Portfolios'
title_zh: WARP：用于恢复训练数据组合的权重空间分析框架
authors:
- Tzu-Heng Huang
- Aditya Goyal
- John Cooper
- Frederic Sala
affiliations:
- University of Wisconsin-Madison
arxiv_id: '2607.01686'
url: https://arxiv.org/abs/2607.01686
pdf_url: https://arxiv.org/pdf/2607.01686
published: '2026-07-01'
collected: '2026-07-04'
category: Training
direction: 训练数据透明度 · 权重空间分析
tags:
- TrainingDataRecovery
- WeightSpaceAnalysis
- ModelMerging
- LLMTransparency
- FineTuning
one_liner: 通过模型插值生成权重空间几何特征，从公开模型权重恢复其微调训练数据的领域混合占比
practical_value: '- 可借鉴模型插值生成伪checkpoint的思路，分析自研LoRA微调模型的训练数据分布合理性，排查domain偏移问题

  - 权重空间几何特征提取方法可复用，用于检测第三方开源大模型是否使用了自家业务私有数据微调，规避数据泄露风险

  - 无参数softmax读出版本的WARP可快速落地，无需额外标注即可估算开源微调模型的训练数据组成，辅助模型选型'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
大模型厂商通常不公开训练数据的领域混合采样权重，现有成员推断类方法仅能检测单个样本是否属于训练集，无法刻画训练语料的全局组成，导致模型使用者对训练分布缺乏可见性，存在信息不对称问题。

### 方法关键点
1. 通过模型合并在基座模型和微调模型之间插值，生成模拟训练轨迹的伪检查点，提取训练数据在权重空间的几何足迹；
2. 提取几何特征后，可选择无参数softmax读出版本快速推理，或在合成混合数据集上训练MLP投影器，映射得到各领域的训练占比。

### 关键结果
在BERT和GPT-2的受控实验中，WARP恢复领域混合比例的平均MAE分别低至0.046和0.104，性能显著优于成员推断基线及可访问真实训练轨迹的对比变种。
