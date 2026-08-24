---
title: Conditional-Independence-Regularized Distributional Autoencoders for Mixed-Type
  Data
title_zh: 面向混合类型数据的条件独立正则化分布自编码器
authors:
- Siyuan Tang
- Gongjun Xu
- Ji Zhu
affiliations:
- University of Michigan
arxiv_id: '2608.20562'
url: https://arxiv.org/abs/2608.20562
pdf_url: https://arxiv.org/pdf/2608.20562
published: '2026-08-20'
collected: '2026-08-24'
category: Other
direction: 混合类型数据表示学习框架
tags:
- Representation Learning
- Autoencoder
- Mixed-type Data
- Regularization
- Generative Modeling
one_liner: 针对数值+类别混合数据，提出带条件独立正则的分布自编码器，兼顾分布恢复与异质变量依赖
practical_value: '- 电商用户/物品混合特征embedding建模时，可复用「数值特征用energy score、类别特征用似然」的分类型损失设计，提升异构特征表示质量

  - 特征融合阶段可引入条件独立正则项，约束embedding同时捕捉数值与类别特征间的依赖关系，减少异构特征信息损失

  - 该方法生成的高质量混合特征数据可用于推荐模型冷启动数据增强，补充稀缺的小流量用户/长尾物品特征样本'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有混合类型（数值+类别）数据的表示学习与生成建模方法，通常仅关注重建精度或无条件生成，无法同时完整恢复数据条件分布、保留异质变量间的可解释结构关系，难以满足电商、广告等场景混合特征的高质量表示需求。

### 方法关键点
1. 条件独立正则化分布自编码器框架通过条件分布匹配+结构正则学习低维表示；
2. 数值变量采用energy-score-based目标函数，类别变量采用似然目标函数，差异化优化异构特征建模；
3. 新增辅助条件独立正则项，引导学习到的表示捕捉数值与类别成分间的依赖关系，理论上可证明最优表示能平衡数值未解释方差、类别条件熵与残差条件依赖三类目标。

### 关键结果
在合成与真实数据集上，类别分布恢复效果显著提升，整体条件分布恢复性能达竞争水平，同时可完整保留混合类型变量的依赖结构。
