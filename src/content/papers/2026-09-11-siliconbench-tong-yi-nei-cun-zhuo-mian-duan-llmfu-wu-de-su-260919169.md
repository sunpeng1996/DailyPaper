---
title: 'SiliconBench: Speed, Memory, and Fidelity for LLM Serving on Unified-Memory
  Desktops'
title_zh: SiliconBench：统一内存桌面端LLM服务的速度、内存与保真度评测
authors:
- Ranran Haoran Zhang
- Aysa Xuemo Fan
- David Munhá Correia
- Alex Cheema
- Rui Zhang
affiliations:
- Penn State University
- University of Illinois Urbana-Champaign
- EXO Labs
arxiv_id: '2609.19169'
url: https://arxiv.org/abs/2609.19169
pdf_url: https://arxiv.org/pdf/2609.19169
published: '2026-09-11'
collected: '2026-09-22'
category: Eval
direction: LLM服务评测 · 统一内存桌面端
tags:
- LLM Serving
- Benchmark
- Apple Silicon
- Unified Memory
- Inference
one_liner: 推出SiliconBench基准，从速度、内存、保真度三维度评测9款Apple Silicon LLM推理引擎
practical_value: '- 本地轻量Agent（如离线推荐调测工具、客服助手）部署优先选vllm-metal：并发1到16时吞吐量超2倍提升，Agent场景TTFT<220ms，内存占用稳定，支持Qwen3.5、Gemma4等最新模型，符合低延迟高并发需求

  - 统一内存设备部署LLM需避免padded batch机制：实测mlx_lm的padded batch在32GB内存设备上会触发内存压缩，延迟升高2.5倍，优先选packed
  token + paged KV cache的引擎架构降低内存浪费

  - 本地多机部署大模型优先选Tensor Parallelism + RDMA传输方案：双机Thunderbolt RDMA下TP可带来1.28~1.37倍解码速度提升，Pipeline
  Parallelism + TCP反而有16~20%性能下降

  - LLM服务选型需额外校验输出保真度：实测ollama吞吐量与vllm-metal接近，但5-shot分类任务F1比A100参考值低30pp，会直接影响RAG、Agent工具调用等任务效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
统一内存桌面（Apple Silicon、DGX Spark等）已成为本地轻量LLM、Agent部署的主流硬件，现有引擎选型仅关注吞吐量指标，忽略了共享内存挤占、并发下性能衰减、输出保真度下降三类隐性问题，缺乏系统的评测基准指导业务选型。
### 方法关键点
- 覆盖9款主流Apple Silicon LLM服务引擎，从速度（吞吐量、TTFT、并发伸缩性）、内存（占用水平、前台应用内存headroom保留能力）、保真度（分类任务F1与A100参考值偏差）三个维度量化评测
- 负载覆盖Chat、Agent两类业务场景，模型选用Qwen3-0.6B、Qwen3.5-0.8B、Gemma 4三款主流小模型，补充27B dense、35B MoE大模型及双机分布式场景评测
- 提出三大选型判定标准：架构就绪度（新模型支持、并发处理能力）、内存管控能力、多机伸缩能力
### 关键结果
- 并发度从1升至16时，仅vllm-metal在Chat、Agent两类场景吞吐量均实现超2倍提升，Agent场景TTFT中位数仅219ms，内存占用稳定在34.9GB，同时通过所有保真度校验、支持全部三款测试模型
- 6款引擎输出F1与A100参考值偏差在1.5pp以内，ollama 5-shot任务F1比参考值低30pp，存在明显保真度缺陷
- 双机分布式场景下，Tensor Parallelism over Thunderbolt RDMA带来1.28~1.37倍解码加速，Pipeline Parallelism over TCP反而出现16~20%性能倒退
### 核心结论
统一内存桌面端LLM服务选型不能只看单并发吞吐量，需同时校验并发伸缩性、内存占用、输出保真度三个维度，否则会出现隐性性能衰减、OOM、业务效果下降等问题
