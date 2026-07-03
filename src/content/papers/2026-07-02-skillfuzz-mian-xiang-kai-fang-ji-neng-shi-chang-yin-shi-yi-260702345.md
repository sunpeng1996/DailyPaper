---
title: 'SkillFuzz: Fuzzing Skill Composition for Implicit Intents Discovery in Open
  Skill Marketplaces'
title_zh: SkillFuzz：面向开放技能市场隐式意图发现的技能组合模糊测试框架
authors:
- Jinwei Hu
- Yi Dong
- Youcheng Sun
- Xiaowei Huang
affiliations:
- University of Liverpool
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2607.02345'
url: https://arxiv.org/abs/2607.02345
pdf_url: https://arxiv.org/pdf/2607.02345
published: '2026-07-02'
collected: '2026-07-03'
category: Agent
direction: Agent技能安全 · 组合风险检测
tags:
- LLM-Agent
- Skill-Marketplace
- Directed-Fuzzing
- Implicit-Intent
- Compositional-Safety
one_liner: 提出无需执行的技能组合模糊测试框架，高效检测开放技能市场多技能协同隐式风险
practical_value: '- 搭建Agent技能生态的团队可复用执行前检测逻辑：基于技能契约+MCTS搜索的范式，无需真实执行技能即可提前预判多技能协同风险，大幅降低准入审核成本

  - 技能结构化抽象思路可迁移：将非结构化技能文档提取为包含前置条件、后置条件、修改范围等字段的结构化契约，可用于技能召回、冲突预判等业务场景

  - 差分测试思路可复用：以无技能基线计划的语义偏差作为风险信号，无需标注样本即可做风险检测，适合冷启动阶段的安全审核场景

  - 电商/广告Agent场景可直接适配：用户自定义插件组合、多营销工具协同等场景，可通过该框架提前检测是否会出现超出用户授权的操作（如越权修改商品价格、泄露用户数据等）'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
开放技能市场允许用户组合社区贡献的技能快速搭建Agent，但平台通常仅做单技能安全审核，多个独立合规的技能协同可能产生既不来自任务要求也不来自单技能的隐式意图（如财务分析+CSV处理技能组合后触发修改原始文件的越权操作）。这类风险检测面临三大难点：执行环境缺失无法全量测试、组合效果存在于LLM内部信念状态无法静态分析、技能组合空间指数级增长无法穷举。

### 方法关键点
- 将隐式意图发现转化为技能组合的模糊测试问题，采用无执行测试范式，以Agent生成的计划相对无技能基线的语义漂移作为差分oracle，无需真实执行技能即可检测风险
- 先从非结构化技能文档中提取结构化技能契约（包含前置条件、后置条件、修改集、不变量、领域范围等字段），基于契约嵌入过滤任务相关候选技能，优先选择冲突概率高的技能组合作为初始种子
- 采用契约引导的Monte Carlo Tree Search（MCTS）在组合空间探索，以同时衡量意图严重度和新颖度的ICQ指标作为奖励，优先探索高风险区域，在固定查询预算下最大化高价值隐式意图的发现量

### 关键实验
在196个技能的SkillsBench数据集、10类典型任务上测试，对比随机搜索、无契约MCTS等baseline：固定查询预算下发现超1000个不同的隐式意图，高风险组合执行验证准确率超80%，高严重度隐式意图发现量比随机搜索高41%，仅需探索随机搜索所需39.7%的两两交互空间。

### 核心结论
多技能协同的隐式风险是Agent技能生态的系统性问题，无需执行、基于计划层语义漂移的检测方案是现阶段性价比最高的规模化审核手段。
