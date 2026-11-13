---
title: 'LazyWeights: Decode-on-Demand Edge LLMs'
title_zh: LazyWeights：按需解码的边缘侧大语言模型压缩加速方案
authors:
- Arnab Sanyal
- Gourav Datta
- Sandeep P. Chinchali
affiliations:
- The University of Texas at Austin
- Case Western Reserve University
arxiv_id: '2611.17108'
url: https://arxiv.org/abs/2611.17108
pdf_url: https://arxiv.org/pdf/2611.17108
published: '2026-11-12'
collected: '2026-11-13'
category: LLM
direction: 边缘LLM · 量化压缩+硬件加速
tags:
- LLM Compression
- Edge Deployment
- Post-training Quantization
- Huffman Coding
- Hardware Acceleration
one_liner: 兼容GGUF格式，通过熵感知量化+专用硬件解码单元实现边缘LLM更小体积更低延迟能耗
practical_value: '- 端侧部署轻量LLM用于推荐理由生成、搜索Query补全、端侧Agent交互的业务，可复用熵感知量化方案，兼容现有GGUF生态的前提下将模型体积最高压缩31.4%，适配更低配的用户设备

  - 边缘侧LLM推理架构可复用「DRAM与L2之间插入专用解码单元」的设计，无需修改上层CUDA内核即可降低30%+的推理延迟与能耗，降低边缘推理服务的硬件成本

  - 小内存设备部署7B级LLM可参考其流式加载+量化压缩组合方案，实现原本无法运行的大模型在4GB内存设备上流式推理，速度最高提升6.6倍'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前边缘LLM部署受内存容量与带宽双重限制：7B模型16位存储占14GB远超多数边缘设备内存，现有固定位宽量化方案（GPTQ、AWQ、llama.cpp）未利用权重分布的非均匀性进一步压缩，软件熵解码延迟比固定位宽高2.5-3.2倍，无法落地。
### 方法关键点
- 熵感知量化：完全兼容GGUF格式，修改GPTQ逻辑采用超级块共享步长+步长缩放策略，让量化编码更集中，降低熵值
- 并行霍夫曼打包：采用11位限长正则码，按32 interleaved lane分块存储，支持并行解码，无需等待前序码解码完成
- 专用硬件解码单元：部署在DRAM与L2之间，直接将霍夫曼码转为固定宽度码供GPU使用，上层推理内核无需任何修改
- 运行时适配：支持prompt-lookup投机解码、CUDA Graph、小内存设备流式加载，覆盖不同边缘硬件场景
### 关键结果
在1%/3.5%可接受perplexity损失预算下，Phi-3-mini、Mistral-7B、SmolLM-1.7B的体积比最优llama.cpp量化格式小5.7%-31.4%；搭配0.21mm² 7nm ASIC解码单元，Orin Nano单token延迟最高降36%、能耗最高降38%，加投机解码后延迟最高降54%、能耗最高降44%；Jetson Nano上单token耗时比CPU版llama.cpp少58%-64%、能耗少53%-57%，可流式运行Mistral-7B，速度提升6.6倍。
> 核心结论：边缘LLM量化的固定位宽是约定而非必须，在内存带宽瓶颈处加专用轻量解码单元，可在完全兼容现有生态的前提下显著提升推理效率
