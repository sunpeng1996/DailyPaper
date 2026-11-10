---
title: 'OptiCover: A Scalable and Multi-Surface Framework for Cold-Start Visual Optimization
  under Semantic Constraints'
title_zh: OptiCover：语义约束下支持多场景的可扩展冷启动视觉优化框架
authors:
- Guillaume Guy
- Mihajlo Grbovic
- Joe Mills
- Selen Uguroglu
- Liwei He
- Pratiksha Kadam
- Nalini Kartha
- Qian Aria Li
affiliations:
- Airbnb
arxiv_id: '2611.12727'
url: https://arxiv.org/abs/2611.12727
pdf_url: https://arxiv.org/pdf/2611.12727
published: '2026-11-09'
collected: '2026-11-10'
category: RecSys
direction: 多模态推荐 · 冷启动视觉优化
tags:
- CLIP
- VLM
- ColdStart
- VisualMerchandising
- ABTest
one_liner: 面向民宿平台的冷启动封面图优化框架，支持语义约束与多场景适配，已落地Airbnb生产环境
practical_value: '- 冷启动物料优化可采用「冻结CLIP+轻量任务头+后校准」的低成本方案，无需全量微调大模型即可实现亿级物料低延迟打分，适配大流量业务场景

  - 物料优化必须增设语义校验环节，用VLM做跨模态接地验证，对比物料内容与商品结构化属性、文本描述，避免仅优化点击率导致的素材误导用户，长期损害平台信任

  - 小流量探索阶段采用ε=0.1的ε-greedy策略收集无偏样本，冷启动阶段优先用离线预训练的点击率模型做exploit，效果优于汤普森采样，待样本积累后再切换bandit策略

  - 跨场景迁移可复用高置信度底层模型，比如首页训练的点击率模型可直接冷启动搜索场景，再结合搜索上下文（如筛选条件）做候选集过滤，能更快拿到转化收益'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
电商平台商品封面图直接影响用户点击与转化，但多数平台由商家自主选择静态封面，存在三大痛点：90%以上新上传物料无交互标签，冷启动问题严重；不同场景（首页、搜索）用户偏好差异大，静态封面无法适配；高点击率素材可能存在语义误导（如民宿封面放周边景点而非实际房屋），损害用户体验。Airbnb每天新增数十万张房源图片，静态封面的低效导致大量潜在收益流失。

### 方法关键点
- 视觉打分模块：基于冻结的SigLIP-2 backbone加轻量MLP头，同时训练合规校验、语义属性、点击率预测多任务，embedding用int8量化压缩至原大小的1/4，支持亿级图片低延迟打分；点击率预测采用pairwise排序损失，后用单调样条做校准，不破坏排序效果的前提下实现点击率预估校准。
- 候选生成：从历史封面、人工标注高潜素材、语义相似高潜素材等维度扩充候选集，扩大优化空间。
- 语义校验：用GPT-4o-mini做跨模态接地校验，对比图片内容与房源文本描述、结构化属性，过滤非代表性误导素材，召回率达98%。
- 在线探索模块：采用ε=0.1的ε-greedy策略收集无偏交互数据，冷启动阶段优先用离线预训练的点击率模型做exploit。

### 关键实验
在线做3组A/B测试，对照组为商家自主选择的静态封面：首页场景3周1000万用户测试，engagement提升1.5%；搜索非上下文版本2周1000万用户测试，点击率提升0.32%但预订量无显著提升；搜索上下文版本（仅对带筛选条件的请求生效）6周100万用户测试，预订量显著提升0.35%，对应数百万美元年增量收入。

### 核心结论
物料优化中，动作空间的质量与语义约束的有效性，是比单纯提升点击率预测精度更重要的转化提升驱动因素
