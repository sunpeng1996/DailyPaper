---
title: 'SparseDecoding: Decoding-Aware Pruning for Accurate and Efficient LLM Inference'
title_zh: SparseDecoding：面向LLM高效准确推理的解码感知剪枝框架
authors:
- Qitong Wang
- Xinwei Niu
- Mingluo Su
- Shanwei Zhao
- Shiai Zhu
- Huan Wang
affiliations:
- Westlake University
- Ant Group
arxiv_id: '2610.12327'
url: https://arxiv.org/abs/2610.12327
pdf_url: https://arxiv.org/pdf/2610.12327
published: '2026-10-07'
collected: '2026-10-09'
category: LLM
direction: LLM推理优化 · 剪枝与稀疏内核设计
tags:
- LLM_inference
- pruning
- sparse_kernel
- N:M_sparsity
- decoding_optimization
one_liner: 提出解码感知剪枝框架与定制N:M SpMV内核，实现A100上最高1.48倍LLM解码加速
practical_value: '- 部署LLM类业务（商品文案生成、导购Agent、推荐理由生成）的团队，可直接复用该剪枝方案，无需额外训练，仅用业务场景prompt让原模型自生成解码激活做校准，即可大幅降低剪枝后的质量损失

  - 推理优化时可直接复用论文开源的N:M SpMV内核，无需依赖cuSPARSELt稀疏TensorCore，在A100上即可拿到1.3~1.48倍的解码端到端加速，尤其适配小batch、长输出的生成场景

  - 业务定制剪枝时，优先用待部署模型自身生成的解码阶段激活做校准，效果远优于通用C4等公共数据集校准，对2:4半结构化稀疏的质量提升尤其显著'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM长输出场景（长文案生成、多轮Agent对话等）的自回归解码阶段为内存绑定，延迟占比极高。现有训练自由剪枝方法用固定语料的teacher-forced激活校准，与实际解码时模型自生成token的分布存在偏移，导致剪枝后生成质量下降明显；同时现有稀疏内核主要优化prefill阶段SpMM操作，对解码阶段占主导的SpMV操作加速效果差，甚至慢于稠密模型，剪枝的理论算力节省无法转化为实际延迟收益。

### 方法关键点
- 算法层：解码感知校准，用待剪枝稠密模型在业务相关prompt上自回归生成的解码阶段激活（丢弃prefill激活）构造校准矩阵，对齐剪枝目标与实际解码激活分布，可直接对接SparseGPT、Wanda等现有剪枝后端，无需额外训练
- 系统层：定制N:M半结构化稀疏SpMV内核，用位掩码索引替代传统列索引，元数据量降低4~16倍；基于50%稀疏率下每32位掩码固定16个非零位的特性，采用固定步长遍历，保证GPU线程负载均衡，大幅降低索引开销

### 关键实验
在Llama3.1-8B、Llama3.3-70B、Qwen3-14B/32B等主流LLM上测试，对比基线为C4数据集校准的常规剪枝方法：
- WritingBench长文本生成任务上，50%稀疏率得分比基线高0.19~0.75分，2:4稀疏率下Qwen3-32B得分从2.99提升到5.31
- ClassEval代码生成任务上，2:4稀疏率下Qwen3-32B的Pass@1从9%提升到24%
- A100上解码端到端加速最高达1.48倍，解决了现有稀疏TensorCore内核解码时慢于稠密模型的问题

### 核心结论
LLM剪枝的校准数据分布必须和实际推理场景的解码激活对齐，同时配套场景专属的稀疏内核才能同时拿到质量和延迟收益
