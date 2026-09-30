---
title: Self-Play Search Distillation for Large Language Model Reasoning
title_zh: 面向大语言模型推理的自博弈搜索蒸馏（SPSD）框架
authors:
- Lorenzo Molfetta
- Wai-Chung Kwan
- Giacomo Frisoni
- Luca Ragazzi
- Gianluca Moro
- Pavlos Vougiouklis
- Jeff Z. Pan
- Pasquale Minervini
affiliations:
- University of Bologna
- University of Edinburgh
- Huawei Technologies R&D (UK) Ltd.
- Miniml.AI
arxiv_id: '2609.30936'
url: https://arxiv.org/abs/2609.30936
pdf_url: https://arxiv.org/pdf/2609.30936
published: '2026-09-24'
collected: '2026-09-30'
category: Reasoning
direction: LLM推理优化 · 自博弈搜索蒸馏
tags:
- Self-Play
- Knowledge Distillation
- LLM Reasoning
- Synthetic Data
- MCTS
one_liner: 通过棋盘游戏自博弈搜索生成可验证推理数据，蒸馏提升LLM推理及跨域迁移能力
practical_value: '- 可复用SPSD的「外部专家生成可验证数据」思路，解决推荐/搜索场景下人工标注决策推理样本成本高、质量上限低的问题，比如用业务规则引擎模拟用户/商家决策路径生成带对比分支的训练数据

  - OPSD训练范式可迁移到LLM4Rec微调场景，对齐学生模型自身生成的决策前缀，避免传统SFT容易过拟合、长训性能下降的问题，提升跨场景推荐泛化性

  - 训练时加入规则变体样本的思路可复用，在电商多场景推荐微调中加入小比例规则扰动的样本，提升模型应对流量规则、活动策略变化的鲁棒性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前提升LLM推理能力高度依赖高质量标注数据，人工标注成本高、能力上限受人类水平限制，而现有合成数据生成方法的质量与学生模型当前能力绑定，无法产出超人类水平的结构化推理监督信号，也难以覆盖决策过程中的选项对比、后果预判等核心推理逻辑。

### 方法关键点
- 提出SPSD框架：先训练MuZero类自博弈搜索专家在棋盘游戏环境中自对弈，生成包含最优决策、可选分支、对手回复、价值估计的搜索记录，经环境重放验证后转换为结构化推理训练数据
- 设计两类监督任务：走棋选择任务输出包含分支对比、后果预判的思考链，状态问答任务覆盖走法合法性、威胁计数等6类基础判断，同步监督模型学习底层状态感知和上层决策能力
- 对比三种微调路径：SFT直接拟合思考链、OPSD将专家推理trace作为特权信息对齐学生自身采样的决策前缀、RuleBot-Distill用启发式规则生成的监督数据作为对照

### 关键实验结果
在Qwen3-4B-Base上训练后，6个数学基准测试平均分从24.1提升到36.6，未见棋盘游戏胜率从15%提升到45%；对比SFT训练后期性能下降的问题，OPSD训练全程性能稳定提升，加入规则变体训练集后数学平均分进一步提升到39.2。

### 核心结论
将外部自博弈搜索专家而非学生模型本身置于数据生成环节，可彻底解耦监督数据质量和学生模型的当前能力边界，为低成本生成超人类水平的推理训练数据提供了可行路径。
