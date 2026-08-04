---
title: 'LiveMem: Maintaining Memory State Continuity in Long-Running LLM Inference'
title_zh: LiveMem：长时运行LLM推理的内存状态连续性维护方法
authors:
- Zhichen Liu
- Ruihan Sun
- Hengjie Yang
- Zipeng Wu
- Zhaohan Chen
- Xiaofan Zhang
- Yang Xu
affiliations:
- NatureSelect.AI
- Southern University of Science and Technology
- Xidian University
arxiv_id: '2608.02515'
url: https://arxiv.org/abs/2608.02515
pdf_url: https://arxiv.org/pdf/2608.02515
published: '2026-08-03'
collected: '2026-08-04'
category: LLM
direction: LLM长时推理 · 内在内存机制
tags:
- Long-Context LLM
- Intrinsic Memory
- Inference Optimization
- Agent Memory
- KV Cache
one_liner: 为预训练注意力LLM新增并行GDN2内存分支，实现超上下文窗口的持续状态连续性推理
practical_value: '- 长时对话Agent可复用LiveMem架构：在现有LLM注意力分支外新增并行GDN2内存分支，冻结主干参数仅训练内存分支，大幅降低长时记忆实现成本，适配电商客服、用户画像持续建模场景

  - 训练范式可直接复用：先用长文档QA数据热身激活内存分支，再用混合任务做SFT+RL，强制模型在上下文截断时依赖内存状态输出，避免模型绕过内存分支

  - 上下文调度策略可迁移：仅保留系统prompt作为attention sink，其他KV采用FIFO淘汰，确保训练推理一致性，可直接集成到现有LLM推理引擎的KV
  cache管理模块

  - 可与RAG方案互补：RAG负责精准召回历史关键信息，LiveMem的内存状态负责维护整体会话上下文连贯性，共同提升长时交互Agent体验'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前长时运行的LLM助手与Agent的交互历史会远超上下文窗口上限，现有RAG、摘要、上下文截断方案仅能提供按需历史访问能力，无法在上下文切换时维持全生命周期的连续状态，导致多轮交互连贯性差、跨上下文的历史信息利用率低。
### 方法关键点
- 架构设计：在预训练全注意力LLM的每个注意力层新增并行GDN2内存分支，输出直接叠加到原注意力输出，主干参数冻结，内存分支初始化为0避免影响原模型效果
- 上下文调度：仅保留系统prompt作为固定attention sink，其他KV采用FIFO淘汰，训练与推理均保持该约束确保一致性，被淘汰KV的信息提前写入固定容量内存状态
- 训练范式：设计内存导向的后训练任务，先用长文档QA做SFT激活内存分支，再用GRPO强化学习优化，强制模型在上下文截断时依赖内存状态作答
### 关键结果
在Wiki QA、对话QA、测试时学习、长文档QA四大类任务上对比Qwen3-4B、RAG、δ-Mem等基线，限制上下文窗口8k/32k：整体准确率LiveMem-RL达51.9%，超过基线最优原生Qwen3的45.8%；当证据完全被逐出上下文窗口时，LiveMem-RL准确率达16.5%，比原生Qwen3高13.4个百分点；内存状态的信息准确率随证据距窗口距离增加仅小幅衰减，稳定性显著优于其他方案。
> 最值得记住：检索机制负责解决「读什么历史」的问题，循环内存状态负责解决「读完后如何全生命周期维持信息连贯性」的问题，二者正交互补
