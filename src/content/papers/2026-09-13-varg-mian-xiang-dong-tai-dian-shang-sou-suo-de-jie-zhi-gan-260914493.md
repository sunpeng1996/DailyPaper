---
title: 'VARG: Value-Aware and Ranking-Aligned Generative Retrieval for Dynamic E-commerce
  Search'
title_zh: VARG：面向动态电商搜索的价值感知排序对齐生成式检索
authors:
- Xiaopeng Chu
- Jianbo Zhu
- Mingmin Jin
- Jing Wang
- Xing Fang
- Wenyi Zhang
affiliations:
- University of Science and Technology of China
- Taobao & Tmall Group of Alibaba
- Nankai University
arxiv_id: '2609.14493'
url: https://arxiv.org/abs/2609.14493
pdf_url: https://arxiv.org/pdf/2609.14493
published: '2026-09-13'
collected: '2026-09-16'
category: GenRec
direction: 生成式检索 · Semantic ID 召回预排一体化
tags:
- Generative Retrieval
- Semantic ID
- E-commerce Search
- GRPO
- SFT
one_liner: 落地天猫的召回预排一体化生成式检索系统，直接输出候选进终排，14天AB测GMV提升1.45%
practical_value: '- Semantic ID设计可复用三层结构：前两层通过RQ-VAE加双向Q2I对比学习生成语义前缀保证相关性，第三层用EB-CVR平滑后的业务价值排序编码，兼顾寻址稳定性和价值优先性，适配电商海量动态商品场景

  - 三阶段SFT训练策略可直接迁移：先学习Item→SID映射，再学习Query→SID语义检索，最后加入用户上下文做个性化检索，配合LO-SFT局部序监督可显著提升同语义簇内高价值商品的排序效果

  - Prefix-GRPO的多源门控奖励设计可复用：覆盖合法性校验、用户行为、终排分优势、相关性四类奖励，结合前缀感知的Token加权，可大幅提升头部高价值商品召回率

  - 工程落地可借鉴增量更新方案：冻结已有商品SID，新商品仅插入空闲槽位，配合历史回放训练避免模型遗忘，适配电商每日商品迭代的动态需求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商搜索传统召回-预排-精排级联架构中，召回层漏选的高价值商品无法在下游环节被召回，现有生成式检索方案多忽略业务价值与终排目标的对齐，且难以适配每日更新的海量动态商品库，亟需一套兼顾相关性、个性化、业务价值，同时支持动态迭代的生成式检索方案，实现召回预排一体化，在有限候选配额下最大化业务收益。

### 方法关键点
- VARG-ID三层结构：前两层通过RQ-VAE加双向Q2I对比学习生成语义前缀保证检索相关性，第三层用EB-CVR平滑后的业务价值排序编码，实现无冲突寻址同时自带价值先验
- 三阶段SFT训练：依次学习Item→SID映射、Query→SID语义检索、用户上下文+Query→SID个性化检索，配合Q2I样本加权、层级Token加权、LO-SFT局部序监督提升效果
- Prefix-GRPO对齐优化：设计门控多源奖励（合法性惩罚、用户行为奖励、终排优势奖励、相关性奖励），结合前缀感知Token加权优化生成策略，对齐业务价值与终排目标
- 双循环每日更新机制：商品侧冻结已有SID，新商品增量映射；模型侧混合历史回放与新鲜数据训练，避免遗忘适配动态商品库

### 关键结果
基于天猫5143万商品、1亿+样本训练，离线Q2I-GMV Recall@1较三层RQ-VAE基线提升15.5pp；Prefix-GRPO较SFT基线GMV Recall@1提升5.47pp；14天20%流量AB测GMV提升1.45%，PCTR提升0.31%，更小候选配额下相关性优于传统检索基线。

> 生成式检索落地电商搜索的核心是在有限候选配额下同时对齐语义相关性、用户个性化偏好与业务价值目标，稳定的ID体系与渐进式训练对齐是落地关键。
