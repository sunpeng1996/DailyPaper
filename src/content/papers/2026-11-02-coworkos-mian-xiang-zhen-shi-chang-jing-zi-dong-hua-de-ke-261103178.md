---
title: CoworkOS:Scaling Agent Coworkers for Real-world Automation
title_zh: 《CoworkOS：面向真实场景自动化的可扩展协作Agent运行框架》
authors:
- Jiajie Jin
- Guanting Dong
- Chengjun Pan
- Xin Deng
- Zhuohui Sheng
- Guoqiang Wang
- Tao Gui
- Yutao Zhu
- Yujia Chen
- Shihong Yi
affiliations:
- 中国人民大学NLPIR
- 复旦大学
- CoworkOS Team
arxiv_id: '2611.03178'
url: https://arxiv.org/abs/2611.03178
pdf_url: https://arxiv.org/pdf/2611.03178
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: Agent协作框架 · 长周期任务运行时
tags:
- Agent Framework
- Human-in-the-loop
- Long-horizon Task
- Runtime Architecture
- Multi-agent Collaboration
one_liner: 提出三层架构的协作Agent运行框架，支持长周期任务、人在环交互与多场景自动化落地
practical_value: '- 三层Agent架构（主Agent+协调器+子Agent）可直接复用在电商大促自动化运营、推荐效果迭代等长周期任务：主Agent管控全局策略，子Agent并行处理数据清洗、AB实验监控等子任务，有效降低主Agent上下文压力，提升并行效率

  - 人在环共享资源协议可迁移到电商Agent辅助运营场景：支持运营人员直接修改Agent生成的活动文案、商品页素材，系统自动识别版本冲突避免人工修改被覆盖，同时把人工修改作为反馈输入迭代后续生成结果

  - 分层语义记忆+任务断点恢复机制可用于推荐系统全链路调优Agent：自动记录多轮AB实验的结论、待优化点，系统中断重启后可自动恢复调优流程，无需人工重传全量上下文'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前协作Agent落地真实生产场景时，同时面临复杂任务高质量交付、长周期任务持续监控决策的双重挑战，现有框架要么只支持单Agent短流程推理，要么缺乏稳定的人在环交互、任务断点续跑能力，难以支撑代码开发、模型训练、专业设计等跨时长大复杂度的真实生产力任务。

### 方法关键点
- 三层运行时架构：主Agent负责全局任务规划、结果验收，协调器运行时负责任务分发、状态同步、子Agent生命周期管理，子Agent独立承接子任务执行，支持同步/异步调度，隔离子任务上下文降低主Agent负载
- 人在环共享应用生态：定义统一资源协议支持文档、PPT、CAD、Blender等多类型资产的版本管理，人和Agent可直接修改同一份工作资产，系统自动检测版本冲突，人工修改可直接作为任务反馈输入
- 持久化工作空间：分层存储工作文件、语义记忆、任务执行日志，支持长周期任务断点恢复，中断后无需重新传入全量上下文即可继续执行

### 关键实验
在12个Agent基准测试、6类真实场景任务上对比OpenHands、Codex、DeepSeek Harness三个主流框架，在生产力、ML编码两个领域平均分位列第一，工具使用、搜索领域位列前二；用其搭建自动后训练的RSI闭环，5轮迭代后Qwen3.6-35B在8个基准上平均分从33.19提升到42.95，涨幅达9.76。

### 最值得记住的一句话
协作Agent落地的核心是把模型决策和运行时管理解耦，模型管策略、运行时管状态与反馈，才能同时支撑复杂短任务和长周期监控需求。
