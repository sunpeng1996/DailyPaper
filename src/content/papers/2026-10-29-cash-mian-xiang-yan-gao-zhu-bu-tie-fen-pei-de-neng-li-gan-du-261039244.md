---
title: 'CASH: A Capability-Aware Subsidy Harness for Advertiser Subsidy Allocation'
title_zh: CASH：面向广告主补贴分配的能力感知调度框架
authors:
- Minmao Wang
- Huihuang Lin
- Likang Wu
- Hongke Zhao
- Shijie Yi
- Fei Pan
affiliations:
- Fudan University
- Kuaishou Technology
- Tianjin University
arxiv_id: '2610.39244'
url: https://arxiv.org/abs/2610.39244
pdf_url: https://arxiv.org/pdf/2610.39244
published: '2026-10-29'
collected: '2026-10-30'
category: RecSys
direction: 广告系统优化 · LLM Agent融合
tags:
- Advertising
- LLM Agent
- Subsidy Allocation
- Estimator Fusion
- Online Experiment
one_liner: 融合LLM Agent与数值响应模型实现账户级广告补贴分配，补贴率不变下营收提升15.35%
practical_value: '- 异构模型融合的边界管控方法可直接复用：为LLM、数值模型等不同预测源定义基于历史误差、样本支撑度的准入license，仅允许可靠区间的预测结果参与全局分配，可阻断单样本误差在约束型分配场景的跨主体传导

  - LLM调用降本方案适配大规模场景：通过预训练的梯度提升树Judge模型提前对账户打分，仅为高价值账户调用LLM，相比全量调用节省70%的token成本，同时保留86%的效果增益，适合大流量下的LLM落地

  - EPCG主动探索逻辑可迁移到冷启动场景：基于期望可靠覆盖增益分配探索配额，可快速扩大低成本数值模型的适用范围，降低长期对LLM的依赖，适合补贴、优惠券等数据稀疏的分配场景

  - 全局约束分配的求解优化可复用：将全局补贴率约束的多账户组合优化转化为对偶分解问题，仅最多1个账户需要整数修复，求解效率适配百万级以上账户量级的电商/广告补贴分配'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
广告平台通过账单折扣给广告主发放补贴是提升冷启动广告主竞争力、优化生态留存的核心手段。传统人工按账户层级配置补贴的方式，无法适配单账户在不同补贴档位的营收响应差异，易造成补贴浪费；单独用LLM做响应预测数值精度不足，单独用数值模型在数据稀疏场景误差大，且单账户的预测误差会通过全局补贴预算约束传导到其他账户，严重影响整体分配效率。
### 方法关键点
- 双预测源互补设计：LLM预测Agent融合业务规则、账户运营信息输出各补贴档位的响应曲线，数值响应模型基于历史执行数据训练输出同维度结果，两者均通过保序投影避免不合理预测
- 能力License机制：基于历史预测误差、样本支持度、区域准入三个维度，为每个预测源的「账户+补贴档位」组合颁发准入许可，仅允许许可范围内的预测结果参与全局分配，阻断不可靠预测的误差传导
- EPCG主动探索：设计Expected Policy Coverage Gain指标，优先为能最大程度扩大数值模型可靠覆盖范围的样本分配探索配额，以少量探索成本降低长期对LLM的依赖
- 高效全局求解：将带全局补贴率约束的多账户分配问题转化为对偶分解问题求解，仅最多1个账户需要整数修复，适配大规模账户量级
### 关键结果
快手线上1个月实验，CASH服务60%流量，对比人工策略对照组，补贴率基本不变的前提下，单账户营收提升15.35%，广告主价值ADVV提升19.86%，14天LTV提升15.24%，14天留存提升1.57个百分点；比纯数值模型基线再提收6.31%。
### 核心结论
异构预测源融合的核心不是加权组合，而是明确每个源的可靠边界，边界内用低成本方案，边界外补高成本方案，再通过主动探索持续扩大低成本方案的覆盖范围
