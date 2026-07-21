---
title: 'Visualization Autocomplete: Visualization Authoring via Stepwise Design Recommendations'
title_zh: 可视化自动补全：基于分步设计推荐的可视化创作系统
authors:
- Hyeon Jeon
- Sungbok Shin
- Niklas Elmqvist
arxiv_id: '2607.15608'
url: https://arxiv.org/abs/2607.15608
pdf_url: https://arxiv.org/pdf/2607.15608
published: '2026-07-17'
collected: '2026-07-21'
category: Other
direction: 分步设计推荐 · LLM蒸馏
tags:
- LLM Distillation
- Sequential Recommendation
- Interactive System
- Design Recommendation
- Autocomplete
one_liner: 提出分步式可视化设计推荐系统VisAutocomplete，蒸馏LLM逻辑为单函数实现低延迟交互
practical_value: '- 做步骤式引导类推荐（如电商后台装修、广告素材生成分步推荐）可复用「当前状态+推荐动作→输出结果」的蒸馏单函数架构，降低交互延迟

  - 大空间探索类推荐（如文案/素材创作路径推荐）可借鉴分步决策+用户可随时干预的设计，平衡自动生成效率和用户可控性

  - 将LLM的复杂推理逻辑蒸馏为单输入输出函数的方案，可复用在低延迟要求的交互式推荐场景，减少LLM调用成本'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
领域专家制作可视化图表时，最大瓶颈并非数据，而是难以在海量设计空间中找到最优的下一步设计路径，即使能识别优质设计，也很难明确落地路径。
### 方法关键点
1. 借鉴文本自动补全思路，将可视化设计重构为序列决策过程，在创作每个阶段基于通用实践推荐具体下一步操作，支持用户随时干预，或委托系统完成多步生成后选择方案。
2. 为实现低延迟响应，将LLM的转换逻辑蒸馏为单个函数，输入当前图表状态+推荐转换动作，直接输出更新后的图表规范，无需反复调用大模型。
### 关键结果
对比LLM vibecoding、微软Excel、自动图表推荐引擎TaskVis三个基线，VisAutocomplete在复杂图表创作的清晰度表现上优于所有基线，易用性与LLM持平。
