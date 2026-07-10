---
title: 'Stop Guessing When to Stop Testing: Efficient Model Evaluation with Just Enough
  Data'
title_zh: 无需猜测评测终止时机：基于数据量自适应的高效模型评测框架
authors:
- Ofir Arviv
- Kristjan Greenewald
- Yotam Perlitz
- Hadar Mulian
- Michal Shmueli-Scheuer
- Leshem Choshen
affiliations:
- IBM Research
arxiv_id: '2607.08522'
url: https://arxiv.org/abs/2607.08522
pdf_url: https://arxiv.org/pdf/2607.08522
published: '2026-07-09'
collected: '2026-07-10'
category: Eval
direction: 大模型自适应评测框架优化
tags:
- sequential testing
- model evaluation
- adaptive evaluation
- statistical significance
- computational efficiency
one_liner: 结合序贯检验与定制停止准则，实现兼顾可靠性、降本80%的自适应模型评测
practical_value: '- 推荐/LLM4Rec离线AB评测可复用该框架的序贯检验逻辑，提前终止无显著差异的模型对比，大幅降低GPU/评测算力成本

  - 可直接复用收益递减检测、最小可检测效应量两类停止准则，适配业务中模型选优、排名等不同评测场景的置信度要求

  - 线上灰度实验可迁移该自适应停止思路，在满足统计显著性前提下缩短灰度周期，加速好模型上线效率'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
固定样本量基准评测具有刚性缺陷，无法适配模型排名、选优、迭代测试等不同场景的统计效力需求，要么造成过量算力浪费，要么结果可靠性不足；尤其当前LLM/VLM、LLM-as-Judge等评测成本激增，该矛盾进一步凸显。
### 方法关键点
提出自适应评测框架，将经典序贯检验统计范式与定制化停止准则结合，针对通用评测需求设计了收益递减检测、最小可检测效应量两类停止规则，可在评测过程中动态判断终止时机，平衡效率与可靠性。
### 关键结果
在Open VLM Leaderboard上验证，相比固定样本量评测，在允许2.5分置信区间宽度、保持统计显著性的前提下，可降低80%的计算成本。
