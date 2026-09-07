---
title: 'RegionFed: Federated Learning for Personalized Query Understanding in Heterogeneous
  Retail Environments'
title_zh: RegionFed：异构零售场景下面向个性化查询理解的联邦学习框架
authors:
- Quoc H. Nguyen
- Ali Lafzi
- Abhijeet Phatak
- Siddharth Pratap Singh
- Rohit Upadhyay
- Yogananda Domlur Seetharama
- Chittaranjan Tripathy
affiliations:
- Walmart Global Tech
arxiv_id: '2609.05403'
url: https://arxiv.org/abs/2609.05403
pdf_url: https://arxiv.org/pdf/2609.05403
published: '2026-09-04'
collected: '2026-09-07'
category: QueryRec
direction: 联邦学习 · 零售查询理解个性化
tags:
- Federated Learning
- Query Understanding
- Transformer
- Differential Privacy
- E-commerce Search
one_liner: 基于梯度冲突的架构鲁棒联邦学习框架，解决Transformer上参数级个性化FL的灾难性崩溃问题
practical_value: '- Transformer上做联邦学习优先选梯度级操作而非参数级修改，可避免tied embedding、LayerNorm带来的训练崩溃，无需改模型代码就能适配T5、RoBERTa等不同架构

  - 跨境/多区域电商的query理解任务可复用梯度冲突（L2距离）作为个性化强度的自适应控制信号，兼顾全局知识共享与区域语义差异（比如同个词不同地区语义不同的问题）

  - 多区域联邦训练可搭配梯度冲突做策略路由：数据充足、冲突低的区域用轻量Grad策略降本，冲突高的区域用Meta策略提准，平衡算力与效果

  - 对隐私要求高的用户query场景，可复用其DP兼容的梯度处理方案，ε≈0.6的差分隐私下仅损失不到1pp的准确率'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
跨境/多区域零售搜索存在显著的区域query语义、消费偏好差异，传统联邦学习（FL）要么全局模型牺牲区域效果，要么参数级个性化FL在Transformer上因共享嵌入、LayerNorm交互出现灾难性崩溃（准确率<10%），同时隐私合规要求不能集中存储用户敏感query数据，亟需架构鲁棒的个性化FL方案。

### 方法关键点
- 三层架构：全局服务器维护共享参数，区域coordinator基于梯度冲突计算个性化权重，客户端仅上传DP加噪梯度、本地做用户级微调
- 梯度级个性化：用区域梯度与全局梯度的L2冲突作为唯一信号，自适应控制区域/用户两级的个性化强度α，避免参数级修改带来的Transformer不稳定问题
- 动态策略路由：根据梯度冲突、区域异质性、数据量自动选择Grad/Interp/Meta策略，算力开销最低仅为FedAvg的1.02倍
- 差分隐私兼容：梯度裁剪加噪后仅泄露聚合统计信息，ε≈0.6下满足隐私要求

### 关键实验
在Amazon ESCI零售query数据集、Amazon Reviews、FEMNIST上验证，对比FedAvg、FedProx、SCAFFOLD、FedTP等基线：RegionFed-Meta在T5-Small上准确率达92.27%，与违反隐私的集中式训练上限（92.04%）差距仅0.23pp，比FedAvg高12.09pp；参数级基线在Transformer上全部崩溃到<10%准确率，跨T5-3B、RoBERTa、CNN架构均稳定涨点，高异质性场景下效果退化仅为FedAvg的1/3。

### 核心结论
Transformer上做联邦个性化，梯度级操作比参数级修改的架构兼容性、稳定性高一个数量级。
