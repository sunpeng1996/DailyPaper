---
title: Rewirable Circuits in Transformers with Loom Attention
title_zh: 基于Loom Attention的Transformer可重写电路架构LoomFormer
authors:
- Da Xiao
- Qingye Meng
- Shengping Li
- Xingyuan Yuan
affiliations:
- Beijing University of Posts and Telecommunications
- ColorfulClouds Technology
arxiv_id: '2611.30634'
url: https://arxiv.org/abs/2611.30634
pdf_url: https://arxiv.org/pdf/2611.30634
published: '2026-11-22'
collected: '2026-11-25'
category: LLM
direction: LLM 架构优化 · 低开销注意力增强
tags:
- Transformer
- LoomAttention
- DualResidualStream
- LinearAttention
- EfficientLLM
one_liner: 提出Loom Attention双流式Transformer，仅加2%-3.7% FLOPs即可媲美3倍算力训练的常规Transformer
practical_value: '- 电商/推荐场景自研小参数LLM（用于商品文案生成、query改写、智能客服）可直接复用LoomFormer架构，仅增<4%
  FLOPs即可获得接近3倍参数量模型的效果，大幅降低训推成本

  - 双残差流（控制流+内容流）的解耦设计可迁移到多模态推荐模型，将用户行为特征、item属性特征分别在不同流处理，减少特征间干扰

  - 垂直层间注意力压缩历史头输出到固定大小矩阵的思路，可用于优化推荐序列建模模块，降低长用户行为序列的建模与推理开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
常规Transformer的层间注意力头组合逻辑在训练后完全固定，不同输入需要的推理电路无法动态适配，只能通过堆参数、增加训练算力来覆盖所有场景，导致小模型效果上限低，大模型落地成本过高。现有残差流优化方案仅支持层粒度的动态聚合，无法实现头粒度的电路重写，收益有限。

### 方法关键点
- 实现Loom Attention，将垂直层间注意力与水平token间注意力交织，每个token可动态选择读取哪些前序头的输出生成Q/K/V，实现推理电路的token级动态重写
- 采用双残差流架构：向量流作为控制流，生成矩阵内存的读写查询/键，控制电路重写逻辑；矩阵流作为内容流，存储压缩后的头输出，承载跨token传递的信息，额外参数量极低
- 用归一化+门控线性注意力实现垂直层间注意力，将朴素实现的O(L²)开销降低到与层数无关的常数级，全模型仅增2.0%-3.7%的前向FLOPs

### 关键实验
在Pile数据集训练，对比Pythia、mHC、MUDDFormer、AttnRes等SOTA基线：2.8B参数的LoomPythia仅增2% FLOPs，下游10个任务平均精度0-shot持平12B参数量的普通Pythia，5-shot超出12B Pythia 0.8个百分点；训练算力仅为同效果常规Transformer的1/3，比现有SOTA残差流基线节省1.7-2.8倍算力。

### 核心结论
仅增加不到4%的额外计算开销，即可让小参数模型获得接近3倍参数量常规Transformer的效果，是低算力场景下LLM落地的极优架构选择
