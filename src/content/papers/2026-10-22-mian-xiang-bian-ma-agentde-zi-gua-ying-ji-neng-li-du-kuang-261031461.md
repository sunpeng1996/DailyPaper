---
title: 'Adaptive Skill Granularity for Coding Agents: Runtime Routing and Macro-to-Micro
  Recovery'
title_zh: 面向编码Agent的自适应技能粒度框架：运行时路由与宏到微恢复
authors:
- Dingxuan Zhang
- Yanhui Jiang
- Jun Wang
- Hefeng Zhou
affiliations:
- Shanghai Jiao Tong University
- Kuaishou Technology Co., Ltd.
- University of Warwick
arxiv_id: '2610.31461'
url: https://arxiv.org/abs/2610.31461
pdf_url: https://arxiv.org/pdf/2610.31461
published: '2026-10-22'
collected: '2026-10-23'
category: Agent
direction: Agent 技能粒度动态调控
tags:
- LLM Agent
- Skill Routing
- Dynamic Granularity
- Failure Recovery
- Coding Agent
one_liner: 提出自适应技能粒度Agent框架，通过运行时路由与宏到微恢复平衡执行鲁棒性与成本
practical_value: '- 业务Agent技能库可新增运行时粒度控制逻辑：标准化任务走宏技能提效率，复杂/故障场景降级到微操作保成功率，例如电商客服Agent的标准化问题走预设流程，异常情况降级到基础工具调用。

  - 技能路由可采用轻量决策树替代大模型判断：仅依赖预定义的任务结构特征（如请求复杂度、历史成功率特征），无额外推理成本且可解释、可审计。

  - 技能库准入可复用宏技能契约范式：要求每个宏技能明确定义适用条件、副作用、校验逻辑、失败分类和降级路径，避免易碎技能拖垮全链路成功率，例如广告投放Agent的批量操作技能必须提前定义失败回滚路径。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent的技能系统大多仅解决预执行的技能检索问题，执行时要么固定用细粒度微操作（鲁棒但成本高），要么固定用粗粒度宏技能（高效但易碎、失败后无有效恢复机制），无动态调整执行粒度的能力，导致鲁棒性和效率无法兼顾，尤其在编码这类高确定性校验的场景下问题尤为突出。

### 方法关键点
- 定义三类执行粒度：微模式（仅用基础工具）、宏模式（仅用组合宏技能）、混合模式（宏执行失败后可降级到微操作），粒度决策独立于技能检索流程。
- 框架分两大模块：1）轻量粒度控制器：基于预执行的任务结构特征（文件数、AST复杂度、任务类型等），用深度不超过4的决策树选择初始执行模式，可解释、无额外推理成本；2）有限状态机（FSM）恢复执行器：宏执行失败时根据故障类型、预定义的恢复开关决定是否降级到微操作，所有状态转换可审计。
- 宏技能必须遵循标准化契约：明确定义适用前置条件、允许的副作用、内部校验逻辑、失败分类和降级路径，保障恢复流程可落地。

### 关键结果
在自研GranBench-Code基准（含简单、中等、重构、故障恢复4类共80个任务）上对比多组基线：
- 固定微模式成功率100%，但token成本是固定宏模式的2倍；固定宏模式成功率仅58.3%，成本仅为微模式的50%。
- 完整自适应框架（学习路由+选择性恢复）在故障注入场景下保持100%成功率，相比无条件降级方案token成本降低44%~51%，相比固定粒度方案在成功率相当的情况下成本降低23%。

### 核心结论
Agent的技能库不应该只是可检索的资源集合，更应该是可控制、可校验、可恢复的执行抽象层。
