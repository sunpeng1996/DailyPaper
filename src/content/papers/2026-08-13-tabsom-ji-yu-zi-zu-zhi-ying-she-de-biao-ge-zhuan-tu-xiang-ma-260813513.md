---
title: 'TabSOM: A tabular-to-image encoding method based on self-organizing maps'
title_zh: TabSOM：基于自组织映射的表格转图像编码方法
authors:
- David Chushig-Muzo
- María Ángeles Rodríguez de Cara
- Eva Milara
- Francisco J. Lara-Abelenda
- Luis Zhinin-Vera
- Diego H. Peluffo-Ordóñez
arxiv_id: '2608.13513'
url: https://arxiv.org/abs/2608.13513
pdf_url: https://arxiv.org/pdf/2608.13513
published: '2026-08-13'
collected: '2026-08-14'
category: Other
direction: 表格数据编码 · 多模态转换
tags:
- Tabular Encoding
- Self-Organizing Map
- CNN
- Interpretability
- Multimodal Conversion
one_liner: 基于SOM实现兼顾特征交互与可解释性的表格转图像编码，性能优于12种现有方案
practical_value: '- 电商/推荐场景的用户、商品、行为特征多为表格型，可借鉴TabSOM思路将结构化特征转图像后喂给ViT/CNN类模型做CTR、CVR预估，补充现有DNN的特征交互挖掘能力

  - 可复用SOM+匈牙利分配的无碰撞特征空间布局方法，解决UMAP、t-SNE等传统降维方法做特征映射时的位置冲突问题

  - 自带的类别区分度特征重要性评分可直接复用做推荐特征筛选，无需额外跑SHAP、XGBoost做特征归因，降低特征分析成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有表格转图像方法仅编码单特征边际值，丢弃特征间关联信息，基于降维的特征映射易出现位置冲突，同时缺乏配套可解释性工具，限制了CV类高性能模型在表格数据场景的落地。
### 方法关键点
基于自组织映射(SOM)构建TabSOM编码框架：
1. 采用SOM分量平面+无碰撞匈牙利分配算法，为每个输入特征分配固定画布位置，避免降维映射的位置冲突
2. 生成双层多尺度图像通道：一层编码固定尺度的特征值，另一层编码特征间pairwise交互的空间关联
3. 配套两套可解释工具：原型启发的部分依赖图、类别区分度特征重要性评分
### 关键结果
- 在公开二分类数据集上对比12种现有表格转图像方法，所有数据集上性能排名前2，且是所有参评方法中方差最低的
- 自带的类别区分度特征重要性评分与XGBoost、SHAP等基线结果一致性高，同时能捕捉额外的输入数据结构信息
