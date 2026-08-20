---
title: PILOT Technical Report
title_zh: PILOT技术报告：面向推荐系统优化的主动实验LLM Agent框架
authors:
- Jiuning Lin
- Ruiquan Lan
- Xiaodong Zhu
- Bin Zhang
- Chengyu Lai
- Chuxin Chen
- Dimin Wang
- Hongtao Cheng
- Jialin Zhu
- Lingqing Zhang
affiliations:
- Taobao
arxiv_id: '2608.18637'
url: https://arxiv.org/abs/2608.18637
pdf_url: https://arxiv.org/pdf/2608.18637
published: '2026-08-19'
collected: '2026-08-20'
category: Agent
direction: 推荐系统优化 · LLM Agent 实验自动化
tags:
- LLM Agent
- Recommendation Optimization
- Online Experimentation
- Knowledge Distillation
- Personalization
one_liner: 提出三角色约束控制环LLM Agent框架，实现推荐主动实验、分群优化与知识沉淀，淘宝落地效果优于无治理Agent
practical_value: '- 复用三角色Agent架构，将LLM选择权限制在确定性服务生成的合法动作集合内，彻底规避幻觉导致的线上风险，可直接用于工业级推荐优化Agent的落地

  - PolicyTree分群优化设计将用户分群与策略绑定，通过原子动作枚举约束搜索空间，兼顾个性化与统计效力，可迁移到流量调优、人群策略迭代场景

  - 记忆的fork-merge架构与置信度生命周期设计，可将单次实验结论沉淀为跨任务可复用的方法论，适合用于A/B实验自动化工具的开发

  - 实验前预注册决策规则、观测期隐藏指标变化方向的机制，可避免后验cherry-pick问题，直接复用到现有A/B实验平台的治理规则中'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有用于推荐系统优化的Agent均为被动响应指标变化，仅支持全局策略调优，且无法沉淀可复用的实验方法论；随着推荐场景用户分群、并行实验数量激增，人工迭代实验的效率已无法满足业务需求，同时无治理的自由探索Agent存在线上风险高、搜索效率低的问题。

### 方法关键点
- 采用三角色约束控制环架构：所有LLM仅能从确定性服务生成的合法动作集合中选择，不可越权，保障线上安全
  1. 实验管理器：负责全实验生命周期管控，覆盖任务接收、观测治理、异常恢复到复盘，高风险决策强制人工确认
  2. 搜索规划器：仅在管理器请求时调用，输出用户分群级别的个性化PolicyTree候选，候选来自确定性基线、LLM带证据假设、有限探索三个通道，所有候选需经过规则校验
  3. 记忆Curator：异步沉淀实验结果到策略证据库和方法论经验库，采用fork-merge隔离跨任务污染，记忆条目需经过多任务验证才能升级置信度
- 采用假设先行的实验范式，所有候选实验需提前注册可证伪的假设、决策条件，避免后验调整标准导致的结论失真

### 关键结果
在淘宝首页猜你喜欢5个实验桶上线，对比无生命周期治理、无结构化假设检验的自由探索Agent ROAM：IPV提升从+1.00%到+1.40%，核心IPV从+0.90%到+1.60%，交易笔数从+0.60%到+0.96%，交易金额从+1.13%到+1.50%，搜索效率从53.3%提升到93.3%，全程无人工干预。

> 最值得记住的一句话：工业级LLM Agent落地的核心不是给LLM最大的自由，而是通过确定性规则划定安全边界，让LLM只在需要判断力的场景发挥价值，同时建立经验沉淀飞轮实现效果复利。
