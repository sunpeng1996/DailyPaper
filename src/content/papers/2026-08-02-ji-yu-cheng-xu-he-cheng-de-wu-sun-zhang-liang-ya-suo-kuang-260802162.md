---
title: Lossless Tensor Compression as Program Synthesis
title_zh: 基于程序合成的无损张量压缩框架Brevis
authors:
- Jieke Shi
- Junda He
- Wenjia Jiang
- Weifeng Sun
- Shidong Pan
- Zhensu Sun
- Chengran Yang
- Peixin Zhang
- Yifan Jia
- Zhou Yang
affiliations:
- Singapore Management University
- CSIRO (Australia)
- AIDX TECH PTE LTD
- University of Alberta
- Alberta Machine Intelligence Institute
arxiv_id: '2608.02162'
url: https://arxiv.org/abs/2608.02162
pdf_url: https://arxiv.org/pdf/2608.02162
published: '2026-08-02'
collected: '2026-08-07'
category: Training
direction: 大模型 checkpoint 无损张量压缩优化
tags:
- Tensor Compression
- Checkpoint Compression
- Program Synthesis
- Lossless Compression
- Model Deployment
one_liner: 提出将无损张量压缩转化为程序合成任务的框架Brevis，压缩比与速度均优于现有通用/张量专用压缩方案
practical_value: '- 大模型服务部署时可引入Brevis压缩LoRA、全量checkpoint，降低模型分发、冷启动加载的存储与带宽成本

  - 在线推理服务的KV cache落地存储场景，可复用Brevis的张量结构感知DSL设计，提升压缩比同时保证无损

  - 批量训练多版本推荐/广告大模型时，用Brevis压缩历史checkpoint，可降低30%+的存储成本且加解压速度满足生产要求'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
大模型、多模态模型数量与参数量高速增长，checkpoint存储、传输、部署成本陡增；通用压缩方案未利用张量结构，现有张量专用压缩依赖固定格式管道，压缩比上限低。

### 方法关键点
提出Brevis框架，将无损张量压缩建模为程序合成任务；设计带类型的领域特定语言DSL，通过可逆算子捕获重复区域、浮点域等张量常见结构；基于小批量张量样本学习checkpoint专属生成先验，引导有界A*搜索合成可直接执行的自包含DSL程序，实现比特级精确重建。

### 关键结果
在10个涵盖语言、音频、图像生成的公开checkpoint上，将2.13TB数据压缩至1.41TB，存储降低33.93%；压缩包比zstd、gzip等4种通用压缩方案小最多30.87%，也优于张量专用压缩方案ZipNN、DFloat11；并发配置下压缩速度3.60GB/s，解压速度6.61GB/s，完全无损。
