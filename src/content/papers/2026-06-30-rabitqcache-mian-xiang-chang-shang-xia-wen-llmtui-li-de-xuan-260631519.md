---
title: 'RaBitQCache: Rotated Binary Quantization for KVCache in Long Context LLM Inference'
title_zh: RaBitQCache：面向长上下文LLM推理的旋转二进制量化KV缓存优化
authors:
- Wenhao Li
- Jinhao Dong
- Hailin Zhang
- Wenhang Shi
- Wei Lu
- Xiaoyong Du
affiliations:
- 中国人民大学
- 北京大学
arxiv_id: '2606.31519'
url: https://arxiv.org/abs/2606.31519
pdf_url: https://arxiv.org/pdf/2606.31519
published: '2026-06-30'
collected: '2026-07-01'
category: LLM
direction: 长上下文LLM推理 · KV缓存量化加速
tags:
- KV_cache
- Binary_Quantization
- LLM_Inference
- Long_Context
- Sparse_Attention
one_liner: 提出带理论误差界的旋转二值量化KV缓存框架，实现长上下文推理2.16倍加速无精度损失
practical_value: '- 长上下文Agent/电商智能客服场景可复用这套Top-p自适应KV缓存选择方案，替代固定Top-k策略，根据注意力稀疏度动态调整token预算，平衡推理速度和回答精度

  - 可复用旋转二值量化+INT4 Query的轻量注意力分数估计方法，将浮点内积转为低比特运算，降低KV缓存内存占用和I/O开销，提升大模型推理吞吐

  - 工程实现上可借鉴异步流水线、懒更新、二进制打包存储、共享内存tiling等优化trick，进一步降低量化、索引构建的overhead，把Prefill阶段性能损耗控制在10%以内'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长上下文LLM推理的核心瓶颈是KV缓存内存占用高、计算复杂度随序列长度二次增长，现有稀疏注意力方法要么采用固定Top-k预算无法适配不同任务的注意力分布差异，要么代理分数估计偏差大、无理论误差保证，难以兼顾效率和生成质量。

### 方法关键点
- 基于JL引理设计旋转二值量化方案，Prefill阶段将Key向量随机旋转后二值化为1bit索引，同时预计算校正因子保证分数估计无偏
- Decode阶段将Query量化为INT4，把高成本浮点内积转为INT4×二值向量的低比特运算，快速估计注意力分数，具备严格的理论误差界
- 支持自适应Top-p检索，根据注意力分布动态选择覆盖p概率质量的最小token集合，无需人工调整固定token预算
- 系统级优化：Prefill阶段异步流水线掩盖量化开销，Decode阶段懒更新批量处理新增token减少Kernel启动开销，定制高性能CUDA Kernel优化向量运算效率

### 关键实验
在LongBench、RULER、GSM8K数据集上测试，对比Quest、DS、SparQ、SnapKV等SOTA基线，RaBitQCache仅用17%左右的token预算就达到90%的注意力召回率，生成精度与全精度注意力持平，解码阶段最高提速3.88倍，端到端推理最高提速2.16倍，Prefill阶段overhead低于10%。

最值得记住的一句话：带理论误差界的无偏注意力分数估计是实现自适应Top-p稀疏检索、兼顾长上下文推理效率和精度的核心前提
