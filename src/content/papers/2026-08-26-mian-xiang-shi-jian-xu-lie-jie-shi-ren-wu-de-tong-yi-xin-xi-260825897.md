---
title: Towards A Unified Information Bottleneck Framework for Time Series Explanations
title_zh: 面向时间序列解释任务的统一信息瓶颈框架
authors:
- Xu Zheng
- Zichuan Liu
- Zhuomin Chen
- Mayur Akewar
- Janki Bhimani
- Jason Liu
- Mo Sha
- Jingchao Ni
- Wei Cheng
- Dongsheng Luo
arxiv_id: '2608.25897'
url: https://arxiv.org/abs/2608.25897
pdf_url: https://arxiv.org/pdf/2608.25897
published: '2026-08-26'
collected: '2026-08-27'
category: Other
direction: 时序可解释性 · 信息瓶颈融合框架
tags:
- Time Series
- Explainable AI
- Information Bottleneck
- Attribution
- Counterfactual
one_liner: 基于信息瓶颈原理提出统一时序解释框架，同时输出可信归因与稳定反事实解释
practical_value: '- 时序类推荐（用户行为序列归因、复购预测解释）可复用该框架的归因+反事实统一思路，同时定位影响决策的核心行为区间与反事实调优方案

  - 信息瓶颈约束防止平凡解的思路可迁移到推荐解释生成任务，避免生成无意义的噪声解释

  - 需反事实解释的业务场景（广告投放效果归因、策略调优）可借鉴参数化变换网络设计，提升反事实结果稳定性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有时间序列解释方法分归因、反事实两类独立研究路线，前者缺失因果验证，后者稳定性差易输出类对抗噪声，且两类方法均易得到平凡解、对分布偏移敏感。

### 方法关键点
基于信息瓶颈原理设计统一目标函数，打通归因与反事实推理链路；提出TimeX++框架，通过参数化变换网络生成嵌入解释的样本，保留的信息输出归因解释，可控移除的信息生成稳定反事实解释，显式约束避免平凡解与分布外反事实。

### 关键结果
在合成数据集与真实基准数据集上，较SOTA基线在归因可信度、反事实稳定性两类指标上均取得一致最优表现。
