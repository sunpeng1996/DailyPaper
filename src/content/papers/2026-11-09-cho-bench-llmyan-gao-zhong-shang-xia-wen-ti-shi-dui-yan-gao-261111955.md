---
title: 'CHO-Bench: How Do Context Hints Affect Ad Rankings in LLM Advertising?'
title_zh: CHO-Bench：LLM广告中上下文提示对广告排序的影响评估基准
authors:
- Shiqi Zhang
- Yang Fei
- Xiaokui Xiao
affiliations:
- National University of Singapore
- PyroWis AI
arxiv_id: '2611.11955'
url: https://arxiv.org/abs/2611.11955
pdf_url: https://arxiv.org/pdf/2611.11955
published: '2026-11-09'
collected: '2026-11-10'
category: RecSys
direction: LLM广告 · 上下文提示排序优化
tags:
- LLM-Advertising
- Ad-Ranking
- Context-Hint
- Benchmark
- CHO
one_liner: 提出LLM广告上下文提示优化问题与CHO-Bench基准，验证不同提示策略的排序增益规律
practical_value: '- 做LLM原生广告的商家可直接复用论文基于营销框架的7种提示生成策略，优先测试Customer Segments、Decision
  Stages两个表现最优的单策略，无需从零搭建提示框架

  - 根据排序链路选型匹配提示策略：embedding-based链路优先用When维度提示，LLM-based精排优先用Who维度提示，无需堆叠全维度信息，Unified融合策略无稳定增益

  - 提示预算配置参考：embedding排序可配置20条以内提示（边际收益递减明显），LLM排序仅需3-5条即可，多增提示无明显收益还会提升推理成本

  - 离线评估上下文提示效果可复用CHO-Bench的配对实验设计，固定其他变量仅修改目标广告提示，无需对接线上系统即可快速验证策略'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM助手、生成式搜索成为新兴广告渠道，ChatGPT Ads允许商家提交自然语言上下文提示补充广告信息，实现非明确搜索场景下的广告匹配，但业界缺乏上下文提示的构建规范，对提示如何影响广告排序、不同策略的效果差异没有量化结论，亟需标准化评估框架。
### 方法关键点
- 基于营销领域价值主张画布、用户旅程框架，拆解出What（产品功能、痛点解决、增益创造）、Who（用户分层、用户任务）、When（使用场景、决策阶段）3大类共7种上下文提示生成策略，额外设计融合7类信息的Unified策略
- 提出CHO-Bench基准，采用配对实验设计：固定候选广告池、排序模型、其他广告信息，仅修改目标广告的上下文提示，对比有无提示的排序差异，排除其他变量干扰
- 覆盖两类主流排序链路：embedding-based相似度排序（融合ad card与最高相似度提示的得分）、LLM-based listwise排序（先选最相关提示再参与排序）
### 关键实验
基于5个公开LLM广告/电商推荐数据集（含1.19万+query、1.99万+广告、2.74万+query-ad对），测试2个提示生成模型、4个排序模型、8种提示策略、5档提示预算，共完成119万+次配对评估。核心结果：上下文提示平均提升0.56-1.16个排名位，top1率提升5.42-14.40个百分点；7种单策略平均增益差异仅0.07-0.24位，Unified无稳定优势；提示数量增加收益边际递减，embedding排序对提示数量的敏感度远高于LLM排序。
### 核心结论
LLM广告的上下文提示优化不需要盲目堆叠信息，针对排序链路选型匹配对应维度的少量提示，投入产出比最高
