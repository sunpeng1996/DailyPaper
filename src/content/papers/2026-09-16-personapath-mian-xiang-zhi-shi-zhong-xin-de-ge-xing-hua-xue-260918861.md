---
title: 'PersonaPath: Towards Knowledge-Centric Personalized Learning Path Planning'
title_zh: PersonaPath：面向知识中心的个性化学习路径规划
authors:
- Yu Liu
- Zeming Liu
- Tianle Zhang
- Zihao Cheng
- Yuhang Guo
- Kehai Chen
- Min Zhang
- Yunhong Wang
- Haifeng Wang
affiliations:
- Beihang University
- Beijing Institute of Technology
- Harbin Institute of Technology (Shenzhen)
- Baidu Inc.
arxiv_id: '2609.18861'
url: https://arxiv.org/abs/2609.18861
pdf_url: https://arxiv.org/pdf/2609.18861
published: '2026-09-16'
collected: '2026-09-17'
category: RecSys
direction: 知识中心个性化学习路径规划基准构建
tags:
- Knowledge Graph
- Personalized Recommendation
- LLM Benchmark
- Learning Path Planning
- User Persona
one_liner: 构建含2000个学习者画像与分层知识图谱的知识中心学习路径规划基准并评测主流LLM性能
practical_value: '- 做分层知识/内容/商品路径推荐时，可参考「知识中心」而非仅交互行为中心的范式，结合用户目标、当前状态、领域依赖关系做规划，适配同行为不同目标的用户差异化需求。

  - 做个性化场景的模型评测时，可复用「细粒度用户persona + 领域知识图谱」的基准构建方法，更精准衡量模型的用户适配能力。

  - LLM做长序列规划类任务时，可重点优化用户个性化适配模块，当前该方向是LLM性能瓶颈，优化后收益空间大。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统自适应学习系统的学习路径规划为习题中心范式，仅基于物品级交互日志推断下一步内容，无法适配交互相似但学习目标不同的用户的差异化路径需求，缺少显式结合用户目标、知识掌握状态、课程级先修依赖的规划能力评测基准。

### 方法关键点
提出知识中心的个性化学习路径规划范式，要求规划器基于用户画像、知识掌握状态、知识先修结构推理下一步学习的教材/单元/知识点；构建PersonaPath基准，包含2000个细粒度学习者画像，覆盖77个学科的347本教材、1751个单元、4092个知识点的分层知识图谱。

### 关键结果
最强LLM在基础教育场景的最终通过率仅29.5%，模型核心瓶颈为个性化适配能力，所有模型的用户路径定制准确率均不超过44.7%。
