---
title: 'TIDE: Tree-Induced Fine-Grained Diagnostic Evaluation from Model Behaviors'
title_zh: TIDE：基于模型行为的树诱导细粒度诊断评估
authors:
- Jiayi Chen
- Hui Li
- Yujiong Shen
- Qiyuan Peng
- Yanxin Li
- Chenhao Huang
- Shaofan Liu
- Guoqiang Zhang
- Junjie Ye
- Shihan Dou
affiliations:
- Fudan University
- Hunyuan Team, Tencent
arxiv_id: '2610.29985'
url: https://arxiv.org/abs/2610.29985
pdf_url: https://arxiv.org/pdf/2610.29985
published: '2026-10-21'
collected: '2026-10-23'
category: Eval
direction: LLM评估 · 细粒度能力诊断
tags:
- LLM Evaluation
- Fine-grained Diagnosis
- Decision Tree
- LLM Judge
- Benchmark Analysis
one_liner: 提出行为驱动的树诱导诊断评估框架TIDE，挖掘LLM基准聚合分下的细粒度能力差异
practical_value: '- 可复用TIDE的行为驱动决策树拆分逻辑，对业务用LLM（如文案生成、query理解）做细粒度能力缺陷定位，替代笼统的准确率评估，精准定位优化方向

  - 基于LLM Judge+信息增益的样本分组方法可迁移到推荐模型效果分析场景，对召回/排序badcase自动聚类归因，减少人工分析成本

  - 跨模型细粒度能力对比方法可直接用于业务LLM选型，针对不同任务（如客服、商品文案）优先选择对应子能力最优的模型，降低部署成本'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前LLM基准评估仅输出单一聚合分，无法反映模型底层细粒度能力差异，既无法指导模型优化方向，也难以支撑精准的模型选型决策。
### 方法关键点
将诊断评估重构为行为驱动的决策树诱导任务，递归构建层级能力树：每个节点由LLM Judge生成分组候选、完成样本到组的分类，再基于行为信息增益选择最优拆分维度，实现能力的逐层拆解。
### 关键结果
在4个基准、5个LLM上验证效果，挖掘出聚合分下隐藏的能力差异：Claude Opus 4.6微观经济市场推理准确率达100%，优于GPT-5.4的83.3%；但合同法推理准确率仅77.8%，落后于GPT-5.4的88.9%。
