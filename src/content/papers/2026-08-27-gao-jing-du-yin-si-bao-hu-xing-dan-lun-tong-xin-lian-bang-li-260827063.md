---
title: An Accurate and Single-Communication Federated Inference Algorithm
title_zh: 高精度隐私保护型单轮通信联邦推理算法
authors:
- Laura Montagnani
- Anthony CC Coolen
- Marianne A Jonker
affiliations:
- Donders Institute, Radboud University, Netherlands
- Saddle Point Science Europe, Netherlands
- Research Institute for Medical Innovation, Radboud university medical center, Netherlands
arxiv_id: '2608.27063'
url: https://arxiv.org/abs/2608.27063
pdf_url: https://arxiv.org/pdf/2608.27063
published: '2026-08-27'
collected: '2026-08-30'
category: Training
direction: 联邦学习 · 单轮隐私推理
tags:
- Federated Learning
- Privacy Preserving
- Taylor Expansion
- One-shot Inference
- Distributed Computing
one_liner: 采用三阶泰勒展开优化单轮联邦推理的对数似然近似，提升小样本场景推理精度
practical_value: '- 跨商家/跨域隐私联合推荐场景，可复用单轮通信联邦架构，大幅降低跨机构交互的通信成本与合规风险

  - 冷启动、小众品类等小样本联合建模场景，可尝试用三阶泰勒展开替代常用的二阶近似，提升对数似然拟合精度

  - 边缘侧节点算力受限的联邦推荐任务，可借鉴该无迭代方案，降低参与方的算力门槛'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
多机构联合分析在生物医学、跨域联合建模等场景需求强烈，但隐私监管要求禁止原始个体数据共享；现有迭代式联邦学习通信成本高，基于二阶泰勒展开的单轮联邦推理在小样本场景下无法捕捉对数似然的偏度等高阶特征，精度不足。
### 方法关键点
仅需参与节点与协调服务器完成1次汇总统计量交互即可完成推理，全程不共享原始数据；采用三阶泰勒展开替代原有二阶近似方案，更精准地拟合局部对数似然函数的高阶特征。
### 关键结果
小样本场景下，相比现有二阶近似单轮联邦推理方案，精度显著提升，同时保留隐私性、通信效率与可扩展性，效果接近中心化建模。
