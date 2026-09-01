---
title: 'From Intent to Evidence: Policy-Steered Multi-Strategy Retrieval for Long-Video
  Agents'
title_zh: 面向长视频Agent的意图驱动多策略检索框架VESTA
authors:
- Can Zhang
- Baofeng Zhang
- Xiaotian Han
- Junyuan Shang
- Yuchen Ding
- Shuohuan Wang
- Dianhai Yu
- Ruirui Li
affiliations:
- Beijing University of Chemical Technology
- Baidu, Inc.
arxiv_id: '2608.31005'
url: https://arxiv.org/abs/2608.31005
pdf_url: https://arxiv.org/pdf/2608.31005
published: '2026-08-31'
collected: '2026-09-01'
category: Agent
direction: 长视频Agent · 策略引导检索
tags:
- VideoAgent
- Policy-Guided Retrieval
- Long-Video Understanding
- Temporal Evidence Ledger
- Training-Free
one_liner: 训练免长视频Agent VESTA，通过意图路由匹配检索策略+时序证据账本，大幅提升长跨度视频理解性能
practical_value: '- 可将意图路由匹配检索策略的设计迁移到电商搜索/推荐Agent：根据用户query意图（找特定商品/多商品对比/品类泛搜），分别切换精准TopK召回、时间去重的广覆盖召回、多候选对比召回策略，替代统一检索逻辑，提升召回匹配效率

  - 时序证据账本可复用在长会话推荐、直播内容理解场景：自动合并冗余观测、标记冲突信息、暴露证据缺口，减少LLM推理上下文长度，同时保留关键时序关联信息，降低推理成本

  - 查询无关的内容分块预缓存机制适合直播、长商品合集等多query复用场景：一次预编码分块存储视觉+文本特征，多用户多query调用无需重复处理全量内容，算力成本可降低一个数量级'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有长视频Agent普遍采用统一的证据获取逻辑，忽略不同问题对证据集中度、覆盖范围、对比区分的差异化需求，容易导致关键证据遗漏、检索效率低下；而预定义细粒度解决流程又会限制Agent的自主探索能力，亟需在证据获取层面提供适配性引导同时保留推理自主性。
### 方法关键点
- 训练免架构，整体采用路径条件约束的「获取-验证-整合」循环，无需额外数据集微调
- 意图路由模块仅根据query和可选候选答案，自动匹配三种检索策略：focused（证据集中时优先精准度）、recall（证据分散时优先覆盖度）、contrastive（需区分竞争假设时优先多候选对比），同时输出证据核算策略配置后续账本的视图
- 构建查询无关的共享视觉-语音场景索引，一次预编码分块存储，所有检索策略复用同一索引降低开销
- 时序证据账本自动整合多轮观测，压缩保留时序位置、来源、覆盖范围、冲突、验证结果等信息，暴露证据缺口引导后续检索，最终推理优先使用已验证观测
### 关键结果
- 在Video-MME-v2上，相比基线VideoARM平均准确率提升2.7pp（50.3% vs 47.6%），6项指标全面提升
- 在15-60分钟的LongVideoBench长视频子集上准确率提升6.9pp，小时级LVBench提升1.5pp，3分钟短clip场景性能无损失，增益随视频时长跨度增大而提升
- 消融实验显示，路由策略贡献3.0pp提升，时序证据账本贡献3.5pp提升，检索基础模块贡献9.3pp提升

> 最值得记住的结论：Agent的引导应该落在证据获取的策略层面，而非限制推理和探索流程，在降低检索成本的同时最大化保留大模型的自主决策能力
