---
title: From LLM Hallucinations to Inspiration in Creative Work
title_zh: 大模型幻觉向创意工作灵感的转化机制与设计建议
authors:
- Xinrui Lin
- Heyan Huang
- Shuning Zhang
- Qi Wang
- Youchao Zhou
- John Vines
affiliations:
- Beijing Institute of Technology
- Tsinghua University
- University of Edinburgh
arxiv_id: '2611.12337'
url: https://arxiv.org/abs/2611.12337
pdf_url: https://arxiv.org/pdf/2611.12337
published: '2026-11-09'
collected: '2026-11-10'
category: LLM
direction: 大模型幻觉 · 创意场景应用设计
tags:
- LLM
- Hallucination
- Creative Generation
- Responsible AI
- HCI
one_liner: 通过20位创意从业者调研构建幻觉灵感判断框架，提出创意场景下LLM负责任设计方案
practical_value: '- 电商文案、商品卖点生成类Agent可按任务阶段调整幻觉容忍度：brainstorming阶段放开约束提升创意性，终稿输出阶段收紧事实校验

  - 可新增幻觉分层标注能力，对不影响核心事实、有启发价值的创意类幻觉单独打标，支持用户留存灵感再修改，避免全量驳回浪费创意

  - 创意类内容生成/推荐系统的幻觉评估可新增「灵感价值」维度，替代单一的事实准确率评价，适配创意场景需求'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
LLM幻觉普遍被视为负面缺陷，但创意场景下幻觉可能带来意外启发，当前缺乏对从业者判断幻觉灵感价值的机制、以及对应交互逻辑的研究。
### 方法关键点
对20位来自科研、设计、社交媒体内容创作的资深从业者开展半结构化访谈，主题分析41个幻觉案例，构建涵盖目标相关性、任务阶段、内容适配性等维度的灵感判断框架，关联未启发、受启发、主动落地三类行为状态。
### 关键结果
明确不同创意阶段的幻觉启发体验差异，提出将灵感价值作为幻觉评估的新增维度，输出4项可落地设计建议，可在保留创意价值的同时降低幻觉负面影响。
