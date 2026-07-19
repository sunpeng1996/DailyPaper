---
title: 'cGAP: Generalized Association Plots with HOMALS-Guided Heatmaps for Visualization
  of High-Dimensional Categorical Data'
title_zh: cGAP：结合HOMALS引导热图的高维分类数据可视化广义关联图
authors:
- Chun-houh Chen
- Shun-Chuan Chang
- Chiun-How Kao
- Yi-Ju Lee
- Shang-Ying Shiu
- Yin-Jing Tien
- ShengLi Tzeng
- Han-Ming Wu
affiliations:
- Institute of Statistical Science, Academia Sinica
- Department of Statistics, National Taipei University
- Holistic Education Center, Mackay Medical University
- Department of Statistics and Data Science, Tamkang University
- Institute for Information Industry
arxiv_id: '2607.15018'
url: https://arxiv.org/abs/2607.15018
pdf_url: https://arxiv.org/pdf/2607.15018
published: '2026-07-16'
collected: '2026-07-19'
category: Other
direction: 高维分类数据可视化框架设计
tags:
- Data Visualization
- Categorical Data
- High Dimensional Data
- HOMALS
- Heatmap
one_liner: 提出结合HOMALS嵌入的高维分类数据可视化框架cGAP，保留原始数据同时提升可解释性
practical_value: '- 电商用户标签、商品属性等高维分类特征的探索性分析，可复用HOMALS嵌入转RGB热图的方法，快速发现特征聚集、异常值，比普通热图可解释性更强

  - 特征重要性验证、用户分群效果校验场景，可引入cGAP的三类联动视图（原始数据热图、样本邻近矩阵、变量邻近矩阵），降低特征工程试错成本

  - Seriation算法重排热图行列的思路可迁移到用户行为序列、商品关联规则的可视化呈现，帮助运营快速捕捉业务规律'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
高维分类数据（标签、属性、二值特征等）广泛存在于各领域，现有可视化方法普遍存在扩展性差、低维投影与原始数据脱节、重预测轻可解释性的问题。

### 方法关键点
1. 提出cGAP可视化框架，支持标称、序数、二值三类分类数据，保留原始数据矩阵同时加入可解释几何结构；
2. 用HOMALS将样本和类别嵌入3D欧氏空间，映射为RGB坐标，相似模式对应相似颜色；
3. 整合三类联动视图：HOMALS引导的原始数据热图、样本邻近矩阵、变量邻近矩阵，用Seriation算法重排行列揭示聚类、异常值和全局-局部结构；
4. 理论证明重心可追溯、投影失真、对比度保留三大特性，保障嵌入到可视化的映射可信。

### 关键结果
在学生分类、哺乳动物牙型、UCI蘑菇数据集、同源基因簇数据集上验证效果，可实现可视化结构与原始分类观测的完全可追溯，支持透明的探索性分析。
