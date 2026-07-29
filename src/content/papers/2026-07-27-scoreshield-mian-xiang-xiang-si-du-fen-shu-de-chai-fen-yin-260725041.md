---
title: 'ScoreShield: Differentially Private Release of Similarity Scores'
title_zh: ScoreShield：面向相似度分数的差分隐私发布机制
authors:
- Behrooz Razeghi
- Parsa Rahimi
affiliations:
- Harvard University
- École Polytechnique Fédérale de Lausanne (EPFL)
arxiv_id: '2607.25041'
url: https://arxiv.org/abs/2607.25041
pdf_url: https://arxiv.org/pdf/2607.25041
published: '2026-07-27'
collected: '2026-07-29'
category: Other
direction: 隐私保护 · 相似度分数差分隐私发布
tags:
- Differential Privacy
- Cosine Similarity
- RAG
- Recommendation System
- Privacy Preserving
- Semantic Retrieval
one_liner: 提出先扰动后投影的差分隐私机制，在保障(ε,δ)-DP前提下大幅降低相似度分数发布的效用损失
practical_value: '- 对外提供语义检索/RAG API的业务可直接复用ScoreShield的「加噪+投影」流程，在满足合规隐私要求的同时最小化排序效用损失

  - 推荐系统向第三方输出召回/排序相似度分数时，可借鉴其全局敏感度校准的高斯噪声策略，替代朴素加噪方案降低效用损耗

  - 大规模Gram矩阵发布场景可复用其平均交替投影求解器，低秩场景下收敛更快、计算误差更低'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
RAG、语义检索、推荐等系统对外输出余弦相似度分数时，存在泄露个体记录、被成员推理攻击的风险；朴素DP加噪方案效用损失大，且分数规模越大损耗呈三次方增长，无法适配大规模场景。

### 方法关键点
提出ScoreShield「先扰动后投影」机制：首先根据分数发布场景的全局敏感度校准高斯噪声，再将结果投影到合法余弦对象的可行域；针对大规模Gram矩阵发布场景，设计平均交替投影求解器保障收敛性，满足(ε,δ)-DP要求。

### 关键结果数字
固定隐私参数下，全成对余弦Gram矩阵发布的平方Frobenius风险的n依赖从朴素高斯基线的Θ(n³)降至O(n²)，低秩Gram矩阵场景局部边界更优；已在RAG、人脸识别、语义检索、推荐系统等多个任务验证有效性。
