---
title: Activation-Guided Graph Retrieval for Cognitive Memory Reconstruction in Language
  Model Systems
title_zh: 面向大模型系统认知记忆重构的激活引导图检索架构
authors:
- Marvin Danig
affiliations:
- Achiral Research
arxiv_id: '2611.13127'
url: https://arxiv.org/abs/2611.13127
pdf_url: https://arxiv.org/pdf/2611.13127
published: '2026-11-09'
collected: '2026-11-11'
category: Agent
direction: Agent 长生命周期记忆检索优化
tags:
- AGGR
- RAG
- Graph Retrieval
- Agent Memory
- Cognitive Architecture
one_liner: 提出激活引导图检索AGGR架构，通过受限图遍历输出带溯源证据图，提升长生命周期Agent记忆可用性
practical_value: '- 构建长生命周期Agent记忆系统时，可复用激活分设计：融合使用频次、时间衰减、显著性、query相似度、权限校验等维度，替代纯语义相似度排序，提升多跳历史证据召回率

  - 图检索遍历阶段增加Fan Attenuation度数衰减逻辑，抑制高热度通用节点（如电商场景的「优惠」「商品」）占用过多检索预算，降低无效遍历开销

  - 可将RAG输出从无结构文本片段升级为带关系、溯源、置信度的证据子图，减少LLM推理时因果/时序推导错误，适配售后溯源、用户消费路径分析等场景

  - 记忆激活的反馈更新仅绑定最终合格业务结果，避免高频检索的热门内容锁死小众有效信息，缓解记忆系统的马太效应问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG系统仅基于query语义相似度召回上下文，无法适配长生命周期Agent的记忆可用性判断需求：记忆的时效性、授权权限、因果路径依赖、是否被后续证据推翻等状态都未纳入召回逻辑，无法处理需要多跳因果、时序溯源的复杂查询，例如决策归因、事件复盘类需求。
### 方法关键点
- 激活引导图检索（AGGR）架构将检索目标从「和query相关的片段」转为「当前推理可访问的经验证据」，最终输出带类型、溯源、置信度、矛盾分支的证据子图而非排序片段列表
- 激活分设计融合query语义相似度、基础激活（使用次数、时间衰减、显著性）、关联cue强度、任务效用、来源权威度、矛盾/过期惩罚项，各维度权重可配置、贡献可审计
- 带度数衰减的受限图遍历：对高度数通用cue做权重衰减，避免其主导遍历路径；递归从新召回的实体生成新cue扩展检索边界，按预算、边际证据增益、矛盾等条件终止遍历
- 授权前置：所有检索、打分仅在用户授权的子图内执行，避免权限泄露；记忆激活更新仅绑定最终合格的业务结果，避免自强化的流行度循环
### 关键实验
本研究为架构预印本，无实测实验数据，给出可复现评测协议：对比基准覆盖lexical检索、常规top-k RAG、无激活的图检索、固定池激活重排、Anthropic定时合并笔记基线（公开效果为较纯检索提升8pct准确率，降低token消耗），评测任务包含决策溯源、时序验证、矛盾检测等，核心指标覆盖答案准确率、因果边F1、过期记忆假阳率、人工审计耗时。
### 核心结论
查询召回回答「什么内容和请求匹配」，激活管控回答「什么经验应该影响当前推理」，二者是长生命周期Agent记忆系统的互补核心组件。
