---
title: Controlling Refusal Behavior of LLMs via Stiefel-Constrained Rotation Steering
title_zh: 基于Stiefel流形约束旋转的大模型拒绝行为控制方法
authors:
- Kirill Bunin
- Dmitry Bylinkin
- Vladimir Aletov
- Daniil Medyakov
- Vladimir Solodkin
- Aleksandr Beznosikov
affiliations:
- BRAIn Lab
- Kandinsky Lab
- Innopolis University
arxiv_id: '2608.30986'
url: https://arxiv.org/abs/2608.30986
pdf_url: https://arxiv.org/pdf/2608.30986
published: '2026-08-31'
collected: '2026-09-01'
category: LLM
direction: LLM行为控制 · 激活引导优化
tags:
- Activation Steering
- Riemannian Optimization
- LLM Safety
- Stiefel Manifold
- Behavior Control
one_liner: 提出参数高效的StiefelSteer旋转激活引导方案，无需预定义拒绝向量，兼顾干预效果与模型通用能力
practical_value: '- 垂直领域Agent对齐可复用该低秩旋转方案：相比加性激活引导，其严格保留激活范数的特性不会大幅损失模型通用能力，适配电商客服、商品文案生成等场景的输出合规约束需求

  - 工程落地可直接复用少层干预+低秩参数设计：仅需训练每层dn+n²个参数（n远小于隐层维度d），无需全量微调，适配1.5B-7B级开源LLM的快速定制对齐

  - 内容风控场景可复用攻防一体设计：同一套学习到的子空间，仅需使用旋转矩阵的转置即可实现拒绝行为的增强/减弱，同时适配越狱攻击防御和敏感输出拦截'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM激活引导技术存在明显缺陷：加性引导易导致激活范数膨胀，大幅损伤模型通用能力；传统旋转引导依赖预定义拒绝向量，表达能力受限，无法适配高维复杂的拒绝行为控制需求，亟需兼顾干预效率与能力保留的轻量方案。

### 方法关键点
- 提出StiefelSteer架构：将激活旋转约束在低秩子空间内，仅需学习子空间基矩阵B（属于St(d,n)流形）和子空间内旋转矩阵Q（属于SO(n)），参数量远低于全维度旋转矩阵
- 采用黎曼优化框架：直接在流形上计算梯度并做投影回缩，全程保证正交约束满足，无需额外正则项
- 损失与部署设计：采用「有害指令交叉熵+通用指令KL正则」的损失函数平衡效果与能力；攻击/防御仅需切换使用学习到的M矩阵及其转置，无需重复训练

### 关键结果
基于Alpaca无害语料、SALADBench有害语料测试，对比Angular Steering、Spherical Steering、RDO等基线：
- 攻击场景：DeepSeek-R1-7B不安全输出率从0.52提升至0.90，强对齐的Qwen2.5-1.5B（基线0不安全输出）可达0.89
- 防御场景：DeepSeek-R1-7B不安全输出率降至0.00，同时ARC准确率、困惑度几乎与原模型持平
- 仅需干预2个中间层、子空间维度n=35即可饱和效果，计算开销极低

> 最值得记住的结论：LLM拒绝行为控制无需依赖预定义拒绝向量，低秩子空间旋转可在几乎不损失通用能力的前提下实现更高效的行为干预。
