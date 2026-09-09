---
title: Learning Length-Extrapolatable Recurrent Models
title_zh: 可长度外推的循环模型学习：时序信用稳定训练方法
authors:
- Hanwen Jiang
affiliations:
- Adobe Research
arxiv_id: '2609.09157'
url: https://arxiv.org/abs/2609.09157
pdf_url: https://arxiv.org/pdf/2609.09157
published: '2026-09-08'
collected: '2026-09-09'
category: Training
direction: 循环模型长上下文训练 · 长度外推
tags:
- Recurrent Model
- Length Extrapolation
- BPTT
- Credit Assignment
- Long Context
- Language Modeling
one_liner: 提出时序信用稳定(CST)方法，短序列训练的循环模型可支持最长128倍训练长度的推理
practical_value: '- 自研Mamba、DeltaNet类循环架构时可直接集成CST训练，无需长序列训练数据即可获得长序列推理能力，大幅降低训练算力与数据成本

  - 电商长用户行为序列（如全年点击/下单序列）召回/排序场景，CST优化的循环模型无KV cache膨胀问题，同时保证远期行为信息的有效利用

  - 跨会话导购Agent的长期记忆模块若采用循环状态实现，CST可提升跨长时间步的历史信息复用准确率，减少记忆丢失'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
循环模型天然具备固定大小KV cache、长序列推理效率高的优势，是长上下文建模的理想架构，但传统BPTT训练的循环模型在推理长度超过训练长度时性能暴跌。传统梯度消失/爆炸分析无法完全解释该问题：梯度衰减本身不决定学习效果，核心瓶颈是远期损失的信用无法有效回传到早期循环状态，导致短序列训练的模型无法适配长序列推理。
### 方法关键点
- 定义状态信用为远期损失对早期循环状态的梯度，是参数梯度的上游信号，将其作为干预靶点
- 核心方法CST（Credit Stabilization through Time）：反向传播时对跨块的状态信用做局部缩放，仅调整信号范数不改变方向，不修改前向计算逻辑与损失函数
- 针对不同场景特化：受控任务用Event-CST，仅在信用收缩超过阈值时触发放大，配合EMA replay降低计算开销；真实文本场景用对称头级CST，独立对每个头的信用做双向缩放（收缩时放大、膨胀时缩小）
### 关键结果
- 合成任务：训练长度1k，推理最长达128k（128倍训练长度），Event-CST在Meta-FSA任务上平均比BPTT准确率高6.58pp，128k下MQAR检索任务准确率提升16.1pp
- 真实语言建模：训练长度4k，推理最长达128k（32倍训练长度），CST在14个数据集-长度组合上全token NLL均降低，长上下文敏感的key token NLL增益是全token的2.5~4.5倍

> 最值得记住的结论：梯度衰减本身不限制循环模型长程学习能力，仅当早期计算的效果需要通过远期损失反馈时，状态信用的稳定传递才会成为性能瓶颈
