---
title: 'Euclid-MCP: A Model Context Protocol Server for Deterministic Logical Reasoning
  via Prolog'
title_zh: Euclid-MCP：基于Prolog实现确定性逻辑推理的MCP服务器
authors:
- Bartolomeo Bogliolo
arxiv_id: '2607.21412'
url: https://arxiv.org/abs/2607.21412
pdf_url: https://arxiv.org/pdf/2607.21412
published: '2026-07-23'
collected: '2026-07-24'
category: Agent
direction: Agent 确定性逻辑推理工具
tags:
- MCP
- Neuro-Symbolic
- Prolog
- Logical Reasoning
- Hallucination Mitigation
one_liner: 提供符合MCP标准的确定性逻辑推理工具，解决LLM规则类任务的幻觉与不可审计问题
practical_value: '- 电商合规类Agent可复用这套架构，将平台规则、营销活动规则、商品准入要求编码为Euclid-IR，替代纯RAG方案，避免规则误判，同时生成可审计的推理链路，适配商品审核、商家权限校验等场景

  - 推荐/广告系统的流量策略校验可借鉴该思路，把频控、人群定向、反作弊规则编码为IR，调用reason工具做确定性校验，避免LLM生成的策略违反业务约束，还可通过what_if工具预判策略迭代的影响

  - 可直接集成到现有Agent框架中作为共享规则推理引擎，所有Agent调用同一套规则知识库，避免不同Agent对规则理解不一致，大幅降低规则迭代的维护成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM在多步逻辑推理、规则类任务（如合规校验、权限审核）上存在幻觉、结果不可控、无审计痕迹的缺陷，现有语义RAG方案依赖相似度匹配，无法保证规则执行的逻辑正确性，而现有神经符号结合的推理方案大多是定制化实现，缺乏标准化调用接口，难以在通用Agent体系中复用。
### 方法关键点
- 提出引擎无关的霍恩子句逻辑中间表示Euclid-IR，语法对人类和LLM都友好，支持事实、规则、查询、否定、算术比较等核心逻辑表达，屏蔽底层推理引擎的语法差异
- 基于MCP标准封装4个通用工具：reason（执行推理返回证明树）、diagnose（解释查询成功/失败原因）、what_if（模拟规则/事实变更的影响）、check_kb（校验知识库合法性），支持LLM自助完成translate-run-inspect-repair的纠错闭环
- 后端对接SWI-Prolog做确定性推理，内置安全沙箱限制危险操作，支持本地stdio和HTTP两种调用方式，可直接对接所有MCP兼容的LLM/Agent框架
### 关键实验结果
- 小知识基地（5-50条事实）：8B/480B LLM与Euclid-MCP准确率均为100%，Euclid-MCP耗时2.5s，与大模型推理耗时相当
- 大规模RBAC数据集（1000+事实）：8B LLM准确率仅40%，480B大模型准确率仅40%，Euclid-MCP准确率100%，耗时仅963ms，比大模型快75%+，输出token仅12个，比大模型节省92%以上
### 核心结论
当事实能完全塞进LLM上下文且推理链较浅时，LLM单独使用足够；超过几百条事实的规则类任务，确定性推理是必选项，语义RAG本质上不适合做规则强制校验
