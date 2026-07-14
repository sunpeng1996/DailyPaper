---
title: 'GEIS: A Generation-Evaluation-Improvement Loop of Agent Skills for Long-Form
  Article Generation'
title_zh: GEIS：面向长文生成的Agent技能生成-评估-改进闭环
authors:
- Jiale Zhang
- Juntao Hu
- Zhijian Ou
affiliations:
- 清华大学SPMI实验室
- TasiTech Co., Ltd.
arxiv_id: '2607.11503'
url: https://arxiv.org/abs/2607.11503
pdf_url: https://arxiv.org/pdf/2607.11503
published: '2026-07-13'
collected: '2026-07-14'
category: Agent
direction: Agent 技能迭代 长文本生成优化
tags:
- Agent-Skills
- Long-Form-Generation
- LLM-as-Judge
- Evaluation-Guided-Improvement
- Modular-Agent
one_liner: 基于模块化Agent技能的生成-评估-改进闭环实现高质量长文生成与能力迭代
practical_value: '- 可将复杂生成类业务（如电商商品长详情页、营销活动文案、种草笔记生成）拆解为独立声明式技能，每个技能仅聚焦单一场景能力，边界清晰易维护，避免prompt臃肿导致的能力耦合

  - 复用生成-评估-改进闭环逻辑，针对推荐理由、商品文案等生成任务，将LLM-as-judge的成对评估结论转化为永久性技能规则补丁，无需微调LLM即可持续提升生成质量，成本低易落地

  - 长文本生成场景可直接复用六阶段写作流程：Request→Plan→Draft→Audit→Refine→Deliver，显性增加审核校验环节，可有效降低幻觉、结构混乱、内容缺失等问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有长文生成（如百科、技术文档、电商长详情页）面临长上下文信息丢失、多质量目标难同时优化、幻觉率高的问题，已有的多Agent流水线（如STORM）能力耦合在prompt和固定流程中，不可审计、难以复用、无法迭代优化，亟需更灵活的模块化方案。

### 方法关键点
- 将长文生成全流程拆解为独立声明式技能，核心写作技能遵循Request→Plan→Draft→Audit→Refine→Deliver六阶段，网页检索、图表生成、质量评估、技能改进等能力均拆分为独立技能，边界清晰可单独优化
- 设计PDF感知的成对评估技能，不设金标准，对称对比两份文档的结构、内容、视觉、交付四个维度，输出结构化可落地的质量诊断报告
- 闭环改进技能自动从评估报告中提取可修复的写作问题，转化为永久性的写作技能规则补丁，无需微调底层LLM即可迭代能力

### 关键实验
数据集为20个维基百科特色文章主题，对比baseline包括Tasi Harness默认生成器、STORM：
1. 相同生成后端下，GEIS比默认生成器总分高8.0分（百分制PDF质量评分）
2. 可比维度下，比STORM结构分高5.6、内容分高2.2
3. 20个主题迭代实验后，写作技能平均得分从82.90提升到86.95，17个主题质量明显提升

### 核心结论
对于复杂长周期生成任务，技能闭环的可解释性、可迭代性，和底层模型能力同等重要
