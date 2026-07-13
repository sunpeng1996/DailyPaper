---
title: 'Git-Assistant: Planning-Based Support for Updating Git Repositories'
title_zh: 基于自动规划的Git仓库更新智能助手Git-Assistant
authors:
- Alfredo Garrachón Ruiz
- Tomás de la Rosa
- Daniel Borrajo
affiliations:
- AI Research, JPMorganChase
arxiv_id: '2607.09224'
url: https://arxiv.org/abs/2607.09224
pdf_url: https://arxiv.org/pdf/2607.09224
published: '2026-07-10'
collected: '2026-07-13'
category: Agent
direction: Agent · LLM结合符号规划落地
tags:
- LLM
- Agent
- Automated Planning
- Tool Use
- Reasoning
one_liner: 结合LLM与自动规划构建Git操作助手，解决纯LLM做仓库管理可靠性不足的问题
practical_value: '- 工具类Agent落地可复用「LLM语义理解+符号规划校验执行」的混合架构，从根本上减少纯LLM生成执行序列的幻觉问题

  - 涉及不可逆操作的Agent场景（如电商线上配置变更、推荐规则更新），可先抽象领域操作的状态转移规则，用自动规划做前置校验，大幅降低线上事故风险

  - 工具Agent的效果验证可参考本文构造合成随机测试环境的方法，低成本覆盖多边界case，不用完全依赖真实场景标注'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
Git作为应用最广的版本控制工具操作门槛高，开发者在分支合并、冲突解决等复杂操作中易出错；纯LLM搭建的Git助手缺乏形式化推理能力，生成的操作序列错误率高，无法保障仓库操作的安全性。
### 方法关键点
1. 采用混合架构：LLM负责解析用户自然语言意图、感知仓库上下文状态，自动规划模块基于Git操作的状态转移规则生成可执行命令序列，全程做正确性、安全性校验。
2. 设计系统化评估方案：构造合成、随机化的Git测试环境，对比纯LLM基线与规划增强的变体在多维度指标的表现。
### 关键结果
实验证明融合形式化规划的方案相比纯LLM方案可靠性大幅提升，仓库管理操作错误率显著降低，验证了符号推理+LLM的混合架构在工具类Agent场景的落地价值。
