---
title: Rethinking Heterogeneous System Disaggregation for Subquadratic Attention
title_zh: 针对次二次注意力LLM的异构计算单元细粒度解耦优化方案
authors:
- Arya Tschand
- Yaosheng Fu
- Vikram Sharma Mailthody
- Nicolai Oswald
- Po-An Tsai
- Ritchie Zhao
- Oreste Villa
- Vijay Janapa Reddi
- Karu Sankaralingam
affiliations:
- Harvard University
- NVIDIA
arxiv_id: '2609.13134'
url: https://arxiv.org/abs/2609.13134
pdf_url: https://arxiv.org/pdf/2609.13134
published: '2026-09-11'
collected: '2026-09-14'
category: LLM
direction: LLM推理 · 异构计算调度
tags:
- Subquadratic Attention
- LLM Inference
- Heterogeneous Computing
- KV Cache
- Disaggregated Serving
one_liner: 提出SQD细粒度解耦方案，将次二次注意力LLM推理拆分部署到异构硬件，显著提升能效与低延迟吞吐量
practical_value: '- 部署采用次二次注意力（滑动窗口/Mamba/稀疏attention）的长上下文LLM时，可参考SQD拆分逻辑，将需访问全量KV
  cache的二次注意力层留在GPU，其余层部署到高内存带宽、高能效的SRAM加速卡，降低推理成本

  - 针对稀疏注意力LLM的KV cache优化，可复用IndexShare跨层预取+经验频率驱逐策略，隐藏跨设备通信延迟，适配实时客服Agent、RAG问答等低延迟场景

  - 搭建异构推理集群时优先保障互连低延迟而非高带宽，跨层激活传输数据量小，低延迟互连可直接降低端到端推理耗时，适合电商实时文案生成、推荐理由生成等场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前次二次注意力已成为前沿长上下文LLM的标准配置，但现有异构推理解耦方案均面向稠密注意力设计，按算子（attention/FFN）或prefill/decode阶段拆分，未利用次二次注意力静态内存占用、低计算强度的特性，导致GPU资源浪费严重，长上下文推理能效低、延迟高，低延迟交互场景（实时Agent、对话）的单token成本居高不下。

### 方法关键点
- 提出SQD细粒度解耦方案，按注意力的计算/内存特性而非算子拆分：将需访问全量KV cache、内存占用随上下文增长的二次注意力（稠密attention、稀疏attention的top-k选择步骤）与prefill阶段共置在DRAM-GPU上共享KV cache；将内存占用固定、计算强度低的次二次注意力+FFN部署在SRAM-only ASIC上，大幅减少跨设备传输次数
- 针对稀疏注意力LLM，设计IndexShare跨层预取+经验秩频率驱逐的KV缓存机制，利用top-k选择的局部性将跨设备通信延迟隐藏在层间计算间隙中，额外开销极低
- 适配全类别次二次注意力架构：线性/滑动窗口注意力按层拆分，稀疏注意力在算子内拆分

### 关键结果
- 8×B200模拟异构系统上，对比纯GPU基线，GLM 5.2、Nemotron 3 Ultra、Gemma 4 31B的tokens/J分别提升53%、31%、56%，1M上下文场景下能效提升最高达71%
- Rubin+LPX异构系统分析模型中，固定功耗预算下对比最优attention-FFN解耦基线，SQD的用户TPS提升1.2~1.5倍，GLM 5.2场景下最高提升3.6倍，低延迟交互场景吞吐量比纯GPU方案高2.7~3.4倍

### 核心洞察
次二次注意力LLM的异构部署不能照搬稠密注意力的拆分逻辑，按注意力的计算/内存特性细粒度拆分才能最大化异构硬件的能效优势
