---
title: 'VIS-Ground: Video Interactive Storytelling with Contextual Grounding'
title_zh: VIS-Ground：面向视频交互叙事的上下文接地框架
authors:
- Bingxuan Li
- Yiwen Song
- Xueqing Wu
- Yanzhou Pan
- Yang Li
- Kuang Su
- Jingyun Liu
- Sebastian Ko
- Huan Zhang
- Tong Zhang
affiliations:
- Google
- University of Illinois at Urbana-Champaign
- University of California, Los Angeles
arxiv_id: '2610.09326'
url: https://arxiv.org/abs/2610.09326
pdf_url: https://arxiv.org/pdf/2610.09326
published: '2026-10-06'
collected: '2026-10-13'
category: Multimodal
direction: 多模态生成 · 视频交互上下文接地
tags:
- Multimodal Generation
- Interactive Storytelling
- Context Grounding
- Constrained Generation
- Video Generation
one_liner: 提出三阶段上下文接地框架VIS-Ground，实现多源输入约束下的可控视频交互叙事生成
practical_value: '- 多源异质上下文（用户意图、历史交互、业务规则）的结构化抽象方法，可直接复用给电商个性化短视频生成、直播互动内容生成场景

  - 「约束归纳+生成后验证修正」的pipeline，可迁移到生成式推荐的内容合规校验、Agent执行动作的约束对齐环节

  - 跨上下文依赖挖掘逻辑，可优化搜索推荐中用户隐式需求（结合历史行为+当前query+场景的潜在需求）识别效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频交互叙事系统仅支持单源指令对齐，无法同时融合初始叙事目标、已生成视频状态、用户新输入三类异质上下文的隐式依赖，导致生成内容逻辑冲突、不符合整体目标。

### 方法关键点
提出VIS-Ground三阶段框架：1. 结构化上下文抽象，关联叙事源、已生成场景、用户请求三类输入，抽取跨上下文依赖；2. 生成约束归纳，将依赖映射为面向候选生成结果的细粒度约束；3. 约束感知视频生成，通过规划、校验、修正、渲染四步确保生成内容满足所有约束。

### 关键结果
在3种主流视频生成骨干上均取得最优效果，相比各骨干最优基线平均绝对提升10.3分，在叙事对齐、知识接地两类指标上均有稳定增益。
