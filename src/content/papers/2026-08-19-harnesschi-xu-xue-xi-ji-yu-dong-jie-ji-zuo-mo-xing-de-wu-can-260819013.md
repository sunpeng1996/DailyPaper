---
title: 'Harness Continual Learning: Continual Adaptation Beyond Model Parameters'
title_zh: Harness持续学习：基于冻结基座模型的无参数更新持续适配框架
authors:
- Borui Kang
- Jinrui Gu
- Junhan Lv
- Wenbin Li
- Lei Wang
- Yang Gao
affiliations:
- State Key Laboratory for Novel Software Technology, Nanjing University
- University of Wollongong
arxiv_id: '2608.19013'
url: https://arxiv.org/abs/2608.19013
pdf_url: https://arxiv.org/pdf/2608.19013
published: '2026-08-19'
collected: '2026-08-20'
category: Agent
direction: Agent持续学习 · 非参数化harness演化
tags:
- Continual Learning
- Agent Harness
- LLM Agent
- Frozen LLM
- Stability-Plasticity
one_liner: 提出围绕冻结基座的Harness持续学习范式，通过带校验的演化机制缓解harness层面遗忘，多场景性能超基线10%
practical_value: '- 电商智能客服、商品选品、广告投放类Agent可直接复用该框架，无需微调基座，仅迭代prompt、记忆、路由规则即可完成多场景持续适配，大幅降低迭代成本

  - 三层校验（当前效果提升、历史效果保留、合法性检查）机制可直接复用到现有Agent迭代流程，解决频繁修改prompt/记忆库后旧场景效果退化的常见问题

  - 历史锚点集设计可直接落地：在电商多场景（售前/售后/大促）Agent迭代时，每个场景保留少量核心校验用例作为锚点，更新后先跑通锚点集再上线，有效避免线上故障

  - 可通过调整历史遗忘容忍阈值Bn灵活适配业务需求：大促等稳定性优先场景设Bn=0，新场景探索阶段可放宽阈值，平衡迭代效率和线上稳定性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有持续学习研究均以模型为核心，依赖参数更新实现能力迭代，但当前工业界Agent大多基于冻结基座开发，通过修改prompt、记忆库、路由规则、工具调用配置等harness组件完成场景适配，这类更新常出现harness层面遗忘：新场景的配置修改会导致已跑通的旧场景能力退化，尚无统一框架解决该问题。

### 方法关键点
- 定义Harness Continual Learning（HCL）范式，学习对象为冻结基座外的4个协同harness组件：Task Interface（输入解析规则、prompt模板）、Experience Memory（原始交互记录+抽象可复用经验）、Capability Map（外部工具接口+内部沉淀技能）、Adaptive Router（路由策略、工作流模板），所有组件统一版本管理。
- 设计带防护的harness演化机制：首先由Continual Optimizer根据执行反馈生成候选harness；再由Continual Evaluator做三层强制校验：当前任务效果提升≥预设阈值、历史锚点集遗忘数≤容忍阈值、配置合法，全部通过才会上线替换现有harness。
- 可通过调整历史遗忘容忍阈值Bn显式控制稳定性-可塑性平衡：Bn=0为强稳定模式，完全不允许旧场景锚点失效；Bn=∞为强探索模式，优先适配新场景需求。

### 关键实验结果
在ALFWorld、Minecraft开放交互场景，文本推理、多模态感知任务流上测试，基座全程冻结，仅更新harness组件。对比静态harness、RAG、MemP等基线，Plasticity-HCL在ALFWorld上平均准确率达62.98%，较基线最高提升15pct；Stability-HCL在多模态任务流上平均准确率达68.92%，超基线26pct，平均遗忘仅0.22；全场景相对基线提升普遍超过10%。

> 最值得记住的一句话：Agent的持续迭代完全可以在不微调基座的情况下实现，通过对harness组件的统一管理和带校验的更新机制，既能持续沉淀能力，又能有效控制旧场景退化风险。
