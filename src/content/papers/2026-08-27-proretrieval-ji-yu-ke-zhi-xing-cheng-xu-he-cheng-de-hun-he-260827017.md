---
title: 'ProRetrieval: Learning to Orchestrate Hybrid Search via Executable Program
  Synthesis'
title_zh: ProRetrieval：基于可执行程序合成的混合搜索编排框架
authors:
- Chengsong You
- Zhen Sun
- Yunhai Hu
- Junwei Zhou
- Xiaoyu Cao
- Binyu Li
- Ziyan Zhao
- Weiyao Wang
- Liren Lu
- Zhijie Ye
affiliations:
- East China Normal University
- New York University
- Matter Innovation Inc.
- ThinRedLine
- Fudan University
arxiv_id: '2608.27017'
url: https://arxiv.org/abs/2608.27017
pdf_url: https://arxiv.org/pdf/2608.27017
published: '2026-08-27'
collected: '2026-08-28'
category: RecSys
direction: 混合检索 · LLM驱动程序合成编排
tags:
- Hybrid Retrieval
- Program Synthesis
- RLHF
- DSL
- Multi-modal Retrieval
- E-commerce Search
one_liner: 训练4B/8B小模型生成混合DSL编排多模态检索，效果超越GPT-5.5等前沿商用大模型
practical_value: '- 可直接复用分层四元奖励（格式/执行/结果/长度）训练小模型生成可执行检索程序，替代少样本调用大模型的方案，大幅降低推理成本同时提升效果

  - 电商商品搜索场景可直接套用混合DSL设计，将SQL结构化过滤（价格/品牌/品类）和文本/图像向量检索结果通过原生SQL逻辑融合，无需自定义复杂融合规则

  - 模型资源有限时优先选择4B小模型+DAPO RL训练的组合，稳定性与性能平衡最优，OOD泛化gap仅1.5pp，适合落地；算力充足时8B SFT即可达到最优效果，无需RL

  - 落地时增加简单的SQL语法后处理步骤（如转义撇号），可将DSL执行成功率提升至接近100%，几乎无额外 overhead'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有混合检索方案要么采用固定融合逻辑（如RRF、自查询检索器），不支持复杂布尔组合，要么RL检索方法仅能对接单一后端，无法同时编排结构化过滤、文本/图像多模态向量检索的异构路径，而电商、办公搜索等场景的用户查询往往同时包含结构化约束（价格、品牌、发件人）和语义/多模态需求，现有方案无法灵活适配。

### 方法关键点
- 设计混合DSL：由标准SQL语句和多模态向量检索列表组成，向量检索的候选集通过占位符注入SQL，复用SQL原生逻辑算子（AND/OR/NOT/嵌套）实现异构结果融合，表达能力覆盖所有现有检索范式
- 两阶段训练：先基于自动构造的（NL查询、黄金DSL、真值结果）三元组做SFT，再用GRPO/DAPO RL优化，采用分层四元奖励（格式正确性、可执行性、Hit@1结果、长度奖励），逐层约束程序质量
- 自动构建两个覆盖不同复杂度查询的数据集：Amazon电商（结构化+文本+图像）、Enron邮件（结构化+文本），包含从单条件到多层嵌套布尔逻辑的查询

### 关键实验
在3k Amazon商品、3k Enron邮件测试集上，对比BM25、BGE重排、RankGPT、DeepRetrieval、LightRAG以及GPT-5.5、Claude Opus 4.7等商用大模型：4B DAPO模型在电商场景Hit@1达0.808，较GPT-5.5提升11.6pp；在邮件场景Hit@1达0.909，较GPT-5.5提升5.4pp；8B SFT模型在电商场景Hit@1达0.820，超过4B RL模型效果，端到端延迟仅50ms左右。

**最值得记住的一句话**：小模型做检索编排的核心难点不是语法正确性，而是跨模态跨后端的逻辑组合能力，RL训练可有效解决SFT在复杂多模态动作空间下的多任务干扰问题，用几十倍更小的模型超过商用大模型的检索效果。
