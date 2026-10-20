---
title: 'DrugHarness: An Evolvable Agent Harness for Computational Drug Discovery'
title_zh: DrugHarness：面向计算药物发现的可演化Agent框架
authors:
- Yuxing Chen
- Zhisheng Zhang
- Cheng Tang
- Wei Li
- Minghui Zhang
- Ziyan Huang
- Shaocong Wei
- Jiawei Chen
- Junru Hu
- Hongze Zhu
affiliations:
- Shanghai Artificial Intelligence Laboratory
- China Pharmaceutical University
- University of the Chinese Academy of Sciences
- Shanghai Jiao Tong University
- Westlake University
arxiv_id: '2610.23791'
url: https://arxiv.org/abs/2610.23791
pdf_url: https://arxiv.org/pdf/2610.23791
published: '2026-10-16'
collected: '2026-10-20'
category: Agent
direction: 科学Agent · 可演化技能框架设计
tags:
- Agent Evolution
- Skill Induction
- Execution Engine
- Feedback Learning
- Scientific Agent
one_liner: 提出面向科学任务的可演化Agent框架，支持技能自主归纳与迭代优化
practical_value: '- 可复用「执行引擎+独立技能评审Agent+反馈迭代」的通用可演化Agent架构，适配电商选品、广告创意生成、商家经营决策等需要累积领域专属技能的场景

  - 从执行轨迹+结果反馈归纳带适用条件可复用技能的逻辑，可迁移到推荐系统的用户行为路径挖掘，提炼可复用的召回/排序规则，降低垂类场景冷启动成本

  - 技能校验的「源数据验证+小流量定向执行试错」双逻辑，可用于LLM生成的推荐文案、搜索query的质量校验，减少线上bad case'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
计算药物发现场景要求Agent可灵活组合科学操作，且适配动态变化的证据与约束，现有通用Agent框架缺乏领域技能持续演化的能力。
### 方法关键点
1. 底层环境整合80+科学操作、生物医学资源与任务专属代码，全链路留存候选对象、执行结果与中间产物的关联关系；
2. 从历史执行轨迹与结果反馈中归纳带可观测适用条件、推荐动作、支撑证据的动作假设，由独立评审Agent通过源验证+定向执行测试校验候选技能，通过的技能纳入库指导后续任务并持续迭代更新。
### 关键结果数字
无演化版本在MolBench上亲和力对比准确率超基线MolClaw-CC 10.8pct，top3活性命中均值高55%；技能演化机制将Qwen的亲和力对比准确率从62.2%提升至81.1%，优化成功率从79.5%提升至87.2%；真实HPK1研究中合成化合物IC50达14.19nM，效力较最优参考物高2.64倍，效果接近资深药物化学家设计的化合物。
