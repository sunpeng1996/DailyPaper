---
title: An MLIR-Based Compilation Method for Large Language Models
title_zh: 基于MLIR的大语言模型编译优化方法
authors:
- Pengchao Hu
- Zhibin Xin
- Yifan Chen
- Yangyang Zhou
- Liang Wang
affiliations:
- Sophgo Inc.
arxiv_id: '2607.15865'
url: https://arxiv.org/abs/2607.15865
pdf_url: https://arxiv.org/pdf/2607.15865
published: '2026-07-17'
collected: '2026-07-20'
category: LLM
direction: 大语言模型 · 编译部署优化
tags:
- LLM
- MLIR
- KV_cache
- Static_Compilation
- Model_Deployment
one_liner: 通过两级MLIR方言与Transformer三阶段拆分实现LLM在专用AI加速器的高效编译部署
practical_value: '- 业务部署LLM服务（如电商智能客服、Agent推理、商品文案生成）时，可参考三阶段拆分策略，将prefill/prefill
  kv/decode分开编译，降低动态调度开销，提升推理吞吐与长对话场景的响应速度

  - KV cache优化可复用静态地址复用+按上下文长度匹配对应decode编译变体的方案，减少内存拷贝，适合多轮对话、长Query理解等需要维护长上下文的业务场景

  - RoPE计算优化技巧可直接复用：预计算cos/sin权重表，用Gather操作代替实时计算，特别适合端侧LLM部署场景，降低算力消耗提升端侧Agent响应速度

  - 若业务使用专用AI加速卡部署LLM，可参考TopOp/TpuOp两级方言的设计思路，屏蔽上层PyTorch/HuggingFace框架差异，快速适配主流开源模型，减少跨模型的适配开发成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Transformer架构LLM已成为AI加速器主流负载，但传统手写算子适配专用硬件成本高、迭代慢，且自回归推理中prompt并行处理与单token生成的计算特性差异大，有限片上内存下调度效率低，亟需通用编译方案解决LLM落地部署的性能瓶颈。

### 方法关键点
- 两级MLIR方言设计：高层`TopOp`方言无关源框架与目标芯片，统一表达模型语义，保留Attention、MLP等粗粒度融合算子边界，方便下层做硬件适配优化；底层`TpuOp`方言携带量化、内存布局、层组信息等芯片属性，直接面向代码生成
- Transformer层三阶段静态拆分：按推理场景拆为三个静态形状模块分别编译：prefill（首次prompt并行处理，无历史KV）、prefill kv（多轮对话/长prompt分段，带历史KV拼接）、decode（单token生成，KV随生成递增），避免动态编译开销
- 配套性能优化：预计算RoPE的cos/sin表，用`top.Gather`代替实时计算降低算力消耗；复用小尺寸因果掩码减少带宽占用；KV cache静态地址规划与原地更新避免内存拷贝

### 关键结果
方案已落地在开源TPU-MLIR编译器与LLM-TPU部署项目，支持Qwen、Llama、InternVL、MiniCPM-V等多系列生成模型，兼容GPTQ、AWQ、AutoRound等主流量化部署形式，可直接生成目标硬件可执行二进制。

> 与其编译一个全动态的Transformer，不如编译多个静态形状变体在运行时调度，更适配专用AI加速器的硬件特性。
