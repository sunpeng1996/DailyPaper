---
title: 'DNA: Unlocking Depth Scaling in CTR Models'
title_zh: DNA：解锁CTR预测模型的深度缩放能力
authors:
- Caiyuan Li
- Wenjie Wu
- Yuheng Huang
- Xiao Zhou
- Silu Zhou
- Ke Chen
- Zinan Zhao
- Xinrui Zeng
- Hanmo Xu
- Chaoqun Song
affiliations:
- Alibaba Group
arxiv_id: '2611.25659'
url: https://arxiv.org/abs/2611.25659
pdf_url: https://arxiv.org/pdf/2611.25659
published: '2026-11-19'
collected: '2026-11-20'
category: RecSys
direction: CTR预估 · 长用户行为序列建模
tags:
- CTR Prediction
- Long User Behavior
- Cross Attention
- Depth Scaling
- Search Ranking
one_liner: 提出双流联结注意力DNA，让用户行为序列随请求动态更新，破解CTR模型深度堆叠增益衰减难题
practical_value: '- 架构上可复用DNA的请求-序列双向交互设计，将序列更新、KV投影全部放到请求侧执行，多候选共享结果，单候选推理成本和同深度CrossAttn几乎无差

  - 多行为序列场景下无需将不同类型行为（点击/加购/购买）合并到统一时间线，通过请求表征作为枢纽实现跨组信息交互，大幅降低序列预处理复杂度

  - 遇到深度堆叠cross-attention增益衰减问题时，无需盲目加层，优先引入请求感知的序列更新机制，可用更少FLOPs获得更高AUC增益，比如DNA-4仅用40%
  FLOPs就超过28层CrossAttn

  - 部署时可拆分请求侧与候选侧计算逻辑，请求侧预计算所有共享资源，候选侧仅执行轻量cross-attention读取，无缝适配现有推荐排序的批推理框架'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业CTR模型堆叠cross-attention层处理长用户行为序列时增益快速衰减，淘宝搜索场景下16层升到28层仅带来0.02pt AUC提升。核心瓶颈是每一层都读取固定的原始行为序列，新增层仅优化查询侧，无法让行为表征随当前请求和深度动态演化；现有序列更新方案要么不感知请求、要么无法跨候选共享、要么复杂度随序列长度二次增长，无法满足工业落地要求。
### 方法关键点
- 双流架构：拆分候选专属F流、请求共享U流和行为序列S流，每一层先让U流和F流分别通过cross-attention读取当前S流表征
- 请求感知序列更新：前D-1层新增Update Block，以更新后的U流为KV、S流为Query做cross-attention，让每个行为token融合当前请求信息，更新后的S流供下一层读取
- 多行为组适配：不同行为组保留独立投影，无需合并到统一时间线，通过U流作为枢纽实现跨组信息交互，复杂度随序列长度线性增长
- 推理优化：U流和S流的更新、KV投影全在请求侧执行一次，所有候选共享，单候选仅需执行F流的cross-attention读取
### 关键实验
基于淘宝搜索曝光日志测试，基线为不同深度的CrossAttn堆叠模型：
- 相同FLOPs下，DNA比CrossAttn高0.08~0.26pt AUC，DNA-4仅用40% FLOPs就超过28层CrossAttn
- 在线A/B测试对比生产2层CrossAttn模型，CTR提升0.8%，GMV提升0.5%
- 单请求候选数达5000时，DNA-4推理成本和4层CrossAttn几乎一致，远低于同效果的10层CrossAttn
> 最值得记住的结论：cross-attention堆叠的增益瓶颈不在查询侧优化，而在让行为序列表征随当前请求动态演化，请求级共享的序列更新可以用极低的增量成本换得大幅效果提升。
