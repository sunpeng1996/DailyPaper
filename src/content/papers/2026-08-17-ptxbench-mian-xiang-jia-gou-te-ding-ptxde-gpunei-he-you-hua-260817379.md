---
title: 'PTXBench: Benchmark and Adapt LLMs for GPU Kernel Optimization with Architecture-specific
  PTX'
title_zh: PTXBench：面向架构特定PTX的GPU内核优化LLM评测基准
authors:
- Genghan Zhang
- Yixin Dong
- Chengze Fan
- Zhichen Zeng
- Yueming Yuan
- Shaowei Zhu
- Kunle Olukotun
affiliations:
- Stanford University
- Carnegie Mellon University
- RadixArk
- Independent Researcher
arxiv_id: '2608.17379'
url: https://arxiv.org/abs/2608.17379
pdf_url: https://arxiv.org/pdf/2608.17379
published: '2026-08-17'
collected: '2026-08-19'
category: Eval
direction: LLM评测 · GPU内核优化
tags:
- PTX
- GPU Kernel Optimization
- LLM Benchmark
- Supervised Fine-Tuning
- CUDA
one_liner: 提出面向架构特定PTX的GPU内核优化LLM评测基准，验证微调提升LLM内核优化能力的核心影响因素
practical_value: '- 大模型推理服务优化时，可参考该基准的PTX性能评测维度，针对性优化GEMM、attention算子的推理速度，降低生成式推荐、RAG检索等业务的大模型调用延迟

  - 垂直领域LLM微调可复用其修复条件训练思路，除数据集大小外，优先保障数据覆盖度、均衡性与teacher模型推理质量，提升微调效果泛化性

  - 对极致GPU算力利用率要求高的业务（如大规模向量检索、MoE模型推理），可尝试用该基准验证LLM生成PTX内核的可行性，替代部分手动优化算子降低研发成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
GPU架构迭代速度快，现有编译器对齐新硬件特性的研发成本高，LLM能否直接利用架构特定PTX实现内核高效优化缺乏统一评测标准，现有LLM的PTX优化能力未被系统验证。
### 方法关键点
构建PTXBench评测基准，覆盖H100、B200 GPU上的GEMM、attention前后向workload，从功能正确性、目标指令执行率、相对前沿库的加速比三个维度评测LLM能力；基于Qwen3.6-27B开展有监督微调，验证修复条件训练等策略的效果。
### 关键结果
复杂attention反向任务上LLM优化成功率大幅下降，所有评测模型均无法在全测试集上性能比肩前沿库；修复条件训练可提升部分任务表现，但泛化性仍不足，除数据集规模外，数据覆盖度、均衡性、推理teacher质量是核心影响因素。
