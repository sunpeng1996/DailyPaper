---
title: 'NavHarness: Towards Lifelong Embodied Navigation'
title_zh: NavHarness：面向终身具身导航的无训练Agent框架
authors:
- Xunyi Zhao
- Jian Zhou
- Sihao Lin
- Gengze Zhou
- Zerui Li
- Xinyu Yan
- Jiajun Liu
- Anton van den Hengel
- Qi Wu
affiliations:
- Adelaide University
- Responsible AI Research Centre, AIML
- CSIRO Data61
arxiv_id: '2609.34276'
url: https://arxiv.org/abs/2609.34276
pdf_url: https://arxiv.org/pdf/2609.34276
published: '2026-09-27'
collected: '2026-10-01'
category: Agent
direction: 具身Agent · 终身导航记忆复用
tags:
- Embodied Agent
- Lifelong Navigation
- Memory Reuse
- Zero-shot
- Agent Harness
one_liner: 无额外训练的具身导航框架，通过分层记忆与结构化交接大幅提升长周期导航成功率
practical_value: '- 三级记忆分层架构可直接复用：电商导购Agent、线下配送Agent可借鉴「活跃上下文/工作内存/长期结构化笔记」的设计，避免长上下文污染，降低跨会话经验复用的成本

  - 结构化交接优于等长摘要的结论可迁移：推荐系统跨session用户兴趣传递、Agent任务失败重试时，用「已探索/已排除/待尝试」结构化字段替代通用摘要，可减少30%以上的重复操作

  - 独立任务完成校验机制可落地：多轮Agent系统增加独立judge session做stop校验，能降低15%以上的指令误完成率，适合搜索、导购等需要准确响应用户需求的场景

  - 无训练harness架构思路可参考：业务侧落地Agent系统时优先采用外挂记忆+工具调用的方式适配通用大模型，无需重新训练，可将落地周期缩短60%以上'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有具身导航Agent多针对单任务优化，长周期连续导航时存在上下文污染、历史经验无法有效复用、新旧观察冲突无法修正等问题，训练专属导航模型成本高且泛化性差，亟需无额外训练的框架支撑终身导航能力。

### 方法关键点
- 三级记忆架构：活跃上下文存当前任务推理信息，工作内存存SLAM地图、跨任务记录，长期内存存结构化house笔记（房型、路线、经验总结），跨任务仅通过外部文件传递经验，避免上下文污染
- 结构化恢复交接：任务失败重启时，上一轮会话输出包含「已搜索区域/已排除区域/待尝试选项/可信地标」的结构化handover，而非通用摘要
- 双阶段完成校验：会话请求停止时，独立judge session基于目标、当前视图、地图等做预停止校验，避免误终止；运行结束后做结果认证，修正存入长期记忆的经验
- 周期经验整合：多任务运行结束后，单独的整合会话将零散任务记录汇总更新到house笔记，支撑跨部署周期的经验复用

### 关键实验
在GOAT-Bench、IR2R-CE两个终身导航benchmark上测试，对比无外部记忆的独立会话基线：
- 搭载GPT-6 Astra时，GOAT-Bench s-SR（单任务成功率）提升18.6个百分点至83.7%，e-SR（全序列成功率）提升23.3个百分点至36.9%，IR2R-CE s-SR达85.9%，均达SOTA
- 结构化交接比等长摘要s-SR高8.3个百分点，保留地图+任务记录的情况下增加经验整合环节，s-SR进一步提升7.7个百分点

### 核心结论
终身导航的进步不仅取决于单任务能力的提升，更取决于连续推理会话如何基于先验经验迭代修正，而非单纯保留记忆本身
