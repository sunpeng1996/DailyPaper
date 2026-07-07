---
title: 'MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale
  Meta-Skill Evolution'
title_zh: MetaSkill-Evolve：双时间尺度元技能实现LLM Agent递归自改进
authors:
- Zefeng Wang
- Minxi Yan
- Jinhe Bi
- Sikuan Yan
- Volker Tresp
- Yunpu Ma
affiliations:
- LMU Munich
- The Chinese University of Hong Kong
- MCML
- MemAgents Lab
arxiv_id: '2607.05297'
url: https://arxiv.org/abs/2607.05297
pdf_url: https://arxiv.org/pdf/2607.05297
published: '2026-07-06'
collected: '2026-07-07'
category: Agent
direction: Agent自进化 · 双时间尺度元技能
tags:
- LLM Agent
- Self-Improvement
- Meta-Skill
- Recursive Evolution
- Skill Evolution
one_liner: 提出双时间尺度共进化框架，让Agent任务技能与迭代元策略无需额外模型即可递归自改进
practical_value: '- 可复用双时间尺度进化框架优化电商/推荐Agent：快环迭代调优商品匹配、召回排序、query理解等任务技能，慢环迭代优化故障诊断、策略迭代等元规则，突破固定迭代逻辑的瓶颈

  - 适配推荐场景分支选择逻辑：除当前效果指标外，额外加入元生产力（策略迭代效率）和分支新颖度权重，平衡探索与利用，避免策略搜索陷入局部最优

  - 直接复用五组件元技能（诊断/检索/分配/提案/执行）的设计，搭建电商场景Agent自迭代流水线，比如大促规则适配、个性化文案生成策略的自动迭代

  - 工程上可借鉴SQLite持久化进化DAG的设计，全链路留存迭代历史，支持跨分支经验复用、迭代过程可解释可回溯，适配电商广告的合规要求'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent的自进化仅优化任务技能（做什么），而迭代改进的元逻辑（怎么优化）是硬编码固定的，无法适配多样化任务场景，迭代效率容易进入瓶颈，无法实现递归自改进。

### 方法关键点
- 双时间尺度进化机制：快环每轮迭代优化任务技能s，慢环每H轮迭代优化元技能m，所有模块共享同一冻结LLM backbone，无需额外训练或新增模型
- 元技能m由5个Markdown格式的策略文件组成，分别对应改进流水线的Analyzer（故障诊断）、Retriever（跨分支经验检索）、Allocator（迭代资源分配）、Proposer（编辑提案）、Evolver（策略落地校验），可复用同一流水线递归优化
- 分支选择评分融合三项权重：当前任务效用U(s)、元生产力P(m|s)（历史迭代效率）、分支新颖度N(b)，避免迭代资源集中在性能停滞的分支
- 全量迭代历史用SQLite持久化为DAG，仅严格优于父节点的子节点进入候选池，失败/中性迭代结果仍可作为经验供跨分支检索复用

### 关键实验
在OfficeQA、SealQA、ALFWorld三个Agent基准上测试，所有方案共享冻结Gemma-4 31B backbone，对比No-Skill、Static-Skill、单级进化（无元技能迭代）基线：
- 相比No-Skill基线，MetaSkill-Evolve在三个基准上分别提升23.54、16.09、1.92个百分点的准确率/成功率
- 相比单级进化基线，仅增加元技能迭代就额外带来6.38、8.05、1.92个百分点的提升，增益完全来自进化策略本身的优化

### 核心结论
Agent的改进策略本身和任务技能一样，可以用同一套迭代框架优化，分开迭代「做什么」和「怎么改进」能大幅突破固定进化逻辑的性能瓶颈
