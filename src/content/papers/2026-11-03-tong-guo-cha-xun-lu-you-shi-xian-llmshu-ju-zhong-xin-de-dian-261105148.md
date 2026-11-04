---
title: Creating Power Flexibility in Datacenters via Query Routing
title_zh: 通过查询路由实现LLM数据中心的电力需求灵活性调控
authors:
- Shivam Patel
- Bingqing Chen
- Jared Fernandez
- Guannan Qu
- Gauri Joshi
affiliations:
- Carnegie Mellon University
- Bosch Center for AI
- Cornell University
arxiv_id: '2611.05148'
url: https://arxiv.org/abs/2611.05148
pdf_url: https://arxiv.org/pdf/2611.05148
published: '2026-11-03'
collected: '2026-11-04'
category: LLM
direction: LLM推理服务 · 能耗优化调度
tags:
- LLM inference
- query routing
- power optimization
- datacenter scheduling
- GPU serving
one_liner: 提出基于查询路由的LLM集群功耗调控框架，无需延迟请求即可实现最高16%总功耗调整
practical_value: '- 可复用论文提出的线性功耗预测模型，基于查询长度、并发度快速估算不同规格LLM实例的功耗，用于推理集群的资源规划和成本核算

  - 多规格LLM混合部署场景，可借鉴查询分类+动态路由的逻辑，在保证返回质量的前提下将简单请求路由到小模型，降低推理成本同时响应电网削峰需求

  - 电商大促等流量波动场景，可复用请求-功耗映射关系，动态调整路由策略平衡服务SLO、推理成本和能耗约束

  - 推理服务调度层可复用请求合并思路：将请求集中到少数实例运行，降低空闲实例的功耗浪费，优化整体能效'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM推理算力需求爆发推动AI数据中心功耗快速增长，预计2030年美国数据中心功耗占总用电量比例可达9.5~15.3%，对电网稳定运行造成巨大压力。现有功耗调控方案多依赖延迟训练、离线推理等非实时任务，无法适配交互式LLM推理的低延迟SLO要求，亟需无需丢包、无需延迟请求的电力灵活调控手段。

### 方法关键点
- 建立LLM推理全链路解析模型：线性拟合token迭代时间、请求驻留时间、吞吐量与请求并发度的关联关系，H100平台下预测误差低于6%
- 提出并发度关联的功耗估算模型：拆分idle固定功耗和动态功耗，可直接通过查询到达率估算集群总功耗，单GPU场景中位RMSE仅5.2W
- 设计查询分类路由调控框架：将查询分为大模型专属、小模型专属、可灵活路由三类，通过调整灵活查询的路由比例，在满足各模型池容量约束下实现功耗动态调整

### 关键实验结果
- 单GPU验证覆盖1B~70B参数模型、4类GPU平台，功耗灵活性估算平均绝对百分比误差仅2.8%
- 10000卡H100集群仿真基于Azure一周真实LLM请求trace，全灵活查询场景下可实现最高16%（1.19MW）的总功耗调整，90%目标功耗调整可在10秒内完成
- GPU可用率降至75%时仍可保留大部分功耗调控能力，鲁棒性优异

### 核心结论
在多规格LLM混合部署的推理集群中，查询路由是兼顾服务质量、推理成本与电力灵活性的低代价调控手段。
