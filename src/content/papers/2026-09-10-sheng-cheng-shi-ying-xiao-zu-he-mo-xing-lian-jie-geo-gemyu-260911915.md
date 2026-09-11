---
title: 'Generative Marketing Mix Modeling: A Causal Inference Framework Linking GEO
  and GEM to Business Impact'
title_zh: 生成式营销组合模型：连接GEO/GEM与业务影响的因果推断框架
authors:
- Masahiro Kato
- Daiki Honma
- Taka Kato
affiliations:
- The University of Tokyo
- Mizuho-DL Financial Technology Co., Ltd.
- NP-hard
arxiv_id: '2609.11915'
url: https://arxiv.org/abs/2609.11915
pdf_url: https://arxiv.org/pdf/2609.11915
published: '2026-09-10'
collected: '2026-09-11'
category: Other
direction: 生成式营销 · GEO/GEM因果归因
tags:
- Causal Inference
- Marketing Mix Modeling
- GEO
- GEM
- Bayesian Inference
one_liner: 提出生成式营销组合模型GMMM，可量化GEO与GEM两类生成式渠道的业务因果效应
practical_value: '- 做生成式搜索下的GEO/GEM效果评估时，可复用GMMM的曝光计算逻辑：将品牌/商品在生成式回答中的出现概率、对应query量级、生成系统市占率、用户注意概率相乘得到有效曝光量，替代传统曝光日志统计，解决非付费自然曝光无日志的问题

  - 生成式营销的效果建模可复用MMM的经典carryover（滞后效应）+Hill（饱和效应）变换，无需从零设计响应函数，且直接从业务数据估计变换参数比固定经验值的效果更好，系数向量RMSE可降低约21.7%

  - 若已有成熟MMM基建，可直接把GEO/GEM作为新增渠道纳入现有框架，无需重构全链路，仅需补充新增渠道的有效曝光计算模块即可，成本低可快速落地'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
生成式AI普及后，传统Marketing Mix Modeling (MMM) 无法衡量GEO（生成式引擎优化）和GEM（生成式引擎营销）的业务效果：自然露出无曝光日志，付费占位也无法统计用户是否注意到品牌/商品信息，导致两类新营销投入的ROI无法量化。

### 方法关键点
- 针对GEO：统计不同query、大模型下品牌的回答出现概率，乘以对应query分市场量级、大模型市占率、用户注意概率，得到GEO有效曝光量
- 针对GEM：将投入金额映射为付费露出量，乘以用户注意概率得到GEM有效曝光量
- 两类有效曝光与传统渠道一致，经过carryover滞后变换、Hill饱和变换后输入响应模型，支持贝叶斯推断融合随机实验结果校正效应
- 给出GEO/GEM因果效应可识别的充分条件，解决多渠道交互、滞后效应下的效应识别问题

### 关键结果
实验基于GPT-4o、GPT-5.6 Luna生成的2240条中英文产品推荐回答，结合模拟业务数据验证：对比固定变换参数的plug-in方法，从业务数据估计carryover和Hill参数可将系数向量RMSE从1.207降至0.945（降幅21.7%）；GEO效应估计的RMSE最低可达5.91%，95%置信区间覆盖率稳定在95%左右，效果接近Oracle基准。

### 核心结论
生成式营销效果评估的核心是把大模型回答中的出现概率转化为与传统渠道可比的有效曝光量，复用成熟MMM因果框架即可低成本落地
