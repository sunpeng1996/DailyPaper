---
title: 'GAAC: Lossless KV Compression for Bandwidth-Efficient LLM Inference on Personal
  Devices'
title_zh: GAAC：面向个人设备带宽高效LLM推理的无损KV压缩方法
authors:
- Yipin Guo
- Arun M George
- Siddharth Joshi
affiliations:
- University of Notre Dame
arxiv_id: '2610.38210'
url: https://arxiv.org/abs/2610.38210
pdf_url: https://arxiv.org/pdf/2610.38210
published: '2026-10-28'
collected: '2026-10-30'
category: LLM
direction: LLM推理优化 · KV cache 无损压缩
tags:
- KV_cache
- Lossless_Compression
- LLM_Inference
- On_device_AI
- Bandwidth_Optimization
one_liner: 提出组自适应加法编解码GAAC，无损压缩KV缓存，降低端侧LLM长上下文推理带宽开销
practical_value: '- 端侧部署Agent/生成式推荐服务可直接复用GAAC方案，无需修改模型精度即可降低26%KV内存占用，长上下文推理提速10%+，完全不影响生成质量

  - 可借鉴组自适应基址偏移编码思路，针对业务常用的BF16/FP8张量仅压缩高冗余指数位，保留符号和尾数位，平衡压缩率与编解码开销

  - 融合KV重建与attention kernel的设计可直接复用，避免全缓存解压的内存开销，适配PagedAttention等现有LLM serving架构，改造成本低收益明显

  - 端侧LLM服务可复用fill-then-finalize块级压缩调度逻辑，增量更新KV缓存，无需逐token压缩，降低在线编码开销'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有端侧LLM推理普遍采用权重量化降低内存开销，但KV cache随上下文长度线性增长，已成为长上下文推理的首要带宽瓶颈；有损KV压缩/剪枝会引入精度损失，在已经使用低比特权重的部署场景下进一步增加效果退化风险，亟需无精度损失的KV压缩方案同时降低存储与带宽开销。

### 方法关键点
- 利用BF16 KV cache的指数位高冗余特性，仅压缩指数位，符号+尾数位直接存储无改动，保证完全无损
- 组自适应加法编码：每8个KV元素为一组，基于预校准的通道级指数连续区间，自动选择3bit/4bit/raw偏移编码，无需码表查找，仅用加法即可完成编解码
- 融合KV重建与attention kernel，按需逐块解压KV，无需全量解压缓存到内存，降低内存流量
- 块级fill-then-finalize压缩调度，对齐PagedAttention块大小，支持增量KV更新，兼容现有LLM serving引擎

### 关键结果
- 基于Qwen、Llama系列4B~35B模型测试，BF16 KV压缩比达1.405~1.407x，KV内存占用降低约26%，优于nvCOMP、SplitZip等现有无损压缩方案
- NVIDIA DGX Spark上64K上下文解码attention提速1.19~1.27x，端到端W4A16解码提速1.04~1.15x，相同KV内存预算下服务吞吐量提升13%~29%
- Apple M4上实现1.02~1.25x的attention提速，适配不同端侧硬件架构；仅用WikiText校准的编码窗口可迁移到代码、数学、知识问答等任务，压缩比损失不超过0.004x

### 核心结论
无损KV压缩通过减少内存流量获得的收益远高于轻量编解码的计算开销，是端侧长上下文LLM部署的低风险高收益优化手段。
