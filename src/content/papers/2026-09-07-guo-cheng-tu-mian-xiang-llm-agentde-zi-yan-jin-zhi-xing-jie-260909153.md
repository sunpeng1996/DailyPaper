---
title: 'Procedural Graphs: Self-Evolving Execution Structures for LLM Agents'
title_zh: 过程图：面向LLM Agent的自演进执行结构
authors:
- Yuxing Lu
- Yicheng Chen
- Shanchan Wu
- Sercan Ö. Arık
affiliations:
- Google
- Georgia Institute of Technology
- Peking University
arxiv_id: '2609.09153'
url: https://arxiv.org/abs/2609.09153
pdf_url: https://arxiv.org/pdf/2609.09153
published: '2026-09-07'
collected: '2026-09-09'
category: Agent
direction: LLM Agent 过程知识结构化与自演进
tags:
- LLM Agent
- Procedural Graph
- Self-Evolution
- Execution Guidance
- Trajectory Distillation
one_liner: 提出显式存储过程知识的Procedural Graph，结合在线引导与离线自演进提升LLM Agent执行表现
practical_value: '- 电商导购/客服/运营类Agent可直接复用Procedural Graph结构，将业务流程（如咨询→查库存→推荐→售后）建模为带<condition、guidance、pitfalls>属性的三元组，减少工具乱调用、重复操作等问题

  - 离线自演进逻辑可迁移到业务流程优化：对比用户交互的成功/失败轨迹，自动迭代流程拓扑和引导语，无需人工频繁调整Prompt或工作流，通过验证门控避免负向优化

  - 在线推理时提取当前节点2-hop子图生成引导的设计，可降低Prompt Token消耗、避免全流程信息过载，尤其适合长链路的电商售后、商家代运营等Agent场景

  - 若现有专家预设的业务工作流效果差，可复用文中的修复逻辑，从失败轨迹中自动迭代修正，无需推翻原有流程，大幅降低优化成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent大多基于累积历史无约束生成下一步动作，过程知识隐式化，长轨迹下极易偏离目标、调用工具顺序错误、重复无效操作；现有结构化工作流要么依赖人工设计，要么仅存储为无关联的规则文本，无法结合执行进度动态引导，也难以基于反馈自动迭代。

### 方法关键点
- 参考知识图谱三元组结构设计Procedural Graph（PG）：节点对应工具调用、推理步骤、任务状态，边为带`condition`（触发条件）、`guidance`（执行建议）、`pitfalls`（避坑提示）属性的合法转移关系，显式存储过程知识
- 在线推理：匹配当前动作定位PG中的活跃节点，提取2-hop邻域子图，由引导LLM生成当前步情境引导，软约束Solver的下一步动作，不限制推理灵活性
- 离线自演进：对比成功/失败轨迹，由LLM refiner生成图编辑方案（增删节点/边、修改属性），仅当新版本在验证集表现不下降时才提交，同时保留被拒编辑的负例记忆避免重复踩坑

### 关键实验
在7个基准（多跳问答、多轮对话、具身任务、长周期企业决策等）、4个主流LLM（Claude Sonnet 4.6、Gemini系列、Grok 4.1 Fast）上测试，对比ReAct、MemoryBank、ExpeL等7个基线：PG在24个模型-基准组合中21个排名第一/并列第一，相比最优基线最高提升9个百分点；长周期金融决策任务上，将Gemini 3.1 Pro的全周期存活率从6%提升到34%；从零自演进的PG表现超过人工设计的工作流，还可修复拉低效果的缺陷专家流程，最高提升33.93个百分点。

### 核心结论
把过程知识从LLM权重和零散Prompt中抽离，用可编辑的结构化图存储，结合动态引导和反馈迭代，是大幅降低Agent长链路执行错误、减少人工优化成本的有效路径。
