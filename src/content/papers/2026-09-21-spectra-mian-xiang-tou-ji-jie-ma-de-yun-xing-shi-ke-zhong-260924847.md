---
title: 'SPECTRA: Adaptive Execution of Speculative Decoding on a Runtime-Reconfigurable
  Tiled Architecture'
title_zh: SPECTRA：面向投机解码的运行时可重构分片硬件架构
authors:
- Gabriele Tombesi
- William Baisi
- Je Yang
- Elisavet Lydia Alvanaki
- Kevin Lee
- Michael Lippe
- Biruk Seyoum
- Luca P. Carloni
affiliations:
- Columbia University
arxiv_id: '2609.24847'
url: https://arxiv.org/abs/2609.24847
pdf_url: https://arxiv.org/pdf/2609.24847
published: '2026-09-21'
collected: '2026-09-22'
category: LLM
direction: LLM边缘推理 · 投机解码硬件加速
tags:
- Speculative Decoding
- Hardware Acceleration
- FPGA
- LLM Inference
- Reconfigurable Architecture
- Edge Computing
one_liner: 提出双层可重构分片架构SPECTRA，适配投机解码各阶段负载，大幅提升边缘端LLM推理性能
practical_value: '- 端侧电商Agent/生成式推荐部署可复用投机解码+可重构硬件适配思路，优化端侧智能导购、离线个性化内容生成的推理延迟，降低端侧部署成本

  - 线上LLM推理引擎优化可参考按kernel粒度切换GEMM/GEMV执行模式的设计，适配prefill、decode不同阶段的算力瓶颈，提升现有GPU/NPU集群的利用率

  - 生成式推荐负载调度可借鉴动态分片+通信原语匹配的思路，针对prompt长度、生成token数波动的场景，动态分配计算资源，降低长尾延迟

  - 边缘电商智能终端（线下导购屏、无人柜交互系统）选型可参考SPECTRA的能效比数据，其比通用Jetson平台高2.9~4.4倍的能效比，适合低功耗边缘场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
边缘端LLM推理受算力和内存资源约束，传统自回归解码为内存绑定的GEMV操作，计算资源利用率极低。投机解码虽可通过小模型预生成token、大模型批量验证的方式减少串行步骤，但其验证阶段的算术强度随投机长度、token接受率动态变化，介于prefill阶段的计算绑定GEMM和decode阶段的内存绑定GEMV之间，固定硬件架构无法兼顾各阶段的资源利用效率，导致投机解码的收益无法充分释放。

### 方法关键点
- 单tile级可重构：PE阵列支持按kernel粒度切换执行模式，GEMM场景用输出固定脉动阵列最大化计算复用，GEMV场景用并行向量通道避免算力浪费，复用同一计算单元仅修改控制逻辑，硬件开销极低
- 系统级动态适配：支持N/K/M三种维度的核内分片，配合DMA/P2P/组播三种通信原语，按各阶段负载特征动态调整tile分配、核划分和通信模式
- 算子融合优化：集成后处理单元，支持GELU、归一化、FlashAttention式流式计算，减少中间数据落盘开销

### 关键实验
基于20 tile FPGA原型测试，覆盖Pythia、SmolLM2、GPT-2三类模型的投机解码负载：① 单tile重构比固定脉动架构提速1.16~2.09倍，比固定向量架构提速3.8~8.02倍；② 系统级动态分片比最优固定分片额外提速1.05~1.25倍；③ 对比Jetson Orin NX/TX2边缘GPU，吞吐量提升3.6倍，能效比提升2.9~4.4倍。

### 核心结论
投机解码的效率瓶颈不仅在算法侧优化，还需要硬件架构适配其动态变化的计算特征，双层可重构设计是兼顾性能和硬件成本的可行路径。
