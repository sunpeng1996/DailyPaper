---
title: 'Profiling What Matters: Context-Aware Item Profiles from Large-Scale Metadata
  for LLM Recommenders'
title_zh: 面向LLM推荐的大规模元数据驱动上下文感知物品画像框架
authors:
- Dojun Hwang
- Seunghan Lee
- Cheonyoung Park
- Sara Yu
- SeongKu Kang
affiliations:
- Korea University
- KT Corporation
arxiv_id: '2608.20801'
url: https://arxiv.org/abs/2608.20801
pdf_url: https://arxiv.org/pdf/2608.20801
published: '2026-08-21'
collected: '2026-08-24'
category: GenRec
direction: 生成式推荐 · 上下文感知物品画像
tags:
- LLM4Rec
- Item Profiling
- Reranking
- Context-aware
- Metadata
one_liner: 提出轻量上下文感知物品画像框架CAIRO，生成用户定制化物品描述提升LLM推荐重排效果
practical_value: '- 物品侧信息处理可复用该架构：离线先将商品元数据拆分为客观属性（结构化抽取+去重统一schema）+ 主观评价标签（从评论抽取多维度特质），避免直接喂全量元数据导致LLM重排效果下降

  - 在线个性化特征选择可复用轻量控制器方案：离线训练2层MLP学习用户-物品对的属性重要性，线上仅需矩阵运算+topk选择，比agentic RAG选特征的latency降低上千倍，适配高并发电商推荐场景

  - 商品主观标签迭代可借鉴其闭环优化方案：收集重排错误case，基于客观属性修正主观标签，无需人工标注即可持续提升画像质量，可直接迁移到商品评论标签提炼场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM在推荐重排阶段已得到广泛应用，但现有方案大多聚焦用户画像优化，物品侧海量异构非结构化元数据难以被有效利用：全量投喂会挤占有限上下文窗口、不同物品的核心特征存在显著差异、同一物品的核心卖点对不同用户也存在个性化区分，直接使用固定属性或静态摘要会严重限制LLM重排效果。

### 方法关键点
- 离线结构化处理：先对物品元数据做领域聚类，抽取统一的领域级客观属性schema，从元数据中结构化抽取每个物品的客观属性；再从用户评论中为每个物品抽取3-7个多维度主观特质，每个特质关联支撑的客观属性避免幻觉。
- 轻量上下文选择器：离线训练2层MLP作为客观属性选择器，基于协同信号学习每个用户-物品对的属性重要性，线上仅需做矩阵运算选出top4相关属性；主观特质直接计算与用户画像的语义相似度，选择匹配度最高的1个。
- 可选离线优化环节：收集重排错误case，基于客观属性修正主观特质，无需人工标注即可持续提升画像质量。

### 关键结果
在Amazon三个公开数据集（电子、游戏、户外运动）上对比主流LLM重排基线，CAIRO平均提升nDCG@5 7.6%~9.9%，搭配优化环节最高提升17.9%；在线单用户画像生成延迟仅0.2~0.3s，比多轮RAG选特征方案快上千倍，与基线方案的在线延迟基本持平。

最值得记住的一句话：给LLM输入的物品信息不是越多越好，经过结构化处理+用户个性化筛选后的信息才能真正提升重排效果。
