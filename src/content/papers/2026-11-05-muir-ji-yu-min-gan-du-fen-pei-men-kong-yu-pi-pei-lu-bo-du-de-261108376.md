---
title: 'Muir: Linear Attention with Sensitivity-Allocated Gating and Matched-Filter
  Readout'
title_zh: Muir：基于敏感度分配门控与匹配滤波读出的线性注意力架构
authors:
- Tushaar Gangavarapu
- Gil Tabak
- Clemens JS Schaefer
affiliations:
- University of Texas at Austin
- Google
arxiv_id: '2611.08376'
url: https://arxiv.org/abs/2611.08376
pdf_url: https://arxiv.org/pdf/2611.08376
published: '2026-11-05'
collected: '2026-11-06'
category: LLM
direction: LLM架构优化 · 长上下文线性注意力
tags:
- Linear-Attention
- Long-Context
- Gated-Delta-Rule
- Hardware-Optimization
- Language-Modeling
one_liner: 优化GDN-2门控分配与读出机制，实现长上下文下更高精度更快训练的线性注意力模型
practical_value: '- 长上下文电商用户行为序列建模可复用低秩门控优化思路：对敏感度低的擦除门采用低秩投影，省出的参数扩容FFN提升事实关联存储能力，适配用户长周期行为召回需求

  - Agent长会话记忆模块可借鉴匹配滤波读出机制：动态加权状态行平衡不同衰减速度的记忆贡献，降低写入擦除强度，延长有效记忆窗口，适配多轮导购、多步推理场景的长上下文需求

  - 大batch长序列训练可复用边界枢轴分块chunkwise核：解决宽矩阵单元下大chunk训练的数值不稳定问题，提升TPU/GPU矩阵单元利用率，降低长序列训练成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有GDN-2等门控delta线性注意力模型对称分配擦除、写入门参数，导致FFN宽度被压缩25%以上；不同衰减速度的状态行范数差异超一个数量级，无权重读出被慢衰减行主导，需强擦除抑制干扰导致记忆窗口短；大chunk下并行训练存在数值溢出、矩阵单元利用率低的问题，无法适配长上下文大模型训练需求。
### 方法关键点
- 基于敏感度分析，擦除门仅在key有激活且状态行有能量时生效，用低秩投影参数化，写入门保留更高秩，所有门控融合为单低秩投影，相同参数预算下FFN宽度扩容30.4%
- 设计匹配滤波读出门，结合静态通道分布与动态token调制加权query，平衡不同衰减速度的状态行贡献，降低写入时擦除强度，延长有效记忆窗口
- 提出边界枢轴分块chunkwise训练核，通过二分树递归分块、边界点拆分衰减系数，避免除法溢出与3D衰减张量，98%运算转移到MXU，适配TPU等宽矩阵单元硬件
### 关键结果
166M-1.34B参数规模下，相比GDN-2困惑度降低1.8-2.0%，相比Transformer降低2.5-3.6%，常识推理准确率最高提升1.9个点；1.34B参数下可从4K训练长度外推到10M token流无困惑度漂移，passkey检索到1M token保持近100%准确率；训练速度相比32K序列Transformer快2.7倍，达到GDN-2 100B token验证损失速度快1.2倍，吞吐量与GDN-2持平。
> 最值得记住的一句话：针对组件敏感度差异做不对称参数分配，结合硬件特性联合优化算法，可在不提升算力成本的前提下同时获得精度与长上下文能力的双重收益。
