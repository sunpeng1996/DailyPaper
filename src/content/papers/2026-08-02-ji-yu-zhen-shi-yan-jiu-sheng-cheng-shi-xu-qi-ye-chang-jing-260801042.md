---
title: What Could the Agent See at 19:05? Generating Temporal Enterprise Scenarios
  from Real Research and Replaying Them to Evaluate Agents
title_zh: 基于真实研究生成时序企业场景并回放以评估AI Agent
authors:
- Tezan Sahu
- Himani Arora
affiliations:
- Microsoft, Hyderabad
arxiv_id: '2608.01042'
url: https://arxiv.org/abs/2608.01042
pdf_url: https://arxiv.org/pdf/2608.01042
published: '2026-08-02'
collected: '2026-08-04'
category: Agent
direction: Agent 时序场景生成与评估框架
tags:
- Agent Evaluation
- Temporal Scenario
- Enterprise Agent
- Reproducible Evaluation
- Synthetic Data
one_liner: 通过研究落地的时序场景生成+预计算差分缓存，实现任意时间点可复现的企业Agent评估
practical_value: '- 做电商/运营/客服Agent评估时，放弃静态数据快照方案，改为预计算各时间点数据与最终状态的差分缓存，既避免未来信息泄露，又能降低多时间点快照的存储与部署成本

  - 生成业务仿真测试场景时，严格按「用户角色→叙事逻辑弧→时间线→跨应用交互记录」的顺序生成，可从根源保证场景逻辑一致性，大幅减少人工校验成本

  - Agent评估链路设计时，将所有LLM调用全部移到预计算阶段，推理/打分路径仅保留确定性数据操作，保证评估结果100%可复现，完美适配迭代阶段的回归测试

  - 新工具/插件接入评估体系时，仅需通过schema自动推断时序行为规则，无需额外开发时序逻辑，接入耗时可从天级降到分钟级'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前企业跨应用AI Agent的离线评估普遍依赖静态数据快照，仅能评估 episode 最终状态，存在三大核心问题：一是未来信息泄露，记录内部的后续更新会污染当前时间点的真值；二是无法覆盖中间时序场景，绝大多数真实业务中出现的中间状态完全没有被评估；三是多快照部署成本极高，单episode要部署数十个租户才能覆盖各时间点，完全不可行，甚至会出现奖励Agent错误输出的情况，也完全无法评估事件触发型的always-on Agent。

### 方法关键点
- 场景生成：基于真实业务素材（访谈、工单、事件报告等）挖掘高频场景种子，按「角色→叙事弧→时间线→跨应用artifacts」的审核式顺序生成全量时序真值数据，时间和数据访问权限作为第一属性内置
- 时序增强：通过规则+LLM解析应用schema，自动推断每条记录的时序变化规则，无需人工配置时序逻辑
- 预计算差分缓存：提前计算每个时间点的记录状态与最终状态的差异，仅存储差分数据，存储成本仅为全量快照的几十分之一
- 回放评估：评估时通过缓存查找合并得到对应时间点、相应用户权限的数据集，无LLM调用，结果完全可复现，且支持任意Agent通过统一适配器接入

### 关键结果
单个人工构造的场景可生成数十个分角色、分时间点的评估用例；新应用接入评估体系的耗时从天级降到分钟级；批量评估运行结果100%可复现，对比静态快照方案覆盖的评估场景量提升10倍以上。

### 核心结论
把所有非确定性操作从评估测量路径中移到预计算阶段，可复现性是Agent迭代的基石，而非事后优化的特性
