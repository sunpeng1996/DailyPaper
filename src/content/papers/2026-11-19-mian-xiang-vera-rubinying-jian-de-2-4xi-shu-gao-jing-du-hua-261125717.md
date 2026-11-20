---
title: 'VR-SparseQuant: Accurate FP4 Quantization with 2:4 Sparsity on Vera Rubin'
title_zh: 面向Vera Rubin硬件的2:4稀疏高精度FP4量化方法VR-SparseQuant
authors:
- Samir Khaki
- Wei-Chen Wang
- Song Han
- Ryan Hanrui Wang
affiliations:
- Nebius Applied AI
- Massachusetts Institute of Technology
arxiv_id: '2611.25717'
url: https://arxiv.org/abs/2611.25717
pdf_url: https://arxiv.org/pdf/2611.25717
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: LLM推理优化 · FP4量化+2:4结构化稀疏
tags:
- FP4_Quantization
- Structured_Sparsity
- LLM_Inference
- Vera_Rubin
- Model_Compression
one_liner: 利用Vera Rubin的2:4稀疏特性，实现精度接近W4A16、速度超BF16的FP4量化方案
practical_value: '- 做LLM驱动的推荐/Agent服务时，可借鉴双稀疏流量化思路，在保持推理延迟可控的前提下降低FP4量化的精度损失，提升大模型调用性价比

  - 服务侧部署MoE结构的推荐大模型时，可复用共享权重GEMM的工程实现，将MoE的FP4推理速度提升至BF16的1.4~2.7倍

  - 针对预量化LLM checkpoint做业务适配时，可直接复用该方法在不重新量化权重的前提下提升激活量化精度，降低适配成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
Vera Rubin等新GPU硬件原生支持FP4精度与2:4结构化稀疏指令，可大幅提升LLM推理吞吐，但传统密集FP4 W4A4量化的激活量化误差大，会显著降低模型质量；W4A16虽然精度高但算力利用率低，无法充分利用硬件FP4算力，亟需兼顾精度与速度的FP4量化方案。

### 方法关键点
- 采用双2:4稀疏流量化机制，将激活拆分为粗粒度+细粒度两个稀疏流，总FP4值预算与密集FP4一致，允许流重叠以修正粗流的量化误差
- 离线校准双流量化比例p，推理时仅需通过块最大值计算两个流的量化尺度，无需在线搜索，贪心分配两个流的稀疏位置，计算开销极低
- 设计共享权重的稀疏GEMM内核，两个流复用同一份权重Tile，共用FP32累加器，避免重复权重加载，适配Vera Rubin的原生VRFP4指令集

### 关键实验结果
对比密集RTN W4A4、W4A16、BF16基准，覆盖Qwen3.5-4B、Nemotron-30B MoE等主流模型：Nemotron-30B的WikiText-2 PPL从6.85降至5.57，AIME2026准确率从78.9%提升至86.7%，接近W4A16精度；GEMM速度最高达BF16的3.1倍，MoE速度最高达BF16的2.7倍，仅比最优密集FP4慢7%~47%。

**最值得记住的一句话**：结构化稀疏不仅可以用于减少计算量，还可以在固定位宽预算下灵活分配精度资源，实现量化精度与速度的双赢。
