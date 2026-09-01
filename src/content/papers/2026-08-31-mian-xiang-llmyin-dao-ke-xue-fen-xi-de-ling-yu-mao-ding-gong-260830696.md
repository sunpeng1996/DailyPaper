---
title: Domain-Grounded Tool Orchestration for LLM-Guided Scientific Analysis
title_zh: 《面向LLM引导科学分析的领域锚定工具编排架构》
authors:
- Jeff Lee
- Sebastien Jourdain
- Cory Quammen
- Patrick O'Leary
- Berk Geveci
affiliations:
- Kitware, Inc.
arxiv_id: '2608.30696'
url: https://arxiv.org/abs/2608.30696
pdf_url: https://arxiv.org/pdf/2608.30696
published: '2026-08-31'
collected: '2026-09-01'
category: Agent
direction: Agent 工具编排 · 领域知识约束
tags:
- Tool Orchestration
- Domain Ontology
- MCP
- LLM Agent
- Plan-Execute-Interpret
one_liner: 提出意图解析-执行-解释三层架构，用领域本体约束LLM规划，消除科学分析脚本生成类错误
practical_value: '- 业务Agent架构可直接复用：拆分LLM意图理解/确定性工具执行/结果解释三层，LLM仅处理自然语言交互，工具层封装固定的查品/退单/调价等业务逻辑，彻底避免LLM代码幻觉，大幅提升Agent可靠性

  - 领域约束落地轻量方案：不需要构建全量领域知识库，仅编写精简JSON格式的领域规则（如电商合规要求、推荐流量分配优先级）约束LLM规划路径，即可大幅降低策略类错误

  - RAG检索优化技巧：仅给LLM输入当前任务相关的单条领域知识，而非全量知识库检索结果，可大幅提升结果解释准确率，该结论可直接复用在所有RAG落地场景

  - 跨场景复用工程范式：核心架构、协议、部署层完全通用，新增业务场景仅需编写对应领域规则和工具包装，比如从大促运营Agent扩展到客服Agent无需重构核心逻辑'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有LLM辅助科学分析方案多采用直接生成API调用脚本的模式，存在API幻觉、分析流程缺失、策略错误等结构性问题，生成的代码可正常运行但输出错误结果，且无法基于执行结果闭环迭代，要求用户同时具备领域专业知识和编程能力，落地门槛极高。

### 方法关键点
- 三层解耦架构：拆分Plan（LLM解析用户意图生成分析计划）、Execute（确定性领域工具执行分析）、Interpret（LLM基于结构化结果输出解释）三个模块，LLM完全不接触执行代码，从架构上消除代码生成类错误
- 领域本体约束：领域专家编写精简JSON格式本体，定义现象、观测指标、对应工具、后续分析步骤、业务意义，LLM仅能从本体声明的合法分析链中选择，从根源减少策略类错误
- 工具层设计规范：所有工具返回结构化定量数据而非图片/确认信息，支持语义字段到实际存储名的动态映射，自动管理分析流水线依赖避免冲突

### 关键结果
在计算流体动力学（CFD）和拓扑数据分析两个领域验证架构，新增第二个领域仅需编写本体和约400行工具包装代码，无需修改核心架构；消融实验显示，领域本体不影响工具选择准确率，但将结果解释准确率从0.41提升至0.91，仅当精准返回单条相关领域知识时增益最大，全量本体返回仅能将准确率提升到0.56。

> 最值得记住的一句话：LLM擅长处理意图理解和自然语言解释，确定性领域执行逻辑应封装为固定工具，不要让LLM生成执行代码。
