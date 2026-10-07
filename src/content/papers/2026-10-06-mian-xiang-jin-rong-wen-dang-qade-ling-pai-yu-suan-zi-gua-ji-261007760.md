---
title: 'Token-Budgeted Escalation for Financial Document QA: Cost Is Predictable,
  Benefit Is the Bottleneck'
title_zh: 面向金融文档QA的令牌预算自适应升级策略：成本可预测，收益是瓶颈
authors:
- Junru Zhu
- Yixin Yang
- Xiaoqing Ding
- Ruoyu Qi
affiliations:
- Independent Researcher
- University of Chicago
arxiv_id: '2610.07760'
url: https://arxiv.org/abs/2610.07760
pdf_url: https://arxiv.org/pdf/2610.07760
published: '2026-10-06'
collected: '2026-10-07'
category: RAG
direction: RAG自适应检索 · 令牌预算优化
tags:
- RAG
- Budget Allocation
- Selective Escalation
- Financial QA
- Efficient LLM
one_liner: 提出共享令牌预算下按收益/令牌比优先的RAG升级分配策略，在金融QA场景降本提效
practical_value: '- 电商/客服类批量RAG服务可复用两阶段分配逻辑：先跑低成本初版结果，再按「预期收益/增量令牌」排序分配深度检索预算，紧预算下提效明显

  - 令牌成本预测难度远低于效果收益预测，用简单岭回归即可达到R²=0.93，紧预算场景优先做准成本预测即可拿到明确收益，无需先死磕收益预测

  - 可根据业务预算动态切换策略：预算紧张时用成本敏感分配策略，预算充足时优先优化收益排序模型'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有自适应RAG方法大多针对单query做检索决策，工业级批量部署时所有query共享统一的令牌预算，不同query升级更深检索的增量令牌成本差异可达数倍，仅按预期收益排序分配资源会导致预算浪费，无法在约束下最大化整体效果。

### 方法关键点
- 两阶段分配流程：所有query先执行低成本top-1检索生成初始答案，基于query特征、top-1检索结果特征、初始答案特征，分别用岭回归+梯度提升树预测升级到top-5检索的质量收益，用岭回归预测升级的增量令牌成本
- 分配策略对比：验证3种可部署策略，分别为仅按预期收益排序、按「预期收益/增量令牌」排序、基于预测值做0/1背包精确优化
- 评估采用文档分组交叉拟合，避免同文档数据同时出现在训练和测试集，保证结果可信度

### 关键结果
实验基于FinanceBench的150个公开金融QA问题，对比随机、检索分margin规则等baseline：
1. 10%增量预算下，收益/令牌比策略的评审质量达0.524，比仅按收益排序高0.034，总令牌消耗比全量top-5检索低46.6%
2. 增量令牌成本预测R²达0.93，MAPE仅9.8%，而有益升级的排序AUROC仅0.60，收益预测是当前核心瓶颈
3. 预算低于30%时成本敏感策略优势显著，预算高于50%时收益排序的影响更大

### 核心结论
紧预算下优先做准成本预测即可拿到显著收益，全预算区间的效果提升瓶颈在于更精准的query级收益预测。
