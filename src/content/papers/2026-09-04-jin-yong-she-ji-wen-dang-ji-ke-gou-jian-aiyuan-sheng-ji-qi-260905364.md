---
title: 'Design Docs Are All You Need: An AI-native Machine-Learning Performance Tool'
title_zh: 仅用设计文档即可构建：AI原生机器学习性能建模工具
authors:
- Samuel Kushnir
- Kimia Noorbakhsh
- Kavya Sreedhar
- Liqun Cheng
- Ming Liu
- Parthasarathy Ranganathan
- Mohammad Alizadeh
- Fred Kjolstad
- Suvinay Subramanian
affiliations:
- Google DeepMind
- MIT
- Stanford
- Google
arxiv_id: '2609.05364'
url: https://arxiv.org/abs/2609.05364
pdf_url: https://arxiv.org/pdf/2609.05364
published: '2026-09-04'
collected: '2026-09-07'
category: Agent
direction: Agent 代码生成工作流工程化实践
tags:
- Code Generation
- Agent Orchestration
- ML Performance Modeling
- Technical Debt
- Design Doc
one_liner: 提出以自然语言设计文档为唯一可信源，通过多Agent编排自动生成零技术债务的ML性能建模库SMART
practical_value: '- 推荐/广告系统的快速迭代模块（如特征工程、模型服务性能调优工具）可复用「设计文档为唯一可信源、代码为可重生成产物」的模式，每次版本更新全量重生成代码，彻底消除历史补丁积累的技术债务

  - 解决大代码库Agent生成的上下文窗口不足问题：将需求按依赖拆分为独立设计文档DAG，每个子Agent仅处理单一文档，生成准确率显著高于全量代码上下文输入的模式

  - 设计文档强制加入step-by-step执行示例、预期输出校验锚点，可大幅降低LLM生成代码的语义歧义，效果远优于仅靠prompt规则约束的方案

  - 可复用动态模型路由策略：核心复杂模块用大模型生成，边缘简单模块用小模型生成，实测可降低80%左右的LLM调用成本，同时不影响核心模块质量'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
ML性能建模工具位于上层模型架构和底层硬件的中间层，两边迭代速度极快，传统增量修改的代码维护模式会持续积累技术债务；同时AI coding Agent受上下文窗口限制，在现有代码基础上做局部修改容易破坏全局架构一致性，长期迭代后代码质量持续下降，维护成本甚至高于完全重写。
### 方法关键点
- 以自然语言设计文档为唯一可信源，主分支几乎无代码，文档按依赖构成DAG，由Agent自动识别依赖边，按拓扑顺序分配独立子Agent逐个生成对应模块代码，每次版本更新全量重生成，从根源消除技术债务
- 设计文档采用「规则+worked example」范式：每个文档包含step-by-step的执行示例、中间态输出、预期成本表达式，作为Agent生成代码的in-context示范，同时自动生成对应单元测试校验输出一致性
- 定义极简递归符号IR，支持两种性能计算模式：fast模式用分析方法快速批量计算上万个设计点的性能，slow模式用模调度做精细化调度分析，所有成本表达式用SymPy做符号传播，一次生成支持全参数空间扫描
- 动态模型路由：核心复杂模块分配能力更强的大模型生成，边缘简单模块用低成本小模型生成，平衡生成质量和调用成本
### 关键结果
- 完整生成包含50个设计文档、9000行规范的性能建模库仅需1.5-3小时，API成本约100美元，仅占常规周LLM使用预算的20%
- 生成的性能模型和手工审计的参考模型（包括TPU Pod上部署的DeepSeek-V3服务）精度一致到舍入误差
### 核心结论
当业务规范迭代速度快于软件可吸收的速度时，把设计文档而非代码作为持久化资产，可彻底消除增量修改带来的技术债务。
