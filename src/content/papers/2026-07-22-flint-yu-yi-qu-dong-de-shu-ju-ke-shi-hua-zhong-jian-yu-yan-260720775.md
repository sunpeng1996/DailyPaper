---
title: 'Flint: A Semantics-Driven Data Visualization Intermediate Language'
title_zh: Flint：语义驱动的数据可视化中间语言
authors:
- Yunhai Wang
- Kecheng Lu
- Junhao Chen
- Alper Sarikaya
- Chenglong Wang
affiliations:
- Microsoft
arxiv_id: '2607.20775'
url: https://arxiv.org/abs/2607.20775
pdf_url: https://arxiv.org/pdf/2607.20775
published: '2026-07-22'
collected: '2026-07-26'
category: Agent
direction: Agent 数据可视化生成中间件
tags:
- Visualization
- Intermediate Language
- LLM Agent
- Semantic Modeling
- Cross-Platform
one_liner: 提出语义驱动的可视化中间语言Flint，支持多库渲染，简化人与AI Agent的可视化创作流程
practical_value: '- 电商运营/商家BI类Agent可复用Flint的分层语义模型，将自然语言查询转成结构化dataSpec+chartSpec，规避LLM直接生成可视化代码的不稳定问题

  - 有多端图表渲染需求的业务（如跨PC/小程序的商家报表、推荐效果看板系统），可借鉴其中间层设计，一套spec编译适配多主流图表库，降低多端开发成本

  - 设计Agent的可视化工具调用协议时，可参考Flint的精简spec结构，降低Agent生成合法参数的难度，减少幻觉'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有可视化创作要么需手动配置大量低层级参数（刻度、轴、格式）效率极低，要么基于表层数据推断默认配置，生成结果鲁棒性差，同时LLM Agent直接生成可视化代码易出错、跨环境适配性差。
### 方法关键点
1. 设计分层数据语义模型，仅需结构化定义数据字段含义（如分类、增量值、数量），无需指定渲染层参数；
2. 编译器基于语义自动推导、优化跨库可视化配置，支持输出Vega-Lite、Apache ECharts、Chart.js等多目标可执行代码；
3. 采用极简spec结构，同时适配人类手动编写与AI Agent自动生成两种场景。
### 关键结果
在不损失可视化质量的前提下大幅简化创作流程，已验证可直接作为LLM Agent的可视化工具调用接口，适配所有主流前端图表库。
