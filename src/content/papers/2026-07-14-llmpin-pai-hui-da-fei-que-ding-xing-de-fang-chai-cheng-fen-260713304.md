---
title: Where Does the Noise Come From? A Variance-Components Decomposition of Non-Determinism
  in LLM Brand Answers
title_zh: LLM品牌回答非确定性的方差成分拆解与采样预算优化
authors:
- Dmitrij Żatuchin
affiliations:
- Estonian Entrepreneurship University of Applied Sciences
- Rankfor.AI
arxiv_id: '2607.13304'
url: https://arxiv.org/abs/2607.13304
pdf_url: https://arxiv.org/pdf/2607.13304
published: '2026-07-14'
collected: '2026-07-16'
category: Eval
direction: LLM品牌测量 · 方差分解优化
tags:
- Variance Decomposition
- Generalizability Theory
- LLM Measurement
- Brand Reputation
- Sampling Allocation
one_liner: 拆分LLM品牌回答4类方差来源，给出最低成本达目标可靠性的采样预算分配规则
practical_value: '- 做LLM品牌口碑/推荐声量测量时，无需重复调用相同prompt超过5次，相同预算优先覆盖多语言、多模型，误差降低效率是新增重复的15倍

  - 跨境电商监测AI渠道品牌声量时，必须纳入多语言采样：查询语言占单条回答方差的26.5%，品牌-语言交互方差达8.6%，单语言测量偏差极大

  - 设计LLM生成结果稳定性评估方案时，可直接复用本文交叉随机效应方差分解框架，拆分不同扰动因素贡献，优化采样成本结构

  - 生成式推荐的效果验证阶段，可参考本文可靠性分配逻辑，优先拓宽测试维度（如query改写、多模型比对）而非重复相同用例'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前行业测量LLM对品牌的评价/推荐结果时，普遍采用固定重复调用相同prompt（通常5次）取平均的惯例，完全忽略了prompt改写、模型差异、查询语言等其他更大的噪声来源，不仅造成采样预算浪费，还导致测量可靠性极低，单条LLM回答几乎不携带有效品牌区分信号。
### 方法关键点
- 基于概化理论构建交叉随机效应模型，将LLM品牌回答的总方差拆分为4个核心独立来源：同prompt重复采样、prompt改写、模型身份、查询语言，以及各维度与品牌的交互项
- 设计3组嵌套REML拟合模型：全语料主效应分解、稳定性子集（同prompt重复5次）的纯采样方差隔离、品牌-维度交互项分解，输出各来源的ICC占比
- 结合方差成分构建决策优化模型，求解固定预算下重复次数、prompt数量、模型数量、语言数量的最优分配组合，实现测量可靠性最大化
### 关键结果
实验基于12933条中东欧20个品牌、8种语言、3个模型（GPT-5.2、Gemini 3 Flash、Perplexity）的回答数据集，核心结论：1. 查询语言占单条回答总方差的26.5%，品牌本身仅占1.5%，单条回答的品牌排序可靠性仅0.01；2. 同prompt重复采样方差占34.8%，但超过5次重复后每新增5次仅降低误差0.0003；3. 相同预算下，新增语言的误差降低效果是新增重复的15倍，全维度覆盖下最高品牌排序可靠性仅0.36。
### 核心结论
LLM品牌测量的可靠性来自多语言、多模型的广度覆盖，而非相同prompt的重复深度。
