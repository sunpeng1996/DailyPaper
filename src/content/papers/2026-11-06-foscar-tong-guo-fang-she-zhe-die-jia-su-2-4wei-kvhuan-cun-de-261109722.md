---
title: 'FOSCAR: Accelerating Decode Attention over 2- and 4-Bit KV Caches through
  Affine Folding'
title_zh: FOSCAR：通过仿射折叠加速2/4位KV缓存的解码注意力
authors:
- Donglin Zhuang
- Pragaash Ponnusamy
- Xiaoxia Wu
- Shuaiwen Leon Song
- Zhongzhu Zhou
affiliations:
- Together AI
- University of Sydney
arxiv_id: '2611.09722'
url: https://arxiv.org/abs/2611.09722
pdf_url: https://arxiv.org/pdf/2611.09722
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: LLM 推理 · KV cache 量化加速
tags:
- KV cache
- Quantization
- Tensor Core
- GPU Kernel
- LLM Inference
- Attention
one_liner: 提出仿射折叠机制优化低比特KV缓存解码注意力，在H100/B200上实现大幅性能提升
practical_value: '- 直接复用FOSCAR开源核替换SGLang/vLLM等推理框架的低比特KV解码核，长上下文Agent服务、生成式推荐的LLM推理吞吐量可提升1.5~3倍，无需修改上层业务逻辑

  - 仿射折叠思路可迁移到推荐场景低比特Embedding查表优化：将逐元素反量化的scale/offset操作移到分组聚合后，大幅降低CUDA核的指令开销，提升Embedding查表吞吐

  - 针对Hopper/Blackwell架构的warp专用流水线设计可复用在推荐自定义CUDA核优化，比如多目标排序的大batch矩阵运算，充分挖掘Tensor
  Core算力

  - 配合FOSCAR的2bit KV缓存可降低长上下文LLM显存占用，支持电商场景下基于用户全历史行为的生成式推荐、Agent导购，无需额外扩卡即可支持更长序列输入'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM解码阶段KV cache访存占比极高，2/4位量化虽能降低HBM流量，但现有内核逐元素反量化的指令开销成为新瓶颈，H100/B200上现有2bit内核仅能达到15%~31%的峰值HBM吞吐量，性能提升远低于预期。

### 方法关键点
- 仿射折叠机制：将KV量化的分组scale、offset从逐元素反量化操作，转移到Attention的QK/PV矩阵乘的另一操作数或输出侧，算术上与全精度反量化完全等价，可将scale/offset操作量降低两个数量级
- 位级Tensor Core operand构造：直接从打包的低比特整数通过位操作构造Tensor Core输入，配合预计算补偿后的scale/offset，无需逐元素数值转换，H100/B200上INT2 KV cache每个元素仅需1/0.19条ALU指令
- 架构适配流水线：针对H100/B200分别设计warp专用流水线，利用wgmma、tcgen05等硬件特性，重叠数据搬运、operand构造、矩阵乘运算，最大化硬件资源利用率

### 关键结果
-  standalone核测试：H100上INT2/INT4核相对FlashInfer BF16几何平均提速3.36×/2.83×，相对TensorRT-LLM FP8提速2.03×/1.71×；B200上INT2/INT4相对FlashInfer BF16提速2.67×/2.30×，相对TensorRT-LLM NVFP4 INT2提速1.16×
- 服务端集成测试：集成到SGLang后，Qwen3-8B 100K长上下文场景下，INT2核相对16位基线峰值总吞吐量提升341%，相对现有2bit基线提升170%，精度无统计显著下降

### 核心结论
低比特量化的性能瓶颈往往不在访存，而在反量化的指令开销，将逐元素操作转换为分组聚合操作是破解这类瓶颈的核心思路
