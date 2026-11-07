---
title: 'Label-Wording Augmentation in a Typed-Decision Encoder: Gains on Unfamiliar
  Words, Not on Abbreviations or Codes'
title_zh: 类型决策编码器的标签表述增强：仅对陌生词生效，对缩写与代码无效
authors:
- Vladimir Beskorovainyi
affiliations:
- Besk Tech
arxiv_id: '2611.08439'
url: https://arxiv.org/abs/2611.08439
pdf_url: https://arxiv.org/pdf/2611.08439
published: '2026-11-05'
collected: '2026-11-07'
category: Training
direction: 大模型训练 · 标签表述增强
tags:
- Cross-Encoder
- Label Augmentation
- Multilingual LLM
- Model Evaluation
- Data Augmentation
one_liner: 对比两款307M多语言跨编码器，验证标签表述增强仅对普通/外来词有效对缩写代码无效
practical_value: '- 做电商客服意图路由、搜索query类目预测等动态标签分类任务时，对普通文本类标签可做多表面形式的标签增强，陌生词场景准确率最高可提24%

  - 若分类标签为缩写、内部编码（如电商SKU编码、货号），无需做标签表述增强，无收益甚至会导致准确率下降

  - 评估模型对标签表述的鲁棒性时，需拆分普通词、外来术语、缩写、编码四类标签集分别验证，避免整体指标掩盖细分场景问题'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
动态传入标签的类型决策模型（如零样本分类、路由编码器）准确率完全依赖调用方传入的标签表述，开发者无法提前控制，需提升模型对不同标签表述的鲁棒性
### 方法关键点
对比两款307M参数多语言Cross-Encoder Ru-Jev，新版本训练时加入多表面形式的标签表述增强；固定输入问题，仅变换18个路由标签的表述，覆盖普通词、外来术语、俚语、缩写、无意义编码共10种标签词汇表开展评估
### 关键结果
普通/外来词场景，增强版准确率最高提升0.24，14组对比中11组统计显著；缩写/无意义编码场景无收益，缩写场景准确率甚至下降，编码场景准确率不超过随机水平；未知数据集上准确率波动为-8.4~+5.6个百分点
