---
title: 'LatComm: Reusable Context Compression for Latent Communication between Large
  Language Models'
title_zh: LatComm：面向大语言模型间隐态通信的可复用上下文压缩
authors:
- Huawei Lin
- Jinting Liu
- Tan Yu
- Weijie Zhao
affiliations:
- Rochester Institute of Technology
- NVIDIA
arxiv_id: '2610.26840'
url: https://arxiv.org/abs/2610.26840
pdf_url: https://arxiv.org/pdf/2610.26840
published: '2026-10-19'
collected: '2026-10-20'
category: LLM
direction: LLM跨模型通信 · 上下文压缩
tags:
- Context Compression
- LLM Communication
- Inference Optimization
- Multi-Agent
- RAG
one_liner: 提出跨冻结LLM的可复用隐态通信接口，大幅降低多query场景重复计算开销
practical_value: '- 多Agent系统通信优化：电商导购/客服多Agent场景中，相同商品/用户上下文只需被编码一次，跨不同角色LLM（商品理解Agent、需求匹配Agent等）复用压缩包，可降低3×以上多query推理耗时，同时减少跨模型token传输成本

  - RAG系统性能优化：推荐/搜索场景的RAG召回的同一篇商品详情、用户评价、活动规则等长文本，编码为固定大小的LatComm包后，多用户/多query场景下无需重复编码，接收器LLM输入token减少57×，同时保留高于单向量基线的准确率

  - 端云协同推荐适配：边缘小模型+云端大模型的分层推荐架构中，可基于LatComm实现跨模型族的上下文传递，无需暴露模型权重，仅需训练少量接口参数即可完成大模型压缩上下文到小模型的信息传递，适配端侧低算力场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多LLM协作（多Agent、RAG、端云协同推荐等）场景中，同一份上下文（商品详情、用户画像、活动规则）常需响应多个query，直接传递文本会导致接收LLM重复处理上下文token，现有压缩/隐态通信方案无法同时满足可复用、固定大小、跨不同LLM可读三个核心需求，冗余计算严重推高推理成本。

### 方法关键点
- 架构保持上下文编码器、接收器两个基座LLM完全冻结，仅训练中间的上下文压缩器、隐态阅读器、层/槽位门控三个轻量模块，无需微调基座权重
- 编码器仅基于上下文生成固定大小的压缩包，与query无关，包大小不随上下文长度增长，默认配置仅384KiB
- 接收器通过cross-attention读取压缩包，门控模块基于当前query动态控制每个槽位的信息权重，不同query可复用同一压缩包的不同信息
- 两阶段训练：第一阶段用上下文重建任务训练所有接口模块，保证压缩包携带完整上下文信息；第二阶段固定压缩器，仅用下游任务微调阅读器和门控，已存储的压缩包无需重新编码

### 关键结果
- 在12个多选QA数据集+3个零样本holdout数据集上，平均准确率较单向量压缩基线最高提升10.2个百分点
- 长文本QuALITY数据集（单上下文平均对应18.1个query）上，接收器输入token减少57×，单上下文多query整体推理速度提升3×，单query推理仅比纯query输入多20ms
- 支持跨模型族、跨大小的LLM配对，覆盖Qwen、Gemma、Llama、Granite等主流模型

跨冻结LLM的轻量隐态通信接口，是兼顾多query复用、低推理成本、跨模型兼容性的最优落地方向之一。
