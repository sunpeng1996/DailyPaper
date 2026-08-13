---
title: Redistribution-based Cost Inference Improves Sparse Safe Offline RL
title_zh: 基于重分配的成本推理优化稀疏安全离线强化学习
authors:
- Ebenezer Gelo
- Geraud Nangue Tasse
- Steven James
- Benjamin Rosman
affiliations:
- University of the Witwatersrand
arxiv_id: '2608.12306'
url: https://arxiv.org/abs/2608.12306
pdf_url: https://arxiv.org/pdf/2608.12306
published: '2026-08-12'
collected: '2026-08-13'
category: Agent
direction: 安全离线强化学习 · Agent训练
tags:
- Offline RL
- Safe RL
- Temporal Credit Assignment
- Cost Inference
- CMDP
one_liner: 提出RCI框架将轨迹级稀疏停止反馈转化为稠密步级成本，提升离线RL安全性能
practical_value: '- 推荐/广告系统的会话级负反馈场景（如用户中途退会、跳转跳出）可借鉴RCI的信用分配思路，将会话级稀疏负信号拆解为步级成本，优化召回/排序模型的负样本标注质量，降低人工标注成本

  - 电商合规策略训练（如广告投放限流、敏感内容拦截）可复用RCI的回报等价重分配理论，在保证策略可行集无损失的前提下，仅用违规终止类的稀疏标签即可完成约束策略训练

  - 离线训练的导购Agent、对话推荐Agent可引入该方法，仅用会话终止类的粗粒度反馈即可学习安全合规约束，无需高成本的单轮对话级标注'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
安全离线RL默认依赖稠密步级成本标注，实际场景仅能获取轨迹级稀疏停止反馈（首次不安全转移时的二元信号，无步级归因），高成本的稠密标注无法规模化落地。

### 方法关键点
1. 将稀疏标注问题转化为时间信用分配问题，RCI框架通过回报分解将稀疏停止反馈转化为稠密步级成本，再基于增强数据集训练约束离线策略
2. 理论证明回报等价重分配可保留CMDP的可行策略集和最优拉格朗日量，变换无理论损失，同时优化成本critic的学习条件

### 关键结果
在高速驾驶、机械臂操作任务上，违规率显著低于稀疏基线与分类器基线，对异构数据集、标签噪声具备鲁棒性
