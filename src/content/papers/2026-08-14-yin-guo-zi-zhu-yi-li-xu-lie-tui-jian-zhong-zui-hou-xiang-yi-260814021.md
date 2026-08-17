---
title: Residual Dominance as a Structural Account of Last-Item Reliance in Causal
  Self-Attention Recommenders
title_zh: 因果自注意力序列推荐中最后项依赖的残差主导结构机制
authors:
- Keito Kozaki
- Keigo Sakurai
- Ren Togo
- Takahiro Ogawa
- Miki Haseyama
affiliations:
- Hokkaido University
arxiv_id: '2608.14021'
url: https://arxiv.org/abs/2608.14021
pdf_url: https://arxiv.org/pdf/2608.14021
published: '2026-08-14'
collected: '2026-08-17'
category: RecSys
direction: 序列推荐 · 自注意力结构分析
tags:
- Sequential Recommendation
- Self-Attention
- SASRec
- Residual Connection
- Recency Bias
one_liner: 揭示因果自注意力序列推荐的最后项依赖源于残差连接的同位置信息保留机制
practical_value: '- 针对SASRec类序列推荐过度依赖最近交互的问题，可在推理阶段对残差分支乘系数α（0.1~0.3区间），在可接受的精度损失下召回部分被最近项掩盖的正确候选，适合需要兼顾推荐新颖性的电商场景

  - 分析序列推荐的位置依赖时，不能仅看注意力权重，需结合残差连接的贡献，可采用论文中的mixing ratio指标量化模型对上下文信息的实际聚合程度，辅助模型调参

  - 针对冷启动/长序列推荐场景，若发现模型过度依赖最近点击，可尝试调整残差连接的初始化/训练时的缩放系数，降低最后项主导效应，充分利用历史交互信号'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有因果自注意力序列推荐（如SASRec）普遍存在过度依赖最后交互项的现象，但仅靠注意力权重无法解释这种不连续的位置特权，现有解释多停留在数据层面的近因偏差，缺乏模型结构层面的机制解释，无法指导针对性优化。

### 方法关键点
- 采用两种诊断工具量化最后项依赖：推理阶段位置扰动（仅保留最后项其余打乱、全序列打乱）、HRLI@K（最后项出现在推荐列表Top-K的比例）
- 引入范数分解方法分析完整注意力块（包含残差、层归一化），定义mixing ratio指标量化上下文信息的聚合程度
- 设计推理阶段残差缩放干预：在不重训的情况下调整残差分支的权重α，验证残差强度与最后项依赖的关联

### 关键实验
在9个公开序列推荐数据集（涵盖Beauty、Sports、ML-1M等不同稀疏度、序列长度场景）上对比SASRec、DuoRec、GRU4Rec、BERT4Rec等基线；实验发现注意力层输出的mixing ratio平均达0.7~0.9，加入残差后骤降至0.1~0.3，证明残差主导了同位置信息保留；调整α至0.1~0.3时，最高可恢复46%的最后位预测漏判（非最后位已能正确排序的样本）。

### 核心结论
因果自注意力推荐的最后项依赖不是仅由注意力权重决定，而是残差连接的全局同位置保留效应与仅用最后位表征预测的接口共同作用的结果。
