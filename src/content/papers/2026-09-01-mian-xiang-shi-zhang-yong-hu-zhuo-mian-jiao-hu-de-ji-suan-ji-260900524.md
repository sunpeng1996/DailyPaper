---
title: Are We There Yet? Assessing Computer-Use Agents for Blind Users' Accessible
  Interaction with Desktop Applications
title_zh: 面向视障用户桌面交互的计算机使用Agent效果评估
authors:
- Satwik Ram Kodandaram
- Monalika Padma Reddy
- Xiaojun Bi
- Jiawei Zhou
- I. V. Ramakrishnan
- Vikas Ashok
affiliations:
- Stony Brook University
- Old Dominion University
arxiv_id: '2609.00524'
url: https://arxiv.org/abs/2609.00524
pdf_url: https://arxiv.org/pdf/2609.00524
published: '2026-09-01'
collected: '2026-09-02'
category: Agent
direction: 计算机使用Agent · 无障碍交互评估
tags:
- Computer-Use-Agent
- Accessibility
- GUI-Agent
- LLM-Evaluation
- Multimodal-Agent
one_liner: 通过3周视障用户真实场景研究+跨模型评测，明确桌面计算机使用Agent的性能、失效模式与用户真实需求
practical_value: '- 开发GUI交互Agent时，建议同时输入UI树+截图双模态信息，避免纯视觉导致的grounding误差，可复用在电商后台操作、广告平台自动化Agent的开发中

  - 多步任务Agent需加入约束绑定、上下文状态跟踪模块，避免执行过程中丢失用户原始指令要求，降低部分完成率

  - 面向终端用户的Agent无需追求完全自动化，加入执行前解释、关键步骤确认、故障排查指引功能，可大幅提升用户接受度

  - Agent效果评估除实验室基准测试外，需引入真实用户的自然场景指令，避免基准数据与实际需求脱节'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前Computer-Use Agent（CUA）在桌面GUI自动化上进展迅速，但针对依赖屏幕阅读器的视障用户的真实场景效果未被系统评估，现有评测多基于模拟任务，无法反映真实失效模式与用户实际需求，填补该缺口对无障碍交互和通用CUA优化均有重要价值。

### 方法关键点
- 自研屏幕阅读器适配的CUA交互层OLLA，无需修改底层Agent架构，支持视障用户非视觉下发指令、监控执行、查看操作历史
- 开展3周IRB批准的纵向日记研究，招募8名视障用户在真实桌面工作流使用OLLA，采集12个应用下的1258条用户指令与全链路执行trace
- 除部署时用的GPT-5外，额外选择Claude Sonnet、Gemini 2.5 CU、UI-TARS、Qwen3-VL共5个模型，在干净应用环境下复现所有指令，控制变量对比效果
- 结合人工标注任务结果、trace分析、用户访谈，从性能、失效模式、非自动化需求三个维度展开分析

### 关键结果
5个模型中GPT-5成功率最高仅为52.5%，其次是Claude Sonnet 48.5%、Gemini 2.5 CU 43.9%、UI-TARS 39.8%、Qwen3-VL 37.9%；失效模式集中在UI grounding（占所有失败的22.6%）、隐藏路径发现（20.7%）、约束丢失、上下文跟踪失效、提前/延迟终止几类；视障用户对CUA的需求远不止全自动化，更需要界面解释、故障排查、操作确认、使用教学等协作式支持。

最值得记住的一句话：当前CUA在真实用户场景的成功率还远达不到可用水平，面向用户的Agent设计应优先做协作式助手而非完全自主的替代者。
