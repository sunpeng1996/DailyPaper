---
title: Quantum-Inspired Pairwise Ranking Aggregation via Active LLM Feedback
title_zh: 基于主动LLM反馈的量子启发式成对排序聚合方法
authors:
- Quan Mai
- Susan Gauch
- Gibson Nkhata
affiliations:
- University of Arkansas, Fayetteville
- Walmart Inc.
arxiv_id: '2610.38683'
url: https://arxiv.org/abs/2610.38683
pdf_url: https://arxiv.org/pdf/2610.38683
published: '2026-10-28'
collected: '2026-10-30'
category: RecSys
direction: 多召回源排序融合 · LLM轻量化重排
tags:
- RankingAggregation
- LLM-as-Judge
- Reranking
- QuantumInspired
- LowCostInference
one_liner: 基于量子启发框架与主动LLM成对判断实现低开销多召回源排序融合，效果优于无监督基线
practical_value: '- 电商搜索/推荐多召回路融合场景可直接复用「高分歧对采样+少量LLM成对判断」范式，每query仅需5-30次LLM调用即可超过RRF等无监督基线，成本比全量LLM重排低一个数量级

  - 可直接落地两种权重更新策略：动量融合适合实时性要求高的在线场景，累计历史重拟合适合精度优先的离线/准实时场景，无需标注数据或模型微调

  - LLM成对判断可复用置信度过滤trick：仅保留logit gap高于阈值的结果更新权重，实测770M级小模型即可满足判断需求，无需调用大参数LLM降低成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多召回源排序融合方案存在明显短板：无监督方法（如RRF、CombSUM）实现简单但缺乏场景自适应能力，效果上限低；有监督LTR或全量LLM重排效果好，但需要大量标注数据或极高的推理成本，在零样本、动态业务场景下落地难度大，亟需兼顾效果与成本的融合方案。
### 方法关键点
- 基于量子启发框架将文档对建模为纠缠量子系统，每个基础召回源对应观测算子，理论上证明最优融合结果为各召回源得分的线性加权，最终排序可通过pointwise线性融合快速计算，无需复杂的成对/列表推理
- 主动采样Top-r召回结果中不同召回源排序分歧最高的文档对喂给LLM做成对判断，仅保留LLM输出logit gap高于阈值的高置信度结果更新融合权重，过滤噪声
- 提供两种适配不同场景的权重更新规则：动量融合用当前批次结果平滑历史权重，稳定性高；累计历史重拟合用全量历史判断结果更新权重，精度更优
### 关键实验
在BEIR、TREC DL 2019/2020共6个基准上测试，以Llama-3.1-8B-Instruct为Judge：累计历史重拟合配置在4个基准上显著优于最优无监督基线（p<0.05），仅需5次LLM调用即可超过最优无监督基线，单query平均仅需25-30次调用；成本仅为SOTA零样本LLM重排的1/10左右，仅用5.6%的LLM调用量超过PRP-Graph重排效果，仅落后最优堆排序重排0.47 NDCG@10。
### 核心结论
多召回源融合无需全量LLM重排，仅对高分歧样本做少量LLM成对判断就能以极低的成本获得接近SOTA重排的效果。
