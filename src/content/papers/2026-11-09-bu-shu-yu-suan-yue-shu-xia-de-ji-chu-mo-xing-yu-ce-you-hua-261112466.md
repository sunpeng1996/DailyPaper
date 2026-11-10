---
title: Prediction with Foundation Models under Deployment Budgets
title_zh: 部署预算约束下的基础模型预测优化框架
authors:
- Zhaohui Xu
- Xiaofei Xu
- Doudou Zhou
affiliations:
- National University of Singapore
- Wuhan University
arxiv_id: '2611.12466'
url: https://arxiv.org/abs/2611.12466
pdf_url: https://arxiv.org/pdf/2611.12466
published: '2026-11-09'
collected: '2026-11-10'
category: Training
direction: 成本可控 · 多模型输出融合与动态路由
tags:
- cost-aware-learning
- model-routing
- foundation-model
- ensemble-learning
- Q-learning
one_liner: 提出两类预算可控的基础模型输出融合方法，兼顾预测精度与平均查询成本
practical_value: '- 电商商品定价、多模态内容理解等多模型融合场景，可复用ACES-T的分支定界搜索法，固定预算下快速选择最优模型组合，避免遍历所有子集的算力浪费

  - 输入异质性强的业务场景（如电商商品详情完整度差异大、用户Query歧义度差异大）可落地ACES-I的动态路由逻辑，用Q-learning判断是否追加调用更高成本的大模型，在平均成本约束下提升预测精度

  - 离线训练阶段可先全量调用所有候选模型得到标注样本，再学习路由策略，避免线上试错成本，完全适配大模型API按调用量付费的业务模式'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
当前基础模型调用存在显著成本差异：商用API按次收费、本地部署算耗相差可达3个数量级，直接调用全量模型成本过高，单模型精度不足；现有融合方法未考虑部署预算约束，也未针对不同输入动态调整调用模型，无法平衡成本与预测精度。
### 方法关键点
- ACES-T：为所有输入调用固定的最优模型组合，通过分支定界搜索在所有预算内的模型子集中快速选择风险最低的组合，联合拟合基础模型输出与原生特征的线性权重，修正模型偏置、利用不同模型的输出互补性
- ACES-I：为不同输入动态选择调用模型，通过反向Q-learning学习「停止查询/调用下一个模型」的决策逻辑，用拉格朗日乘子控制平均查询成本，通过交叉拟合避免过拟合，最终在验证集上选择符合预算的最优路由策略
### 关键实验
覆盖仿真场景与亚马逊笔记本价格预测数据集，对比Zero-Query、Single-Query、FSP、SRE等基线：
- 仿真场景1（固定最优模型组合适配所有输入）：ACES-T在1/4成本下接近全量调用的精度，MSE低至0.275
- 仿真场景2（输入异质性高）：ACES-I比ACES-T的MSE低37.6%
- 电商价格预测任务：ACES-T仅用全量调用60%的成本就达到与其几乎一致的log-RMSE（0.318），精度显著优于所有基线
### 核心结论
最值得记住的结论：预算约束下，多个单独精度不高的低/中成本模型的互补融合收益，往往远高于调用单一高成本大模型
