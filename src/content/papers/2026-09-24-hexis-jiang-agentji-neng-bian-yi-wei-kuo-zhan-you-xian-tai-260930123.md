---
title: 'HEXIS: Compiling Skills into Extended Finite State Machines'
title_zh: HEXIS：将Agent技能编译为扩展有限状态机的执行框架
authors:
- Minghao LI
arxiv_id: '2609.30123'
url: https://arxiv.org/abs/2609.30123
pdf_url: https://arxiv.org/pdf/2609.30123
published: '2026-09-24'
collected: '2026-09-25'
category: Agent
direction: Agent执行管控 · 技能编译
tags:
- Agent
- FSM
- Skill Compilation
- LLM Execution
- Control Optimization
one_liner: 将Agent技能自动编译为扩展FSM，分离知识与控制流，大幅提升执行成功率并降低token消耗
practical_value: '- 电商客服、商品审核、售后处理等有固定SOP的Agent场景，可直接复用该架构：将SOP中不变的规则写入FSM各状态的本地prompt，流程跳转编译为显式条件，避免LLM自主推理步骤时遗漏流程，提升合规性

  - 长链路Agent任务（如用户需求挖掘、经营数据分析）可通过该架构降低推理成本：仅当前状态的相关prompt与变量进入上下文，配合Qwen3.8-27B这类基座可降低38.4%~88.9%的token消耗

  - 可兼容现有技能资产：已经通过SkillOpt等方案优化过的业务技能文档，再经过HEXIS编译为FSM，可在原有优化基础上再提升近10%的成功率，无需重构现有技能体系

  - 跨模型迁移成本极低：编译完成的FSM可直接切换不同基座LLM，无需针对目标模型重新训练或调整流程，适配业务不同成本/性能要求的模型选型'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent执行技能时，需每次从全量技能文档+历史上下文推理下一步动作，易遗漏流程、违反SOP要求，长任务上下文膨胀进一步放大执行偏差；而现有技能优化、记忆增强方案仍将流程控制权完全交给LLM推理，未从根源解决控制偏差问题。
### 方法关键点
- 核心设计：分离技能的知识与控制流，知识保留在FSM各状态的本地prompt中供LLM完成单状态内推理，控制流编译为显式状态跳转规则，由runtime基于变量值直接判断跳转，无需LLM推理下一步动作
- 编译流程：首先基于技能文档、工具接口初始化FSM的状态、变量、跳转规则，再通过执行轨迹对齐补充缺失的状态、数据依赖与分支，更新仅在静态检查+全量历史轨迹重放通过后才生效
- 执行逻辑：每个状态仅读取所需变量，执行本地操作（LLM生成/工具调用）后更新变量，按预设优先级匹配跳转条件进入下一状态，直到触发终止条件
### 关键实验
在4个基准数据集（SpreadsheetBench、LiveMath、DABench、LongSeal）、4款不同基座LLM上测试，对比Skill+ReAct、AWM、SkillOpt等5种基线：
- 平均成功率较Skill+ReAct提升16.1个百分点，16个测试场景中15个优于原生执行
- Qwen3.8-27B执行token量降低38.4%~88.9%
- 与SkillOpt结合后在SpreadsheetBench上成功率达84.2%，较原生Skill+ReAct提升38.6个百分点
### 核心结论
把技能中可固化的流程逻辑交给显式状态机管控，LLM仅负责单状态内的推理生成，是平衡Agent执行可控性、通用性、推理成本的高性价比路径
