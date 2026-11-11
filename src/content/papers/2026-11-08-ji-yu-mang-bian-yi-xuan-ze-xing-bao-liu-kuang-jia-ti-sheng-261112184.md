---
title: 'Blind Variation, Selective Retention: Improving Creative Idea Generation in
  AI Scientists'
title_zh: 基于盲变异-选择性保留框架提升AI科学家的创意生成能力
authors:
- Guowei Xu
- Jiaru Zou
- Mete Erdogan
- Haotian Ye
- Pan Lu
- James Zou
affiliations:
- Stanford University
arxiv_id: '2611.12184'
url: https://arxiv.org/abs/2611.12184
pdf_url: https://arxiv.org/pdf/2611.12184
published: '2026-11-08'
collected: '2026-11-11'
category: Agent
direction: Agent 科学发现创意生成优化
tags:
- Creative Generation
- Agent Framework
- Scientific Discovery
- BVSR
- Prompt Optimization
one_liner: 提出分阶段信息使用的BVSR框架，约束探索阶段信息输入提升AI科学家创意提案质量
practical_value: '- 电商/广告文案生成、新品创意挖掘场景可复用分阶段信息策略：生成阶段故意限制过多过往爆款/同品类信息输入，避免创意同质化，筛选阶段再结合业务数据做效果校验，平衡创意和ROI

  - 推荐系统冷启动/新召回路径探索场景可借鉴：探索阶段仅输入基础任务约束，不灌入现有召回排序规则特征，避免被现有逻辑锚定，筛选阶段再用历史AB实验数据过滤无效方案，降低试错成本

  - Agent 决策流设计可复用两阶段架构：探索模块降信息输入增强多样性，记忆模块沉淀历史验证结果做候选粗筛，大幅减少下游高成本验证（线上实验、用户调研）的资源消耗'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有AI科学家Agent生成创意时输入全量任务信息，易被已知方案锚定，生成的提案缺乏原创性、非显见性，难以产出高价值突破性发现。

### 方法关键点
1. 受认知科学BVSR框架启发，拆分信息使用逻辑：盲变异阶段仅输入受限任务上下文生成提案，刻意规避已知路径锚定，拓宽探索边界；
2. 选择性保留阶段学习同任务下历史验证提案及其效果数据，粗筛高潜力候选进入高成本实证验证环节。

### 关键结果数字
在5种提案模型、12种科学任务上验证，相比SOTA提示词基线，高创意高效用提案占比显著提升；选择性保留阶段可过滤50%无效候选，同时保留绝大多数Top性能提案；集成到现有AI科学家工作流后，在基因表达分析、药物响应预测等5类任务上均取得更优发现效果。
