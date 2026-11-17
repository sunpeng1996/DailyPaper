---
title: 'SWE-CoWork: Benchmarking Coding Agents as Digital Employees in Organizations'
title_zh: SWE-CoWork：面向企业组织内数字员工的编码Agent评测基准
authors:
- Xinping Lei
- Minghao Liu
- Ruijie Zhu
- Xiaohui Hu
- Xingqiao Li
- Ao Zhang
- Wenhao Chai
- Han Li
- Tao Wang
- Jingyuan Zhang
affiliations:
- TokenWave AI
arxiv_id: '2611.20218'
url: https://arxiv.org/abs/2611.20218
pdf_url: https://arxiv.org/pdf/2611.20218
published: '2026-11-14'
collected: '2026-11-17'
category: Agent
direction: Agent 编码数字员工协作能力评测
tags:
- Agent Benchmark
- Multi-Role Collaboration
- Requirement Tracking
- Coding Agent
- Autonomous Workflow
one_liner: 推出覆盖101个真实开发任务的多角色协作编码Agent基准，揭示全链路需求跟踪核心痛点
practical_value: '- 搭建业务Agent落地评测体系时，可参考该基准的多角色权责划分、分散需求模拟框架，还原真实业务协作场景，提升评测结果的业务参考性

  - 业务Agent（如电商运营/投放Agent）的全流程设计中，需新增需求持续跟踪模块，避免未跟进问题、已获取需求未落地等漏项

  - 跨角色需求对齐场景可复用「定位对应负责人提问→校验需求完整性」的交互范式，提升零散需求的采集准确率'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有编码Agent评测多聚焦孤立编码任务，未还原真实企业中跨角色协作、分散需求采集对齐的完整开发流程，无法准确衡量Agent作为数字员工的实际落地能力。
### 方法关键点
推出SWE-CoWork基准，包含101个真实仓库的开发任务，覆盖11种编程语言、12个应用领域；模拟含26名不同职责、有限知识的同事的企业环境，要求Agent从简短交接出发，完成跨角色需求采集、冲突化解、开发实现并通过私有可执行测试。
### 关键结果数字
11款模型评测显示，top2模型的F2P测试通过率约63%，但完整任务完成率不足8%；提前提供完整需求可将Seed Evolving、GPT-6 Astra的F2P提升16个百分点，但完整任务成功率无变化；Claude-Opus-5.5 93%的首问能找对负责人，但仅能获取64%的分散需求，31%自报完成的需求未通过测试，全链路需求跟踪是核心瓶颈。
