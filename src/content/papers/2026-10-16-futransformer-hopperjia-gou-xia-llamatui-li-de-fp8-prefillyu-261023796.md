---
title: 'FuTransformer: FP8 prefill and INT4 decode for Llama-style inference on Hopper'
title_zh: FuTransformer：Hopper架构下Llama推理的FP8 Prefill与INT4 Decode优化
authors:
- Wei Wang
arxiv_id: '2610.23796'
url: https://arxiv.org/abs/2610.23796
pdf_url: https://arxiv.org/pdf/2610.23796
published: '2026-10-16'
collected: '2026-10-19'
category: LLM
direction: LLM低精度推理 · Hopper架构优化
tags:
- LLM Inference
- FP8
- INT4 Quantization
- KV Cache
- CUDA Kernel
- Hopper GPU
one_liner: 针对NVIDIA Hopper GPU设计分阶段低精度Llama推理核，性能显著优于PyTorch与CODA
practical_value: '- 部署LLM驱动的推荐/Agent服务时，可复用Prefill用FP8、Decode用INT4的分阶段精度策略，在可控精度损失下降低推理延迟

  - 基于H100集群的LLM服务可直接借鉴RMSNorm增益预折叠入权重、KV缓存直接写入、Hadamard变换降量化误差的工程Trick，提升吞吐

  - 小batch高并发的多轮对话、个性化生成场景，优先采用Fragment对齐的INT4 Decode优化，比PyTorch INT4实现快1.3~6.3倍

  - 用户Query长度差异大的搜索/推荐场景，开启Packed Prefill可在不均匀长度请求下比Padding方案最高提速5倍'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
Transformer推理的Prefill与Decode阶段瓶颈差异显著：Prefill阶段权重重用率高，瓶颈为矩阵乘与激活数据搬运；单token Decode阶段权重重用率低，瓶颈为权重与KV缓存读取。现有实现未针对推理场景做端到端低精度+算子融合优化，Hopper GPU的硬件潜力未被充分释放。

### 方法关键点
- 分阶段精度策略：Prefill采用FP8精度保障大矩阵乘效率，Decode采用INT4精度降低访存量
- Prefill优化：基于GEMM+epilogue架构，实现KV缓存直接写入、RMSNorm固定增益预折叠入权重、延迟缩放直接输出FP8、支持无Padding的Packed输入，大幅减少中间张量读写开销
- Decode优化：INT4权重与KV缓存按Tensor Core MMA Fragment布局存储，直接在寄存器中反量化无需生成中间Tile；引入块对角Hadamard变换降低INT4量化对离群通道的敏感度

### 关键结果
基于H100 GPU测试：Prefill最高比编译后PyTorch FP8快1.48倍，算力达1.29 PFLOP/s；INT4 Decode在8B/70B模型、batch 1~32下比最优PyTorch实现快1.3~2.4倍，比自身FP8 Decode快31%~51%；完整Llama-3.1-8B单batch Decode仅需2.8ms，比官方transformers实现快2.9倍；INT4量化（GPTQ权重+旋转INT4缓存）后WikiText-2 perplexity仅从6.24升至7.18，精度损失可控。

针对Transformer推理两阶段的差异化瓶颈做拆分优化，效果远好于用统一精度与架构适配全流程的方案。
