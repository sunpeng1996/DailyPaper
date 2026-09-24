---
title: Riemannian Structure and Optimization for a Class of Low-Parametric Orthogonal
  Matrices
title_zh: 低参数结构化正交矩阵的黎曼结构与优化算法
authors:
- Ali Aliev
- Maxim Rakhuba
affiliations:
- HSE University
arxiv_id: '2609.27982'
url: https://arxiv.org/abs/2609.27982
pdf_url: https://arxiv.org/pdf/2609.27982
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: 结构化矩阵优化 · LLM参数高效微调
tags:
- Riemannian Optimization
- Structured Matrix
- PEFT
- LLM Fine-tuning
- Orthogonal Matrix
one_liner: 针对Group-and-Shuffle正交矩阵族提出高效黎曼优化框架 可用于LLM参数高效微调
practical_value: '- 做LLM/大模型PEFT时，可替换LoRA使用本文提出的GS正交矩阵适配器，参数规模相当的前提下，RoBERTa微调平均准确率比欧氏优化SGD高1.73个百分点，仅增加5-7%的训练/推理开销

  - 大模型线性层压缩场景，可复用本文的结构化矩阵参数共享机制，最多可降低52%的适配器参数量，仅损失不到1个百分点的下游任务精度

  - 优化受限空间参数更新时，可复用本文基于AD的黎曼梯度计算trick，无需显式构造稠密矩阵，大幅降低内存占用与计算量'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Group-and-Shuffle（GS）结构化正交矩阵兼顾表达性与计算效率，在LLM参数高效微调、模型压缩等场景已得到应用，但传统欧氏优化忽略其几何结构，存在稳定性差、精度低的问题，且现有方法无高效的黎曼优化实现方案。
### 方法关键点
- 证明无约束GS块分解不构成光滑流形，仅当块为正交/酉矩阵时才满足流形条件，针对m=2的常用场景推导全套黎曼优化工具，包括切空间投影、回缩、向量运输算子
- 提出基于自动微分（AD）的梯度计算方法，无需显式构造稠密矩阵，自动适配参数共享、重叠支撑等场景，大幅降低计算与存储开销
- 支持固定边界置换矩阵初始化，可从恒等变换开始训练，适配大模型微调的增量更新需求
### 关键结果
- 合成矩阵逼近任务中，收敛速度与精度均优于传统Cayley参数化欧氏优化基线
- RoBERTa-base微调GLUE基准，相同1.38M参数量下，黎曼SGD比欧氏SGD平均得分高1.73分，仅比欧氏AdamW低1.19分，训练开销仅5-7%
- 引入参数共享后，适配器参数量可从1.38M降至0.65M，下游任务平均精度仅损失不到2分
### 核心结论
结构化正交矩阵的黎曼优化方案，在几乎不增加开销的前提下，可大幅提升PEFT的稳定性与精度，是LoRA之外极具潜力的大模型微调方案
