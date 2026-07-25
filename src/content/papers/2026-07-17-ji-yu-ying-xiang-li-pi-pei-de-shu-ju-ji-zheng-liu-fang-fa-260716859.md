---
title: Dataset Distillation by Influence Matching
title_zh: 基于影响力匹配的数据集蒸馏方法
authors:
- Haoru Tan
- Wang Wang
- Sitong Wu
- Xiuzhe Wu
- Yangtian Sun
- Chirui Chang
- Shaofeng Zhang
- Xiaojuan Qi
affiliations:
- HKU
- CUHK
- Stanford
arxiv_id: '2607.16859'
url: https://arxiv.org/abs/2607.16859
pdf_url: https://arxiv.org/pdf/2607.16859
published: '2026-07-17'
collected: '2026-07-25'
category: Training
direction: 模型训练优化 · 数据集蒸馏
tags:
- Dataset Distillation
- Influence Estimation
- Training Efficiency
- Synthetic Data
- Vision-Language
one_liner: 提出基于训练最终结果对齐的Inf-Match数据集蒸馏方法，线性时间估算样本影响力，效果超越现有基线
practical_value: '- 推荐场景小样本微调/蒸馏可复用结果对齐思路，无需对齐中间梯度，直接对齐收敛参数效果，降低蒸馏复杂度

  - 线性时间样本影响力估算方法（一阶泰勒+优化动态展开）可直接复用，用于筛选推荐训练集高价值样本，提速模型迭代

  - 多模态跨模态检索场景可直接复用Inf-Match做数据集蒸馏，用少量合成数据降低跨模态召回模型训练成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有数据集蒸馏方法多对齐训练过程中间代理信号（如每步梯度、训练轨迹），依赖凸性假设或高复杂度逆Hessian乘积计算，泛化性有限，难以适配多模态等复杂场景。
### 方法关键点
1. 提出结果导向的Inf-Match框架，对齐小合成数据集与全量数据集训练后的收敛参数影响力，而非中间训练过程
2. 设计全可微样本级影响力估算器，通过展开优化动态+一阶泰勒近似实现线性时间复杂度计算，无需逆Hessian乘积或凸性假设
3. 最小化合成数据集与真实数据集的影响力差异来学习合成样本，实现训练效果对齐
### 关键结果
- 分类任务：Tiny-ImageNet（每类10样本）精度达31.5%，较NCFM基线提升4.7%
- 多模态检索任务：Flickr30K数据集用200-1000个合成样本时，平均检索精度较NCFM提升2.5%，优于所有过程匹配基线
