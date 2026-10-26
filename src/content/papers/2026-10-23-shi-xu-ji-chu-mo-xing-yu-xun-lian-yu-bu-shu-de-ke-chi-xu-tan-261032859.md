---
title: 'Sustainability of TSFM Deployment and Pretraining: From Carbon Footprint Analysis
  to Mitigation via Pruning'
title_zh: 时序基础模型预训练与部署的可持续性：碳足迹分析及剪枝优化
authors:
- Cécile Luc
- Nathanaël Lemonnier
- Ievgen Redko
affiliations:
- Schneider Electric
arxiv_id: '2610.32859'
url: https://arxiv.org/abs/2610.32859
pdf_url: https://arxiv.org/pdf/2610.32859
published: '2026-10-23'
collected: '2026-10-26'
category: Training
direction: 时序大模型训练部署效率优化
tags:
- TSFM
- Carbon Footprint
- Model Pruning
- Zero-shot Forecasting
- Deployment Efficiency
one_liner: 量化TSFM全生命周期碳成本，提出无梯度剪枝方案降本几乎无损零-shot性能
practical_value: '- 大模型选型可复用全生命周期成本核算逻辑：高请求量场景预训练大模型可快速摊销成本，低流量场景选用定期重训的小模型ROI更高

  - 大模型部署轻量化可借鉴无梯度剪枝方案：裁剪7%-8%的冗余encoder块，可实现6%-9%的延迟、算力成本下降，几乎不损失下游零-shot性能

  - 可将算力/碳成本纳入搜索推荐大模型上线评估指标，平衡效果和长期运营成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
Time Series Foundation Models (TSFM) 零-shot时序预测能力优异，但预训练前期投入成本高，全生命周期的成本收益对比需定期重训的任务专属监督模型缺乏量化评估，同时TSFM部署阶段的低成本优化方案也存在缺口。
### 方法关键点
1. 构建工业场景下的累计碳成本核算框架，对比TSFM与传统监督模型的全生命周期投入；
2. 采用无梯度剪枝准则移除TSFM冗余encoder块，无需额外训练即可降低模型部署成本。
### 关键结果数字
- 大流量/高频查询部署场景下，Chronos-2的预训练成本可在数月内摊销完成，长期成本优于传统模型；小流量/低频查询场景下传统模型长期成本始终更低；
- 裁剪7.9%参数（单个encoder块）可稳定降低6~9%的FLOPs、碳排放、推理延迟，在25个零-shot预测任务基准上性能几乎无损失。
