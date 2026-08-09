---
title: 'Tracing the Heart: An Evidence-Linked Pipeline for Heart-Failure Feature Engineering'
title_zh: 追踪核心：面向心力衰竭特征工程的证据关联处理管线
authors:
- Soorya Ram Shimgekar
- Michelle Hu
- Dorisa Shehi
- Daniel Kang
- Roy Ka-Wei Lee
- Koustuv Saha
- Christian Poellabauer
- Christopher Lee
- Sajeev Singh
- Piyum Zonooz
affiliations:
- Nimblemind
- Singapore University of Technology and Design
- University of Illinois Urbana-Champaign
- Florida International University
- University of California Los Angeles
arxiv_id: '2608.06366'
url: https://arxiv.org/abs/2608.06366
pdf_url: https://arxiv.org/pdf/2608.06366
published: '2026-08-06'
collected: '2026-08-09'
category: MultiAgent
direction: 多智体协作 · 自动化特征工程
tags:
- MultiAgent
- Feature Engineering
- LLM
- Auditability
- EHR
one_liner: 提出规则锚定的多智能体系统nMAS，实现可审计的自动化心衰EHR特征工程，提升表型预测性能
practical_value: '- 跨多源异构数据做特征工程时，可复用「业务规则锚定+多智能体分工生产+独立LLM审计」的架构，保证特征可溯源、符合业务逻辑，适配电商多源行为/交易/商品特征加工场景

  - 高合规要求的特征生产场景（如广告合规、用户隐私相关特征），可引入限制级独立LLM做特征合规性、来源可追溯性的自动校验，大幅降低人工审核成本

  - 分层产出结构化基础特征+规则锚定高阶聚合特征的模式，可复用在用户/物品分层特征体系搭建中，兼顾统计准确性与业务适配性'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
电子健康记录（EHR）特征工程占数据科学家39%-45%的工作量，心衰场景需整合碎片化EHR数据与符合临床指南的专业推理，现有规则/LLM方法自动化程度低、可维护性与证据可追溯性差，是临床AI落地的核心瓶颈。

### 方法关键点
提出nMAS多智能体管线，锚定临床规则生成证据关联的特征，输出后经限制级LLM审计，校验三类核心指标：结构完整性、规则合规性、来源可追溯性，最终输出结构化特征与规则评分聚合特征两类结果。

### 关键结果
在500份模拟患者记录、9张EHR源表上测试，生成132个结构化特征、70个规则评分聚合特征；新增聚合特征后，HFrEF表型预测hold-out AUROC从0.895升至0.963，HFpEF从0.870升至0.910；独立LLM评估特征的证据支撑与方法合理性得分达满分的81.5%。
