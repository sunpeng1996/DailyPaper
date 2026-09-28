---
title: Depth-adaptive Inference of Looped Language Models via Continuous Depth Batching
title_zh: 基于连续深度批处理的循环语言模型深度自适应推理框架
authors:
- Kristian Schwethelm
- Daniel Rueckert
- Georgios Kaissis
affiliations:
- Technical University of Munich
- Imperial College London
- Munich Center for Machine Learning
- Hasso Plattner Institute, University of Potsdam
arxiv_id: '2608.09444'
url: https://arxiv.org/abs/2608.09444
pdf_url: https://arxiv.org/pdf/2608.09444
published: '2026-09-24'
collected: '2026-09-28'
category: LLM
direction: 循环语言模型 · 推理效率优化
tags:
- LoopedLM
- InferenceOptimization
- KV Cache
- ContinuousBatching
- EarlyExit
one_liner: 首个端到端实现循环LM的连续深度批处理 最高达99%理论加速比
practical_value: '- 业务侧使用循环LM部署Agent、商品文案生成、推荐理由生成服务时，可直接复用CDB调度框架，在不损失精度的前提下最高提升1.5x吞吐，降低推理成本

  - 可直接复用异步调度+前瞻门的工程trick，将GPU idle时间从10%降至0.5%左右，适合高并发电商/推荐场景的LLM在线服务降延迟提吞吐

  - 自研循环LM适配业务场景时，尽量压缩prelude、coda等非循环边界层的参数量，边界层开销越小，CDB的加速效果越接近理论上限

  - 深度感知共享KV cache设计可直接复用，能将循环核KV内存降低至原来的1/rmax，提升单卡可承载的并发请求数'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
循环语言模型（Looped LM）支持深度自适应推理，对简单token减少循环次数、复杂token增加循环次数，可显著降低计算量，但不同循环次数的token无法复用标准连续批处理的统一前向传播，计算节省难以转化为实际推理速度提升；此前的连续深度批处理（CDB）仅停留在理论模拟阶段，调度开销大，实际运行速度甚至低于固定深度批处理。

### 方法关键点
- 分阶段调度：将推理流程拆分为prefill、prelude、循环核、coda四个独立队列，支持refill（动态补全空闲batch槽位）和no-refill两种模式，通过最小coda批大小K平衡边界层执行效率与循环核batch大小
- 深度感知KV cache：支持last-exited（退出时复制最终KV状态到剩余槽位）和shared（每循环步覆写单KV槽位）两种设计，兼容paged attention，shared cache可将循环核KV内存降低为原来的1/rmax
- 异步调度+前瞻门：提前一个循环步预判token退出状态，将GPU idle时间从10.27%降至0.56%，几乎消除调度开销

### 关键实验
在单张H100上测试Ouro 1.4B（全循环架构）、Huginn 3.5B（50%Transformer层在边界），数据集覆盖Alpaca、ShareGPT、ArXiv，对比基线为标准连续批处理CB：
- Ouro上refill模式最优，吞吐达到CB的1.32~1.53x，实现理论加速上限的96%~99%
- Huginn上no-refill模式最优，吞吐达到CB的1.30~1.37x，实现理论加速上限的83%~96%
- 线上serving场景下，CDB可承载更高请求率，相同延迟下吞吐量提升显著

### 核心结论
循环LM的深度自适应推理效率需要架构与调度协同设计，非循环边界层开销越小，越容易接近理论加速上限
