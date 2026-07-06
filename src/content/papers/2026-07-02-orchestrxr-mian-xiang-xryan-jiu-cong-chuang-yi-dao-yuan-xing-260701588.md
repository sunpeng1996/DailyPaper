---
title: 'OrchestrXR: A Multi-Agent System for Idea-to-Prototype XR Study Authoring'
title_zh: OrchestrXR：面向XR研究从创意到原型开发的多智能体系统
authors:
- Shuqi Liao
- Chenfei Zhu
- Karthik Ramani
- Voicu Popescu
affiliations:
- Purdue University
arxiv_id: '2607.01588'
url: https://arxiv.org/abs/2607.01588
pdf_url: https://arxiv.org/pdf/2607.01588
published: '2026-07-02'
collected: '2026-07-06'
category: MultiAgent
direction: 多智能体工作流编排 · XR应用生成
tags:
- MultiAgent
- Workflow Orchestration
- Human-AI Collaboration
- Prototype Generation
- XR
one_liner: 提出分阶段编排的多智能体工作流，支持从自然语言需求生成可运行Unity XR研究原型
practical_value: '- 多阶段分治Agent架构可复用：针对复杂长链路任务（如营销活动从创意到落地、商品3D素材生成）拆为专属子Agent，通过结构化Schema传递信息，避免跨阶段信息失真

  - 统一人机交互设计可借鉴：复杂Agent工作流中保留单一自然语言交互入口，支持用户中途修正需求，大幅提升生成结果可控性

  - 执行环境与Agent层解耦思路可落地：生成结果直接对接下游生产环境（如电商素材平台、推荐规则引擎），减少人工后处理成本'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
XR研究从创意到可运行原型的链路分散在研究设计、3D场景搭建、交互逻辑实现三个独立环节，缺乏端到端可控的自动化支持，人力成本高。

### 方法关键点
OrchestrXR多智能体系统将XR原型生成拆为3个串联的专属Agent阶段：1）研究设计Agent输出标准化研究方案；2）场景生成Agent输出3D场景规范；3）交互生成Agent输出可执行交互逻辑；全程通过结构化Schema传递各阶段输出，保留用户原始意图，同时提供统一自然语言交互入口支持用户中途调整需求，最终直接生成Unity可运行工程。

### 关键结果数字
12名XR研究者参与的用户实验显示，系统可有效支持早期XR研究创作，各阶段用户意图保留度表现优异。
