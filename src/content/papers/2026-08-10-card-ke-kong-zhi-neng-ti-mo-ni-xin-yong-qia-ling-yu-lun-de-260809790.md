---
title: 'CARD: Controlled Agentic Reddit Discussions for Credit Card Simulation'
title_zh: CARD：可控智能体模拟信用卡领域Reddit讨论的框架
authors:
- Yaoning Yu
- Kai-Min Chang
- Ye Yu
- Yi-Chia Wang
- Haojing Luo
- Haohan Wang
affiliations:
- University of Illinois Urbana-Champaign
- U.S. Bank
- Stanford University
- Starc.Institute
arxiv_id: '2608.09790'
url: https://arxiv.org/abs/2608.09790
pdf_url: https://arxiv.org/pdf/2608.09790
published: '2026-08-10'
collected: '2026-08-11'
category: Agent
direction: 智能体社交模拟 · 金融UGC生成
tags:
- MultiAgent
- SocialSimulation
- LLMGeneration
- FinanceNLP
- DistributionAlignment
one_liner: 提出规划-生成-校准闭环的多智能体框架，生成分布与真实高度对齐的信用卡领域论坛讨论
practical_value: '- 做UGC类内容生成/社区仿真时，可复用「抽象规则规划+角色约束生成+分布对齐校准」的三段式架构，避免生成内容同质化、不符合社区氛围

  - 生成序列内容时可加入context dropout技巧，随机屏蔽部分历史上下文，模拟真实用户不会读完全部讨论再回复的行为，降低生成内容的语义重复率

  - 垂直领域内容仿真的指标设计可参考：从词汇/语义多样性、语气/观点分布、结构特征、叙事/情感特征四个维度定义对齐目标，比单一的流畅度/相关性指标更能保障真实感

  - 批量内容生成的后处理可复用分指标迭代校准+核心属性约束机制，优化目标指标的同时不破坏内容核心功能（如推荐/答疑立场）'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有金融仿真仅聚焦交易、借贷等行为建模，未覆盖消费者讨论这类影响消费决策的核心UGC场景；通用社交仿真框架未适配金融领域的沟通特征，生成内容与真实社区分布偏差大。真实可控的信用卡讨论仿真可支撑产品设计、营销策略的前置验证，无需大规模真实世界干预，具备明确产业价值。
### 方法关键点
- 讨论规划器：从匹配的真实讨论中提取结构（回复深度、分支数、评论数）与单条评论的抽象属性（金融角色、立场、讨论议题类型、语气、长度等），生成非内容级的生成指导
- 内容生成器：基于评论规划、种子帖、部分历史上下文（加入context dropout随机屏蔽部分历史，模拟真实用户不读完全部讨论再回复的行为）生成符合角色要求的评论
- 自循环校准器：逐指标优化生成集合与真实集合的分布差距，每次迭代仅优化单个目标指标，同时保护其他指标不退化、保留评论核心金融属性（立场、角色等），迭代到无统计显著差异或达到上限
### 关键实验
基于Reddit 150条信用卡种子帖，对比OASIS、SynthPAI两个通用社交仿真基线，跨4个LLM验证：CARD的指标统计非拒绝率最高达91.7%（基线最高仅37.5%），分布距离比基线平均降低40%+，盲测中62%的生成讨论被判定为真实或无法区分，领先基线25pct以上。
### 核心结论
垂直领域UGC仿真不能只追求单条内容的通顺合理，必须从集合层面匹配真实社区的分布特征，才能实现足够的真实感。
