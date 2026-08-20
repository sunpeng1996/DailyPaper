---
title: 'LEDGER: Claim-to-Evidence Trace Graphs for Auditing LLM Agents'
title_zh: LEDGER：用于LLM Agent审计的主张-证据追溯图系统
authors:
- Daehong Kim
- Haichao Miao
- Shusen Liu
affiliations:
- Carnegie Mellon University
- Lawrence Livermore National Laboratory
arxiv_id: '2608.18398'
url: https://arxiv.org/abs/2608.18398
pdf_url: https://arxiv.org/pdf/2608.18398
published: '2026-08-19'
collected: '2026-08-20'
category: Agent
direction: LLM Agent 可观测性与审计系统
tags:
- LLM Agent
- Observability
- Audit
- Trace Graph
- Provenance
one_liner: 构建分层主张-证据追溯图，支持LLM Agent执行过程的可审计追溯与人工核验
practical_value: '- 电商导购/运营分析类Agent可复用该分层追溯架构，将推荐结论、分析结果关联到用户行为、商品数据、工具调用记录、校验步骤，大幅降低人工审核成本

  - 推荐系统全链路血缘建设可复用LEDGER定义的语义边类型（uses/produces/checked_by/supports），实现特征、模型、排序结果的可追溯，方便问题排查与合规审计

  - Agent日志存储无需仅保留平层流水，可参考三层结构（Trace Record/Evidence Node/Workflow Node）做层级聚合，既保留原始证据，又支持快速定位异常环节'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
LLM Agent已可执行长周期复杂任务（工具调用、代码执行、文件编辑、分析报告生成等），但现有可观测系统仅提供平层执行日志，用户核验输出正确性需要手动重建任务结构与证据关联，审计成本随任务复杂度线性上升，亟需面向证据追溯的审计架构。

### 方法关键点
- 采用sidecar架构无侵入接入Agent会话，捕获全量执行事件（工具调用、返回结果、文件操作、生命周期事件等）生成不可篡改的Trace Record作为底层证据
- 构建三层追溯图结构：底层Trace Record保留原始日志，中层Evidence Node将关联记录聚合为可核验工作单元（分为动作、artifact两类），上层Workflow Node将相关证据聚合为6类任务阶段（context/plan/inspect/execute/validate/claim）
- 定义6类带语义的有向边（frames/uses/produces/informs/checked_by/supports）连接各层节点，支持从最终主张反向追溯到支撑的动作、artifact、校验步骤
- 配套可视化仪表盘，支持层级下钻、原始证据查看、追溯图生成过程审计

### 关键实验
未设置定量对比基线，通过两个实际任务案例验证：空气质量数据集分析任务中可完整还原从原始数据→清洗→分析→结论的全链路artifact血缘，自动暴露错误修复流程；NetworkX代码库新增功能任务中可清晰区分功能实现、边界case修复、校验等不同阶段，支持定位每一处代码修改的依据和验证记录。

最值得记住的一句话：Agent的可观测性不等于可审计性，平层日志只能记录「发生了什么」，而面向证据的追溯图才能回答「为什么这个结论是可信的」
