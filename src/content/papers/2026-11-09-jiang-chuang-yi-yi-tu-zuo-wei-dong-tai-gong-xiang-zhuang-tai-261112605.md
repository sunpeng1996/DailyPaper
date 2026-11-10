---
title: 'Creative Intent as an Evolving Shared State: Supporting Cross-Stage Human-AI
  Video Co-Creation'
title_zh: 将创意意图作为动态共享状态：支持跨阶段人机协同视频创作
authors:
- Yuhang Jin
- Mengfei Chen
- Hanwei Zheng
- Songruoyao Wu
- Kejun Zhang
arxiv_id: '2611.12605'
url: https://arxiv.org/abs/2611.12605
pdf_url: https://arxiv.org/pdf/2611.12605
published: '2026-11-09'
collected: '2026-11-10'
category: Agent
direction: Agent 人机协同内容创作
tags:
- Human-AI Collaboration
- Creative Intent
- AI Agent
- Video Co-creation
- Interactive System
one_liner: 提出将创意意图作为动态共享状态的设计思路，开发跨阶段人机协同视频创作系统VideoMaker
practical_value: '- 电商短视频/广告脚本创作工具可复用「创意意图跨阶段对齐」思路，在每个生成节点增加人工确认环节，大幅降低AI生成偏离业务brief的概率

  - 可直接复用「共享Agent+领域知识库」架构，搭配电商商品知识库、爆款脚本库，支撑初始需求的多风格扩写，同时保障生成内容符合业务要求

  - 多阶段创作流程设计可迁移到AI生成广告素材的全链路工具，从需求拆解、脚本生成到素材渲染全流程保留用户/业务意图的一致性'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
生成式AI已渗透视频创作全链路，但创作者面临创意意图在多阶段创作中对齐、传递、协商的难题，现有工具多为单阶段孤立功能，无法支撑跨阶段的人机协同意图共识。
### 方法关键点
1. 将创意意图定义为全流程动态更新的共享状态，设计6阶段渐进式意图转化的创作workflow
2. 核心设计Seed Panel交互模块，支持创作者在关键节点与AI协商，显式确认、修正、更新意图
3. 搭载共享AI Agent，配套多风格脚本库、电影语言知识库，实现初始意图的差异化扩写与保真转化
### 关键结果
30人被试内实验显示，系统可有效支撑创意意图的扩写与跨阶段传递，意图保留度显著提升，但人工确认意图与AI自主创作的边界仍难以长期维持
