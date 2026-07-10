---
title: 'Agents That Teach: Towards Designing Incidental Learning Back into AI-Assisted
  Software Development'
title_zh: 会教学的Agent：将偶发学习融入AI辅助软件开发流程
authors:
- Rohit Mehra
- Samdyuti Suri
- Prithviraj K Tagadinamani
- Kapil Singi
- Vikrant Kaulgud
- Adam P. Burden
affiliations:
- Accenture Labs, India
- Accenture, USA
arxiv_id: '2607.06101'
url: https://arxiv.org/abs/2607.06101
pdf_url: https://arxiv.org/pdf/2607.06101
published: '2026-07-07'
collected: '2026-07-10'
category: MultiAgent
direction: 多智体协作 · 人机交互学习设计
tags:
- MultiAgent
- Human-Agent Interaction
- Incidental Learning
- Knowledge Debt
- Coding Agent
one_liner: 提出6项人机交互设计原则，落地为多Agent系统SHIELD，在不干扰开发流程的同时为开发者植入偶发学习环节
practical_value: '- 搭建用户侧Agent助手时可参考该设计思路，在不干扰用户主任务流程的前提下插入轻量化知识点提示，降低用户对AI输出的理解门槛，减少决策风险

  - 多Agent架构分工可复用：拆分任务执行Agent、知识抽取Agent、时机触发Agent，兼顾主任务效率与附加价值输出，例如电商客服Agent可在解决问题的同时同步推送相关产品知识

  - 知识负债评估思路可迁移到商家运营场景：追踪B端商家对AI推荐运营策略的理解程度，对长期依赖AI决策的商家补全适配的运营知识，提升商家留存'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
AI coding Agent已成为软件开发核心工具，大幅提升生产效率的同时，切断了开发者通过自主问题解决完成偶发学习的路径，长期会导致技能退化，积累无法理解Agent输出的「知识负债」，偶发学习无法自然恢复，必须主动融入人机交互流程。
### 方法关键点
提出6项兼顾生产效率与学习效果的人机交互设计原则，落地为多Agent系统SHIELD，复用编码Agent的自身推理过程，挖掘上下文匹配的带外学习时机，完全不打断开发者正常工作流。
### 关键结果
行业统计显示当前42%的提交代码为AI生成/辅助，预计2027年占比将达65%，该设计可实现生产率提升与开发者能力成长的互补，而非零和博弈。
