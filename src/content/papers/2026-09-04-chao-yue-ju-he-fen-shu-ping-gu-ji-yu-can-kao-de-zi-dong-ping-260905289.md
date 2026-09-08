---
title: 'Beyond Aggregate Scores: Behavioral Correctness Assumptions for Assessing
  Reference-Based Automatic Evaluation Methods'
title_zh: 超越聚合分数：评估基于参考的自动评测方法的行为正确性假设
authors:
- Maria Mahbub
- Ashley Rice
- Michael R. Munroe
- Amidu Kamara
- Amir Sadovnik
affiliations:
- Oak Ridge National Laboratory
- DHS Science and Technology Directorate
arxiv_id: '2609.05289'
url: https://arxiv.org/abs/2609.05289
pdf_url: https://arxiv.org/pdf/2609.05289
published: '2026-09-04'
collected: '2026-09-08'
category: Eval
direction: NLG自动评测 · 元评估诊断框架
tags:
- Automatic Evaluation
- Meta-Evaluation
- NLG Evaluation
- Reference-based Evaluation
- Behavioral Testing
one_liner: 提出行为正确性假设框架，诊断基于参考的NLG自动评测方法的隐藏行为差异
practical_value: '- 为GenRec/LLM客服/RAG输出选型自动评测指标时，可引入行为正确性假设做针对性校验，避免仅靠聚合分数选到不符合业务需求的指标

  - 针对现有在用的自动评测指标，可复用本文的受控文本变换方法测试其稳定性、配置敏感度，提前规避线上评测波动风险

  - 聚合分数接近的多个评测方案，可通过行为画像差异筛选最匹配业务场景（如文案改写/语义匹配需求）的方案'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有基于参考的NLG自动评测的元评估仅通过与人类判断的聚合一致性评分，无法暴露可控条件下的评测行为缺陷，难以支撑不同场景的指标选型决策。
### 方法关键点
构建行为正确性假设互补框架，划分「正确性保留」「正确性变更」两类假设分类体系，通过对生成文本做受控变换（如同义词替换、语义篡改等），校验不同评测器的预期打分行为，覆盖 lexical、字符级、语义、LLM-based、混合类共5类主流评测器，多维度分析其行为特征、稳定性、敏感度、重复运行波动、配置敏感性与复现性。
### 关键结果
无任何一款评测器能满足全部预设的正确性假设；聚合性能接近的评测器行为画像差异极大，传统聚合评估会掩盖大量关键诊断信息。
