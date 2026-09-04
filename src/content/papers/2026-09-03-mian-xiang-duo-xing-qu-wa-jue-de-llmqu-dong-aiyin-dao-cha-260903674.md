---
title: 'LLM4AIGQ: LLM-based AI Guidance Query Generation Framework for Multi Interest
  Mining'
title_zh: 面向多兴趣挖掘的LLM驱动AI引导查询生成框架LLM4AIGQ
authors:
- Xiangchen Pan
- Jiayi Xu
- Jing Wang
- Xing Fang
- Lingyun Zhu
affiliations:
- 华中科技大学
- 阿里巴巴集团
- 南开大学
arxiv_id: '2609.03674'
url: https://arxiv.org/abs/2609.03674
pdf_url: https://arxiv.org/pdf/2609.03674
published: '2026-09-03'
collected: '2026-09-04'
category: QueryRec
direction: Query推荐 · LLM多兴趣挖掘
tags:
- AIGQ
- Multi-Interest
- SFT
- RL
- DPO
- Query Recommendation
one_liner: 提出SFT-RL-DPO三阶段训练的LLM引导查询生成框架，解决传统方案语义漂移、多兴趣挖掘不足问题
practical_value: '- 训练流程可复用：对无明确ground truth的生成类推荐任务，可直接复用「大模型蒸馏SFT+多目标奖励RL+DPO蒸馏推理能力」的三阶段训练范式，避免手工规则覆盖不全的问题

  - 多目标奖励设计可借鉴：针对Query生成的多维度要求，可从推理过程、单query、单兴趣、全局多样性四个层级设计奖励，兼顾合规性、业务价值和用户体验

  - 部署架构可直接落地：采用近线预生成+在线检索的架构，既规避LLM推理延迟问题，又能保证Query的时效性，适合电商高并发低延迟场景

  - 数据处理trick：用大模型压缩item长标题为短核心标题，可降低26.8%输入token量，减少10.7%推理RT，同时让生成Query更简洁'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统电商引导查询采用Q2AIGQ两阶段范式，先召回用户主搜索query再规则泛化，存在信息级联损失导致的语义漂移，且过度依赖用户-物品共现关系，无法挖掘用户多兴趣，生成的引导Query价值低、购买意图匹配度差；同时该任务无明确ground truth，在线部署对延迟要求高，现有方案难以同时满足效果和效率要求。

### 方法关键点
- 数据预处理：用大模型将商品长标题压缩为核心短标题，删除营销冗余信息，同时截断最近50条行为序列降低计算开销
- 三阶段训练：第一阶段SFT用拆分后的单兴趣序列训练，学习引导Query的生成风格；第二阶段RL采用think-aloud推理模式，设计推理层、query层、兴趣层、全局层四级多目标奖励，用GRPO优化多兴趣拆分和Query生成能力；第三阶段DPO将think模式的推理能力蒸馏到非think模式，减少生成token数降低推理延迟
- 部署架构：近线每积累N次用户交互后批量生成引导Query存入映射表，在线请求时直接检索返回，满足低延迟要求

### 关键结果
基于淘宝天猫真实行为数据集训练，对比Qwen3-122B、Deepseek-V4-Pro等零样本大模型，最终模型Recall@10达0.2101，S级高价值Query占比86.16%；在线A/B测试10%流量时uCTR提升4.46%，扩量到40%流量后仍稳定提升2.53%。

**值得记住的结论**：无明确ground truth的生成类推荐任务，通过RL多目标奖励优化+DPO推理蒸馏，可让小参数量模型效果超过大参数量零样本模型，同时兼顾在线部署效率。
