---
title: 'RAG-Stack: Co-Optimizing RAG Serving Performance and Quality'
title_zh: RAG-Stack：RAG服务质量与性能联合优化框架
authors:
- Haiqiang Zhang
- Yuanqing Lei
- Wanting Li
- Tao Zhang
- Wenqi Jiang
affiliations:
- ETH Zurich
- Columbia University
- National University of Singapore
arxiv_id: '2608.03487'
url: https://arxiv.org/abs/2608.03487
pdf_url: https://arxiv.org/pdf/2608.03487
published: '2026-08-04'
collected: '2026-08-05'
category: RAG
direction: RAG服务 · 质量性能联合调优
tags:
- RAG
- Pareto Optimization
- Performance Tuning
- Cost Model
- Bayesian Optimization
one_liner: 提出覆盖算法与系统设计空间的RAG联合优化框架，高效找到质量-性能帕累托前沿
practical_value: '- 搭建业务RAG系统时可复用RAG-Stack的参数拆分思路：仅对影响回答质量的算法参数做真实效果评估，系统部署参数用成本模型预测，大幅降低调优开销

  - RAG调优可引入跨阶段子信号引导贝叶斯优化，无需独立调优每个模块，避免忽略模块耦合导致的次优解，在有限评估预算下拿到更优的质量-性能tradeoff

  - 业务RAG跨硬件迁移时可复用历史质量评估结果，仅用成本模型重新预估性能，不需要全量重跑效果实验，大幅降低迁移成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG系统调优存在三大痛点：孤立优化单个模块会忽略跨阶段耦合导致次优解；仅搜索算法配置不考虑系统部署优化，无法拿到最优性能；部署测速成本高，硬件迁移后需要全量重调，难以高效找到质量与性能的最优权衡点。

### 方法关键点
- 框架由3个核心组件构成：RAG-PE是感知阶段子指标的多目标贝叶斯优化器，结合端到端效果和单阶段诊断信号（如检索召回率、生成置信度）引导配置搜索，减少无效探索；RAG-IR是系统无关的RAG工作负载抽象层，将算法配置转为统一的工作流与执行Trace，解耦逻辑计算与物理部署；RAG-CM是ML+解析融合的性能成本模型，无需真实部署即可预测指定硬件下的最优部署方案与服务性能。
- 支持两种运行模式：从零开始搜索帕累托前沿，以及跨硬件迁移时复用历史质量评估结果，仅做少量迭代补全新的前沿。

### 关键结果
在RAGEval、MS MARCO数据集上测试，相同迭代次数下，RAG-Stack找到的帕累托前沿覆盖的归一化质量-性能空间在RAGEval上比SOTA配置搜索方法高52.5%，在MS MARCO上高153.2%；跨硬件迁移时，比从零开始重优化的前沿覆盖空间高182.2%。

**最值得记住的一句话**：RAG调优不能割裂算法效果与系统性能，将算法配置与系统部署参数解耦后联合优化，能在更低成本下拿到业务最优的运行点。
