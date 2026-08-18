---
title: 'When Context Misleads: Intent-Guided Decoding for Robust Retrieval-Augmented
  Generation'
title_zh: 面向鲁棒RAG的意图引导解码：解决检索上下文误导问题
authors:
- Haolin Jin
- Pengyue Yang
- Huaming Chen
affiliations:
- The University of Sydney
arxiv_id: '2608.16515'
url: https://arxiv.org/abs/2608.16515
pdf_url: https://arxiv.org/pdf/2608.16515
published: '2026-08-17'
collected: '2026-08-18'
category: RAG
direction: RAG鲁棒性优化 · 意图感知解码仲裁
tags:
- RAG
- Decoding
- Factuality
- Faithfulness
- Intent-Aware
- Source-Arbitration
one_liner: 解码阶段基于用户意图动态仲裁RAG上下文与参数记忆的信任权重，无需改模型或检索管线
practical_value: '- 可复用IGD的两级仲裁思路优化电商导购Agent的RAG系统：用户要求严格按商品详情回答时优先检索上下文，求客观常识时优先模型参数记忆，避免被爬取的错误商品信息误导

  - 答案层过滤+token级校正的轻量架构可迁移到搜索Query改写/智能客服场景：高置信度错误的召回结果直接拦截，其余场景仅微调解码分布，不影响正常召回结果的使用

  - 无需重新训练LLM、不改动现有检索管线的特性适合业务快速迭代，可直接叠加到现有RAG系统上做事实性增强，几乎无额外迁移成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RAG对检索上下文采用固定信任策略，要么过度信任错误/误导性上下文导致事实错误，要么过度不信任上下文，无法满足用户「严格按给定内容回答」的需求，存在事实性（符合客观真理）和忠实性（符合给定上下文）的天然权衡，固定策略无法适配不同用户意图。

### 方法关键点
- 设计三个并行解码分支：用户分支（原始RAG输入）、上下文分支（强制按检索内容回答）、记忆分支（闭卷仅靠参数记忆回答，采用3种prompt ensemble降低波动）
- 两级仲裁机制：第一级答案层过滤，对记忆分支置信度远高于上下文分支、且用户分支不排斥记忆答案的高置信冲突场景，直接返回记忆答案；其余场景走token级校正
- Token级校正：仅当上下文与记忆分支的token分布JSD超过阈值时激活干预，结合用户意图先验（严格模式优先上下文、事实模式优先记忆）、分支熵置信度、源可靠性加权调整用户分支的token分布

### 关键结果
在3个忠实QA基准（KILT-NQ、TriviaQA、SQuAD）和3个事实冲突基准（ConflictBank、NQ-Swap、CounterFact）上测试5款主流LLM，对比Direct RAG、SCR/RCR置信度推理、MADAM-RAG多Agent等基线：
- Truth模式下，IGD较Direct RAG最高提升65.4pp的事实准确率，同时忠实QA准确率仅下降0.6-7.2pp，整体意图对齐得分（IA）提升9.6-23pp
- Strict模式下，IGD较Direct RAG平均提升1.3-3.9pp的上下文遵从准确率，未损害用户要求严格按上下文回答的体验

最值得记住的结论：RAG的核心矛盾不是召回质量，而是根据用户意图动态校准对检索上下文和参数记忆的信任度，解码阶段的轻量干预可以在不改动现有管线的前提下大幅提升鲁棒性。
