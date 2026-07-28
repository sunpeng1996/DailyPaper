---
title: 'JarvisHub: An Open Harness for Canvas-Native Multimodal Creative Agents'
title_zh: JarvisHub：面向画布原生多模态创意Agent的开源运行框架
authors:
- Yunlong Lin
- Zixu Lin
- Zhaohu Xing
- Biqiang Li
- Chenxin Li
- Haonan Wang
- Haitao Wu
- Hengyu Liu
- Jianghai Chen
- Kaituo Feng
affiliations:
- JarvisX Team
arxiv_id: '2607.23588'
url: https://arxiv.org/abs/2607.23588
pdf_url: https://arxiv.org/pdf/2607.23588
published: '2026-07-25'
collected: '2026-07-28'
category: Agent
direction: 多模态创意Agent · 开源运行框架
tags:
- Multimodal Agent
- Creative AI
- Open Source Framework
- Canvas Native
- Long-horizon Task
one_liner: 提出以画布为统一共享状态的开源多模态创意Agent框架，支持长周期创作全流程管控与可追溯迭代
practical_value: '- 搭建电商营销内容生成Agent时，可复用画布作为统一项目状态的设计，将文案、海报、短视频、版本记录、用户反馈全部结构化存储为带类型的画布节点，彻底解决聊天式Agent上下文丢失、中间态不可追溯的问题

  - 参考协议桥设计，给Agent的画布读写、工具调用增加权限校验、操作格式校验与全量日志记录，降低Agent操作失误导致的内容错误风险，适配电商营销内容的合规审核要求

  - 全流程轨迹记录机制可直接迁移到业务中，结构化存储Agent的每一步操作、工具调用结果、用户反馈、状态变更，既可以用于训练Agent的任务规划能力，也可作为内容合规审计的凭证'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前多模态创意生产工具存在明显短板：单步生成工具会丢弃中间上下文，聊天式Agent依赖线性会话无法承载空间布局、版本分支等复杂状态，节点工作流工具需要手动配置固定流程，商业创意Agent系统又全部闭源，无法支持长周期多模态创作Agent的状态管理、工具调度、反馈迭代等核心问题的研究与落地。
### 方法关键点
- 以可编辑画布作为用户与Agent共享的唯一项目状态，用带类型的节点和有向边存储所有多模态资产、依赖关系、版本记录、用户反馈、空间布局信息，支持资产可寻址、可复用、依赖可追溯
- 三层核心架构：画布状态层统一存储项目全量信息，协议桥层管控Agent的读写权限、操作校验与日志审计，Agent运行时层封装5类工具族，支持Skill复用、跨轮次记忆、子Agent并行执行
- 全轨迹记录机制，存储每一轮的用户请求、画布状态、Agent动作、工具返回结果、反馈信号、状态变更，支持过程评估与模型训练
### 关键实验
基于GPT-5.5作为Agent后端，搭配GPT Image 2、Seedance 2.0、Gemini 3.1 Pro等工具，在叙事媒体生成、交互式网页开发、演示文稿生成3类典型长周期创意任务上完成定性验证，所有任务均可保持资产风格、叙事逻辑、结构的跨步骤一致性，全流程中间态可追溯、用户可随时干预调整。
### 最值得记住的一句话
画布不仅是用户的可视化交互界面，更是Agent与人类共享的外部记忆、动作空间与唯一项目状态载体，长周期复杂Agent任务的核心是对共享状态的可管控迭代。
