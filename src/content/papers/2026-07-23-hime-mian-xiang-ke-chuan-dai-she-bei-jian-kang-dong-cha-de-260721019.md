---
title: 'HiMe: Real-Time Self-Hosted Personal Agent Platform for Health Insights with
  Wearable Devices'
title_zh: HiMe：面向可穿戴设备健康洞察的实时自托管个人Agent平台
authors:
- Wei Liu
- Siya Qi
- Linhai Zhang
- Lorainne Tudor Car
- Yulan He
affiliations:
- King's College London
- The Alan Turing Institute
arxiv_id: '2607.21019'
url: https://arxiv.org/abs/2607.21019
pdf_url: https://arxiv.org/pdf/2607.21019
published: '2026-07-23'
collected: '2026-07-26'
category: Agent
direction: 个人健康Agent · 本地自托管实时处理
tags:
- LLM Agent
- Edge Deployment
- Real-time Processing
- Privacy Preserving
- Long-term User Modeling
one_liner: 开源可本地部署的实时个人健康Agent平台，兼容多类可穿戴设备，兼顾隐私效率与长期用户建模
practical_value: '- 本地自托管Agent架构可复用在电商用户隐私敏感场景，如用户行为本地分析、个性化推荐不回传敏感数据

  - 「数据库作为一等组件+实时流处理+长期用户建模」的设计范式，可迁移到用户行为序列类推荐系统的工程实现

  - 效果效率联合优化做低成本Pareto最优的思路，可用于端侧/边缘侧LLM Agent部署的资源调度'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
传统可穿戴健康信号分析框架僵化、个性化能力不足，当前无开源可本地部署的LLM Agent方案，无法同时满足实时健康数据处理、用户隐私保护、长周期用户建模需求，且长时序可穿戴数据无法直接适配LLM上下文窗口限制。
### 方法关键点
1. 遵循三大设计原则：数据库作为一等核心组件、效果效率联合优化实现低成本Pareto最优、实时流数据处理+长周期用户建模；
2. 架构兼容全品类主流可穿戴设备生态，支持完全本地私有化部署，数据全链路不出用户私域；
3. 内置工具链、健康监控面板、对话交互、主动健康任务、Agent深度分析等完整能力。
### 关键结果
已开源全部工程代码，本地部署下无用户数据外传，端到端健康洞察生成延迟满足实时交互要求，支持用户长期个性化健康监测。
