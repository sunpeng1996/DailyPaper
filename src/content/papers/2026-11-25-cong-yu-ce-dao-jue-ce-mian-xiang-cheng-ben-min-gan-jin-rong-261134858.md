---
title: 'From Prediction to Decision: Decision-Focused Fine-Tuning of Autoregressive
  Tabular Transformers for Cost-Sensitive Financial Events'
title_zh: 从预测到决策：面向成本敏感金融事件的自回归表格Transformer决策导向微调
authors:
- Ashkan Golgoon
- Giacomo Domeniconi
- Samuel Atkins
- Sergio Servantez
- Zain Khandwala
affiliations:
- AI Center of Excellence, U.S. Bank
arxiv_id: '2611.34858'
url: https://arxiv.org/abs/2611.34858
pdf_url: https://arxiv.org/pdf/2611.34858
published: '2026-11-25'
collected: '2026-11-27'
category: Training
direction: 大模型微调 · 成本敏感决策优化
tags:
- Cost-sensitive Learning
- Fine-tuning
- Autoregressive Transformer
- Fraud Detection
- Utility Optimization
one_liner: 针对成本敏感金融事件，提出决策导向微调方法，替代事后阈值，显著提升欺诈检测业务效用
practical_value: '- 电商风控/反薅羊毛场景可复用「决策目标直接嵌入微调」思路，替代事后阈值调整，将客损、资损等异构成本直接写入损失函数，省去后处理链路

  - 微调时加预训练模型KL锚定、辅助语言建模项的trick可直接复用，既能优化业务目标，又不会损失模型原有泛化性和概率校准能力

  - 样本级成本敏感损失的闭式梯度计算方法可落地，避免强化学习类方法的采样、critic训练开销，适配高吞吐风控/推荐在线推理场景'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统自回归Transformer做金融事件（如欺诈）预测仅优化概率精度，后续依赖事后成本矩阵阈值生成决策，无法最大化异构不对称的业务效用，漏判高价值欺诈、误拒小额交易的成本差异巨大，传统类别加权、focal loss等成本敏感方法效果不佳。

### 方法关键点
1. 直接面向机构自定义的金额缩放成本矩阵微调预训练模型，优化受限softmax输出的期望效用，损失为预测概率的线性函数，梯度可闭式计算，无需采样、critic或优势估计；
2. 加入预训练模型的KL锚定项、辅助语言建模项，保留模型校准能力和生成属性；
3. 支持GRPO风格的组归一化变体，可扩展到轨迹级奖励优化。

### 关键结果数字
在0.11%样本占比的高不平衡信用卡欺诈任务上，每1000次决策的实有效用比贝叶斯阈值交叉熵模型提升0.08，填补70%→76%的最优解gap，对应每千笔交易增收约12美元，10次种子实验结果一致显著（p=0.002），远超传统成本敏感方法。
