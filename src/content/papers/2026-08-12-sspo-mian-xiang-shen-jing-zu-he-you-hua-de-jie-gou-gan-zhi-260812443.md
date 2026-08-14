---
title: 'SSPO: Structure-Aware Similarity-Weighted Preference Optimization for Neural
  Combinatorial Optimization'
title_zh: SSPO：面向神经组合优化的结构感知相似度加权偏好优化
authors:
- Yuanyu Li
- Jintao Xu
- Zijiang Liu
- Yongzhi Qi
- Ningxuan Kang
- Jianshen Zhang
- Wei Qi
- Chen Xie
- Zuo-Jun Max Shen
affiliations:
- 京东供应链技术团队Y
- 清华大学工业工程系
- 香港大学
arxiv_id: '2608.12443'
url: https://arxiv.org/abs/2608.12443
pdf_url: https://arxiv.org/pdf/2608.12443
published: '2026-08-12'
collected: '2026-08-14'
category: Training
direction: 神经组合优化 · 偏好优化训练
tags:
- Neural Combinatorial Optimization
- Preference Optimization
- Training Strategy
- Supply Chain
- SSPO
one_liner: 提出结构感知相似度加权偏好优化算法SSPO，解决NCO训练两类缺陷，已落地京东生产级设施选址系统
practical_value: '- 偏好优化类训练（如RLHF、NCO训练）可引入结构感知相似度加权策略，对差异大的样本分配更高权重，同时缓解梯度极化、基线冗余问题，降低训练方差

  - 可复用零参数方案：直接基于编码器已有节点表征构造自适应样本嵌入，无需额外增加模型参数即可提升训练效果

  - 电商供应链类组合优化业务（仓配选址、路径规划、资源调度）可直接替换原有RLOO等训练方法，落地成本低收益明确'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
神经组合优化（NCO）现有训练方法存在两类核心缺陷：偏好优化类仅锚定单最优解，丢弃其余样本的细粒度质量与结构信号，导致梯度信号极化；均值基线类对所有采样样本均匀加权，结构相似样本引入大量冗余信息，梯度方差居高不下。
### 方法关键点
提出SSPO，通过异质性加权的留一基线对所有采样解联合打分，给结构差异更大的解分配更高权重，在同一机制下同时解决两类缺陷；基线采用零参数、问题自适应的解嵌入方案，直接复用编码器已有节点表征，无额外参数开销。
### 关键结果
在TSP、EFL、JSP三类基准任务上效果全面优于此前最优的锚定基线、均匀加权基线；对照实验验证结构感知加权是效果提升的核心驱动因素；基于SSPO训练的EFL策略已落地京东生产级设施选址系统，验证大规模工业可用性。
