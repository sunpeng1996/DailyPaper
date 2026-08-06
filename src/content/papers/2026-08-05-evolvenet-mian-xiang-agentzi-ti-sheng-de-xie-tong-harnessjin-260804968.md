---
title: 'EvolveNet: Collaborative Harness Evolution for Agent Self-Improvement'
title_zh: EvolveNet：面向Agent自提升的协同Harness进化框架
authors:
- Jun Nie
- Yonggang Zhang
- Qianshu Cai
- Yiu-ming Cheung
- Xinmei Tian
- Bo Han
affiliations:
- Hong Kong Baptist University
- University of Science and Technology of China
- The Hong Kong University of Science and Technology
arxiv_id: '2608.04968'
url: https://arxiv.org/abs/2608.04968
pdf_url: https://arxiv.org/pdf/2608.04968
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: Agent 多智体协同自进化优化
tags:
- Agent
- Harness Evolution
- Program Aggregation
- Federated Optimization
- Self-improvement
one_liner: 提出分布式协同Harness进化范式，无需集中原始数据即可聚合多Agent经验实现全局提升
practical_value: '- 跨域合规场景（如多地域电商/广告Agent、多商家平台Agent）可直接复用「本地进化-聚合适配」范式，原始数据无需跨域传输即可实现全局经验复用，满足数据监管要求

  - 多场景Agent的prompt/工作流合并可借鉴scope-typed机制，区分全局通用策略和场景专属策略，从架构层面避免不同场景的策略冲突，减少人工调试成本

  - 线上Agent迭代可复用行为准入门控机制，仅保留新增解决问题数≥新增故障数的版本，大幅降低迭代回滚风险，保证线上服务稳定性

  - 多场景Agent优化可采用并行进化思路，串行优化深度由最慢分支决定而非总场景数，最高可降低5倍以上的迭代周期，加速业务落地'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有Agent Harness（负责上下文构建、工具调用、错误恢复的可执行程序）进化均采用集中式范式，需汇聚所有部署节点的原始业务数据才能完成优化。但实际生产中Agent通常跨组织、跨地域部署，数据因合规、隐私、商业保密等要求无法集中，导致跨域经验无法复用，单节点进化速度慢、场景覆盖有限。

### 方法关键点
- 采用「广播共享Harness→本地独立进化→聚合适配→重新分发」的循环范式，仅传输Harness代码改动、相对基准的行为效果数据，原始业务数据全程留存本地
- 实现证据引导的scope-typed程序聚合：将本地进化产生的改动分为两类，跨多场景验证有效的升级设为GLOBAL全局生效，仅单场景有效的升级设为HOME场景专属、条件触发，从架构上避免不同场景的改动冲突
- 新增行为准入门控：聚合后的候选Harness必须在验证集上新增解决的问题数≥新增失败的问题数才会被采纳，否则直接回滚到上一版本，保证全局能力不退化

### 关键实验
在text-to-SQL、数据科学编码、Agent工作流等5类场景测试，对比未进化Harness、单最优客户端、仅按场景路由等baseline：
1. 所有场景下效果均显著提升，DS-1000编码数据集上准确率从55.5%提升至68.5%，比单最优客户端高出9个百分点
2. 并行进化相比串行进化最多可降低5.4倍的串行耗时，多客户端并行场景下精度无损失
3. 对无任何客户端训练数据的泛化场景（如DS-1000的Pytorch子集），准确率仍提升13.4个百分点

Agent协同优化的共享载体不必是模型参数，可执行的Harness程序同样可以跨域传递经验，且数据合规性更好、传输成本更低。
