---
title: 'Metis: Memory Foundation Model'
title_zh: Metis：原生内置记忆能力的基础模型
authors:
- Zeyu Zhang
- Ziliang Guo
- Yihang Sun
- Xichong Zhang
- Xixuan Hao
- Zehao Lin
- Yang Zhang
- Xiaoyan Zhao
- Tong Shen
- Bo Tang
affiliations:
- MemTensor (Shanghai) Technology Co., Ltd.
- 中国人民大学
- 新加坡国立大学
- 上海交通大学
- 同济大学
arxiv_id: '2607.26760'
url: https://arxiv.org/abs/2607.26760
pdf_url: https://arxiv.org/pdf/2607.26760
published: '2026-07-28'
collected: '2026-07-31'
category: Agent
direction: Agent 原生记忆架构与能力优化
tags:
- Native Memory
- Foundation Model
- AI Agent
- Memory Attention
- Mid-training
one_liner: 提出首个原生内置记忆能力的基础模型原型，支持无梯度在线记忆更新，效率优于外部记忆方案
practical_value: '- 电商导购Agent、个性化推荐等多轮交互场景可复用该原生记忆架构，替代现有RAG外部记忆模块，降低检索、上下文拼接带来的推理延迟，同时解决RAG难以端到端优化的问题

  - 可借鉴其记忆专用训练数据构造流程：基于现有公开基准合成覆盖记忆/更新/遗忘/反思4类操作、多噪声等级的多轮交互数据，用于中训阶段对齐模型的记忆能力

  - 其记忆更新仅需前向传播、无梯度的特性可直接复用在高并发线上服务场景，无需额外的梯度计算资源开销，适配电商大促等高流量交互场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有AI Agent的记忆能力基本通过RAG等外部模块实现，存在架构解耦导致记忆与模型推理适配差、梯度无法回传难以端到端优化、额外的检索/拼接/预填充操作推高推理延迟等问题，具备原生记忆能力的基础模型研究尚处于空白阶段。
### 方法关键点
- 架构设计：在标准Transformer Block中插入Metis Block，由静态的超内存块（训练阶段优化，负责记忆更新逻辑）和动态的本地内存块（推理阶段动态更新，存储记忆状态）组成，通过记忆注意力分支将历史信息融入当前推理
- 训练方案：构造覆盖记忆、更新、遗忘、反思4类核心记忆操作的大规模多轮交互训练数据集，设计记忆重建、记忆操作、正则化三类优化目标，仅训练新增记忆相关参数，冻结主干模型权重完成中训
- 推理优化：记忆更新仅需前向传播，无需梯度计算，记忆状态为固定大小矩阵，不会随交互轮数增长线性提升计算与存储开销
### 关键结果
对比传统RAG外部记忆方案，无需额外引入检索、上下文拼接、预填充步骤，单轮推理额外开销降低30%以上，记忆更新速度提升2个数量级；在多轮记忆问答基准上，10轮以内交互准确率平均提升11.2%，20轮以上长交互准确率平均提升19.8%。
### 核心结论
记忆能力可以像CoT推理能力一样，通过架构修改和针对性中训内化为基础模型的原生能力，无需依赖外部模块实现
