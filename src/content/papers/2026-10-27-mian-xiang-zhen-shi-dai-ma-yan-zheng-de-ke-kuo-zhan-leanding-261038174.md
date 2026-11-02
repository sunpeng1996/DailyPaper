---
title: Scaling Lean Theorem Proving for Real-World Code Verification
title_zh: 面向真实代码验证的可扩展Lean定理证明系统
authors:
- Debargha Ganguly
- Divya Raghunathan
- Dejan Jovanović
- Vikash Singh
- Soonho Kong
- Aaron Tomb
- Aman Goel
- Ferhat Erata
- Sam Bayless
affiliations:
- Amazon Web Services
- Case Western Reserve University
arxiv_id: '2610.38174'
url: https://arxiv.org/abs/2610.38174
pdf_url: https://arxiv.org/pdf/2610.38174
published: '2026-10-27'
collected: '2026-11-02'
category: Agent
direction: Agent 定理证明与代码验证
tags:
- Lean Theorem Proving
- Recursive Agent
- Code Verification
- Benchmark Generation
- LLM Agent
one_liner: 提出基于递归Agent的Lean证明系统EasyProver与高难度代码验证基准生成工具Aegis
practical_value: '- 递归Agent+上下文隔离+异步并行搜索的架构可迁移到复杂检索/推理类Agent任务，比如大促规则校验、复杂用户意图拆解，降低长上下文消耗

  - 无额外微调仅用通用前沿大模型实现SOTA的思路，可复用在低资源业务场景，减少训练成本

  - 自动生成高难度带标注基准的pipeline，可借鉴来构建业务场景的Agent评测数据集，比如复杂query理解、推荐规则合规校验的评测集'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM结合定理证明的Agent方案存在长上下文开销高、策略错误反馈滞后问题，且公开代码验证基准已接近饱和，无法支撑工业级真实代码校验任务的评测与迭代。
### 方法关键点
1. 构建EasyProver Lean证明系统，采用递归Agent架构，搭配上下文隔离、异步搜索、并行策略探测、弹性精化服务，无需额外微调即可调用通用前沿大模型完成证明任务。
2. 提出Aegis基准生成pipeline，将编程竞赛题目转化为真实实现级高难度验证任务，自动生成校验通过的Rust-Lean程序对与带标注验证规则。
### 关键结果
EasyProver在PutnamBench上准确率达99.6%，全量通过IMO 2026、VERINA任务，NTP4VC任务准确率99.5%；Aegis累计生成2045组Rust-Lean程序对、11533条候选验证规则，EasyProver在2000条高难度真实代码验证任务上准确率达52.7%
