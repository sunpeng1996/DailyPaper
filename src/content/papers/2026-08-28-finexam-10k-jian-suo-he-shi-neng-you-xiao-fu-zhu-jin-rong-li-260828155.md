---
title: 'FinExam-10K: When Retrieval Helps Financial Reasoning?'
title_zh: FinExam-10K：检索何时能有效辅助金融推理
authors:
- Yan Lin
- Jingyu Sun
- Zhongliang Guo
- Qing Li
- Zhuohan Xie
- Yuxia Wang
affiliations:
- INSAIT, Sofia University "St. Kliment Ohridski"
- Newcastle University
- University of Manchester
- University of Melbourne
- University of Aberdeen
arxiv_id: '2608.28155'
url: https://arxiv.org/abs/2608.28155
pdf_url: https://arxiv.org/pdf/2608.28155
published: '2026-08-28'
collected: '2026-08-31'
category: RAG
direction: RAG 金融推理评测与触发优化
tags:
- RAG
- Benchmark
- Financial Reasoning
- Gating Mechanism
- Function Calling
one_liner: 构建覆盖CFA全三级、FRM全两级的金融推理评测基准，验证门控触发的FunctionGraph-RAG可提升推理效果
practical_value: '- 复杂推理场景不要盲目全量启用RAG，可训练轻量门控仅对7%-10%高难度query触发RAG，兼顾 latency 与效果

  - 多模块协同推理系统要做正负收益权衡：Function-RAG类方案能救回错误但也会误改正确答案，需补充收益兜底逻辑

  - 垂直领域任务做基准评测时可拆分「全知识覆盖」「给定上下文推理」双轨道，区分知识缺失和推理能力不足的问题'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有金融推理评测缺乏统一覆盖CFA全三级、FRM全两级的基准，同时RAG在复杂推理场景下收益边界模糊，常出现救回错误与误改正确答案的收益抵消问题。
### 方法关键点
构建含10198道专家重标注题目的FinExam-10K评测集，拆分「全知识覆盖」「给定上下文推理」双轨道，区分知识缺失与推理能力短板；针对Function-RAG、FunctionGraph-RAG净收益为负的问题，训练仅用公开数据的轻量门控模块，根据query和初始回答判断是否触发RAG。
### 关键结果
17款参测模型整体最优准确率为85.29%，Hard难度赛道全量知识覆盖任务最优准确率仅34.68%；门控模块仅对7.9%的query触发FunctionGraph-RAG，在5088道留验集上准确率从70.83%提升至71.23%（p=0.0446）
