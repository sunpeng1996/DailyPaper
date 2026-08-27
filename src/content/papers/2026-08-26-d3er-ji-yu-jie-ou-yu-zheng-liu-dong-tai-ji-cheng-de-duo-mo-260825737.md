---
title: 'D3ER: Supporting Multi-Modal Recommendation via Disentangle and Distillation-based
  Dynamic Ensemble'
title_zh: D3ER：基于解耦与蒸馏动态集成的多模态推荐方法
authors:
- Bingnan Wang
- Yi Li
- Xiongxin Tang
- Fanjiang Xu
- Jiangmeng Li
affiliations:
- Institute of Software, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
arxiv_id: '2608.25737'
url: https://arxiv.org/abs/2608.25737
pdf_url: https://arxiv.org/pdf/2608.25737
published: '2026-08-26'
collected: '2026-08-27'
category: RecSys
direction: 多模态推荐 · 特征解耦与集成优化
tags:
- Multimodal Recommendation
- Feature Disentanglement
- Gradient Boosting
- Knowledge Distillation
- Ensemble Learning
one_liner: 首次将蒸馏增强的梯度Boosting引入多模态推荐，解耦模态同质异质信息，较SOTA最高提升7.58%的Recall@50
practical_value: '- 多模态特征解耦可直接复用：电商场景商品图文特征可通过「实例级InfoNCE+分布级Wasserstein距离对齐」方案，拆分跨模态共享信息（如商品品类、核心卖点）和单模态独有信息（如面料文字描述、版型视觉特征），提升特征区分度

  - 多模型集成优化Trick：替代传统联合训练方式，采用梯度Boosting交替训练不同信息对应的子模型，每个子模型专注拟合上一轮累积模型的残差，可显著提升对冷启动用户偏好的捕捉效果

  - 梯度Boosting工程优化方案：通过知识蒸馏将多轮历史模型的知识蒸馏到单一累积模型，无需存储所有历史模型权重，仅增加少量训练开销，推理速度与原backbone持平，可直接嵌入现有推荐pipeline

  - 调参参考：特征解耦的对齐损失权重、单模态独有信息的分离阈值可在论文给出的范围（αc/αw:1e-4~1e-1，dm:0.01~10）内通过网格搜索适配业务场景，平衡特征相关性与信息量'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态推荐方法普遍联合学习跨模态共享的模态同质信息（HOI）与单模态独有的模态异质信息（HEI），会稀释两类信息对不同用户样本的预测偏好，导致表征区分度下降，实验验证独立训练两类信息的效果显著优于联合训练，亟需适配样本级偏好的高效集成策略。

### 方法关键点
- 特征组件解耦（FCD）模块：通过2个MLP分别提取各模态的共享、独有特征，结合实例级InfoNCE损失与分布级Wasserstein距离实现跨模态共享特征对齐，再通过L2距离约束同模态共享与独有特征分离，无需额外标注即可完成无监督解耦。
- 知识蒸馏增强梯度Boosting（KDBoost）模块：为HOI、视觉HEI、文本HEI分别训练子模型，每轮随机选择子模型拟合上一轮累积模型的损失负梯度（残差），再通过知识蒸馏将多轮子模型知识合并到单一累积模型，加入全局校正正则缓解Boosting固有的局部最优问题。
- 训练流程：先预训练FCD模块10 epoch，再用KDBoost交替优化子模型50 epoch，推理仅需调用累积模型打分排序。

### 关键结果
在Amazon Baby、Sports、Clothing三个公开多模态推荐数据集上，对比15个SOTA基线，接入MGCN、DiffMM、PGL等主流backbone时，Recall@50最高提升7.58%，NDCG@50最高提升6.28%，推理开销与原backbone持平。

### 核心启示
多模态特征并非融合得越早越全越好，先解耦不同类型信息再针对性动态集成，可更好适配不同用户的偏好差异。
