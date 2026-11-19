---
title: 'MemoSync: Co-Managing Developer-Agent Metamemory Across Contexts'
title_zh: MemoSync：跨上下文的开发者-Agent元记忆协同管理系统
authors:
- Baiqiao Zhang
- Junze Li
- Chunyang Luo
- Yuying Tang
- Wenshuo Zhang
- Shiyuan Piao
- Dingdong Liu
- Shuai Ma
- Xiaojuan Ma
affiliations:
- The Hong Kong University of Science and Technology
- Peking University
- Institute of Software, Chinese Academy of Sciences
arxiv_id: '2611.24165'
url: https://arxiv.org/abs/2611.24165
pdf_url: https://arxiv.org/pdf/2611.24165
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: Agent 人机协作记忆优化
tags:
- Agent Memory
- Human-AI Collaboration
- Metamemory
- Coding Agent
- Memory Alignment
one_liner: 提出跨上下文开发者-Agent元记忆共管系统MemoSync，解决记忆错配问题提升协作效率
practical_value: '- Agent记忆分层设计可直接复用：将用户偏好、场景规则、会话临时信息划分为personal/project/session三级
  scope，跨场景迁移时先抽象通用规则再适配目标场景，避免规则泄露、过时规则生效，可直接用于电商智能客服Agent、个性化推荐Agent的记忆系统

  - 全流程记忆管控逻辑可迁移：复用「生成前记忆候选审核+当轮记忆自定义选择→生成中记忆引用实时溯源+中断修正→生成后记忆使用效果审计」的闭环设计，解决大模型应用记忆黑盒问题，可落地到推荐Agent的标签使用溯源、广告文案生成的规则合规校验场景

  - 记忆对齐评估框架可借鉴：参考文中记忆对齐度、监控准确率、控制准确率的三维度量体系，量化用户对Agent的记忆预期和Agent实际存储/使用状态的偏差，优化可控Agent的迭代效果'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前AI Agent跨会话、跨场景工作时，人类对Agent存储、检索、使用的记忆可见性极低，双方记忆错配会导致规则泄露、过时规则生效、输出不符合预期等问题，现有自动记忆、静态配置方案都无法同时满足人类对Agent记忆的监控和控制需求，严重影响人机协作效率。

### 方法关键点
- 基于12名高频使用编码Agent开发者的形成性研究，明确开发者对Agent记忆的4维管控需求：演化（记忆如何变更）、选择（每轮调用哪些记忆）、执行（记忆如何被应用）、影响（记忆对输出的作用）
- 记忆采用三级scope划分：个人级、项目级、会话级，跨上下文迁移时自动完成源记忆抽象、目标场景适配，避免源场景细节泄漏
- 全流程记忆管控闭环：生成前审核记忆候选、自定义选择当轮工作记忆，生成中实时展示记忆引用支持中断修正，生成后审计记忆使用效果标记违规项
- 兼容现有Markdown配置文件，可直接对接现有Agent框架，无需额外LLM API改造

### 关键结果数字
132名参与者的组间实验对比自动记忆（Auto）、静态配置（Static）两个基线：MemoSync组任务得分比Auto高21.3%，比Static高14.7%；记忆对齐率比两个基线分别高38.2%、27.5%；参与者执行了更多监控控制操作，但感知工作负荷无显著提升。9人一周的灰度部署验证该系统可无缝融入日常工作流程。

**最值得记住的一句话：** Agent记忆应当作为人和Agent均可读、可编辑、可操作的共享表示，而非Agent侧的黑盒模块
