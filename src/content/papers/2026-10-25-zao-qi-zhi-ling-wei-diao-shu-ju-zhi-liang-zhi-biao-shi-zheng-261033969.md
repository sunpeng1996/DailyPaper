---
title: '"High-Quality" Data for Early-Stage Instruction Tuning: An Empirical Study
  of Data Quality Metrics'
title_zh: 早期指令微调数据质量指标实证研究：各类指标有效性对比
authors:
- Vladimir Necula
- David Gvadzabia
- Sofia Serrano
affiliations:
- University of Cambridge
- Lafayette College
arxiv_id: '2610.33969'
url: https://arxiv.org/abs/2610.33969
pdf_url: https://arxiv.org/pdf/2610.33969
published: '2026-10-25'
collected: '2026-10-27'
category: LLM
direction: 指令微调 · 数据质量评估
tags:
- Instruction Tuning
- SFT
- Data Quality
- Response Ratio
- LLM Alignment
one_liner: 通过跨模型跨数据集控制实验，验证响应长度占比是预测指令微调数据效用最稳健的指标
practical_value: '- 做Agent/智能客服SFT数据筛选时，优先用response ratio（响应token数/提示token数）作为低成本筛选指标，无需复杂语义模型即可快速过滤低效用数据

  - 做电商导购文案生成、商品属性生成等下游任务SFT时，优先构造高response ratio的训练样本，固定token预算下能更快提升模型生成效果

  - 自研LLM4Rec模型做指令微调时，可复用token-balanced分桶方法做数据效用评估，避免按样本数分桶带来的训练成本偏差

  - 语义对齐、语义密度类指标效果高度依赖数据集分布，不建议作为单独筛选指标，可搭配response ratio做二次过滤'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
指令微调是LLM对齐的核心环节，但“数据质量”长期定义模糊，现有候选指标（语义对齐、语义密度等）缺乏跨场景的稳健性验证，固定训练预算下如何快速筛选高效用SFT数据是产业界核心痛点。

### 方法关键点
- 选取4类样本级质量指标：总长度、response ratio（响应token数/提示token数）、语义密度（响应token逆对数频率均值）、语义对齐（prompt与响应的句向量余弦相似度）
- 采用token-balanced分桶：按指标排序后按总token量三等分，保证每桶训练成本一致，规避按样本数分桶的偏差
- 控制变量实验：在Qwen3.5-9B、Llama-3.1-8B两个基座，Natural Instructions、FLAN两个数据集上用LoRA微调，以验证困惑度、LLM-as-judge得分作为效用评估标准
- 交叉消融实验：分别移除高response ratio、高语义对齐样本后重训，验证指标独立效用

### 关键结果
- 跨所有模型-数据集组合，高response ratio分桶的模型验证困惑度比低/中分桶平均低8%~12%，LLM-as-judge得分平均高0.7~1.2分
- 语义对齐、语义密度的效用高度依赖数据集：Natural Instructions中高对齐分桶效果好是因为48.7%的高response ratio样本落在高对齐分桶；FLAN中高对齐分桶效果差是因为49.2%的高response ratio样本落在中对齐分桶
- 交叉消融后，移除高对齐样本对response ratio的效果影响<5%，但移除高response ratio样本后语义对齐的效果下降超过40%

最值得记住的结论：固定token预算下，高响应占比的样本带来的训练收益远高于语义更对齐但响应更短的样本，简单的长度占比指标即可覆盖绝大多数数据筛选需求。
