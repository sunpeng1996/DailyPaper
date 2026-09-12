---
title: 'Pairit: A Platform for Live Experiments on Human-AI Collaboration'
title_zh: Pairit：支持人机协作实时实验的通用平台
authors:
- Harang Ju
- Sinan Aral
arxiv_id: '2609.09789'
url: https://arxiv.org/abs/2609.09789
pdf_url: https://arxiv.org/pdf/2609.09789
published: '2026-09-09'
collected: '2026-09-12'
category: Agent
direction: 人机协作 · 实验平台搭建
tags:
- Human-AI Collaboration
- Experiment Platform
- Agent Deployment
- Configuration as Code
- Collaborative Task
one_liner: 提供仅需YAML配置即可定义部署人机协作实时实验的可复用通用平台
practical_value: '- 做电商导购Agent、客服Agent的人效对比实验时，可参考单YAML配置化的实验框架，无需重复开发会话、匹配、数据埋点逻辑，大幅降低实验开发成本

  - 可复用其高分辨率人机交互埋点方案，采集人机协作任务中的协商、沟通、决策全链路数据，用于优化Agent的响应策略、协作流程

  - 团队内部验证Agent与运营、文案等人工岗位的协作流程时，可基于该平台的可配置实验图逻辑快速搭建定制化测试流程，缩短方案验证周期'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
人机协作组织设计的因果实验缺少统一可配置框架，现有平台仅支持纯人间会话或基础人机聊天，无法在同一套可审计配置中同时定义AI通信、共享空间操作、任务路由、团队匹配等全流程逻辑，实验代码复用性极低、难以复现和共享。
### 方法关键点
推出Pairit在线实验平台，仅需单个YAML文件即可声明完整可执行实验图，内置页面、路由、随机分组、用户匹配、会话、共享工作空间、服务端Agent托管、问卷、定时器、自定义HTML组件等原子能力，支持任意数量人与AI Agent组合的实时协作实验。
### 关键结果
已通过多轮真实部署验证可行性，支撑多篇同行评审发表研究，可完整捕获人机双人组的通信、协商、协作全流程高分辨率行为轨迹，实验配置标准化可审计、易跨团队共享复用。
