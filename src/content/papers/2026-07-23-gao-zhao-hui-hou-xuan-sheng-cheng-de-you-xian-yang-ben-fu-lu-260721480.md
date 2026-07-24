---
title: 'Finite-Sample Coverage Audits for High-Recall Candidate Generation: Certification
  and Learning-Theoretic Design'
title_zh: 高召回候选生成的有限样本覆盖率审计方法与理论保证
authors:
- Martin Anthony
- Kaveh Salehzadeh Nobari
affiliations:
- Data Science Institute, LSE
- Department of Mathematics, LSE
- The Inclusion Initiative, LSE
arxiv_id: '2607.21480'
url: https://arxiv.org/abs/2607.21480
pdf_url: https://arxiv.org/pdf/2607.21480
published: '2026-07-23'
collected: '2026-07-24'
category: RecSys
direction: 候选生成 召回率审计与理论保障
tags:
- Candidate Generation
- Recall Audit
- Finite Sample Guarantee
- Coverage Certification
- Label Complexity
one_liner: 提出候选生成召回率的有限样本审计框架，给出严格理论保证与可落地工具包
practical_value: '- 做召回/粗排效果审计时，必须采样被排除的候选池做标注，仅在召回命中池里标注无法得到有效的漏召回率保证

  - 可复用论文给出的二项/超几何分布逆运算工具，用最少标注量得到严格的漏召回率上界/召回率下界统计保证，避免渐近近似导致的指标虚高

  - 做多版本召回策略对比时，可采用预固定策略族+独立审计集的设计，用单次审计即可得到所有策略的同时认证，大幅节省标注成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
召回/候选生成是推荐、搜索、RAG系统的第一阶段，漏召回的相关item会在全链路彻底丢失，无法被下游环节恢复；现有召回率评估多依赖近似置信区间，无有限样本下的严格有效性保证，且普遍仅在召回命中池内采样标注，无法得到准确的漏召回质量界，亟需可落地、有理论背书的审计方法。
### 方法关键点
- 证明不可能定理：仅基于召回命中池的标注、候选生成器输出与无标注数据，无论样本量多大，都无法给出非平凡的漏召质量上界，审计必须采样被排除的候选池。
- 推导有限语料下的标注复杂度下界：要以高概率认证漏召相关item数<m，平均至少需要采样Ω(N₀/m)个排除池样本（N₀为排除池总大小），证明排除池采样是极小极率最优的审计方案。
- 开发可直接部署的有限样本审计工具包：基于二项/超几何分布逆运算，支持单排除池审计漏召质量、双池（排除+命中）审计召回率、预定义嵌套候选生成器族的同时认证、扰动鲁棒性压力测试。
- 明确设计-认证分离原则：待评估的候选生成器/策略族必须在查看审计标注前固定，否则认证保证失效。
### 关键结果
零漏召理想场景下，非自适应排除池采样的标注量仅比理论下界高log(1/δ)的常数因子，达到最优缩放；所有审计保证均为严格有限样本下的，无渐近假设。
### 最值得记住的一句话
召回效果审计必须看被你丢掉的那些item，只看命中池永远不知道你漏了多少。
