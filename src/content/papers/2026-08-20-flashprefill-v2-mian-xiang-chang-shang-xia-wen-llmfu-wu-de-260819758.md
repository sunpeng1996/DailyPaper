---
title: 'FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving'
title_zh: FlashPrefill V2：面向长上下文LLM服务的块稀疏Prefill注意力优化
authors:
- Qihang Fan
- Huaibo Huang
- Zhiying Wu
- Bingning Wang
- Ran He
affiliations:
- CASIA
- UCAS
- Tencent WeChat
arxiv_id: '2608.19758'
url: https://arxiv.org/abs/2608.19758
pdf_url: https://arxiv.org/pdf/2608.19758
published: '2026-08-20'
collected: '2026-08-21'
category: LLM
direction: 长上下文LLM推理 · Prefill性能优化
tags:
- Sparse-Attention
- LLM-Serving
- Prefill-Acceleration
- KV-Cache
- FP8-Inference
one_liner: 生产可用的块稀疏Prefill注意力算子，128K上下文下FP8精度较FA2最高提速47.26倍
practical_value: '- 部署长上下文Agent、RAG系统时可直接集成FlashPrefill V2作为SGLang的注意力后端，128K上下文下TTFT最多降低4.8倍，大幅提升用户查询响应速度

  - 做LLM推理优化时可复用均值校正trick，仅增加不到20%的额外开销就能将极端稀疏下的精度损失控制在1.5个点以内，尤其适配FP8量化场景

  - 线上长上下文服务配合chunked prefill使用时，建议chunk大小设为8K以上，可最大化发挥FlashPrefill V2的稀疏加速收益，避免索引计算开销抵消加速效果

  - 块稀疏注意力算子的PackGQA内存访问、warp specialization、pingpong流水线设计可直接复用，适配Hopper架构GPU优化推理性能'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文LLM已成为Agent、RAG、长文档理解等场景的刚需，但注意力的二次复杂度导致prefill阶段计算开销极高，此前的FlashPrefill只是算法原型，存在极端稀疏下精度失控、算子落后于最新FlashAttention3/4、不兼容paged KV cache与连续批处理等问题，无法直接落地生产。

### 方法关键点
- 新增均值校正项：对裁剪的KV块用池化后的均值统计量计算替代贡献，在softmax中合并精确计算块与校正块的结果，极端稀疏下精度损失可控
- 适配Hopper架构重构稀疏注意力算子：采用PackGQA内存布局、warp专业化生产消费流水线、pingpong GEMM-softmax重叠调度，原生支持FP8推理，对齐FlashAttention3/4的执行效率
- 原生支持paged KV cache与连续批处理，可直接作为SGLang等主流推理框架的注意力后端，无需修改模型定义与调度逻辑

### 关键结果
在NVIDIA H20 GPU上测试，对比FlashAttention2、FA3/4对齐的稠密基线、MInference等稀疏方案：128K上下文下BF16精度比FA2快27.19倍，FP8精度快47.26倍；比FA3/4稠密基线BF16快17.54倍、FP8快30.49倍；RULER、LongBench精度仅比全注意力低不到1个点；集成到SGLang后128K上下文下TTFT最高降4.8倍，请求吞吐量提升2.4倍。

最值得记住的一句话：块稀疏注意力只要做好精度校正与工程适配，完全可以在几乎无损精度的前提下实现数十倍的长上下文prefill加速，具备生产落地价值。
