---
title: 'Lights, Camera, Carbon: Architectural Scaling Laws for Video Generation Energy
  Consumption'
title_zh: 视频生成能耗的架构缩放定律与无侵入式能效评估框架
authors:
- Nidhal Jegham
- Boris Gamazaychikov
- Sasha Luccioni
affiliations:
- University of Rhode Island
- Sustainable AI Group
arxiv_id: '2607.04553'
url: https://arxiv.org/abs/2607.04553
pdf_url: https://arxiv.org/pdf/2607.04553
published: '2026-07-05'
collected: '2026-07-12'
category: Eval
direction: 多模态生成模型能耗评估与缩放定律研究
tags:
- Text-to-Video
- Energy Consumption
- Scaling Law
- Sustainable AI
- Diffusion Model
one_liner: 提出无需访问模型权重的双向框架，可精准预测文生音视频模型的推理能耗
practical_value: '- 电商生成式商品短视频广告选型时，可复用该框架估算不同文生视频模型的推理能耗，无需访问私有模型权重即可快速完成成本对比

  - 大模型推理服务调度系统可复用该无侵入式能耗估算思路，结合生成分辨率、时长参数快速预估单请求成本，优化资源分配

  - 生成式内容推荐业务可直接套用该缩放公式，快速核算单条生成内容的能耗成本，辅助生成策略的ROI管控'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
文生视频/文生音视频模型逐步在电商广告、内容生成场景落地，现有能耗评估方法需访问模型权重、参数等内部信息，缺乏跨架构通用的标准化评估方案，无法支撑能效对比与成本管控。
### 方法关键点
基于视频扩散模型计算绑定的特性，设计双向评估逻辑：正向仅通过分辨率、时长等可观测生成参数+架构第一性原理预测能耗；反向通过观测推理时间反推架构缩放行为，以精度作为架构有效性判定标准。能耗可拆解为二次项+线性项的组合，项系数直接对应底层架构复杂度，全程无需访问模型内部信息。
### 关键结果
在8.3B~27B参数区间的6个开源模型、3种GPU配置上验证，所有架构下的能耗预测MAPE低于3%，可作为文生视频模型可持续性基准的标准化评估框架。
