---
title: 'AgentRewind: Recoverable Execution for Long-Horizon LLM Agents'
title_zh: 《AgentRewind：面向长周期LLM Agent的可恢复执行框架》
authors:
- Yu Zhuang
- Kefei Chen
- Yitong Duan
- Shuxin Zheng
- Jian Li
- Xu-Yao Zhang
affiliations:
- University of Chinese Academy of Sciences
- IIIS, Tsinghua University
- Zhongguancun Academy, Beijing
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2608.14380'
url: https://arxiv.org/abs/2608.14380
pdf_url: https://arxiv.org/pdf/2608.14380
published: '2026-08-14'
collected: '2026-08-17'
category: Agent
direction: LLM Agent长周期执行容错优化
tags:
- LLM Agent
- Long-Horizon Task
- Checkpoint
- Rollback
- Benchmark
one_liner: 提出对齐Agent上下文与环境的可回滚框架，配套长周期任务基准，提升长流程Agent执行成功率
practical_value: '- 电商智能运营、客诉闭环等长流程业务Agent可接入双checkpoint机制，避免早期操作错误（如误改商品配置）导致全链路失败，无需全程重跑

  - LLM驱动的推荐物料生成、A/B测试自动化等Agent可复用回滚+错误记忆注入逻辑，回滚到有效节点的同时留存失败经验，降低重复错误率

  - 工程落地可借鉴轻量文件级checkpoint方案，仅追踪工作区文件变化+Agent上下文日志，资源开销远低于全系统快照，适合业务场景

  - 长流程Agent评估可参考MettleBench的多依赖有序验收checklist设计，同时评估最终成功率与阶段性进度，更贴合业务实际需求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
长周期LLM Agent执行过程中早期错误会在上下文和环境状态中持续传播，现有方案多侧重前置规划优化与执行中安全检查，错误发生后缺乏有效恢复手段，导致任务成功率随执行长度骤降。
### 方法关键点
1. 运行时在Agent每次决策边界生成对齐的**上下文+环境状态双checkpoint**，仅追踪工作区文件变化，低开销实现环境状态回滚
2. 支持Agent主动触发回滚操作，回滚时注入之前失败尝试的总结记忆，避免重复出现同类错误
3. 构建MettleBench长周期工程任务基准，包含82个带多依赖有序验收标准的任务，同时支持最终成功率与阶段性进度评估
### 关键实验
在MettleBench上对比Continue、Restart with Experiences、Safety Review三类基线：GPT-5.4底座下AgentRewind较最强基线任务成功率提升25.6pp至87.8%，平均检查点进度提升12.9pp至94.3%；在Terminal-Bench 2.0上成功率较基线提升4.4pp至83.1%，且适配3种不同Agent框架均带来稳定提升。
### 核心结论
长周期Agent的容错核心是上下文与环境状态的对齐回滚+错误记忆留存，收益远高于单纯重试或前置安全检查。
