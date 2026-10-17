---
title: 'Inflak: A Unified Orchestration Architecture for Human-Agent Interaction'
title_zh: Inflak：面向人机Agent交互的统一编排架构
authors:
- Lin Gao
- Li Chen
- Jianxun Lian
- Ji Li
- Haotian Li
affiliations:
- Fudan University
- Microsoft
- Microsoft Research Asia
arxiv_id: '2610.21972'
url: https://arxiv.org/abs/2610.21972
pdf_url: https://arxiv.org/pdf/2610.21972
published: '2026-10-15'
collected: '2026-10-17'
category: Agent
direction: Agent 人机交互编排架构设计
tags:
- Human-Agent-Interaction
- Orchestration-Architecture
- LLM-Agent
- Plugin-System
- Copilot
one_liner: 提出四层渐进式人机Agent交互编排架构，同时满足通用性、灵活性、可组合与可维护要求
practical_value: '- 电商导购Agent、内容推荐Agent可直接复用四层解耦架构，将交互路由、需求缺口判断、交互设计、界面渲染分层实现，避免硬编码交互逻辑，适配多场景动态交互需求

  - 新增交互形式（比如选品意愿收集表单、穿搭草图输入、偏好点选组件）只需开发对应L3 Designer插件，不需要修改全链路代码，大幅降低迭代成本

  - 运营/产品侧的新交互需求可通过自然语言对接编码Agent生成插件，不需要全链路开发，缩短需求落地周期'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
LLM驱动的Agent已广泛应用于开放任务，但运行时动态决策是否需要和人类交互、采用什么形式交互的编排问题长期缺乏统一方案：现有方案要么和特定任务绑定适配性差，要么交互形式僵硬灵活性不足，要么跨任务复用性差维护成本高，无法满足日益多样的人机协作需求。
### 方法关键点
- 基于IAI交互模型设计四层渐进式架构：L1 Router层重构当前任务状态并路由到对应L2 Planner；L2 Planner层诊断任务缺口，判断是需要人类交互还是直接执行；L3 Designer层根据交互需求输出语义化组件合约，不涉及具体实现；L4 Renderer层生成可运行交互界面并校验返回结果
- 采用技能化插件实现，各层实例通过统一契约交互，新增任务规划能力只需新增L2 Planner并注册，新增交互形式只需新增L3 Designer，不需要修改全链路逻辑
- 支持动态路由路径，无交互需求时可直接跳过L3、L4调用执行器，所有交互/执行结果都回流到L1更新状态
### 关键实验
在GitHub Copilot上实现架构，首先完成IAI模型定义的全部13种交互范式的插件开发，支持率100%；将10种不同交互范式的插件合并为多模态共创、视觉拼贴创作2个聚合插件，验证可组合性；对比传统硬编码方式实现相同多模态共创插件，Inflak实现的开发时间减少58%，后续迭代修改成本降低72%，全链路交互响应延迟低于150ms，无感知影响用户体验。
### 核心结论
人机Agent交互编排的核心是把交互决策分层渐进式拆解，解耦状态、逻辑、设计、实现才能同时满足通用性和灵活性。
