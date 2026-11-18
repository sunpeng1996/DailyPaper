---
title: 'Deal With It: On Better Schedules for Listwise Reranking'
title_zh: 列表式LLM重排优化调度：基于轮询分桶的DealRank方案
authors:
- Benjamin Clavié
- Herumb Shandilya
- Hanna Lichtenberg
- Aamir Shakir
- Makoto P. Kato
affiliations:
- Mixedbread
- National Institute of Informatics
- University of Tsukuba
arxiv_id: '2611.22392'
url: https://arxiv.org/abs/2611.22392
pdf_url: https://arxiv.org/pdf/2611.22392
published: '2026-11-17'
collected: '2026-11-18'
category: RecSys
direction: 检索重排 · LLM列表式重排调度优化
tags:
- LLM Reranking
- Listwise Ranking
- Scheduling
- Retrieve-then-Rerank
- Efficiency
one_liner: 提出按检索排名轮询分桶的DealRank调度，无损排序质量下大幅降低列表式LLM重排延迟
practical_value: '- 现有列表式LLM重排调度（如BlitzRank）可直接替换原连续分桶逻辑为按检索排名轮询分桶，无需改动其他逻辑即可将修复调用占比从59%降至14%，降低延迟无质量损失

  - 百/千级候选重排的业务场景可直接复用DealRank的分层调度逻辑：100候选2轮完成、1000候选3轮完成，相比滑动窗口提速11倍，比并发BlitzRank提速1.1~1.4倍

  - 所有并行分桶类任务（如多batch打分、粗排分桶选优）都可借鉴轮询分桶思路，避免高相关候选集中在单一分桶被截断，尤其适用于上游召回排序有一定质量的场景'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Listwise LLM重排受限于上下文窗口大小与上下文退化问题，无法单次处理数百条候选，依赖多轮调度完成重排；现有并行调度多采用连续分桶逻辑，上游召回返回的高相关候选易集中在单一桶内，被配额截断后需要额外修复调用，既提升延迟又导致调度轮数不稳定。

### 方法关键点
- 核心分桶逻辑：将上游召回返回的候选按原生排名轮询分桶（类似发牌），每个桶均匀分布不同排名段的候选，避免高相关候选集中在单一分桶被截断
- DealRank调度规则：100候选场景分为5个桶各20条，并行重排后每桶取Top4进入最终20条重排，共2轮固定轮数；1000候选场景采用分层轮询分桶，仅需3轮固定轮数，无额外修复调用
- 理论证明：在上游召回结果的相关度随排名单调下降的假设下，轮询分桶是等配额分桶策略中截断真实Top10候选最少的最优方案，性能优于连续分桶和随机分桶

### 关键结果
实验覆盖TREC-DL19/20、BEIR共1622条查询，上游召回采用BM25、Qwen3-Embedding-4B，对比7种主流调度方案，在6款开源/闭源LLM上验证：
- nDCG@10与最优调度差距小于0.1，无显著质量损失
- 比并发BlitzRank提速1.1~1.4倍，1000候选场景下比滑动窗口提速11倍
- 轮询分桶替换BlitzRank的连续分桶后，修复调用占比从59%降至14%，无显著质量变化

### 核心结论
上游召回有一定质量的前提下，并行分桶选优场景用轮询分桶替代连续分桶，是几乎无成本的效率优化手段
