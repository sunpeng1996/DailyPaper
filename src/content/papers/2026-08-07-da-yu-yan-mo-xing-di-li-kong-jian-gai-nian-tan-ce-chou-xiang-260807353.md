---
title: 'Geo-Spatial Concept Probing of Large Language Models: Abstraction, Compositionality,
  and Grounding'
title_zh: 大语言模型地理空间概念探测：抽象性、组合性与落地性
authors:
- Karim Radouane
- Jose G Moreno
- Lynda Tamine
affiliations:
- University of Toulouse, IRIT
arxiv_id: '2608.07353'
url: https://arxiv.org/abs/2608.07353
pdf_url: https://arxiv.org/pdf/2608.07353
published: '2026-08-07'
collected: '2026-08-10'
category: LLM
direction: LLM概念探测 · 空间认知能力评估
tags:
- LLM
- Probing
- Spatial Concept
- Concept Understanding
- Benchmark
one_liner: 设计面向地理空间概念的可控探测基准，分析LLM结构化概念理解能力及模型规模等影响因素
practical_value: '- 本地生活/到店推荐类LLM应用可复用该探测框架，验证LLM空间概念理解能力，降低位置相关推荐错误率

  - 涉及LBS的Agent任务（如配送路径推荐、到店服务匹配）可参考基准测试集做候选LLM的能力前置筛选

  - 空间类Query理解（如用户搜索「周边3公里亲子乐园」）可基于研究的概念属性设计语义匹配逻辑'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有LLM概念理解评估方案多混淆多种技能，或对底层概念及属性缺乏精准控制，无法客观衡量LLM真实的结构化概念掌握水平。
### 方法关键点
1. 围绕概念三大核心属性（抽象性、组合性、落地性）搭建可控探测框架
2. 构建面向方向、距离、拓扑等空间概念及其组合的专用基准，以QA任务作为能力评估代理
3. 覆盖不同架构、训练范式、模型规模的LLM开展对照实验，分析能力影响因素
### 关键结果
当前主流LLM在空间概念的组合推理、场景落地层面存在显著缺陷；模型规模提升仅能有限改善抽象概念理解能力，对复杂组合推理任务增益极低。
