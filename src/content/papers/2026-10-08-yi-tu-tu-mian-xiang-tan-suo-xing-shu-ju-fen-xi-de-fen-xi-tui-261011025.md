---
title: 'Intent Graph: Navigating the Analytical Reasoning Space for Exploratory Data
  Analysis'
title_zh: 《意图图：面向探索性数据分析的分析推理空间导航系统》
authors:
- Junran Yang
- Shruti Badrish
- Teanna Barrett
- Leilani Battle
affiliations:
- University of Washington
arxiv_id: '2610.11025'
url: https://arxiv.org/abs/2610.11025
pdf_url: https://arxiv.org/pdf/2610.11025
published: '2026-10-08'
collected: '2026-10-10'
category: Agent
direction: Agent 人机协同探索性数据分析
tags:
- LLM
- EDA
- Knowledge Graph
- Intent Graph
- Human-AI Collaboration
one_liner: 提出结合意图图与双层知识图谱的LLM人机协同EDA系统DAG，透明化分析推理全路径
practical_value: '- 承接运营/用户的自然语言数据分析需求时，可复用「抽象概念→数据变量」的双层知识图谱设计，避免LLM直接生成分析逻辑时的概念错配，比如分析“高价值用户特征”时先将“高价值”拆解为消费额/复购率等可落地指标再推进

  - 电商搜索query解析、用户咨询Agent等模糊意图理解场景，可复用意图DAG的内容寻址设计，支持多路径意图收敛、分支回溯，避免单次解析错误导致全链路偏差，同时留存推理全链路可解释性

  - 开发LLM辅助BI/报表生成系统时，可参考语法驱动的意图拆解框架，将复杂需求拆解为原子分析模板（趋势/对比/关联/值汇总），降低生成结果不可控性，同时支持用户按需调整拆解路径'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有LLM辅助EDA工具多为单轮输出分析结果，推理路径不透明，分析师无法查看已探索路径、缺失方向与选择依据，也无法干预LLM的概念假设，易出现概念与数据的错配；传统EDA工具则需要分析师手动完成从模糊业务问题到具体分析逻辑的全链路拆解，效率低且易遗漏可行分析方向。

### 方法关键点
- 定义分析意图语法，将所有分析需求拆解为4类原子分析类型（值汇总/趋势/关联/对比），每个类型对应固定的数据槽位规则，槽位填充后自动匹配可视化模板
- 构建双层关联结构：①意图DAG：将模糊自然语言问题拆解为多层半结构化分析任务节点，支持分支、回溯、多路径收敛，节点采用内容寻址避免重复生成；②双层知识图谱：上层为问题相关的领域概念层，下层为数据集变量与关联关系层，通过桥接边明确概念到可落地数据变量的映射，支持缺失/代理变量的主动告知
- 系统仅需数据集Schema与用户查询作为输入，通过3轮LLM调用自动生成两类图谱，无需预设领域本体，最终可将落地的分析节点自动生成交互式分析看板

### 关键实验
目前仅完成系统设计与电影数据集的场景走通验证，尚未开展量化用户实验，后续将通过用户研究验证系统对分析师推理效率的提升效果。

### 核心结论
面向模糊需求的LLM辅助系统，核心不是替代人做决策，而是把推理路径本身转化为可审计、可交互的人工制品，让人在可控的前提下获得LLM的领域知识增益
