---
title: 'Quantization-Aware Healing: A Practical Recipe for Recovering Compressed,
  4-Bit LLMs'
title_zh: 量化感知修复：恢复4位压缩大语言模型的实用方案
authors:
- Bakbergen Ryskulov
- Iker García-Ferrero
- David Montero
- David Jansen
- Ali Hashemi
- Jezabel R. Garcia
- Antonio Tiene
- Román Orús
affiliations:
- Multiverse Computing
arxiv_id: '2608.20953'
url: https://arxiv.org/abs/2608.20953
pdf_url: https://arxiv.org/pdf/2608.20953
published: '2026-08-21'
collected: '2026-08-24'
category: Training
direction: 大语言模型压缩 · 4位量化训练优化
tags:
- Quantization
- Knowledge Distillation
- LLM Compression
- QAT
- 4-bit LLM
one_liner: 提出直接从原始未压缩大模型蒸馏修复4位结构压缩LLM的量化感知修复方案，收敛快稳定性高
practical_value: '- 业务侧自研Agent/生成式推荐小模型时，结构压缩+4位量化后优先采用QAH方案从原始大模型蒸馏，相比QAT可减少7倍训练步数，无需手动调优早停策略，避免模型坍塌

  - 4-bit LLM部署时可将量化阶段作为额外的性能优化环节，叠加一轮大模型蒸馏，可实现显存降为1/4的同时，多数任务性能超过压缩后的bf16模型

  - 分布式训练量化LLM时优先选择FSDP2后端，实测在推理、科学类任务上性能比DeepSpeed最高高8.6分，避免分布式后端带来的隐性性能损失

  - 长上下文4-bit模型训练可复用离线Top-K logits + Chunked KL loss实现，峰值显存大幅降低，32k上下文训练可在常规GPU硬件上完成'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM生产部署普遍采用结构压缩+4位量化组合方案降本，但两步叠加会严重损失推理、数学、代码、长上下文能力；传统QAT修复方案收敛慢、易过拟合坍塌，且先结构压缩再量化的场景下，常规量化感知蒸馏用的压缩后bf16 checkpoint本身就是蒸馏产物，存在固有性能天花板，亟需稳定高效的修复方案。
### 方法关键点
- 提出Quantization-Aware Healing (QAH)：直接以原始未压缩大模型为教师，对结构压缩+4位量化后的学生模型做KL散度蒸馏，不依赖压缩后的bf16中间 checkpoint，突破性能天花板
- 工程优化：离线预计算教师的Top-100 logits，采用Chunked KL loss实现，峰值显存从O(BLV)降到与序列长度线性相关，支持32k上下文训练
- 训练trick：冻结embedding、层归一化、部分注意力组件，避免量化带来的权重漂移
### 关键结果
在GPT-OSS 120B→60B→MXFP4 pipeline上测试：QAH修复后的4位模型在7/9个基准上匹配或超过压缩后的bf16模型，其中长上下文AA-LCR提7.4分、数学AIME2025提5.6分；相比QAT基线收敛快7倍，训练全程稳定无坍塌，无需手动调早停；模型显存仅为bf16版本的1/4，参数量为原始120B的一半，在LiveCodeBench上性能追平原始120B模型。
> 值得记住的结论：在基于蒸馏的修复pipeline中，量化步骤不是需要最小化的损耗环节，而是额外施加教师监督提升模型能力的机会
