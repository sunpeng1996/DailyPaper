---
title: 'Towards Looped Models Done Right, Part I: Topology, Input Injection, Recurrent-State
  Design'
title_zh: 循环语言模型优化实践（一）：拓扑、输入注入与循环状态设计
authors:
- Benhao Huang
- Chufan Shi
- Junlin Chen
- Shicheng Wen
- Zhengzhong Liu
- Eric Xing
- Xuezhe Ma
affiliations:
- Institute of Foundation Models
- University of Southern California
- Carnegie Mellon University
arxiv_id: '2610.23036'
url: https://arxiv.org/abs/2610.23036
pdf_url: https://arxiv.org/pdf/2610.23036
published: '2026-10-15'
collected: '2026-10-19'
category: LLM
direction: 循环大语言模型 · 架构优化
tags:
- Looped LLM
- MoE
- Transformer
- Architecture Optimization
- Reasoning
one_liner: 拆解循环LLM三大设计维度，验证最优架构可迁移至MoE，参数量较同算力FFN少75%
practical_value: '- 搭建Agent推理模块时，可复用prelude-loop-coda三明治架构，提升用户多轮需求解析、优惠规则计算等复杂任务的推理准确率

  - 垂域LLM（如电商文案生成、用户query理解）部署时，采用循环MoE架构可在相同推理FLOPs下将驻留参数量降低75%，大幅节省显存开销，效果接近同算力全参数FFN
  MoE

  - 针对强上下文依赖任务（如售后多轮会话理解、推荐理由生成），可在循环迭代中注入prelude表征，提升上下文信息利用率，减少迭代过程的信息丢失'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
AI硬件算力增速远高于显存带宽增速，Looped LLM通过复用Transformer块可大幅降低显存占用，但现有两大主流架构（Ouro、Huginn）的设计收益未被系统拆解，不同设计选择的实际效果、是否可迁移至MoE场景均不明确。
### 方法关键点
- 将Looped LLM架构拆解为三大独立维度：迭代包络（循环块放置位置）、输入注入策略、循环状态组织，严格控制参数规模、逻辑深度、训练token量对齐做 ablation
- 核心对比两类架构：Ouro（全栈循环，无独立prelude/coda层，输入为原始token embedding）、Huginn（三明治架构，独立prelude/coda层仅执行1次，中间Transformer块循环复用，每轮迭代注入prelude输出的上下文表征）
- 验证架构设计对MoE的迁移性，所有对比组严格对齐训练、推理FLOPs
### 关键结果
- 730M参数规模下，完整Huginn架构在10个覆盖知识、推理、代码的benchmark上全面优于Ouro，其中MATH500提升12分、GSM8K提升7.05分
- 8B驻留/0.8B激活参数的Huginn MoE，较同FLOPs的32B参数FFN MoE驻留参数量减少75%，在DROP、GSM8K上超过FFN MoE，MATH500与之持平，在8/10个benchmark上优于Ouro MoE
### 核心结论
Looped LLM的性能增益核心来自三明治架构和输入注入，随机初始化、高低分层状态无稳定增益，架构优化可在不增加显存开销的前提下大幅提升推理能力
