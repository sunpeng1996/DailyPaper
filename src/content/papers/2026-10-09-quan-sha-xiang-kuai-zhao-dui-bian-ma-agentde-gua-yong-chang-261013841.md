---
title: 'Returning to Development States: When Full Sandbox Snapshots Help Coding Agents'
title_zh: 全沙箱快照对编码Agent的适用场景与效果评估
authors:
- Daniel Thi Graviet
- Tanmay Shah
affiliations:
- Daytona
- University of Waterloo
arxiv_id: '2610.13841'
url: https://arxiv.org/abs/2610.13841
pdf_url: https://arxiv.org/pdf/2610.13841
published: '2026-10-09'
collected: '2026-10-12'
category: Agent
direction: Agent 执行容错与状态复用优化
tags:
- Coding Agent
- Sandbox Snapshot
- Go-Explore
- State Restoration
- Test-time Search
one_liner: 通过对比实验明确全沙箱快照提升编码Agent性能的适用场景与现存缺陷
practical_value: '- 设计长链路电商运营/客服/工单处理Agent时，若链路涉及数据库/缓存/中间件状态变更，可采用全环境快照做状态复用，避免重复执行前置步骤浪费token与执行时间

  - 短链路、所有状态可通过文本/代码复现的Agent任务（如商品文案生成、简单规则改写），直接从头重试成本更低，无需引入复杂的快照机制

  - 落地Agent状态复用机制时，需同步优化状态价值评估、预算动态分配、上下文传递三个模块，仅实现状态可恢复不足以提升整体性能'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
编码Agent执行失败后默认从头重试，会丢弃执行过程中积累的依赖安装、数据库写入、服务启动等非代码仓库状态，浪费大量token与算力；现有状态留存方案仅覆盖文本、Git提交维度，无法完整保存执行环境，亟需明确全环境快照的适用边界与投入产出比。
### 方法关键点
- 借鉴Go-Explore搜索思路，基于Daytona全沙箱快照保存Agent执行的完整中间状态，失败后选取高价值快照恢复，启动新Agent继续执行
- 控制总token预算完全一致，对比快照分支重试、独立从头重试、仅Git diff恢复三类方案的任务成功率与资源消耗
- 系统性梳理快照方案的四类典型失效模式：预算碎片化、错误状态留存、Agent上下文传递成本、状态选择信号弱
### 关键结果
- 在Terminal-Bench 2.0的5个通用文件型任务上，独立从头重试成功率68%（17/25），快照分支重试仅24%（6/25）
- 在定制多服务修复任务（进度保存在Git未追踪的SQLite数据库中）中，全快照恢复成功率80%（4/5），干净重启、仅Git diff恢复成功率均为0%，且快照方案单任务token消耗仅为其他方案的1/2
### 核心结论
全环境快照仅在任务进度存在于代码仓库外时才有明确收益，状态恢复能力不等于状态选择与利用能力
