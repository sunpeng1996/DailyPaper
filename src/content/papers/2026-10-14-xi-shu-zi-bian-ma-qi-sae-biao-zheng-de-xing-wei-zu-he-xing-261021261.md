---
title: Behavioral Compositionality of Sparse Autoencoder Representations
title_zh: 稀疏自编码器（SAE）表征的行为组合性研究
authors:
- Haotian Ma
- Ziye Mei
- Frederic Sala
affiliations:
- University of Wisconsin–Madison, Department of Computer Sciences
arxiv_id: '2610.21261'
url: https://arxiv.org/abs/2610.21261
pdf_url: https://arxiv.org/pdf/2610.21261
published: '2026-10-14'
collected: '2026-10-17'
category: LLM
direction: 大模型可解释性 · SAE表征组合性
tags:
- SAE
- Sparse Autoencoder
- Compositionality
- Feature Interaction
- Model Interpretability
one_liner: 提出SAR指标衡量SAE特征高阶交互未解释行为偏差，验证SAE坐标组合性更优但仍需考虑交互项
practical_value: '- 做生成式推荐的用户/物品特征拆解时，可引入SAR指标衡量低阶特征组合的误差边界，避免盲目假设特征加性独立，减少组合干预的效果偏差

  - 用SAE做LLM4Rec的特征对齐时，优先保留一阶特征效果的同时补充少量二阶交互项，即可在参数成本可控的前提下大幅提升表征拟合度

  - 做Agent意图识别/工具调用的特征可解释性分析时，可复用本文的随机旋转基准对比方法，验证学习到的稀疏特征的组合有效性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
SAE广泛用于LLM激活拆解、可解释性分析、特征干预，但现有应用默认特征效果可加性叠加，未量化高阶交互对下游行为的影响，也未验证SAE学习到的坐标是否比随机子空间更具组合性。

### 方法关键点
1. 提出SAE Additivity Residuals (SAR)指标，量化指定交互阶数以上未解释的行为变异，可作为低阶近似的联盟排序误差上界；
2. 设计和同子空间保和随机旋转的对比实验，分离SAE表征本身的组合性和下游计算带来的组合性；
3. 对比一阶、二阶、三阶特征交互的拟合效果。

### 关键结果数字
1. 18组不同模型和行为设置下，SAE学习到的坐标一阶残差显著低于随机旋转基准；
2. 所有设置下二阶交互项均可提升留出集联盟排序效果，优于参数匹配的随机三阶项模型；
3. 特征干预实验中，加入二阶建模将秩保真度从0.5874提升至0.7790，排序误差从0.1444降至0.0606。
