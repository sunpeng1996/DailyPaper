---
title: Selective State-Space Adaptation and Retrieval for Language Model Reasoning
title_zh: 面向大模型推理的选择性状态空间适配与检索框架
authors:
- Atahan Dokme
- Larry Heck
affiliations:
- Georgia Institute of Technology
arxiv_id: '2607.19326'
url: https://arxiv.org/abs/2607.19326
pdf_url: https://arxiv.org/pdf/2607.19326
published: '2026-07-21'
collected: '2026-07-22'
category: Training
direction: 参数高效微调 · 大模型推理优化
tags:
- LoRA
- Mamba
- Parameter-Efficient Fine-Tuning
- Multi-hop Reasoning
- Retrieval Adapter
one_liner: 提出token级MaLoRA和上下文级MaRA两种Mamba增强适配器，多跳推理超LoRA平均+6.8F1
practical_value: '- 可复用MaLoRA的动态门控思路，给业务侧现有LoRA微调任务增加Mamba驱动的token级缩放，适配多轮导购Agent、长序列用户行为理解等场景，仅增加50%参数量，训练成本和原生LoRA基本持平

  - MaRA的模型附属检索架构可直接迁移到RAG类业务，无需额外训练独立召回/重排模型，直接复用LLM前16层隐藏状态做上下文段打分，在商品评价检索、用户历史行为段筛选等场景效果优于BM25和通用Embedding，参数量仅新增3M

  - 分层适配的设计逻辑可复用：token级权重动态调整+段级上下文筛选的组合，可直接落地到长上下文复杂需求处理场景（如大模型重排、多轮会话意图理解），两者增益叠加几乎无重叠'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
原生LoRA采用静态参数更新，对所有输入、所有token都施加相同的适配强度，既无法捕捉多步推理任务中token级、实例级的状态变化，也不能自主筛选上下文中的相关片段，限制了大模型在长上下文、多跳推理场景的表现。

### 方法关键点
- MaLoRA：用Mamba模块替换LoRA的静态缩放因子，基于输入序列的历史token状态生成动态标量门控，动态放大/抑制每个token对应的LoRA更新强度，参数量仅比原生LoRA高50%
- MaRA：复用冻结大模型前16层的隐藏状态，对上下文段落做注意力池化后，用Mamba做段级序列建模，打分筛选和查询最相关的top-k片段，无需训练独立召回模型，仅新增约3M参数量
- 两个适配器独立作用，MaLoRA负责token级权重适配，MaRA负责上下文段筛选，增益互补无明显重叠

### 关键结果
在3个冻结基座（Qwen-2.5-7B、Llama-3.1-8B、Gemma-2-9B）、2个多跳推理数据集上对比LoRA、DoRA、TopLoRA等基线：单独MaLoRA较LoRA平均提升3.1~7.9 F1，长上下文RULER QA-2任务平均提升2.2%准确率；单独MaRA段检索召回比BM25高33.6pp，比8B参数的Qwen3-Embedding高5.1pp；两者结合的全系统较LoRA平均提升+6.8 F1（相对+10.5%），最优场景提升+9.3 F1（相对+18.2%）。

**最值得记住的一句话**：基于状态空间模型的分层动态适配，是比单纯提升LoRA秩、增加参数量更高效的大模型推理优化路径，可与检索能力无缝结合。
