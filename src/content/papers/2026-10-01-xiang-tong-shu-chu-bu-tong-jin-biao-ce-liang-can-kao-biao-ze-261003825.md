---
title: 'Same Output, Different Gold: Measuring How Reference Choice Moves a Multilingual
  Benchmark Score'
title_zh: 相同输出不同金标：测量参考标注选择对多语言基准分数的影响
authors:
- Parth Kulshreshtha
- Shivali Dalmia
- Abhishek Mukherji
affiliations:
- Centific
arxiv_id: '2610.03825'
url: https://arxiv.org/abs/2610.03825
pdf_url: https://arxiv.org/pdf/2610.03825
published: '2026-10-01'
collected: '2026-10-14'
category: Eval
direction: 多语言评测 · 基准稳定性优化
tags:
- Evaluation
- Multilingual
- Benchmark
- Annotation
- Uncertainty
- F1-score
one_liner: 量化多语言基准中金标选择对系统评分与排名的影响，提出参考敏感度带计算方法
practical_value: '- 业务效果评测（如生成式推荐文案、RAG召回、Agent决策结果评测）时，需验证多标注员聚合规则的鲁棒性，避免金标偏差误导结论

  - 上线新评测基准前，可复用文中参考敏感度带计算方法，量化标注规则对评分的影响区间，与分数同步公示避免错误排名

  - 跨境电商等多语言业务场景需透明化标注聚合规则，规避未公开默认规则导致的跨语言评测结果失真'
score: 6
source: huggingface-daily
depth: abstract
---

## 动机
现有基准评测几乎只关注系统输出质量，默认参考金标为固定常量，忽略标注聚合规则选择带来的金标偏差会大幅影响评测结果可信度。
## 方法关键点
基于6语种个人可识别信息检测基准的留存标注数据，固定待评测系统输出，替换不同规则生成的金标（双独立标注员结果、默认聚合金标、专家重标注金标），量化评分波动幅度。
## 关键结果数字
单系统评分最大波动达4.95 F1点（95% CI [3.23, 6.27]），最差语种波动达7.55 F1点；双系统对比的排名波动达2.95 F1点（95% CI [1.97, 3.87]），可直接改变单语种下的系统排名；偏差根源是未公开的默认聚合规则会保留单个标注员结果，导致金标与待评测输出存在部分重叠。
