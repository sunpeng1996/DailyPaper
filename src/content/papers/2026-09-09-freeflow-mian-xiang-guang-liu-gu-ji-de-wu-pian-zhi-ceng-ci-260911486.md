---
title: 'FreeFlow: A Bias-free Hierarchical Transformer for Optical Flow Estimation'
title_zh: FreeFlow：面向光流估计的无偏置层次Transformer
authors:
- Vladislav Bargatin
- Alexander Yakovenko
- Khaled Abud
- Dmitriy Vatolin
affiliations:
- Lomonosov MSU AI Center
- Lomonosov Moscow State University
- MSU Institute for Artificial Intelligence
arxiv_id: '2609.11486'
url: https://arxiv.org/abs/2609.11486
pdf_url: https://arxiv.org/pdf/2609.11486
published: '2026-09-09'
collected: '2026-09-13'
category: Other
direction: 光流估计 · 无归纳偏置Transformer
tags:
- Optical-Flow
- Vision-Transformer
- Hierarchical-Attention
- Inductive-Bias
- High-Resolution-Inference
one_liner: 提出无任务特定归纳偏置的层次Transformer光流估计架构，精度达SOTA且1080p推理内存高效
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有光流方法为提升精度，普遍依赖关联体、特征扭曲、迭代优化等任务特定归纳偏置，这类预定义启发式规则会约束模型表达能力，同时带来管线复杂度提升、额外计算成本等问题。

### 方法关键点
FreeFlow为无任何光流专属组件的层次Transformer架构，仅采用单个前馈编解码器，融合三类注意力机制：窗口注意力实现局部处理、移位窗口注意力完成跨窗口信息交换、降分辨率全局注意力捕捉长程依赖；架构天然支持随模型容量扩展，从微小到大参数量版本均可获得稳定精度增益。

### 关键结果数字
无标准归纳偏置的前提下，在多个主流光流基准达到SOTA效果：Sintel数据集Clean/Final拆分EPE分别为0.68/1.48，KITTI-2015 Fl-all指标为3.23，Spring 1px指标为3.192，同时1080p推理内存效率优异。
