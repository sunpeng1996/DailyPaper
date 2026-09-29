---
title: 'Change the Product, Keep the Parameters: Associative Algebra Layers for Transformers'
title_zh: 保留参数更换矩阵乘积规则：Transformer结合代数层
authors:
- Ilya Koziev
- Ivan Oseledets
affiliations:
- DAIMLD, Moscow, Russia
- Artificial Intelligence Research Institute, Moscow, Russia
arxiv_id: '2609.32814'
url: https://arxiv.org/abs/2609.32814
pdf_url: https://arxiv.org/pdf/2609.32814
published: '2026-09-26'
collected: '2026-09-29'
category: LLM
direction: LLM高效推理 · 矩阵运算优化
tags:
- Transformer
- EfficientInference
- MatrixMultiplication
- AssociativeAlgebra
- ThroughputOptimization
one_liner: 用结合代数替换Transformer线性层标准矩阵乘法，同等参数量下提升生成吞吐量
practical_value: '- 针对实时性要求高的业务场景（如Agent实时交互、电商个性化文案生成、搜索query实时改写），在可容忍轻微效果损失的前提下，可替换大模型FFN层为结合代数层，实现6%+的端到端生成吞吐量提升，无额外参数量和存储开销

  - 优化MoE专家层运算效率时，可借鉴分块乘积剪枝思路，根据业务对效果的容忍度选择合适的分块数q，在主流模型形状下可实现1.5~11.5倍的FFN层kernel加速

  - 落地时可直接复用论文的q值筛选规则：`q ≤ min{M/m₀, K/k₀, N/n₀}`（m₀/k₀/n₀为GPU高效执行GEMM的最小块尺寸），避免分块过小导致GPU利用率下降，抵消算力节省的收益'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Transformer中的线性投影层是核心算力消耗来源，传统快速矩阵乘法均以保留标准乘积规则为前提优化执行路径，而线性层权重与网络整体是端到端联合训练的，无需严格绑定标准矩阵乘法规则，存在通过更换更低成本乘积规则降低计算量的空间。

### 方法关键点
- 基于有向图构造结合代数乘积规则，剪去边与边相乘的冗余块运算，q分块下的矩阵乘法MAC数降低为原有的(2q-1)/q²，符合Alder–Strassen下界，理论上是该规则下的最优实现
- 为每个token位置分配固定行类型，仅执行对应行的乘积逻辑，兼容因果掩码、KV cache解码等Transformer原生特性，无需修改注意力、归一化等其他组件
- 支持任意矩形块运算，可直接适配FFN、注意力投影等不同形状的线性层，参数量与标准稠密层完全一致，无额外存储开销

### 关键结果
- 训练2个110M参数量的Decoder-only LLM，除FFN层乘积规则外完全对齐，训练token数为12.3B，对比基线为同参数量稠密Transformer
- 端到端生成吞吐量在代码、数学、QA、俄英翻译四个场景分别提升6.8%、7.0%、7.8%、6.2%
- 下游任务效果存在可接受的损失：GSM8K EM下降0.98个百分点，IFEval loose准确率下降3.4个百分点，MBPP pass@1下降2.8个百分点
- 单FFN kernel在Qwen3-32B等主流开源模型形状下，可实现1.5~11.5倍的运算加速比

### 核心结论
在允许轻微效果损失的推理场景下，无需修改模型结构、不增加参数量，仅更换线性层的乘积规则即可获得可观的吞吐量提升，是大模型业务落地性价比极高的优化方向。
