---
title: Generalized Gibbs Ensemble Weighting for Forecast Combination
title_zh: 用于预测集成的广义吉布斯系综加权方法
authors:
- Prasen R. Nuthanakaluva
- Nava K. Gaddam
affiliations:
- Independent Researcher, Oxford, UK
- Utrecht University, Utrecht, Netherlands
arxiv_id: '2608.28116'
url: https://arxiv.org/abs/2608.28116
pdf_url: https://arxiv.org/pdf/2608.28116
published: '2026-08-28'
collected: '2026-08-31'
category: Other
direction: 预测集成 · 自适应加权框架
tags:
- Forecast Combination
- Ensemble Learning
- Gibbs Weighting
- Online Learning
- UCB
one_liner: 提出基于归一化预测损失吉布斯变换的集成加权框架GGEW，支持在线自适应调参适配多样部署场景
practical_value: '- 电商需求预测、推荐多排序模型融合场景可复用GGEW的归一化损失指数加权逻辑，替代简单平均/逆损失加权baseline，提升集成鲁棒性

  - 在线服务场景可复用Local-UCB自适应调参机制，无需全量网格搜索即可动态适配超参数，降低在线计算开销

  - 多专家Agent任务结果融合时，可引入多样性感知分数修正项，避免性能相近的专家权重冗余，提升融合效果'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有预测集成规则（均值、逆损失加权等）的效果随数据集、预测窗口、部署场景、基模型分歧度波动大，缺乏灵活自适应的通用加权方案。
### 方法关键点
1. 构建GGEW概率框架，将基预测模型视为专家，对归一化预测损失做吉布斯指数变换生成集成权重，新增数值稳定、多样性感知分数修正、在线超参适配三个扩展模块；
2. 衍生出Stable Gibbs、Directional Gibbs-NCL等多个变体，核心算法一致，仅指数加权规则内的分数不同；
3. 在线部署采用Local-UCB bandit机制，动态调整学习率、多样性强度、方法变体，无需每步做全量超参数网格搜索。
### 关键结果
在M4竞赛官方提交结果、交通小时级/电力小时级/太阳能周级时序数据集上验证，吉布斯式自适应加权在多个基准场景下性能具备竞争力，适配性优于传统集成基线，无通用绝对优势。
