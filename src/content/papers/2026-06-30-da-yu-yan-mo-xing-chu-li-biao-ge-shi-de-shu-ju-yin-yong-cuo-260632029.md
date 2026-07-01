---
title: 'When LLMs Read Tables Carelessly: Measuring and Reducing Data Referencing
  Errors'
title_zh: 大语言模型处理表格时的数据引用错误：测量与缓解方法
authors:
- Yuqing Yang
- Qi Zhu
- Zhen Han
- Boran Han
- Zhengyuan Shen
- Shuai Wang
- Vassilis N. Ioannidis
- Huzefa Rangwala
affiliations:
- University of Southern California
- AWS AI Labs
arxiv_id: '2606.32029'
url: https://arxiv.org/abs/2606.32029
pdf_url: https://arxiv.org/pdf/2606.32029
published: '2026-06-30'
collected: '2026-07-01'
category: LLM
direction: 大语言模型 · 表格任务错误检测与缓解
tags:
- Data Referencing Error
- Table Reasoning
- Critic Model
- Rejection Sampling
- LLM Evaluation
one_liner: 系统分析LLM表格任务的数据引用错误，提出轻量检测critic与推理优化方案，最高提升准确率12%
practical_value: '- 电商/客服Agent处理订单表、商品属性表等结构化数据查询场景，可复用DRE错误分类和检测框架，避免LLM错引/遗漏表格数据导致的回答错误，提升回答可信度

  - 推理时优化可直接复用critic过滤+分段拒绝采样策略，无需微调基座模型，仅增加轻量检测模块即可提升结构化查询准确率，效果比纯prompt引导更稳定

  - 4B小参数critic的两阶段训练范式（SFT蒸馏大模型标注+RLVR微调）可直接迁移，小模型检测成本远低于调用大模型做judge，适合线上高吞吐场景部署

  - 可将DRE作为补充评估维度，弥补仅看最终答案准确率的评估盲区，精准定位LLM在结构化数据处理场景的bad case'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM在表格类任务上表现优异，但普遍存在数据引用错误（DRE）：即使正确理解表格结构，仍会错引、编造或遗漏表格值，这类错误会直接破坏推理步骤的可靠性，且仅评估最终答案准确率的常规指标无法捕捉到DRE，此前相关分析均为小规模、单模型的碎片化研究，缺乏系统评估和低成本缓解方案。
### 方法关键点
- 拆分表格DRE为两类：错误引用（单值错配、行列混淆、编造内容）、信息遗漏（遗漏满足条件的整行/整列内容）
- 采用带ground truth的LLM-as-a-Judge（Sonnet 3.7）自动检测DRE，针对长推理响应做分段检测，人工校验准确率达92.67%
- 推理时优化：两类无侵入缓解策略，一是critic-based过滤，采样N个候选后筛选无DRE的子集再做多数投票；二是分段拒绝采样，对带思考分段的推理模型逐段检测，不合格则重采样该段，避免错误传播
- 轻量critic训练：基于Qwen3-4B-Instruct，采用两阶段训练，第一阶段用大模型标注结果做SFT蒸馏，第二阶段用RLVR微调提升泛化性，仅需单一数据集标注即可跨任务跨模型泛化
### 关键结果
- DRE在所有测试模型（1.7B~20B参数）和所有表格任务（QA、事实校验、表格转文本）中普遍存在，Qwen3-8B即使加引导prompt仍有12.5%的DRE率
- 用Sonnet 3.7做critic时，拒绝采样最高可提升准确率11.96%
- 训练得到的4B Critic平均F1达78.2%，比基线提升8.65%，用于拒绝采样可稳定降低DRE率，提升准确率最高6.89%
### 核心结论
数据引用错误是LLM在结构化数据任务中普遍存在的可避免错误，而非模型能力的根本限制，仅通过推理时的critic检测和重采样即可显著提升效果
