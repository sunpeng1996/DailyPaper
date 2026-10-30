---
title: 'R2QRec: Learning Recommendation Queries from Retrieval Feedback'
title_zh: R2QRec：基于检索反馈学习推荐查询
authors:
- Weixin Chen
- Shuchang Liu
- Hailan Yang
- Yuhan Zhao
- Li Kang
- Xuefeng Zhang
- Chenghao Zhang
- Xinyuan Wang
- Hanchen Yang
- Yinghao Wu
affiliations:
- Kuaishou Technology
- Hong Kong Baptist University
arxiv_id: '2610.39984'
url: https://arxiv.org/abs/2610.39984
pdf_url: https://arxiv.org/pdf/2610.39984
published: '2026-10-29'
collected: '2026-10-30'
category: QueryRec
direction: 查询生成式推荐 · 检索反馈强化学习
tags:
- QueryGeneration
- RetrievalFeedback
- LLM4Rec
- LoRA
- GRPO
- RRF
one_liner: 基于检索反馈两阶段训练推荐查询生成器，无需标注查询或奖励模型，在3个公开数据集取得SOTA性能
practical_value: '- 伪标签构造trick：无需人工标注query，直接用现有检索系统验证生成的候选query，能召回目标item的留作SFT训练集，大幅降低标注成本，可直接复用在电商搜索推荐的query生成场景

  - 强化学习优化方案：用GRPO基于RRF融合后的目标item秩做组内相对奖励，加KL约束防止偏离SFT基线，解决多query融合后的排序优化问题，不需要单独训练奖励模型，适合生成式推荐端到端调优

  - 低改造成本架构：保持检索系统、item索引完全冻结，仅用LoRA微调LLM的query生成器，推理阶段可灵活调整query数量K适配不同算力，可直接接入现有检索链路

  - 跨域迁移结论：图书域上跨域训练的生成器性能超过域内训练模型，多域业务可尝试用高资源域训练的生成器直接迁移到低资源域，节省训练成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于query的推荐依赖目标item标题做监督，或直接prompt生成query，没有利用检索端真实反馈优化，且交互日志无用户query标注，无法直接监督query生成效果，多query融合后的排序质量也无法通过单个query的标注保证。

### 方法关键点
- 两阶段训练框架，第一阶段Item-Verified Supervision：用Base LLM生成候选query，仅保留能在检索系统中召回目标item（rank≤τ）的query作为SFT训练集，用LoRA微调生成器
- 第二阶段Fusion-Aware Refinement：基于GRPO强化学习，生成G组多query集合，每组K个query，检索后用RRF融合排序，基于目标item的融合秩计算log-rank奖励，加KL约束防止偏离SFT基线，仅更新LoRA参数
- 全流程仅训练query生成器，检索系统、item索引、LLM主干完全冻结，无需人工标注query或单独训练奖励模型

### 关键结果
在Yelp、MovieTV、Amazon Books三个公开数据集对比13个基线（含SASRec、BERT4Rec、GPT4Rec、BIGRec等），R2QRec在23/24个指标上取得SOTA，NDCG@10相对最优基线分别提升68.7%（Yelp）、3.5%（MovieTV）、42.1%（Books）；消融实验显示检索验证模块带来1.04个百分点的NDCG@10提升，RL阶段再带来0.74个百分点提升。

### 核心结论
生成式推荐的监督信号不需要局限于item文本标注，可通过下游检索的真实反馈自动构造，端到端优化最终推荐效果。
