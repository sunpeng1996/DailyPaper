---
title: Conformal Selection for Hierarchical Streaming Data
title_zh: 面向分层流数据的共形选择方法
authors:
- Zhenyuan Sun
- Chengyao Yu
- Ruixing Ming
- Bingyi Jing
affiliations:
- Peking University
- Southern University of Science and Technology
- Zhejiang Gongshang University
- The Chinese University of Hong Kong, Shenzhen
- Shenzhen Loop Area Institute
arxiv_id: '2611.26328'
url: https://arxiv.org/abs/2611.26328
pdf_url: https://arxiv.org/pdf/2611.26328
published: '2026-11-19'
collected: '2026-11-21'
category: Other
direction: 共形推断 · 分层流数据FDR控制
tags:
- Conformal Selection
- Streaming Data
- False Discovery Rate
- Hierarchical Data
- Online Decision Making
one_liner: 提出无分布的分层流数据在线选择方法OHS与OHSF，满足任意时刻的FDR控制要求
practical_value: '- 电商/广告流排序场景中，可借鉴OHS的组间/组内e-value构造方法，对不同类目/人群分层的候选流做FDR控制，降低误推荐率

  - 带用户反馈的在线召回/选品场景，可复用OHSF的反馈迭代逻辑，在保证FDR约束的前提下提升优质候选召回率

  - 流数据covariate shift场景下的决策逻辑可直接迁移，适配电商大促、节假日等分布偏移的业务场景'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有在线共形选择框架依赖i.i.d./可交换数据假设，无法适配分层结构流数据（如不同类目商品流、多来源广告候选流），核心挑战是分层结构下逐候选构造有效统计量。
### 方法关键点
1. 提出无分布的在线分层选择方法OHS，分别为组间、组内样本构造基于秩的e-value，将平均e-value输入在线e-BH流程实现候选选择；
2. 扩展得到带反馈版本OHSF，利用响应反馈提升选择效力；
3. 可泛化到协变量偏移、效应相关响应选择等场景。
### 关键结果
理论上在温和的分层可交换性和数据到达假设下，任意时刻均可实现FDR控制，模拟及真实数据集实验均验证了方法有效性。
