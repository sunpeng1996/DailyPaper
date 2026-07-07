---
title: 'OptiAgent: End-to-End Optimization Modeling via Multi-Agent Iterative Refinement'
title_zh: OptiAgent：基于多智能体迭代优化的端到端运筹建模框架
authors:
- Adriana Laurindo Monteiro
- Nayse Fagundes
- Gabriel Mattos Langeloh
- Gustavo de Oliveira Kanno
- Priscila Louise Aguirre
- Thiago Costa Rizuti da Rocha
- Victor Leme Beltran
affiliations:
- Instituto de Ciência e Tecnologia do Itaú, Brasil
arxiv_id: '2607.05346'
url: https://arxiv.org/abs/2607.05346
pdf_url: https://arxiv.org/pdf/2607.05346
published: '2026-07-06'
collected: '2026-07-07'
category: Agent
direction: 多Agent 自动化运筹问题建模
tags:
- Multi-Agent
- Optimization
- Iterative Refinement
- LLM4OR
- Feedback Loop
one_liner: 提出带多轮反馈校验的六角色多智能体框架，自动将自然语言运筹问题转为可运行求解代码
practical_value: '- 多Agent分工+定向反馈环的架构可直接复用在广告/推荐的约束优化场景，比如预算分配、库存调度等，将复杂任务拆解为解释、建模、校验、代码生成等专用角色，减少单步LLM生成的
  hallucination

  - 五元素（Sets/Parameters/Variables/Objective/Constraints）结构化建模范式可迁移到所有需要形式化约束的业务问题，统一中间输出格式，提升后续校验、迭代的可解释性与可debug性

  - 不同类型错误定向回传对应上游Agent的设计，可大幅降低Agent协作的迭代成本，避免全流程重跑，适合对实时性有一定要求的业务优化场景，可直接复用在基于LangGraph的Agent工作流中'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM自动处理自然语言描述的运筹优化问题时，普遍存在数学建模错误、代码可运行性低、流程黑盒不可审计等问题，传统单步生成或普通多Agent方案无法覆盖结构缺陷、数学矛盾、代码错误等多类故障，且建模过程不透明，难以满足工业场景对结果可信度的要求，极大限制了LLM在运筹优化类业务中的落地。

### 方法关键点
- 架构为6个专用Agent串行流水线：依次为解释Agent（将自然语言转结构化问题描述）、建模Agent（输出五元素标准化数学公式）、分析Agent（判定问题类型如LP/MILP）、校验Agent（从结构、代数、语义三层做质量管控）、代码生成Agent（输出对应求解库的可执行代码）、求解Agent（沙箱运行代码输出结果）
- 设计4类定向反馈环：校验不通过回传建模/解释Agent、代码运行错误回传代码生成Agent，每类循环最多迭代3次，避免无限循环
- 全程共享AgentState记录所有中间产出与反馈信息，全流程可审计，用户可查看每一步修正的原因与内容

### 关键实验
在4个公开运筹数据集（NLP4LP、IndustryOR、LogiOR、ComplexOR，共455个覆盖LP/ILP/MILP/NLP的问题）上，和GPT-5.4、Claude Sonnet 4.5、ORThought、LLMOPT等10余个基线对比，基于GPT-5.4的OptiAgent在3个数据集上取得SOTA：IndustryOR准确率84.34%、LogiOR准确率70.65%、ComplexOR准确率100%，在最具挑战性的分布外数据集LogiOR上比次优基线高16个百分点以上，平均循环率27.8%~61.4%，平均单问题处理耗时43.85s~122.6s。

### 核心结论
多Agent架构的性能增益核心来自任务分解与定向反馈迭代，而非单纯的prompt工程，透明可追溯的中间校验环节是提升复杂推理类任务可信度的关键。
