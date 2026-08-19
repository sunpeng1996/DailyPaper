---
title: 'FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution'
title_zh: FreeToken：带宽自适应执行的原生边缘MoE推理服务系统
authors:
- Shuo Yang
- Xiaoze Fan
- Melissa Pan
- Haocheng Xi
- Zhe Wang
- Shanlin Sun
- Kurt Keutzer
- Song Han
- Matei Zaharia
- Chenfeng Xu
affiliations:
- UC Berkeley
- Stanford University
- MIT
- University of Texas at Austin
arxiv_id: '2608.16157'
url: https://arxiv.org/abs/2608.16157
pdf_url: https://arxiv.org/pdf/2608.16157
published: '2026-08-16'
collected: '2026-08-19'
category: LLM
direction: MoE LLM 边缘推理服务优化
tags:
- MoE
- Edge Inference
- LLM Serving
- Hybrid CPU-GPU
- Bandwidth Adaptive
one_liner: 实现消费级硬件上大参数量MoE模型高效推理，性能超现有系统1.3-2.3倍
practical_value: '- 端侧Agent部署场景可借鉴q*带宽自适应调度策略，根据设备实测PCIe/CPU带宽动态拆分MoE专家的GPU加载/CPU执行，提升推理速度

  - 多轮Agent会话场景可复用语义锚点状态缓存机制，在工具调用、对话轮次等语义边界保存checkpoint，避免上下文修改后的重复预计算，降低TTFT

  - 资源受限的MoE部署场景可借鉴动态LRU专家缓存+全层双缓冲预取设计，在有限VRAM下支撑更大参数规模的MoE模型推理'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
当前开源MoE架构模型能力快速接近闭源系统，但大参数量MoE推理高度依赖数据中心级GPU资源，普通消费级硬件难以高效运行；现有边缘推理系统未适配MoE稀疏激活特性、Agent多轮会话预填充开销大、静态调度策略无法适配异构边缘硬件的动态资源变化，导致大模型端侧部署门槛极高。

### 方法关键点
- 预填充阶段：采用全层双缓冲机制，并行化专家加载与GPU计算，隐藏PCIe传输开销；新增语义锚点状态缓存，在工具调用、对话轮次等语义边界保存状态checkpoint，上下文修改后仅需重新预填充新增后缀
- 解码阶段：设计全局共享LRU专家缓存捕获相邻token的路由局部性，降低缓存miss率；提出q*带宽自适应调度策略，根据实测的PCIe传输带宽和CPU计算带宽，动态拆分miss专家到GPU加载/CPU执行，最大化资源利用率
- 弹性内存管理：支持运行时动态调整VRAM在专家缓存和KV cache之间的分配，无需重启推理引擎；优化模型加载逻辑，直接将专家权重加载到最终内存布局，消除启动热身开销

### 关键实验
在6款硬件（8GB RTX4060笔记本到96GB RTX PRO 6000工作站）、4种真实Agent工作负载上测试，对比llama.cpp、Ollama、KTransformers等基线：RTX5090上Qwen3.6-35B吞吐量77-83tok/s、DeepSeek-V4-Flash 284B吞吐量22-25tok/s，比基线高1.5-2.3倍；8GB RTX4060笔记本可运行35B模型，吞吐量39.3tok/s，超过Codex生产环境中位数33tok/s；RTX PRO 6000可运行753B GLM-5.2，吞吐量是llama.cpp的2倍；最坏情况TTFT低于44s，远低于基线的150s以上，避免Agent客户端超时。

**最值得记住的一句话**：边缘大模型部署的边界越来越不由硬件容量决定，而是由调度软件对现有CPU、GPU、内存等资源的编排能力决定。
