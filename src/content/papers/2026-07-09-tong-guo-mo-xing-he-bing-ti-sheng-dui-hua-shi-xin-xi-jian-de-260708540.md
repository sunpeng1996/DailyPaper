---
title: Improving Ad-hoc Search Effectiveness for Conversational Information Retrieval
  via Model Merging
title_zh: 通过模型合并提升对话式信息检索的即席搜索效果
authors:
- Ahmed Rayane Kebir
- Jose G. Moreno
- Lynda Tamine
affiliations:
- University of Toulouse, IRIT
arxiv_id: '2607.08540'
url: https://arxiv.org/abs/2607.08540
pdf_url: https://arxiv.org/pdf/2607.08540
published: '2026-07-09'
collected: '2026-07-10'
category: RecSys
direction: 对话式检索 · 模型合并优化
tags:
- Conversational Retrieval
- Model Merging
- Dense Retrieval
- Catastrophic Forgetting
- Zero-shot
one_liner: 零训练成本合并即席与对话检索模型，缓解灾难性遗忘，提升跨场景泛化性能
practical_value: '- 电商对话导购、智能客服问答场景，无需多任务重训，直接合并通用商品检索模型与小样本微调的对话检索模型，节省70%以上的模型适配算力成本，同时缓解单轮搜索效果下降问题

  - 合并时优先选用Model Soup或Slerp策略，采用分层插值调优：Transformer低层多分配对话模型权重、高层多分配通用检索权重，仅需千级别验证样本即可得到最优融合系数

  - 业务同时存在单轮搜索、多轮对话两个检索入口时，可共用一套合并后的模型，无需部署两套独立模型，降低推理服务维护成本和资源占用

  - 缺标注数据的垂类对话检索场景，合并通用检索模型与小样本垂类微调模型，可提升OOD泛化性能，最多带来10%以上的top-k检索精度提升'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
对话式信息检索（CIR）需结合多轮上下文解析用户意图，当前主流方案是将通用即席检索模型在对话数据集上微调，但会引发灾难性遗忘，原有单轮检索性能最高下降24%；现有多任务学习方案需联合重训、算力成本高，早期停止策略无法同时兼顾单轮、多轮场景的性能，亟需零训练成本的方案平衡两类场景效果。

### 方法关键点
- 采用同源模型合并范式：以在MS MARCO上预训练的通用即席dense retriever ANCE为基底，合并其微调后的对话检索变体QRACDR，无需额外训练数据和梯度更新
- 对比两种主流合并策略：①Model Soup：线性加权合并全量参数，实现简单；②Slerp：球面线性插值，沿参数向量的角路径合并，更好保留模型权重范数
- 分层插值优化：对Transformer不同层设置独立的融合系数，仅在域内小验证集上调优系数，OOD数据完全不参与调参，避免数据泄露

### 关键结果
实验覆盖7个公开检索数据集，对比基线包括原始ANCE、微调后QRACDR、多任务微调、早期停止策略：
1. 合并模型性能与多任务微调相当，将对话模型在MS MARCO上的14% NDCG@3损失降低到3%
2. OOD对话场景CAsT20上NDCG@3最多提升10.11%，完全消除对话模型在重写query场景下8.47%的性能损失
3. 零-shot跨任务场景下NDCG@3最高提升15%

> 最值得记住的结论：同源模型的零成本参数合并，是解决下游微调灾难性遗忘、平衡多场景性能的高性价比方案，效果优于多任务重训和早期停止
