---
title: 'GatewayBench: Unified Capability and Security Evaluation Platform for MCP
  Gateways'
title_zh: GatewayBench：面向MCP网关的统一能力与安全评测平台
authors:
- Yitian Zheng
- Zhaorun Chen
- Haoyu Li
- Bo Li
affiliations:
- Tsinghua University
- University of Chicago
- University of Illinois Urbana-Champaign
arxiv_id: '2610.23449'
url: https://arxiv.org/abs/2610.23449
pdf_url: https://arxiv.org/pdf/2610.23449
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent系统MCP网关评测与架构选型
tags:
- MCP
- Agent
- Evaluation
- Tool Calling
- Security
- Gateway
one_liner: 首个面向MCP网关的统一评测基准，覆盖能力、效率、安全维度，对比两类主流网关架构优劣
practical_value: '- 内部Agent工具规模<500的场景优先选flattened网关，实现简单、交互延迟低，弱模型下任务成功率比hierarchical高25%以上

  - 工具规模>1000的大规模Agent部署选hierarchical网关，token消耗不随工具数增长，对抗工具注入攻击的能力提升30%+

  - MCP网关、Agent harness、底层LLM要联合选型，使用GPT-4及以上强模型可完全抹平hierarchical网关的任务成功率差距，同时保留其安全与成本优势

  - 做企业级Agent安全管控，优先选hierarchical架构的网关，可大幅降低恶意工具注入的攻击面，且不需要额外改造Agent逻辑'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
MCP已成为LLM Agent对接异构工具的标准协议，MCP网关作为Agent与工具间的核心中间件，直接决定Agent的任务表现、资源开销与安全性，但此前没有系统性框架验证不同网关架构的实际效果，选型缺乏量化依据。
### 方法关键点
- 对主流MCP网关做分类：① flattened 网关：全量暴露所有工具列表给Agent；② hierarchical 网关：仅暴露工具发现元工具，Agent按需检索相关工具
- 评测集覆盖6个领域共524个任务，包含11118个真实工具、251个MCP服务器，支持动态注入无关噪声工具模拟不同规模的工具池
- 评测维度覆盖任务成功率、攻击成功率、端到端延迟、token消耗4大类可量化指标
### 关键实验
对比7款业界主流MCP网关、3种Agent配置（GPT-5.1/5.4、OpenAI Agents SDK/OpenClaw harness），核心结果：
1. 无噪声工具场景下，弱模型（GPT-5.1）中flattened网关任务成功率比hierarchical高27.8pct，强模型（GPT-5.4）下差距缩小至2.1pct
2. 注入1500个噪声工具后，flattened网关单轮token消耗达233k，是hierarchical的18.5倍，任务成功率反低2.3pct
3. hierarchical网关的工具注入攻击成功率比flattened低25pct以上，安全优势显著
### 核心结论
MCP网关选型核心取决于工具规模：小工具集选flattened降本提效，大规模工具集选hierarchical兼顾效率与安全，且网关需与底层LLM、Agent harness联合优化
