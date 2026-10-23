---
title: The Value of Memory in Language Agents
title_zh: 语言Agent记忆的价值评估框架与落地设计原则
authors:
- Zehao Lin
- Erenkai Zhu
- Helan Hu
- Xixuan Hao
- Chunyu Li
- Kai Chen
affiliations:
- MemTensor
- Shanghai Jiao Tong University
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2610.31303'
url: https://arxiv.org/abs/2610.31303
pdf_url: https://arxiv.org/pdf/2610.31303
published: '2026-10-22'
collected: '2026-10-23'
category: Agent
direction: Agent 记忆系统价值量化与优化
tags:
- Language Agent
- Memory System
- Decision Theory
- Memory Valuation
- Agent Design
one_liner: 构建决策理论框架量化Agent记忆全生命周期价值，给出3条可落地的记忆系统优化原则
practical_value: '- 做电商导购Agent/用户生命周期记忆系统时，可复用风险-成本前沿方法权衡记忆存储、检索、修订开销与决策损失，不要盲目全量存储历史会话

  - 记忆索引（比如用户行为Semantic ID指针）哪怕不带直接业务决策信息，只要能降低检索成本就有价值，可单独为高价值用户/高复购场景配置专属记忆索引层

  - 多项目/多场景共享Agent记忆时，必须记录记忆的证据依赖关系，更新单场景记忆时避免误删其他场景的有效状态，防止跨品类推荐/多任务Agent效果退化

  - 评估记忆系统效果时要区分「记忆本身信息损失」和「Reader/LLM使用记忆的能力损失」，调优时不要只优化记忆压缩率，也要同步优化记忆读取Prompt'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent记忆研究多聚焦架构设计，缺乏统一的价值量化框架，无法回答「存储什么记忆、什么时候检索、怎么修订记忆」的ROI问题，也无法区分记忆本身损失、Reader使用能力、评估规则偏差对效果的影响。

### 方法关键点
- 构建决策理论框架，将记忆价值量化为「避免的任务决策损失」，覆盖历史写入、持久化存储、检索使用、修订全生命周期，定义风险-成本 frontier 衡量不同记忆策略的ROI
- 设计5组反例，分别验证查询时序、指针价值、记忆与Reader协同、交互反馈、需求不确定性对记忆价值的影响
- 提出3条可测试的设计假设：基于决策后果分配记忆资源、保留未知需求的恢复选项、沿证据依赖链更新记忆

### 关键实验结果
在LoCoMo多会话对话数据集测试：无记忆F1为0，仅保留压缩记忆F1仅0.016，加BM25 bounded recovery后F1提升至0.329，接近标注证据参考的0.333；双项目更新任务中，评估规则变化会让记忆效果得分波动17.9pp，与记忆本身质量无关。

最值得记住的结论：记忆的价值从来不是存储的信息量大小，而是它能在多大程度上降低未来决策的损失与检索成本。
