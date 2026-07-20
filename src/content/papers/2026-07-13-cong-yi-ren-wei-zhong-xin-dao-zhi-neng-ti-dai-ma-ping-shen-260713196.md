---
title: 'From Human-Centric to Agentic Code Review: The Impact of Different Generations
  of Generative AI Technology on Review Quality'
title_zh: 从以人为中心到智能体代码评审：生成式AI对评审质量的影响
authors:
- Suzhen Zhong
- Shayan Noei
- Bram Adams
- Ying Zou
arxiv_id: '2607.13196'
url: https://arxiv.org/abs/2607.13196
pdf_url: https://arxiv.org/pdf/2607.13196
published: '2026-07-13'
collected: '2026-07-20'
category: Agent
direction: Agent 人机协作效率与质量实证研究
tags:
- Agent
- LLM
- Human-AI Collaboration
- Empirical Study
- Process Optimization
one_liner: 基于百万级GitHub PR数据实证分析AI/Agent参与代码评审的效率与质量影响
practical_value: '- 引入AI/Agent落地业务流程（如内容审核、推荐策略评审）优先选渐进式，避免快速全量替换导致的效率升质量降问题

  - 人机协作任务可采用「Agent初审发起+人类终审把关」的流程，平衡整体效率与输出质量

  - 优化AI参与的任务流时，优先打磨人机/多Agent交互模式，其对效率的影响远高于单任务特征优化'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
代码评审是软件质量保障的核心环节，但人力负担极高，LLM、AI Agent逐步加入评审流程后，其对效率与质量的实际影响缺乏大规模实证支撑。
### 方法关键点
基于207个GitHub项目的102万条已评审PR数据，覆盖纯人工评审、LLM辅助评审、Agent参与评审三代模式，划分三类AI落地策略：渐进式引入AI、快速引入LLM、快速引入AI Agent，将评审讨论建模为交互序列刻画人-LLM-Agent的协作模式。
### 关键结果数字
- 渐进式引入AI、快速引入Agent场景下，Agent发起或多Agent参与的评审决策速度显著提升，但效率增益未同步带来评审质量提升
- AI参与后，人机协作模式成为评审效率的最强解释因子，传统评审活跃度、PR类型等特征的重要性保持稳定
