---
title: Interpretable AI with Local Distillation
title_zh: 面向可解释AI的局部蒸馏方法
authors:
- Erin Craig
- Yiling Huang
- Snigdha Panigrahi
affiliations:
- Department of Biostatistics, University of Michigan
- Department of Statistics, University of Michigan
arxiv_id: '2608.23538'
url: https://arxiv.org/abs/2608.23538
pdf_url: https://arxiv.org/pdf/2608.23538
published: '2026-08-24'
collected: '2026-08-25'
category: Other
direction: 可解释AI · 局部蒸馏建模
tags:
- InterpretableAI
- Distillation
- LocalRegression
- Lasso
- Stability
one_liner: 通过黑盒教师引导局部正则化线性学生模型，兼顾高精度与单样本级可解释性
practical_value: '- 推荐/广告排序模型可解释性优化可复用该框架：针对单个请求蒸馏出局部稀疏线性模型，快速定位影响决策的核心特征，满足合规/风控的解释需求

  - 用户/商品亚群挖掘可借鉴其扰动重训+聚类思路：对局部蒸馏后的模型做聚类，挖掘特征权重模式一致的群体，比全局规则粒度更准

  - 小样本场景可参考伪观测锚定方法：用已有大模型的预测结果作为加权伪样本，降低局部模型在小样本下的拟合波动'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有黑盒模型（如Tabular Foundation Model、GBDT）精度远高于传统方法，但可解释性缺失，无法满足高风险决策场景的透明性要求；传统局部线性建模存在局部范围难定义、解释工具有限的痛点。
### 方法关键点
提出局部蒸馏框架，用黑盒教师模型指导每个查询点的正则化线性学生模型训练：
1. 教师模型基于预测结果相似度给训练样本加权定义局部范围，同时将查询点的教师预测作为伪观测点锚定拟合，权重可从数据自动估计
2. 解释层面向局部目标加入小高斯扰动后重训，用特征选择频率判断单样本可靠特征，聚类扰动后的拟合结果挖掘全局稳定亚群，lasso惩罚下已证明特征选择概率的稳定性
### 关键结果
17个基准数据集上精度几乎追平教师模型，同时每个测试点输出稀疏线性可解释模型；癌症基因表达数据集上成功捕捉到全局线性模型和黑盒模型无法发现的、特征使用异质的患者亚群
