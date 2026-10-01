---
title: Component-Aware Feedback for Self-Evolving Programs
title_zh: 面向自进化程序的组件感知反馈优化方法
authors:
- Ethan Lin
- Jinming Nian
- Yi Fang
affiliations:
- Santa Clara University
arxiv_id: '2609.38639'
url: https://arxiv.org/abs/2609.38639
pdf_url: https://arxiv.org/pdf/2609.38639
published: '2026-09-29'
collected: '2026-10-01'
category: RecSys
direction: 自进化系统优化 · 组件感知反馈
tags:
- Evolutionary Search
- LLM Reranking
- Attribution Memory
- Multi-Objective Optimization
- Self-Evolving System
one_liner: 为LLM引导的进化搜索引入组件级归因反馈，大幅提升搜索效率与多目标优化效果
practical_value: '- 自进化优化推荐/搜索pipeline时，可复用组件级归因机制，无需让LLM从杂乱历史推断编辑效果，搜索速度可提升2/3，大幅降低调优算力成本

  - 做多目标优化（如推荐效果vs算力成本/latency平衡）时，引入本地+全局双参考帧的反馈记忆，能更高效找到兼顾多指标的最优解，可参考文中reranking场景实现效果提升同时降11%token消耗

  - 做RAG/reranking系统自动调优时，可直接借鉴这套进化搜索框架，用本地部署的中小尺寸LLM就能实现优于人工设计的pipeline效果，且跨域泛化性提升11%

  - 进化搜索的突变prompt设计中，不要仅放全量代码和整体得分，加入「组件变更-指标变化」的对应记录，可显著降低LLM推理负担，提升迭代有效性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM引导的进化搜索仅保留候选程序和整体适配度得分，丢弃了组件编辑与指标变化的对应关系，突变LLM需从杂乱历史推断过往编辑效果，导致搜索速度慢、稳定性差，尤其本地部署小模型优化多组件系统时问题更突出，也难以高效平衡效果、成本等多目标。

### 方法关键点
- 新增`observe`步骤：每次评估后对比子代与父代的组件（函数、模块级常量）差异，关联对应的全量指标变化向量，存入归因记忆
- 双参考帧存储：本地帧对比子代与父代，记录单次编辑的即时效果，取最近10条放入突变prompt；全局帧对比子代与初始种子，记录完整谱系的累计变化，搜索停滞时调用辅助策略生成
- 完全复用现有进化搜索的评估结果，无需额外LLM调用或标注，可直接嵌入AdaEvolve等现有框架，无需修改搜索控制器

### 关键实验结果
在12个BRIGHT reranking数据集上对比AdaEvolve基线，采用本地部署的Qwen3.6-35B-A3B模型：
- 纯效果优化目标下，中位数仅用1/3迭代次数即达到基线最终效果，最终nDCG@10相对提升7.2%，跨域泛化时得分保留率从79%提升至90%
- 成本感知优化目标下，输出的pipeline在nDCG更高的同时，单query token消耗降低11%

### 核心结论
当优化多组件交互的系统时，告知突变模型哪些组件变动带来了哪些指标变化，和选择哪些程序进行突变同等重要
