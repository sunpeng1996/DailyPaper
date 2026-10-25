---
title: 'BrickWright: Agentic Creation of Physically Feasible Brick Builds'
title_zh: BrickWright：生成物理可行积木搭建方案的智能体框架
authors:
- Ava Pun
- Kevin Dai
- Sally Chen
- Maxwell Jones
- Ruixuan Liu
- Kangle Deng
- Changliu Liu
- Maneesh Agrawala
- Deva Ramanan
- Jun-Yan Zhu
affiliations:
- Carnegie Mellon University
- Independent Researcher
- Stanford University
arxiv_id: '2610.31651'
url: https://arxiv.org/abs/2610.31651
pdf_url: https://arxiv.org/pdf/2610.31651
published: '2026-10-21'
collected: '2026-10-25'
category: Agent
direction: Agent 工具调用与约束验证框架
tags:
- Agent
- Tool Calling
- Validation Loop
- Code Generation
- 3D Generation
one_liner: 提出带装配工具与物理验证模块的智能体框架，生成100%物理可行的文本/图像转乐高方案
practical_value: '- Agent + 领域封装API + 实时校验反馈的工作流，可直接迁移到电商定制化商品（如定制家具、3D打印周边）的生成场景，大幅降低方案不可行率

  - 通用LLM搭配领域工具链的效果优于垂直专用小模型，业务中可优先基于通用LLM做工具封装，减少垂直模型训练和迭代成本

  - 推理阶段的计划-执行-校验迭代loop设计，可复用在推荐/广告场景的合规校验环节（如广告素材生成的多维度合规校验、定制化推荐方案的可行性校验）'
score: 4
source: huggingface-daily
depth: abstract
---

**动机**：现有代码生成Agent做3D实物建模时，常输出带漂浮、碰撞、部件不连通问题的无效装配方案，无法落地到实体搭建场景。
**方法关键点**：1. 提出BrickWright框架，引导预训练Agent调用专属Python工具包BrickLayer生成乐高搭建代码；2. BrickLayer封装易用的积木装配API，以及物理可行性校验器（检查零件真实性、碰撞、漂浮、连通性）；3. 采用计划-编码-校验-迭代的工作流，基于校验反馈自动修正生成结果。
**关键结果**：在512个测试prompt上，基线Agent物理合格率仅9%（GPT-6 Luna）~69%（GPT-6 Astra），BrickWright引导的Agent实现100%合格率，同时提升轻量Agent的prompt贴合度，在文本转积木任务上优于专用模型，且BrickLayer API相比原生LDraw降低50%推理成本。
