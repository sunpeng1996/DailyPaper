---
title: 'Work Agents: Systems, Capabilities, and Optimization'
title_zh: 《工作智能体：系统架构、核心能力与优化方法》
authors:
- Zishan Xu
- Enjun Du
- Mingqi Gao
- Cheng Yang
- Junhao Shen
- Zirong Chen
- Zhiyuan Yao
- Yifu Guo
- Yuquan Lu
- Jinyang Huang
affiliations:
- 上海交通大学
- 香港大学
- 香港科技大学（广州）
- 清华大学
- 浙江大学
arxiv_id: '2610.35845'
url: https://arxiv.org/abs/2610.35845
pdf_url: https://arxiv.org/pdf/2610.35845
published: '2026-10-25'
collected: '2026-10-27'
category: Agent
direction: 工作智能体 · 系统框架与能力优化
tags:
- WorkAgent
- AgentSystem
- AgentCapability
- AgentOptimization
- AgentEvaluation
one_liner: 提出以工作为中心的统一框架，系统性定义工作智能体的能力体系、优化路径与评估方法
practical_value: '- 电商/广告场景Agent开发可直接复用「工作持久性、工作开放性」二维框架拆解任务复杂度，比如售后工单处理属于高持久高开放任务，商品文案生成属于低持久低开放任务，匹配不同的harness设计，避免能力冗余或不足

  - 5类核心能力族的划分可直接套用到业务Agent的模块设计，清晰划分感知、推理、规划、执行、校验的模块边界，降低系统重构成本

  - 优化阶段优先参考「模型+harness联合优化」思路，复杂的状态管理、依赖追踪、重试逻辑直接在harness层实现，无需依赖大模型微调，降低落地成本

  - 业务评估放弃唯单步正确率论，从工作产出质量、环境状态变更、流程完成度、约束满足度多维度评估，更贴近实际业务价值'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent研究缺乏统一视角保障复杂跨工具、跨流程任务的可靠执行，无法支撑工作场景下持续、可验证的任务交付需求，亟需系统级框架指导工作智能体的设计、优化与评估。

### 方法关键点
- 定义工作智能体六要素系统架构：任务、大模型核心、运行时harness、状态化工作空间、工作产出、校验机制，明确各组件交互逻辑
- 用工作持久性（交付即结束/跨阶段持续责任）、工作开放性（任务要素预定义/执行中动态发现）两个维度对工作场景分类，匹配不同能力要求
- 梳理5类核心能力族：感知理解、推理决策、规划协调、执行与状态管理、校验恢复与重规划，形成闭环执行链路
- 覆盖三类优化路径：大模型优化（预训练/中训练/后训练）、harness优化（接口/流程控制/记忆）、二者联合优化，同时给出面向工作产出的评估体系

### 关键结果
作为综述类研究，系统性梳理100+相关工作的benchmark、能力边界、优化效果，覆盖会话级到工作空间级5类工作形态的最佳实践，为不同复杂度的工作智能体落地提供了参考路径。

### 最值得记住的一句话
工作智能体的核心是产出可验证的工作结果，而非单纯输出正确的单步响应或工具调用。
