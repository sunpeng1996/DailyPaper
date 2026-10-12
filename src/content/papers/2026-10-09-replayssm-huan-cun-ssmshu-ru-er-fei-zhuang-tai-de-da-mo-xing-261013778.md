---
title: 'ReplaySSM: Cache SSM Inputs, Not State'
title_zh: ReplaySSM：缓存SSM输入而非状态的大模型推理加速方案
authors:
- Ze-Wei Liou
- Harris Nover
- Amey Naik
- Andrii Skliar
- Igor Shovkun
- Ido Shahaf
- Tri Dao
affiliations:
- Princeton University
- NVIDIA
arxiv_id: '2610.13778'
url: https://arxiv.org/abs/2610.13778
pdf_url: https://arxiv.org/pdf/2610.13778
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: LLM推理 · SSM解码优化
tags:
- SSM
- Inference Optimization
- Speculative Decoding
- Quantization
- vLLM
one_liner: 重构SSM状态表示降低解码内存开销，同时支持低成本推测解码与低精度量化
practical_value: '- 若业务使用Mamba-2/GDN等SSM架构大模型做Agent推理、商品文案生成，可直接将ReplaySSM集成到vLLM，batch
  256场景下标准解码提速1.2-1.47倍，推测解码吞吐量提升1.8倍，显著降低推理成本

  - 做大模型低精度量化优化时，可复用双精度checkpoint设计：高精度checkpoint负责循环更新，低精度checkpoint负责输出计算，既降低内存开销，又避免量化误差累积，长序列生成场景下KL散度最多可降36倍，下游准确率损失可忽略

  - 长序列Agent推理、长文本商品描述生成等场景，优先选择支持ReplaySSM的SSM混合架构模型，相比纯Transformer的KV cache开销更低，长序列下延迟表现更稳定'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前Mamba-2、Gated DeltaNet等SSM结构的混合大模型已在生产中广泛落地，但传统逐步更新循环状态的解码模式存在三大痛点：服务级batch下状态I/O内存开销占比过高成为性能瓶颈、无低成本回滚机制导致推测解码几乎无收益、量化误差随循环累积严重劣化长序列生成质量，亟需更高效的SSM状态管理方案。

### 方法关键点
- 重构SSM状态表示：用固定checkpoint + 最近输入缓存替代逐步更新的状态，仅当缓存填满时才将输入折叠更新到checkpoint，大多数步骤无需写入全量状态，核心状态内存流量减半
- 适配推测解码：缓存的输入让回滚仅需移动缓存指针，同时实现仅输出的验证逻辑，无需实例化中间状态，大幅降低推测解码的额外开销
- 双精度checkpoint设计：低精度checkpoint负责非刷写步骤的输出计算，高精度checkpoint负责刷写时的循环更新，彻底切断低精度量化误差的循环传播路径

### 关键结果
在vLLM上实现对Mamba-2、GDN的支持，batch size 256下：标准解码速度较优化后的vLLM基线提升1.20-1.47倍；120B级MoE模型推测解码吞吐量达到vLLM基线的1.8倍；低精度场景下NVFP4输出+FP16循环更新的配置，128K长序列生成KL散度较共享NVFP4 checkpoint降低36倍，GPQA-Diamond准确率损失从13.05个百分点降至2.36个百分点。

最值得记住的结论：SSM解码的性能瓶颈本质是内存而非计算，解耦输出计算与状态更新的设计可同时解决性能、回滚、量化误差三类核心问题。
