---
title: 'Veritas: A Verifier Generation Harness for Agent Tasks'
title_zh: Veritas：面向Agent任务的自动验证器生成框架
authors:
- Daoan Zhang
- Qinbo Bai
- Dehai Min
- Xingyu Mu
- Ziyi Chen
- Jianing Yin
affiliations:
- ByteDance Inc. USA
- University of Illinois Chicago
- New York University
arxiv_id: '2611.13336'
url: https://arxiv.org/abs/2611.13336
pdf_url: https://arxiv.org/pdf/2611.13336
published: '2026-11-09'
collected: '2026-11-11'
category: Agent
direction: Agent工具框架 · 自动验证器生成
tags:
- Agent
- Verifier Generation
- LLM Agent
- Agent Evaluation
- Self-Improvement
one_liner: 通过三个专属机制自动生成Agent任务验证器，效果优于7种主流通用harness
practical_value: '- 电商售后、客服类Agent的任务验证规则可复用Veritas三机制：用Evidence Header明确验证器可读取的订单/对话/状态输入范围，用领域规则库补全业务未明文写的合规要求，用编写原则避免验证规则过严/过松，大幅降低人工编写验证规则的成本

  - Agent效果评估时可复用κ*指标设计逻辑：未返回结果的缺失判定为错误，避免仅统计成功返回样本导致的效果虚高，更贴近业务真实表现

  - 现有业务Agent harness可直接叠加三个机制作为插件，实验显示其对弱harness提升效果最明显，无需重构全量替换现有架构，落地成本低'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
自改进AI系统的迭代效果高度依赖验证器的判决准确性，现有验证器多为人工编写，成本高昂且无法适配海量零散业务场景，同时人工编写的规则易存在缺陷，导致Agent出现奖励黑客问题，是自改进系统落地的核心瓶颈。

### 方法关键点
- 三大核心机制：① Evidence Header 明确验证器可观测的输入范围，规定环境最终状态优先级高于执行轨迹，避免检查不可见信息或忽略可用证据；② Domain Rule Library 挂载6个领域共19603条隐含规则，补全任务文本未提及的领域政策/业务规范要求；③ Authoring Principles 共9条编写规则，替代测试校验逻辑，避免验证器过严/过松或交付失败。
- 生成后自带探针校验+一轮修复机制，验证器崩溃或接受已知错误结果时触发重生成，提升交付率。
- 支持自改进循环，在验证集上迭代优化规则，避免过拟合单个任务。

### 关键结果
固定GLM-5.2模型时，Veritas在4个执行类基准上与官方判决的一致性κ*全面优于7种基线harness，相对最优基线最高提升0.078（Terminal-Bench）、0.074（TB-Science）；三个机制可直接迁移到其他harness，能将Claude Code在Terminal-Bench上的κ*从0.238提升至0.586。

### 核心结论
Agent系统中，harness对验证器质量的影响不逊于大模型本身，生成的验证器错误多为错拒正确解而非漏判错误解。
