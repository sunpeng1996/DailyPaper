---
title: 'TruthInsightBench: An Evidence-Grounded Benchmark for Automated Evaluation
  of Open-Ended Scientific Discovery Agents'
title_zh: TruthInsightBench：面向开放式科学发现Agent的证据导向评测基准
authors:
- Zhibo Yang
- Chen Zhang
- Yuewei Zhang
- Hao Wang
affiliations:
- TruthInsight-AI
arxiv_id: '2609.05079'
url: https://arxiv.org/abs/2609.05079
pdf_url: https://arxiv.org/pdf/2609.05079
published: '2026-09-04'
collected: '2026-09-07'
category: Eval
direction: 科学发现Agent 自动化评测基准
tags:
- Agent
- Benchmark
- LLM-as-Judge
- Automated Evaluation
- Scientific Discovery
one_liner: 推出面向开放式科学发现Agent的证据导向自动化评测基准，无需逐例人工标注
practical_value: '- 可复用LLM-as-Judge的多维度+确定性聚合打分框架，替代电商推荐/广告策略迭代中的人工效果评估，大幅降低标注成本

  - 盲测任务设计思路可迁移到业务Agent效果评测：仅暴露目标和输入数据，隐藏预期结果，避免评测过拟合，更贴合真实业务场景

  - 能力维度拆分思路可复用：做Agent能力瓶颈定位时，可将执行能力、可信度维度（鲁棒性、可证伪性等）分开打分，精准定位迭代方向'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有科学发现Agent评测基准均为复现任务设计，围绕隐藏目标研究做结果匹配，无法衡量真实开放式探索的发现能力。
### 方法关键点
1. 构建覆盖10个科学领域的40个盲测任务，仅公开中性研究目标与固定数据，隐藏源结论、预期值与分析路径，要求Agent自主挖掘数据可支撑的结论；
2. 采用固定LLM judge从6个维度（落地为29个基于输出产物的评测项）评估Agent主张的证据成熟度，打分聚合全自动化、确定性，无需逐例人工标注，支持迭代过程中反复评测。
### 关键结果
4款编码Agent在固定基座模型上得分仅为58.4-60.3/100，两两无统计学差异；能力瓶颈为科学判断而非编码，在对照组设置、鲁棒性、可证伪性、跨数据集泛化等可信主张维度表现严重不足。
