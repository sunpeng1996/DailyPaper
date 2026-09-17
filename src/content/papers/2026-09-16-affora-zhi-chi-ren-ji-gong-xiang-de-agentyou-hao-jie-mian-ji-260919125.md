---
title: 'Affora: A Design System for Agent-Friendly Interfaces'
title_zh: Affora：支持人机共享的Agent友好界面设计系统
authors:
- Jin Gao
affiliations:
- Independent Researcher, USA
arxiv_id: '2609.19125'
url: https://arxiv.org/abs/2609.19125
pdf_url: https://arxiv.org/pdf/2609.19125
published: '2026-09-16'
collected: '2026-09-17'
category: Agent
direction: Agent 人机共享界面设计系统
tags:
- Computer-use Agent
- Interface Design
- Agent Experience
- Human-Agent Collaboration
- Design System
one_liner: 提出兼顾人机共享的界面设计系统Affora，在不改变用户体验的前提下大幅提升Agent操作成功率
practical_value: '- 电商后台/商家运营类Agent可复用Affora的语义substrate设计，将操作控件、状态、可选值显性化写入DOM，无需修改前端视觉样式即可降低Agent交互成本，适配商品上架、订单处理等自动化场景

  - WebAgent研发团队可参考Affora的可执行检查规则，在前端上线前做Agent友好性校验，提前规避控件语义缺失、状态不显性等导致Agent失败的问题

  - 电商大促活动页、广告投放页等既需要个性化视觉效果，又需要Agent自动投放/核验的场景，可复用「语义层不变、视觉层灵活」的分层设计，兼顾视觉效果和Agent操作可靠性'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前computer-use agent已广泛用于各类软件操作，但面向人类设计的界面普遍存在控件语义缺失、状态不显性、可选操作隐藏等问题，导致Agent操作失败率高；单独为Agent构建专用接口又会割裂人机体验，无法兼顾人类用户的使用习惯和监管需求，亟需一套平衡两者的界面设计方案。
### 方法关键点
- 界面拆分为两层：语义substrate层（包含控件、状态、可选值、操作关系等机器可读结构）、视觉渲染层，两层完全解耦，视觉样式可自由调整只要语义层符合规范
- 从组件、布局、流程、站点四个维度输出可落地设计规则，同时提供开箱即用的UI组件库和可自动化执行的Agent友好性检查工具
- 所有规则基于三项对照实验结论：语义缺陷是Agent操作失败的核心原因、语义层固定时视觉变化几乎不影响Agent性能、人类交互设计原则无法直接迁移到Agent场景
### 关键结果数字
- 基准测试集上，Affora将Agent任务成功率从基线的77%提升至100%，ARIA语义增强方案无明显提升
- 电商场景WebShop补充隐藏单选框语义规则后，任务成功率从8%提升至68%
- 完整工作流测试中，Agent操作次数下降21%~40%，总Token消耗降低24%~41%
### 核心结论
Agent操作效率不只是模型优化问题，合理的界面语义设计可以在不改变人类用户体验的前提下，大幅降低Agent的推理和交互成本
