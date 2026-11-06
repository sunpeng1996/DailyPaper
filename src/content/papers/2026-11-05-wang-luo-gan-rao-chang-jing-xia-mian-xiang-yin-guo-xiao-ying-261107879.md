---
title: Network Effect Decomposition for Causal Effect Estimation under Network Interference
title_zh: 网络干扰场景下面向因果效应估计的网络效应分解方法
authors:
- Zhirong Huang
- Wenzhen Zhang
- Guangquan Lu
- Boyan Chen
- Debo Cheng
- Shichao Zhang
arxiv_id: '2611.07879'
url: https://arxiv.org/abs/2611.07879
pdf_url: https://arxiv.org/pdf/2611.07879
published: '2026-11-05'
collected: '2026-11-06'
category: Other
direction: 因果效应估计 · 网络干扰消除
tags:
- Causal Inference
- Network Interference
- Effect Estimation
- Observational Data
- Potential Outcomes
one_liner: 提出NEDNet分解个体与邻域因果响应路径，显著降低网络干扰下因果估计的PEHE误差
practical_value: '- 社交电商/好友裂变场景的效果评估可借鉴双路径拆分思路，分离用户自身干预效应与邻域曝光效应，避免SUTVA假设失效带来的偏差

  - 存在用户社交关联/流量溢出的A/B实验中，可参考参考归一化分解方法校准组间对比结果，提升实验结论可信度

  - 好友推荐/社群营销效果归因时，可引入路径专属邻域上下文建模，更精准拆分个体转化与社交传播的贡献'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有网络观测数据因果估计方法通常联合建模个体干预与邻域暴露变量，响应组件隐式不可解释，且网络干扰会导致SUTVA假设失效，估计误差高。
### 方法关键点
1. 提出NEDNet架构，将条件输出参数化为预处理基线、个体干预响应、邻域暴露响应三条独立路径
2. 为两条响应路径注入路径专属的邻域上下文预处理信息
3. 采用参考归一化分解方法，等效于零混合干预-暴露对比，保证分解唯一可解释
### 关键结果
在BlogCatalog、Flickr半合成基准数据集上，无论同质响应还是协变量异质响应场景，NEDNet的个体效应、同伴效应、总效应的PEHE均为所有对比方法最低
