---
title: 'CopyLoop: Fast Looped Transformer Decoding via Context Copying and Shallow
  Screening'
title_zh: CopyLoop：基于上下文复制与浅层筛选的循环Transformer快速解码
authors:
- Wenyu Du
- Stephen Chung
affiliations:
- DualverseAI
arxiv_id: '2610.38822'
url: https://arxiv.org/abs/2610.38822
pdf_url: https://arxiv.org/pdf/2610.38822
published: '2026-10-28'
collected: '2026-10-30'
category: LLM
direction: 大语言模型推理加速 · 循环Transformer解码
tags:
- Looped_Transformer
- Decoding_Acceleration
- Speculative_Decoding
- Training_Free
one_liner: 训练免的循环Transformer解码算法，结合上下文拷贝与浅层筛选，最高提速10.7倍
practical_value: '- 电商/广告长文案生成、多轮Agent推理这类有重复上下文的生成任务，可直接集成CopyLoop替代原生AR解码，无需额外训练即可获得2.74~10.7倍推理提速

  - 部署时可复用轻量校准策略：仅针对所用Looped Transformer架构校准1次浅层筛选深度ds，拷贝尾长K直接用通用默认值（Base模型6、Thinking模型2）即可，跨任务性能损失不超过10%

  - 短响应场景（生成结果<64token，如query改写、短推荐理由）下CopyLoop固定开销会抵消收益，不建议使用；长响应（>128token）场景收益最高'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Looped Transformer通过共享Transformer块重复计算，可在不增加参数量的前提下提升模型性能，但每个token需完成全部循环步才能启动下一个token生成，解码延迟随循环深度线性增长；现有自推测解码方案仍需逐token生成草稿，受限于串行解码开销，亟需更高效的无训练加速方案。

### 方法关键点
- 块构造：将模型预测的首token与历史上下文匹配到的最长重复后缀拼接，组成多token候选块，无匹配时回退为单token块
- 浅层筛选：候选块统一推进到指定浅层深度ds，逐token和前序token的浅层预测对比，仅保留最长匹配前缀，错误后缀直接释放KV缓存
- 并行流水线：保留的token继续向全深度推进的同时，用筛选后的最后一个token的浅层预测作为下一个候选块的首token，新块直接进入流水线无需等待前序块完成全深度校验
- 全深度校验：token到达全深度后再次做因果校验，按顺序提交正确token，丢弃不匹配的分支

### 关键实验
在Ouro、Raven、Huginn家族的6个Looped Transformer checkpoint（含Base和Thinking模型）上测试，覆盖代码生成、数学推理任务，对比AR、PLD、LoopSpec、WaveFront四个基线，Base模型相对AR解码提速2.98×~10.70×，Thinking模型提速2.74×~3.52×，14/16个Base配置、8/8个Thinking配置性能超过所有基线。

### 核心结论
CopyLoop的核心收益来自浅层筛选和连续调度的协同效应，仅在长响应、存在大量可复用重复上下文的生成场景下能最大化提速收益。
