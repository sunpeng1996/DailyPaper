---
title: Can Decision Models Replace LLMs in Real-World Contact Center Classification
  and Judging Tasks?
title_zh: 决策模型在真实呼叫中心分类与判定任务中替代LLM的可行性分析
authors:
- Md Tahmid Rahman Laskar
- Xue-Yong Fu
- Shashi Bhushan TN
affiliations:
- Dialpad Inc.
arxiv_id: '2611.22949'
url: https://arxiv.org/abs/2611.22949
pdf_url: https://arxiv.org/pdf/2611.22949
published: '2026-11-17'
collected: '2026-11-18'
category: Eval
direction: 大模型评估 · 决策类任务选型指导
tags:
- Decision Model
- LLM Evaluation
- Zero-shot
- Classification
- Cost Optimization
- Contact Center
one_liner: 零-shot场景下对比9种决策模型与13种LLM在8类呼叫中心任务的表现，给出落地选型指导
practical_value: '- 电商客服/售后意图分类、合规判定等边界明确的决策类任务，可优先尝试决策模型替代通用LLM，大幅降低推理成本同时保证效果

  - 落地时可基于决策模型的预测置信度做分级路由：高置信结果直接输出，低置信转通用LLM/人工审核，兼顾成本与准确性

  - 决策模型选型不能仅看整体准确率，需重点验证其拒答表现、位置偏置水平是否匹配业务要求

  - 小参数决策模型不适合复杂判定类任务，这类场景仍需使用大尺寸决策模型或通用LLM'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
呼叫中心存在大量意图识别、合规校验、知识库匹配等边界明确的决策类任务，通用生成式LLM推理成本高，决策模型作为低成本替代方案的真实场景效果尚未得到系统验证。
### 方法关键点
零-shot设置下，对比9款决策模型、13款生成式LLM在8类呼叫中心任务（6类分类、2类判定）的效果、成本表现。
### 关键结果
- 多数决策模型在分类任务上效果追平前沿LLM，闭源API决策模型单请求成本为所有参评API模型最低
- 决策模型高置信预测准确率更高，可支持生产环境选择性路由
- 多数决策模型核心短板是拒答率低，贡献了与最强LLM的大部分效果差（仅Gemini-Decision-1例外）
- 小参数决策模型判定任务效果下滑明显，且更容易出现位置bias
