---
title: 'Foresight: planning future perception in streaming VLMs without retraining'
title_zh: Foresight：无需重训的流式视觉语言模型未来感知规划框架
authors:
- Ashok Prasad Neupane
- Dipan Bartaula
- Ankit Belbase
- Saugat Adhikari
- Samip Ghimire
- Saroj Poudel
- Binod Bhattarai
- Danda Pani Paudel
affiliations:
- Independent Researcher
- NAAMII, Nepal
- University College London, UK
- University of Aberdeen, UK
- INSAIT, Sofia University
arxiv_id: '2610.03123'
url: https://arxiv.org/abs/2610.03123
pdf_url: https://arxiv.org/pdf/2610.03123
published: '2026-10-02'
collected: '2026-10-05'
category: Multimodal
direction: 多模态VLM · 流式推理架构优化
tags:
- VLM
- streaming inference
- KV cache
- training-free
- proactive inference
one_liner: 提出无需重训的流式VLM主动感知框架，性能超需训练SOTA且接近实时
practical_value: '- 双流共享KV缓存的架构可直接复用在直播电商实时Agent场景，比如用户实时交互触发的商品推荐、弹幕回复助手，无需微调基座，大幅降低落地成本

  - 动态调整采样帧率+按需过滤无关视觉token的技巧，可迁移到长视频/直播内容的理解召回链路，低价值时段降低采样率减少30%+的计算开销

  - 带滞回阈值+ refractory interval的触发防抖策略，可直接用在推荐系统实时事件触发场景，比如用户实时行为触发的个性化push、券发放，大幅降低误触率

  - 无需训练的规划推理范式，适合业务端快速上线轻量多模态Agent，无需收集标注数据做微调，需求响应周期从天级降到小时级'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有流式VLM均为被动响应已到达的输入，计算路径固定无法适配动态场景变化，要么需要额外微调适配流式场景，要么采用固定采样策略浪费算力，在主动响应类实时交互场景（如直播助手、实时监控）表现不佳。
### 方法关键点
- 采用Siamese双LLM架构，共享权重、输入编码器与KV缓存：Ingest LLM持续处理流入token，作为唯一写入方更新KV缓存，无阻塞；Think LLM只读缓存快照，异步规划未来计算，不干扰主感知链路
- 每次规划输出包含三类信息：下次推理时间、待校验的任务目标、到下次推理前的采样帧率，同时支持动态配置KV缓存压缩、视觉token保留/忽略类别
- 采用diff增量更新计划，仅解码变化的配置字段，配合轻量执行器实现微秒级动态重配置，全程冻结基座无需任何微调
### 关键实验
以冻结的Qwen3-VL-8B为基座：①OmniPro Online主动响应任务joint F1达23.0，比最强需训练基线MiniCPM-o 4.5高9.5%；②StreamingBench整体准确率66.0%，达到SOTA；③OVO-Bench比原生基座提升15.4个点，证据晚出现的Forward场景增益最高达18.7个点，推理速度接近实时。
> 最值得记住的结论：大模型的预判能力最有价值的用法不是输出预测结果，而是用来指导自身未来的计算资源分配。
