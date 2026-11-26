---
title: 'EgoUseBench: Benchmarking Computer-Use Agents under Evolving First-Person
  Contexts'
title_zh: EgoUseBench：动态第一人称上下文下计算机操作Agent基准测试
authors:
- Yurun Chen
- Biao Yi
- Qihang Yu
- Keting Yin
- Shengyu Zhang
affiliations:
- Zhejiang University
arxiv_id: '2611.34466'
url: https://arxiv.org/abs/2611.34466
pdf_url: https://arxiv.org/pdf/2611.34466
published: '2026-11-24'
collected: '2026-11-26'
category: Agent
direction: Agent 第一人称动态场景评测
tags:
- Agent
- Benchmark
- First-person Vision
- Multimodal Agent
- Ego Use
one_liner: 提出覆盖三类交互场景的693任务基准，评测动态第一人称上下文下的计算机操作Agent性能
practical_value: '- 开发AR眼镜/直播场景下的电商购物Agent时，可复用Graft/Refresh/Clarify三类动态需求更新机制，适配用户边操作边提需求的真实场景

  - 长时序多模态Agent的视觉历史管理优先采用压缩历史（隔帧采样）方案，比全量历史降本30%以上，且性能比文本摘要更稳定

  - 面向动态需求的Agent可增加场景变更主动提醒模块，能提升最高13%的动态任务成功率，适配直播导购、实时客服等场景

  - 动态意图跟踪模块必须配套历史动作可回滚机制，避免新需求出现时旧错误选择残留，这是当前Agent失败的核心原因之一'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
AR智能眼镜等穿戴设备让Agent可基于用户实时第一人称上下文完成数字任务（如加购用户手持商品、检索当前操作的教程），但现有计算机操作Agent基准仅支持静态上下文与固定需求，无法衡量Agent适配动态演进的观测信息、用户意图的能力。

### 方法关键点
- 划分三类交互场景：仅接收显式指令的Computer-Use、预加载全量第一人称上下文的Offline Ego Use、流式输入观测+动态更新用户意图的Online Ego Use
- 任务按动态更新逻辑分为三类：Graft（用户主动修改需求）、Refresh（新观测刷新上下文，旧决策可能失效）、Clarify（Agent主动发问澄清指代歧义）
- 异步维护三类独立演进状态：第一人称观测流、用户需求集、网站操作状态，支持动态更新校验与结果回溯

### 关键实验
基于74小时真实第一人称录像构建693个任务，覆盖商品选品、教程检索、地点收藏三类场景，评测6款主流大模型：跨模型平均成功率Computer-Use为86.1%、Offline Ego Use为64.2%、Online Ego Use为63.4%；Online场景比Offline场景token消耗低16.4%~38%；增加场景变更提示可提升最高13%的动态任务成功率。

### 核心结论
动态第一人称场景下Agent失败的核心原因不是感知能力不足，而是意图跟踪断层、旧决策未及时修正。
