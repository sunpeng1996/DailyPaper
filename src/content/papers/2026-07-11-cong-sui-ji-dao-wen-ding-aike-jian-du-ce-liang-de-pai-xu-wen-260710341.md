---
title: 'From Stochastic to Stable: Rank Stability and Structural Sufficiency in AI
  Visibility Measurement'
title_zh: 从随机到稳定：AI可见度测量的排序稳定性与结构充分性
authors:
- Ronald Sielinski
affiliations:
- IQRush
arxiv_id: '2607.10341'
url: https://arxiv.org/abs/2607.10341
pdf_url: https://arxiv.org/pdf/2607.10341
published: '2026-07-11'
collected: '2026-07-14'
category: Eval
direction: 生成式搜索可见度 · 评估框架
tags:
- generative search
- AI visibility
- rank stability
- convergence framework
- evaluation methodology
one_liner: 提出结合排序稳定性与结构充分性的AI可见度测量收敛框架，自动判定数据采集停止时机
practical_value: '- 做生成式搜索SEO/站外流量投放时，可复用该双判据框架评估自身域名在生成式搜索结果的排名稳定性，避免基于少量采样错误判断投放效果

  - 搭建推荐/搜索链路的效果评估体系时，可借鉴该无需预设采集量的收敛判定方法，自动停止实验数据采集，节省算力和时间成本

  - 多平台/多场景的排序效果对比实验中，可参考结构充分性判据区分「排序稳定」和「结论可落地」两个状态，降低决策误判率'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
生成式搜索的AI可见度测量缺乏科学的数据采集量判定标准，现有固定预算采样得到的排名稳定性、精度未知，无法支撑可靠的业务决策。

### 方法关键点
提出无需预设查询量、相关系数阈值、置信区间宽度阈值的序列收敛框架，双判据互补：
1. 排序稳定性：判断排序相关系数轨迹是否达到结构平台期
2. 结构充分性：判断已确立域名（置信区间不含0）的引用份额离散度是否高于估计不确定性
仅依赖观测到的引用分布规律（排序结构、不确定性分布、观测/已确立域名边界）驱动停止决策。

### 关键结果
在Gemini、SearchGPT、Perplexity共30组平台-话题组合上验证，框架可自适应不同平台/话题的引用分布，证明不存在跨场景通用的固定采集预算，收敛性可直接通过观测分布结构判定。
