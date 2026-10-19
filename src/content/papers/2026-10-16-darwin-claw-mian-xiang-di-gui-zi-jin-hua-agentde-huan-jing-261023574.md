---
title: 'Darwin-Claw: Environment-Adaptive Experience Consolidation for Recursively
  Self-Evolving Agents'
title_zh: Darwin-Claw：面向递归自进化Agent的环境自适应经验整合框架
authors:
- Mingze Yin
- Xiaohan Wang
- Dian Li
- Longfei Luo
- Jiahong Yan
- Yiheng Zhu
- Chang-Yu Hsieh
affiliations:
- Zhejiang University
- Tencent
- Zhongguancun Academy
arxiv_id: '2610.23574'
url: https://arxiv.org/abs/2610.23574
pdf_url: https://arxiv.org/pdf/2610.23574
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent自进化 · 经验沉淀与技能优化
tags:
- Self-Evolving-Agent
- Experience-Consolidation
- Skill-Evolution
- Lifelong-Learning
- LLM-Agent
one_liner: 提出基于分层经验整合的自进化Agent框架，无需修改模型参数即可稳定提升跨场景任务性能
practical_value: '- 可复用「分层经验抽取+因果验证」流程，将电商/推荐场景的用户交互轨迹（如偏好归因、query纠错规则）提炼为结构化经验单元，无需修改底层模型参数即可快速优化业务效果

  - 可复用经验单元的生命周期管理机制（试用期-正式槽位-淘汰），严格控制prompt长度避免上下文过载，适合推荐系统prompt工程的持续迭代

  - 支持跨用户/业务线的经验共享与集体进化，可将不同品类/商家的运营经验沉淀为通用技能插件，降低重复开发成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM Agent多为单会话孤立运行，无法从历史交互中持续学习适配特定用户环境；现有自进化方案直接注入原始交互轨迹，无明确归因导致行为模式混乱、更新不可控，随着LLM基础推理能力提升，场景化经验的系统化管理已成为Agent进化的核心瓶颈。

### 方法关键点
- 分层经验整合系统：异步处理新会话轨迹，先提取技能调用片段，再通过LLM筛选携带学习信号的有效轨迹，生成包含触发条件、执行策略的结构化经验单元（EU）
- 因果验证与多维度打分：新EU上线后通过两步LLM pipeline验证效果相关性与因果性，按任务效果、覆盖度、执行效率三个维度加权评分，保证经验的可靠性
- 外部化内存生命周期管理：EU按性能竞争占用技能的固定槽位，经历「试用期-正式槽位-自动淘汰」的状态机流转，全程无需修改底层模型参数即可实现稳定进化

### 关键实验
在包含60个长周期跨域任务的WildClawBench上测试，相比基线整体任务成功率提升24.1%，其中工具使用类任务提升31.6%，极端难度任务提升33.2%；在RSIBench自优化训练任务上，相比传统上下文传递方案平均性能提升12.3%，其中SWE-P、Terminal-Bench 2.0任务分别提升68.8%、34.1%。

### 核心观点
不是最强的物种存活，也不是最聪明的，而是最能适应环境变化的物种存活。
