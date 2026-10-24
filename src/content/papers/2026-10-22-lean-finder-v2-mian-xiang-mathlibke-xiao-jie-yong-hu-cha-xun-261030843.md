---
title: 'Lean Finder V2: Semantic Search for Mathlib That Disambiguates User Queries'
title_zh: Lean Finder V2：面向Mathlib可消解用户查询歧义的语义搜索系统
authors:
- Jialin Lu
- Xiaoyu Liu
- Hengrui Luo
- Rodrigo Stehling
- Linxi Liu
- Weiran Sun
- Yuepeng Wang
- Wuyang Chen
affiliations:
- Simon Fraser University
- Rice University
- University of Pittsburgh
arxiv_id: '2610.30843'
url: https://arxiv.org/abs/2610.30843
pdf_url: https://arxiv.org/pdf/2610.30843
published: '2026-10-22'
collected: '2026-10-24'
category: QueryRec
direction: 语义搜索 · 查询消歧与改写优化
tags:
- Semantic Search
- Query Disambiguation
- Adversarial Training
- Query Rewriting
- Information Retrieval
one_liner: 通过对抗生成标注歧义短查询结合双层消岐策略，实现Mathlib语义搜索新SOTA
practical_value: '- 短模糊查询场景可复用「对抗生成标注歧义query+模型层+输入层双层消歧」架构，解决电商搜索/推荐query冷启动、标注不足问题

  - 业务搜索场景缺少短查询标注数据时，可通过对抗训练批量生成高质量带标签的歧义短查询，大幅降低标注成本

  - 现有搜索系统可叠加独立的query改写优化模块，在召回SOTA基础上进一步提升检索准确率，改造成本低收益明确

  - Agent调用外部检索工具时，可引入同款query消歧逻辑，提升工具调用准确率与下游任务效果'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有Mathlib语义搜索默认用户输入上下文丰富的查询，但实际人类数学家、编码Agent的查询多为短属性、别名等隐式内容，歧义性强，且真实短查询带标注数据稀缺，检索效果差。
### 方法关键点
1. 用对抗训练批量生成带标注的短歧义查询，解决标注数据不足问题；
2. 采用互补的双层消歧策略：模型层微调适配歧义查询语义匹配，输入层做query改写补全隐含信息。
### 关键结果
在人工标注的MathlibQR基准上，相对之前SOTA检索系统至少取得11%的相对提升；叠加优化后的query改写模块后检索效果进一步提升；在人类和Agent交互的无标注查询集上被评为最优系统；集成到Claude Code后，下游定理证明任务成功率明显上升。
