---
title: Modular Cognitive Architecture Emerges in Large Language Models
title_zh: 大语言模型中自发涌现类人脑模块化认知架构
authors:
- Pengrui Han
- Jacob Andreas
- Evelina Fedorenko
- Andrea Gregor de Varda
affiliations:
- Massachusetts Institute of Technology
arxiv_id: '2608.13567'
url: https://arxiv.org/abs/2608.13567
pdf_url: https://arxiv.org/pdf/2608.13567
published: '2026-06-26'
collected: '2026-08-17'
category: LLM
direction: 大语言模型 · 认知架构与功能模块化
tags:
- Modularity
- Cognitive Architecture
- Mechanistic Interpretability
- LLM
- Functional Specialization
one_liner: 通过46项跨认知域任务的电路分析，证实大语言模型自发涌现与人脑对齐的模块化功能分区
practical_value: '- 搭建垂直领域Agent时，可针对特定认知域（如优惠计算、用户情绪理解、商品物理属性推理）定向微调对应模块神经元，比全量微调成本低、跨域干扰小

  - 设计MoE架构的推荐/广告大模型时，可参考本文验证的模块化边界划分专家功能，减少人工设计偏差，降低跨任务干扰，提升推理稳定性

  - 做LLM推理优化时，可针对电商场景特定任务（如意图理解、售后响应、规则计算）仅调度对应域的神经元，减少无效计算，提升推理速度

  - 多任务LLM训练时，可引入跨域干扰损失主动诱导功能分区，缓解灾难性遗忘，提升多任务整体表现'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
人脑的模块化功能分区（语言、推理、社会认知等独立模块）是生物进化的偶然产物，还是智能系统的通用底层规律？此前仅能从生物神经实验中观测，缺乏无代谢压力的人造系统验证。LLM作为全新的通用智能范式，为验证这一假设提供了理想实验对象，同时模块化特性也对AI系统架构设计、可解释性优化、推理效率提升有重要实践价值。
### 方法关键点
- 构建覆盖4大认知域（语言处理、形式推理、物理推理、社会推理）的46项任务，每项任务设计仅关键变量不同的输入最小对，保证响应差异仅来自目标认知能力
- 采用Attribution Patching梯度方法，计算每个MLP神经元对特定任务的因果贡献度，定位各任务的核心功能神经元
- 通过统计不同任务核心神经元的重叠度、跨任务消融实验，验证模块化架构的存在性与因果特异性
### 关键结果
在6个24B~123B参数量的主流开源LLM上测试：同域任务核心神经元重叠度达12.9%，是跨域重叠度3.0%的4倍以上；同域神经元消融带来的准确率下降达25.9%，是跨域消融2.5%的10倍；语言模块域特异性最强，消融仅导致自身任务准确率降20.4%，对其他域影响小于0.5%；低性能GPT-2未涌现出推理域的细粒度模块化结构。
### 核心结论
模块化并非生物大脑独有的进化产物，而是智能系统为避免跨域计算干扰、缓解多任务学习灾难性遗忘自发形成的通用架构规律。
