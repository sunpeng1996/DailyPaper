---
title: 'VideoTapestry: Query-Adaptive Memory Refinement for Multi-Agent Long-Video
  Understanding'
title_zh: VideoTapestry：面向长视频理解的多智能体查询自适应记忆精炼框架
authors:
- Yucheng Liu
- Yufei Yin
- Mingxiao Feng
- Jiajun Deng
- Wengang Zhou
- Houqiang Li
affiliations:
- University of Science and Technology of China
- Jilin University
- Hangzhou Dianzi University
- Institute of Artificial Intelligence, Hefei Comprehensive National Science Center
arxiv_id: '2610.06672'
url: https://arxiv.org/abs/2610.06672
pdf_url: https://arxiv.org/pdf/2610.06672
published: '2026-10-05'
collected: '2026-10-06'
category: MultiAgent
direction: 多智体协作 · 分层记忆优化
tags:
- MultiAgent
- HierarchicalMemory
- LongVideoUnderstanding
- TrainingFree
- QueryAdaptive
one_liner: 免训练多智能体长视频理解框架，通过查询自适应分层记忆精炼最高提17.2%准确率
practical_value: '- 可将分层记忆+多智能体分粒度处理架构迁移到长用户行为序列推荐：将用户行为拆分为全局历史、周期事件、细粒度交互三层，对应三个专属Agent做粗到细的兴趣挖掘，既避免长序列信息丢失，又降低冗余计算

  - 查询自适应记忆优化trick可直接复用：先预构建通用静态记忆库，推理时仅对query相关分支做定向信息补充，无关分支做压缩处理，兼顾全局上下文保留和实时推理性能，适合搜索/推荐低延迟场景

  - 免训练多智能体协作范式可快速落地：无需微调基座LLM，仅通过prompt定义Agent职责、交互流程和停止规则即可提升任务效果，大幅降低业务落地的训练成本和周期'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
长视频理解需要同时保留全局上下文和定位细粒度关键证据，现有两类范式各有缺陷：自上而下查询驱动探索易受定位误差影响错过关键片段，自下而上查询无关记忆构建会遗漏特定问题需要的细节，二者互补但难以有效融合。
### 方法关键点
- 预构建三层静态分层记忆：SuperEvent（全局叙事上下文）、MacroEvent（事件级时序结构）、Subgraph（细粒度关系证据），底层结构固定不随query修改
- 三个尺度对齐的专属Agent：Overview Agent负责Super层粗检索和全局记忆优化，Skim Agent负责Macro层上下文检索和事件范围缩小，Focus Agent负责Subgraph层细粒度证据验证，各Agent仅在对应尺度上下文内工作，通过分支选择和检查目标传递实现协作
- 复合查询自适应记忆组装：仅对query相关分支做定向多模态观测和记忆补充，无关分支压缩保留全局框架，最终按原层级组装记忆供独立Answer Agent生成结果，全程免训练
### 关键实验
在LVBench、LongVideoBench（Long）、Video-MME（Long）、EgoSchema四个长视频理解benchmark上测试，以GPT-5.5为基座时，比直接推理分别提升17.2%、14.9%、9.8%、7.0%的绝对准确率，达到SOTA；消融实验显示去掉ASR、多智能体协作分别降5.5、4.5个点，分层记忆的全局框架和相关分支优化有互补作用，叠加提升7.5个点；该范式泛化性强，在GPT、Qwen等多个基座上均能稳定提升7.0-9.5%准确率。
### 核心结论
预构建通用分层记忆+查询驱动定向精炼的免训练多智能体范式，是解决长序列理解任务的高性价比方案。
