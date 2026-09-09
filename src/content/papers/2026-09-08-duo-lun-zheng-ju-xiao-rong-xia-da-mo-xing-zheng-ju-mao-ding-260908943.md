---
title: Evaluating and Improving Evidence-Grounded Fact-Checking in LLMs via Multi-Round
  Evidence Ablation
title_zh: 多轮证据消融下大模型证据锚定事实核查的评估与优化
authors:
- Xingyu Deng
- Mingzi Cao
- Nikolaos Aletras
- Xi Wang
- Mark Stevenson
affiliations:
- University of Sheffield
arxiv_id: '2609.08943'
url: https://arxiv.org/abs/2609.08943
pdf_url: https://arxiv.org/pdf/2609.08943
published: '2026-09-08'
collected: '2026-09-09'
category: RAG
direction: LLM事实核查 · 证据依赖评估与训练优化
tags:
- Fact-Checking
- RAG
- LLM-Evaluation
- LoRA
- Counterfactual-Training
one_liner: 提出证据消融评估框架FAE与反事实训练框架REAL，强化LLM事实核查的证据依赖度且不损失预测精度
practical_value: '- 电商/广告领域的RAG类业务（商品问答、客服Agent、合规校验）可复用FAE框架，多轮删除模型引用的证据片段，验证模型回答是否真的依赖检索结果而非幻觉/参数知识，解决RAG「伪引用」问题

  - 做RAG的SFT训练时，可复用REAL的正负样本构造方案：正样本给全上下文输出正确结果，负样本删除支撑证据强制输出「信息不足」，大幅提升回答的证据锚定度，避免参数知识干扰

  - 电商平台虚假宣传核查、商品参数校验场景可直接复用REAL训练方案，基于多源商品官方信息构造训练集，让模型仅基于录入的官方信息判定宣传真实性，不受预训练里的过时/错误商品知识影响'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前基于RAG的LLM事实核查系统，仅靠预测准确率无法区分决策是来自给定证据还是预训练参数知识，参数知识的过时、错误会导致高风险场景（如合规校验、电商虚假宣传判定）的决策不可靠，现有标准评测指标无法捕捉这种证据依赖度不足的问题。

### 方法关键点
- 提出**FAE**评估框架：迭代删除模型每轮输出的支撑证据，观测预测标签变化，通过IS（即时敏感度）、ER（终态保留率）、IO（理想偏移度）三个指标量化证据依赖程度，理想状态下删除支撑证据后模型应立即输出`NOT_ENOUGH_INFO`
- 提出**REAL**训练框架：构造正反样本对，正样本输入全量证据输出正确标签+证据索引，负样本删除所有支撑证据强制输出信息不足；同时用多模型投票补充标注证据集，避免标注不全导致负样本残留有效支撑证据
- 训练时联合优化正反样本损失，仅需LoRA微调即可生效，无需全量调整LLM参数

### 关键结果
在FEVER、SciFact、Climate-FEVER、Check-COVID四个跨领域数据集上实验，对比GPT-4o-mini、Gemini-2.5-Flash、Qwen-2.5-32B等基线：
- 基于Llama3.1-8B的REAL在FEVER上标签准确率从83.08%提升至95.66%，IS（证据删除后准确率下降幅度）从43.79%提升至99.06%，完全达到理想证据依赖表现
- 跨领域迁移能力优异，在未微调的3个域外数据集上，FAE三项指标均显著优于所有基线，同时保持最高的标签准确率
- 对比标准SFT，REAL仅损失不到1%的初始准确率，证据依赖度提升8倍以上

> 最值得记住的结论：大模型在RAG场景下的高准确率不代表其回答真正依赖检索到的证据，仅靠标准评测指标会掩盖参数知识导致的不可靠风险
