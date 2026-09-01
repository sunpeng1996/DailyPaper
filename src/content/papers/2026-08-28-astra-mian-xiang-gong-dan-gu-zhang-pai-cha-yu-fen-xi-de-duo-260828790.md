---
title: ASTRA - Agentic System for Ticket Resolution and Analysis
title_zh: ASTRA：面向工单故障排查与分析的多智能体系统
authors:
- Shashidhar Reddy Javaji
- Mohamed Trabelsi
- Jin Cao
- Huseyin Uzunalioglu
affiliations:
- Stevens Institute of Technology
- Nokia Bell Labs
arxiv_id: '2608.28790'
url: https://arxiv.org/abs/2608.28790
pdf_url: https://arxiv.org/pdf/2608.28790
published: '2026-08-28'
collected: '2026-09-01'
category: Agent
direction: 多智能体协作 · 工单故障自动化排查
tags:
- Multi-Agent
- LLM-as-Judge
- Claim-Evidence Grounding
- Incident Automation
- RAG
one_liner: 协调三类专业信息采集智能体与裁判编排迭代闭环，生成证据可溯源的故障排查报告
practical_value: '- 多智能体任务拆分可直接复用：处理电商客诉、广告异常排查、商家工单这类多源信息合成任务时，拆分历史召回、日志/反馈分析、知识库检索三类专用智能体，比单智能体端到端生成可控性更高、幻觉更少

  - claim-evidence中间表示适配生成类业务：推荐理由生成、广告文案合规校验等场景可增加显式主张-证据绑定环节，所有生成内容关联原始溯源片段，既支持自动化校验，又能将虚构内容占比压制到极低水平（本方案低于3%）

  - 裁判-编排迭代闭环落地性强：将评估指标拆解为可落地的细分维度，低分项直接映射到对应智能体的定向查询，设置迭代轮次上限、避免重复查询，在保证效果的同时控制算力成本

  - 长文本预处理trick可迁移：处理用户评论串、系统日志等长文本时，先做确定性规则过滤（关键词、严重等级、关联任务特征词），再做模板聚类去重，最后输入LLM做结构化分析，比全量输入或直接截断性价比高得多'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
企业运维团队处理故障工单需要跨历史工单、系统日志、技术文档三类异构证据做合成推理，现有自动化方案多为单步端到端生成，缺乏显式证据建模与溯源能力，信号稀疏分散的场景输出难验证，电信等高可用领域对报告可审计性要求极高，现有方案无法满足需求。

### 方法关键点
- 多智能体分工：三类专用信息采集智能体按序执行：`TicketSimilarityAgent`采用「稠密检索+LLM两阶段重排」召回相关历史工单；`LogAgent`先通过5层确定性规则过滤百万级日志行，再做上下文扩展，最终输出结构化日志发现；`DomainKnowledgeAgent`基于前两类智能体的输出定向查询知识库，三类输出严格禁止交叉归因
- 显式中间层：所有智能体输出转化为claim-evidence结构化表示，每个主张绑定原始来源片段、标注支持度，从架构层面避免跨源错误归因
- 迭代闭环：`JudgeAgent`按5个维度对草稿报告评分，低于阈值的项由`Orchestrator`生成定向查询指令下发给对应智能体，最多迭代5轮，避免无效循环

### 关键实验
在987条真实电信故障工单上测试，平均综合质量分4.13/5，59.9%的报告能正确定位组件级故障区域，报告相关性4.88/5、清晰度4.94/5，虚构技术细节的错误占比低于3%；硬件故障诊断效果远差于软件/配置故障（Cohen's d=0.80），迭代闭环可提升报告完整性但不会显著提升根因准确率。

### 最值得记住的一句话
多智能体落地的核心不是堆砌角色数量，而是用显式结构化中间层将信息采集和内容生成解耦，从架构层面约束幻觉、保证可审计性。
