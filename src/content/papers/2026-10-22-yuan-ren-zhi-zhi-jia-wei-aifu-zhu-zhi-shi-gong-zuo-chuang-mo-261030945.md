---
title: Metacognitive Scaffolds Create Productive Friction for AI-Assisted Knowledge
  Work
title_zh: 元认知支架为AI辅助知识工作创造有效摩擦
authors:
- Viktor Kewenig
- Lev Tankelevitch
- Sean Rintel
- Advait Sarkar
- Abigail Sellen
affiliations:
- Microsoft Research, United Kingdom
arxiv_id: '2610.30945'
url: https://arxiv.org/abs/2610.30945
pdf_url: https://arxiv.org/pdf/2610.30945
published: '2026-10-22'
collected: '2026-10-24'
category: Agent
direction: Agent 人机交互引导优化
tags:
- Metacognitive Scaffold
- Human-AI Collaboration
- AI-Assisted Work
- Prompt Engineering
- User Study
one_liner: 通过297人对照实验验证AI辅助场景元认知支架效果，证实能力可迁移及主客观效果偏差
practical_value: '- 设计电商AI文案生成、投放策略Agent时，可在交互层加入目标定义、任务拆解的动态引导支架，哪怕小幅提升用户认知负荷，也能显著提升输出质量

  - 评估AI辅助工具效果时不能仅依赖用户主观易用性评分，要结合实际产出质量、长期能力迁移效果综合判断，避免为了追求「好上手」牺牲核心业务效果

  - 给运营/投放人员开发的AI工具，可通过前置元认知引导自动将用户模糊需求转化为结构化prompt，降低prompt工程门槛，沉淀的结构化需求还可作为特征优化推荐/广告模型'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
生成式AI普及后，知识工作者的工作重心从内容生产转向规划、评估、调度，面临更高的元认知负担，现有AI辅助工具大多追求极致易用，忽略了元认知引导对产出质量与能力迁移的长期价值。
### 方法关键点
开展297名参与者的随机组间对照实验，覆盖594份写作任务：实验组使用带动态元认知支架的AI写作界面，强制引导用户完成目标明确、任务拆解两步后再生成内容；对照组使用默认聊天交互界面。后续移除支架测试能力迁移效果，3天后开展内容主题召回测试。
### 关键结果数字
- 支架组写作质量较对照组显著提升，移除支架后该质量优势仍稳定保留
- 3天后支架组参与者的内容主题召回率显著优于对照组
- 支架组用户主观评价AI帮助度更低、认知负荷更高，与实际产出效果存在明显偏差
