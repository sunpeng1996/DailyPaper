---
title: Learning Collective Dynamics with Differentiable Gaussian Representations
title_zh: 基于可微高斯表示的群体行为动态学习
authors:
- Jianxiang Ma
- Mingfu Zhang
- Xiaocui Yang
- Yichen Gao
- Junzhao Huang
- Yuesong Hou
affiliations:
- OranAI
- OranAI Ltd.
- Northeastern University School of Computer Science and Engineering
arxiv_id: '2609.28405'
url: https://arxiv.org/abs/2609.28405
pdf_url: https://arxiv.org/pdf/2609.28405
published: '2026-09-23'
collected: '2026-09-24'
category: RecSys
direction: 群体行为预测 · 可微高斯建模
tags:
- Collective Dynamics
- Gaussian Mixture Model
- Differentiable Modeling
- User Behavior Prediction
- Temporal Modeling
one_liner: 提出可微高斯动态模型DGD，从聚合数据学习群体异质性与反馈机制，提升群体行为预测精度
practical_value: '- 可复用DGD的高斯混合建模思路，从平台聚合行为数据学习用户群体异质性响应倾向，替代人工划分用户分群的规则

  - 可引入可微聚合+反馈循环的架构，用于电商大促、内容平台热点等场景的群体行为趋势预测，优化备货/流量调度策略

  - 重参数化积分+时序递归的联合训练范式，可迁移到聚合数据监督的用户分布建模任务，避免依赖细粒度个体行为标签'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
从聚合行为计数数据学习群体动态，需同时关联群体响应分布、当前观测与未来行为，现有方法难以同时兼顾异质性建模、可微训练与反馈机制刻画。
### 方法关键点
提出Differentiable Gaussian Dynamics (DGD)框架，核心包含三个组件：1）高斯混合建模异质性响应倾向；2）接触强度与行为概率的可微聚合模块；3）更新后续响应的反馈递归结构；通过重参数化积分与时序递归，仅用聚合预测误差即可联合训练分布、观测函数和反馈参数。
### 关键结果
在KuaiRand-Pure、Online Retail II 4个数据窗口上，DGD联合行为负对数似然优于带联合行为头的DeepAR适配版本；Retail 2010数据集上1天行为计数MAE为4.71，较基线6.88降低31.5%；相比固定高斯，学习分布在KuaiRand标准推荐窗口下行为负对数似然相对降低10.82%；移除反馈动态会使受控实验联合KL从0.0340升至0.2577。
