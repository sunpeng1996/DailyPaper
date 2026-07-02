---
title: 'Identifying and Resolving Pitfalls of Knowledge-Based VQA Benchmarks: Auditing,
  Repairing, and Augmenting'
title_zh: 知识型视觉问答基准缺陷识别与修复的审计增强方法
authors:
- Qian Ma
- S M Rayeed
- Charles V. Stewart
- Qiong Wu
- Yao Ma
affiliations:
- Rensselaer Polytechnic Institute
- AT&T Chief Data Office
arxiv_id: '2607.00159'
url: https://arxiv.org/abs/2607.00159
pdf_url: https://arxiv.org/pdf/2607.00159
published: '2026-06-30'
collected: '2026-07-02'
category: Eval
direction: 多模态大模型评测 · KB-VQA基准优化
tags:
- KB-VQA
- VLM
- Evaluation
- Benchmark
- RAG
one_liner: 揭示现有KB-VQA基准核心假设失效问题，提出审计修复与多实体增强协议优化评估
practical_value: '- 构建多模态商品搜索/问答评测集时可复用审计修复协议，先校验答案可推导性、问题约束完整性，避免评测结果失真

  - 针对电商多模态交互Agent场景，可引入多实体增强策略构造歧义样本，倒逼模型提升视觉-知识映射与消歧能力

  - 评估多模态RAG系统时不能仅依赖准确率指标，需增加推理路径可验证性维度，避免高估模型实际落地能力'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有KB-VQA评测默认以准确率作为知识落地推理能力的代理指标，隐含三大易被忽视的前提假设：标注答案可从关联知识库推导、问题约束充分无歧义、视觉场景需要落地消歧。实际现有基准普遍违反上述假设，大量样本存在答案缺失/矛盾、问题约束不足、单实体场景跳过视觉-知识映射等问题，导致模型排名失真、推理能力被高估。
### 方法关键点
1. 提出系统化审计修复协议，校验并修正样本的答案可推导性、问题清晰度缺陷；
2. 提出受控多实体增强协议，构造带视觉歧义的样本，强制模型完成复杂视觉-知识映射与消歧推理。
### 关键结果
在修正+增强后的基准上重新评测，模型性能趋势与原基准存在显著差异，原基准普遍高估模型推理能力的问题得到有效解决。
