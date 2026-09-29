---
title: 'PReCache: Efficient KV Cache Sharing for Multi-LoRA Agents via Low-Rank Precomputation
  and Neutral Reconstruction'
title_zh: PReCache：基于低秩预计算与中性重建的多LoRA Agent KV缓存共享方案
authors:
- Hyesung Jeon
- Hyeongju Ha
- Jae-Joon Kim
affiliations:
- Seoul National University
arxiv_id: '2609.34054'
url: https://arxiv.org/abs/2609.34054
pdf_url: https://arxiv.org/pdf/2609.34054
published: '2026-09-27'
collected: '2026-09-29'
category: MultiAgent
direction: 多Agent推理 · KV cache 优化
tags:
- KV cache
- LoRA
- Multi-Agent
- LLM Inference
- Serving Optimization
one_liner: 免训练兼容现有LoRA适配器，极小精度损失下大幅降低多Agent场景KV缓存冗余与重复prefill开销
practical_value: '- 多角色电商Agent（导购/客服/售后）共享底座时可复用LR cache预计算逻辑，每个角色LoRA无需重复处理历史上下文，能大幅降低TTFT，提升用户体验

  - 单流式端侧Agent部署选lazy prefill调度，服务端高并发多Agent场景用double batching调度，两种调度无需修改现有LoRA适配器即可落地

  - 若对精度要求极高优先选ReBaseShared，平均仅1.1%精度损失；对性能敏感优先选PreLRShared，最高可获3.1×TTFT加速、2.3×吞吐量提升

  - 共享base cache+低秩LR cache的存储结构可大幅降低长对话多Agent场景的显存开销，适合长上下文电商咨询、多轮导购等场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多LoRA Agent系统通过共享底座模型实现角色定制，是电商导购、智能客服、多轮推荐Agent的主流部署方案，但每个Agent需要独立处理不断增长的共享上下文、构建专属KV缓存，带来极高的内存与计算冗余；现有KV缓存共享方案要么需要额外训练、架构改造，要么直接复用其他Agent缓存导致角色特异性效果下降，还无法消除重复prefill开销。

### 方法关键点
- 整体免训练兼容现有LoRA适配器，将KV cache拆分为公共base cache和轻量agent专属低秩（LR）cache
- PreLRShared：新上下文首次处理时，预计算所有Agent的LR cache，后续Agent无需重新处理历史上下文即可直接调用自己的LR cache
- ReBaseShared：用无适配器的中性隐藏状态重建共享base cache，消除base cache对上一个Agent的依赖，进一步降低精度损失
- 适配两种部署场景：单流推理用lazy prefill调度，在当前Agent结束后统一做中性重建；并发服务用double batching调度，将适配路径和无适配器路径合并进连续服务批次消除排队延迟

### 关键实验
在HotpotQA、ScienceQA数据集上，基于LLaMA-3.1-8B、Ministral-8B，对比NonShared、FullShared、各类选择性重计算、BaseShared等baseline：PreLRShared单流推理下最高3.1×TTFT加速、2.3×吞吐量提升；ReBaseShared平均精度仅比无缓存共享低1.1个百分点，与BaseShared精度相当；两者峰值显存仅比FullShared高2%，比选择性重计算方案低17~23%。

### 最值得记住的一句话
多LoRA Agent场景下KV缓存共享无需改造现有LoRA即可实现，仅通过低秩预计算和中性重建就能同时兼顾精度、速度、显存三者的最优平衡。
