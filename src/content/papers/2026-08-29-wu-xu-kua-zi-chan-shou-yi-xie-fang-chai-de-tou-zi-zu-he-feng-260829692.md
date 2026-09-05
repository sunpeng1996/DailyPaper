---
title: 'Portfolio Risk Bounds without Cross-Asset Return Covariances: Distributional
  Fields from Language-Model Representations'
title_zh: 无需跨资产收益协方差的投资组合风险边界：基于大模型表征的分布场
authors:
- Marcus Gawronsky
- Chun-Sung Huang
affiliations:
- University of Cape Town
arxiv_id: '2608.29692'
url: https://arxiv.org/abs/2608.29692
pdf_url: https://arxiv.org/pdf/2608.29692
published: '2026-08-29'
collected: '2026-09-05'
category: Other
direction: 投资组合风险管控 · LLM表征应用
tags:
- Portfolio Risk
- Wasserstein Distance
- LLM Embedding
- Robust Allocation
- Distributional Fields
one_liner: 用LLM表征的企业分布特征，实现无需跨资产协方差的投资组合风险上界计算与低波动配置
practical_value: '- 做多品类营销预算分配、多广告位组合收益波动管控时，可借鉴Wasserstein距离的分布特征计算风险上界，避免高维场景下跨对象协方差估计难、噪声大的问题

  - 商品/商家的风险管控场景可复用基于文本embedding（评价、舆情、新闻等）的分布特征构建逻辑，替代部分难以获取的交叉统计指标

  - 短周期、高维组合的决策优化场景可参考本文的凸松弛目标设计，降低小样本下统计量估计误差带来的决策偏差'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
传统投资组合风险评估依赖跨资产收益协方差，在短周期、高维面板场景下协方差估计噪声大、参数维度高，难以支撑可靠的资产配置决策。

### 方法关键点
1. 基于企业级分布型特征，通过多企业Wasserstein-2散度推导系统性投资组合方差的严格上界，无需跨资产协方差，仅需边际波动率规模；
2. 加权 pairwise 松弛得到可检验凸性的优化目标，归一化资产配置仅依赖观测的信息几何特征，不受公共映射尺度影响；
3. 输入采用Qwen3-Embedding-8B提取的企业新闻文本表征作为分布特征来源。

### 关键结果
2018-2022年52家企业面板测试中，基于大模型表征的配置方案在4个预设上限投资组合群体的样本内方差百分位处于0.69-1.33区间，远优于等风险加权基线的21.1-28.6百分位，不同冻结LLM表征均一致优于基线。
