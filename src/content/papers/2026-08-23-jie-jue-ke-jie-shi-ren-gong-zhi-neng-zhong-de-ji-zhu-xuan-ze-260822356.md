---
title: Addressing the Selection Problem in Explainable AI
title_zh: 解决可解释人工智能中的技术选择问题
authors:
- Claire Vlases
- Katelyn Morrison
affiliations:
- Carnegie Mellon University
arxiv_id: '2608.22356'
url: https://arxiv.org/abs/2608.22356
pdf_url: https://arxiv.org/pdf/2608.22356
published: '2026-08-23'
collected: '2026-08-25'
category: MultiAgent
direction: 多智能体编排 · XAI技术自动匹配
tags:
- XAI
- Multi-Agent
- LLM Orchestration
- Explanation Generation
- Query Understanding
one_liner: 形式化定义XAI技术选择问题，提出多智能体LLM编排方案自动匹配用户查询与合适的XAI解释技术
practical_value: '- 可复用多Agent LLM编排思路搭建推荐/广告系统XAI模块，自动匹配用户/运营的自然语言疑问与对应解释技术：比如问「为什么给我推这个」自动调用归因解释，问「怎么调整能不推这个」自动调用反事实解释

  - 推荐系统的XAI能力可参考该思路封装底层多种解释技术，对外仅保留自然语言交互入口，大幅降低运营/用户的使用门槛

  - 面向业务侧的AI工具平台可复用「用户自然语言查询→自动路由到对应算法能力」的架构，屏蔽底层技术复杂度，降低使用门槛'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有XAI技术品类繁多，但用户研究显示实际落地效果差，核心痛点是传统XAI接口呈烟囱式设计，要求用户自行将自然语言表达的疑问匹配到对应解释技术，普通用户不具备相关专业背景，这一系统性gap被定义为XAI选择问题。
### 方法关键点
1. 从哲学视角通过前提-结论逻辑形式化定义XAI选择问题，明确要求用户将自身不确定性转化为技术选择是传统方案的核心前置障碍；
2. 提出多智能体LLM编排工具作为结构解，通过LLM理解用户自然语言查询，自动路由到最合适的XAI技术（显著性、反事实、样本例、查询式等），屏蔽底层技术差异。
### 关键结果
已完成方案的逻辑验证并给出落地实例，可完全免除用户的XAI技术选择门槛。
