---
title: A unified framework for global and local interpretability using adaptive derivative-ordered
  random explanation
title_zh: 基于自适应导数阶随机解释的全局与局部可解释性统一框架
authors:
- Lemen Chao
- Ming Lei
- Anran Fanga
affiliations:
- School of Information Resource Management, Renmin University of China
- Key Laboratory of Data Engineering and Knowledge Engineering
arxiv_id: '2609.17171'
url: https://arxiv.org/abs/2609.17171
pdf_url: https://arxiv.org/pdf/2609.17171
published: '2026-09-15'
collected: '2026-09-16'
category: Other
direction: 可解释AI · 黑盒模型解释框架
tags:
- XAI
- Interpretability
- Black-box Model
- Randomized SVD
- Open-source
one_liner: 提出统一全局与局部可解释性的ADORE方法，效果优于LIME、SHAP，已开源Python包
practical_value: '- 可直接调用开源ADORE包替代LIME/SHAP，用于推荐/广告排序模型的特征重要性分析、Bad Case归因，对非线性特征交互的建模能力更强

  - 全局+局部统一解释的思路可复用：既可输出全量特征重要性排序指导特征迭代，也可对单用户推荐结果做个性化归因，支撑可解释推荐需求

  - 随机SVD+动态稀疏检测的优化技巧可迁移到高维稀疏电商特征的分析场景，大幅降低大规模特征下的解释计算开销'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有事后可解释方法存在分析流程碎片化、非线性特征交互建模能力不足、计算效率低、强依赖特定模型架构的问题，无法同时覆盖全局特征重要性分析与单样本局部解释两类需求。
### 方法关键点
提出ADORE统一解释框架：
1. 利用一阶、二阶导数适配非线性模型复杂度，在同一框架内捕捉特征-样本交互
2. 融合全局特征重要性与局部样本贡献，同时量化特征影响的幅度与方向，可识别影响模型决策的关键样本
3. 引入随机SVD与动态稀疏检测优化计算效率，可支撑高维大规模数据集的解释需求
### 关键结果
在表格、文本、图像三类模态数据集上实验，ADORE的复杂交互处理能力、计算效率均优于LIME、SHAP，已开源Python包可直接调用。
