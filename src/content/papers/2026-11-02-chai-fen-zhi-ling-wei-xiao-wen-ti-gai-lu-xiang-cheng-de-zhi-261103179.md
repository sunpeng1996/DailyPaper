---
title: 'Every Clause Counts: Instruction-Following Reranking by Multiplying Small,
  Answerable Questions'
title_zh: 拆分指令为小问题概率相乘的指令遵循重排序框架DMReranker
authors:
- S. M. Mahbub Uddin Ahmed
- Abdullah Al Musaddiq
affiliations:
- United International University
- Islamic University of Technology
arxiv_id: '2611.03179'
url: https://arxiv.org/abs/2611.03179
pdf_url: https://arxiv.org/pdf/2611.03179
published: '2026-11-02'
collected: '2026-11-03'
category: RecSys
direction: 指令感知搜索重排序 · 零样本优化
tags:
- Reranking
- Zero-Shot
- Instruction Following
- InfoSearch
- Probability Fusion
one_liner: 零训练DMReranker拆分子问题乘概率，InfoSearch WISE指标远超GPT-4o
practical_value: '- 电商带约束query（如「官方旗舰店 纯棉 男生T恤」）可复用该拆分逻辑，将query拆分为核心意图+约束条款，每个条款单独打分相乘，避免约束被排序模型忽略，提升高需求用户的搜索满意度

  - 商品/内容的固定属性（品类、材质、受众、来源、格式等）可预计算小模型打分的概率分布，全局复用给所有相关query，无需每次重排序都调用大模型，大幅降低推理成本

  - 零样本场景下无需训练定制重排序模型，用小模型拆分子问题打分融合的效果优于直接调用GPT-4o做列表重排序，成本仅为其1/47，适合中小团队快速落地指令感知搜索能力

  - 若业务对严格指令合规率要求高，可将概率乘积改为平均计算，仅损失少量WISE即可换取SICR的大幅提升，适配不同业务的指标优先级'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前用户搜索query常附带明确约束（如要官方文档、适配新手、指定语言），但传统重排序模型仅优化主题相关性，会将满足约束但相关性略低的结果排在后面，甚至GPT-4o做列表重排序在InfoSearch基准上的平均WISE仅为33.5，指令遵循能力严重不足。

### 方法关键点
- 指令解析：用Gemma-4-26B将带约束的query拆分为核心主题和多类约束条款，新增自校验步骤仅保留用户明确提及的约束，避免误生成规则干扰排序
- 子问题打分：用9B参数量的Clef-flash小模型为每个约束生成独立窄问题，输出满足概率；文档固定属性（来源、受众、格式、语言等）预计算概率分布，可全局复用给所有相关query，置信度低于0.3时调用27B大模型补全
- 无训练融合：直接将主题相关性概率与所有约束满足概率相乘得到最终排序分，任意条款不满足都会大幅压低得分，无需训练任何参数

### 关键结果
在InfoSearch基准6个维度上测试，DMReranker宏观WISE达50.9，远超GPT-4o的33.5和最优开源重排序模型RankZephyr的14.5；无指令原始模式下nDCG@10达82.9，接近GPT-4o的83.8，无相关性损失；总成本仅为GPT-4o列表重排序方案的1/47，单query成本不到1美分。

最值得记住的话：将复杂的指令遵循任务拆分为独立可验证的小问题，通过概率融合得到结果，是兼顾效果、可解释性和成本的零样本落地路径。
