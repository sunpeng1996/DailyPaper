---
title: 'Learn2Play Bench: How Well Do LLM Agents Learn from Experience in Unfamiliar
  Environments?'
title_zh: Learn2Play Bench：陌生环境下LLM Agent经验学习能力测评基准
authors:
- Yibo Li
- Jinhang Qiu
- Zhi Zheng
- Qianyun Guo
- Jiaying Wu
- Shuo Ji
- Bryan Hooi
affiliations:
- National University of Singapore
arxiv_id: '2610.08215'
url: https://arxiv.org/abs/2610.08215
pdf_url: https://arxiv.org/pdf/2610.08215
published: '2026-10-07'
collected: '2026-10-09'
category: Agent
direction: LLM Agent 经验学习能力测评
tags:
- LLM Agent
- Benchmark
- Experience Learning
- Self-Evolving
- Human-Agent Comparison
one_liner: 提出含20个反直觉规则文本游戏的测评基准，系统对比影响LLM Agent经验学习的多维度因素
practical_value: '- 自进化Agent记忆模块设计可优先保留原始交互历史而非仅存储提炼后的规则/策略，避免过早形成的错误结论限制后续探索，适合电商推荐场景的用户反馈迭代链路

  - Agent落地优先选择与backbone适配的原生harness（如Claude配Claude Code、GPT配Codex），可同时提升7%+性能并降低30%+推理成本

  - 跨场景迁移的Agent需设计核心规则与表面特征解耦的学习机制，避免仅记忆场景特化操作，适配电商多站点、多品类的陌生业务环境

  - 推荐系统冷启动探索可参考人类行为模式，增加策略多样性触发机制，避免过早收敛到次优解，提升最优策略的发现概率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent经验学习测评多采用预训练知识已覆盖的熟悉任务，无法区分性能提升来自复用预训练知识还是真的通过交互学习了新规则，缺乏可控的陌生环境学习能力测评基准，无法系统对比不同模型、记忆方法、harness对学习效果的影响。

### 方法关键点
- 设计20个全新文本游戏，规则均为反直觉/未公开内容，Agent无前置知识可复用，必须通过交互发现隐藏规则，支持自动评分与结果复现
- 分为固定实例、重排实例两类游戏，后者仅改变表层元素、核心规则不变，用于测试知识跨场景迁移能力
- 设计Max、Mean、Learning Gain、Learning Slope四类指标，分别测评峰值性能、平均性能、总提升幅度、学习速率

### 关键实验
对比11款主流LLM backbone、6种自进化记忆方法、3种Agent harness，同时与21-30名人类玩家的表现对标。核心结果：1）原始交互历史记忆（MEMORY）比规则提炼类方法（如Reflexion、AWM）平均Max高4-7分，学习斜率高0.6-2.4；2）Top1人类玩家峰值得分84.3，高于最优Agent的81.8，策略相似度比Agent低12pct，失败后创新高概率高11pct；3）同backbone下适配的harness可提升Max7-17分，同时降低推理成本30%+；4）重排场景下弱模型学习斜率下降最高达2.67，强模型仅下降0.59。

**最值得记住的一句话**：LLM Agent自进化的效果上限不仅取决于模型本身，记忆存储方式、harness适配度、探索策略的影响远大于预期，原始证据留存比过早的知识提炼更利于未知环境下的持续学习。
