---
title: 'SkillRep: Characterizing and Understanding the Representation Design Space
  of Agent Skill Retrieval'
title_zh: SkillRep：Agent技能检索的表征设计空间刻画与理解
authors:
- Tianyi Sun
- Pengfei Yao
- Yanze Wang
- Hongda Chen
- Yunyun Han
- Jun Sun
- Chuanrui Hu
- Yafeng Deng
affiliations:
- EverMind, Shanda Group
- Peking University
- Southeast University
arxiv_id: '2610.32336'
url: https://arxiv.org/abs/2610.32336
pdf_url: https://arxiv.org/pdf/2610.32336
published: '2026-10-23'
collected: '2026-10-26'
category: Agent
direction: Agent技能检索 · 表征设计空间优化
tags:
- skill_retrieval
- dense_retrieval
- LLM_agent
- query_expansion
- hybrid_retrieval
one_liner: 组合5种表征模块实现Agent技能检索SOTA，量化请求-技能gap解释模块交互规律
practical_value: '- 技能检索/工具调用场景可直接复用5模块组合架构：优先做encoder对比微调，搭配query/doc双端LLM扩展、背景投影、BM25混合检索，比单模块优化收益更高

  - 混合检索不要用RRF，改用z-score归一化后线性加权的CombSUM方案，避免大得分差的正确结果被稀疏检索结果冲掉，实测比RRF收益高3pct左右

  - 无微调资源的场景优先上背景投影+doc端扩展，有微调资源后优先换query端扩展+lexical通道，模块收益优先级会随encoder是否微调反转

  - 可复用gap量化方法（背景/未表述词汇/稀释损失）定位现有检索系统的瓶颈，针对性优化而不是盲目堆模块'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM Agent技能检索面临请求与技能表述差异大的核心痛点，现有方案仅独立采用1-2种表征优化策略，未系统探究多模块叠加效应，也无量化方法拆解每个模块解决的具体gap，导致优化存在较强盲目性，在大规模技能库下性能衰减明显。
### 方法关键点
- 定义5维表征设计空间，组合构建SkillRep检索器：0.6B Qwen3-Embedding对比微调、query/doc双端LLM扩展（query生成假设技能、doc生成伪请求）、背景投影去除嵌入共性冗余、BM25稀疏检索通道，分数融合采用z-score归一化后线性加权的CombSUM方案
- 提出3个可量化指标拆解请求-技能gap：背景（嵌入共性方向带来的排序干扰）、未表述词汇（请求未覆盖的技能关键术语）、稀释损失（单向量表征丢失的局部匹配信息）
- 构建111247条技能的UniPool数据集，来自公开技能注册库，无近重复样本，更贴近真实部署场景
### 关键结果
在SRA-Bench官方26262技能库上MRR@10达79.21，比同规模SOTA高7.02；在11万量级UniPool上MRR@10达76.46，比同规模SOTA高8.79；在SkillsBench的易/难两个 tier 上均取得最优性能。
### 核心结论
解决同一段gap的模块会相互重叠、收益不叠加，解决不同gap的模块才会互补，模块收益优先级会随基础encoder是否微调发生反转。
