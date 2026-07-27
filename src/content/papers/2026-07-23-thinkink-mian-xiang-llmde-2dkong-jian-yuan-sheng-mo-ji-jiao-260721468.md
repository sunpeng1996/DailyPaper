---
title: 'Thinkink: 2D Spatial Ink-native Interaction with LLMs'
title_zh: Thinkink：面向LLM的2D空间原生墨迹交互系统
authors:
- Mohammad Hasan Payandeh
- Daniel Vogel
- Jian Zhao
affiliations:
- Cheriton School of Computer Science, University of Waterloo
arxiv_id: '2607.21468'
url: https://arxiv.org/abs/2607.21468
pdf_url: https://arxiv.org/pdf/2607.21468
published: '2026-07-23'
collected: '2026-07-27'
category: LLM
direction: LLM原生墨迹交互 · 人机协同创意
tags:
- Digital_Inking
- 2D_Spatial_Canvas
- Human_AI_Interaction
- LLM
- Ideation_Tool
one_liner: 支持手写/草图输入、共享画布墨迹输出的原生LLM交互工具及设计启示
practical_value: '- 多模态输入的语义树解析结构可复用：适配电商场景用户手绘需求、手写评价等非结构化输入的意图识别，提升Query理解准确率

  - 2D空间上下文关联逻辑可迁移到Agent创意协作工具：用于电商营销海报、直播间物料的人机协同创作画布，支持零散输入的上下文串联

  - 状态机驱动的轻量UI控制逻辑可借鉴：降低复杂人机交互场景的用户操作成本，可用于商家端智能运营工具的交互流程设计'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
用户普遍通过手写笔记、草图在2D空间外化创意，现有LLM交互范式未适配原生墨迹创作流程，无法利用空间上下文信息，人机协同创意效率低。
### 方法关键点
1. 构建Thinkink交互系统：支持手写文本、手绘草图作为Prompt输入，LLM生成的文本、草图以类墨迹形式在共享2D画布空间融合输出，符合用户原生创作习惯
2. 设计语义树结构简化墨迹语义解析，基于状态机实现轻量UI显式控制，降低用户操作门槛
3. 采用三阶段用户研究迭代设计：先开展12人形成性研究梳理现有墨迹创作实践，再通过6人诊断性研究定位人机交互痛点，最终落地可用工具
### 关键结果
10人终期用户研究验证工具可有效融入用户创意生成流程，输出了原生墨迹LLM交互的系列可落地设计启示
