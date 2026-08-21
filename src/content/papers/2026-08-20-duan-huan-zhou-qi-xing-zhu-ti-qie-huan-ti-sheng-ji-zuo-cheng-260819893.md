---
title: 'Interrupting the Loop: Periodic Subject Changes Raise Judged Surprise and
  Connection in Base Language Models'
title_zh: 断环：周期性主题切换提升基座LLM生成内容的惊喜度与连贯性
authors:
- Roberto I. Ono Filho
affiliations:
- Independent researcher
arxiv_id: '2608.19893'
url: https://arxiv.org/abs/2608.19893
pdf_url: https://arxiv.org/pdf/2608.19893
published: '2026-08-20'
collected: '2026-08-21'
category: LLM
direction: 基座LLM长文本生成优化
tags:
- Long-form Generation
- Base LLM
- Generation Intervention
- LLM Evaluation
- Candidate Generation
one_liner: 验证每数百token注入新主题的干预可显著提升基座LLM长生成的惊喜度与连贯性
practical_value: '- 电商长文案/种草内容生成可复用「每150-300token注入关联新主题」的trick，提升内容新鲜感同时不降低用户感知的连贯性

  - Agent生成营销活动方案、推荐策略候选时，可加入周期性主题中断干预，将有效独特候选数量提升3-4倍

  - 长文本生成效果评估可复用文中的窗口式评估协议，避免上下文超出评测范围带来的评估偏差'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
基座LLM无约束生成长文本时普遍存在内容重复、新鲜感不足的问题，现有长生成效果评估易受上下文溢出干扰，且缺乏简单可落地的生成质量优化干预手段。

### 方法关键点
针对3款基座LLM设计24组对照实验，核心干预为每数百token注入新主题（中断），同时设置重复抑制、上下文重置、衔接词插入等对照条件，采用窗口式评估框架，对齐LLM评测与人类评测结果验证干预效果。

### 关键结果数字
周期性主题中断较仅做重复抑制，可让生成内容惊喜度提升1.2-1.4分、连贯性提升0.8分；150-300token的中断周期下，65%-80%的生成窗口可同时获得惊喜度与连贯性收益；在线装箱任务中该干预可将有效独特启发式候选数量提升3-4倍，且不会降低最优解质量。
