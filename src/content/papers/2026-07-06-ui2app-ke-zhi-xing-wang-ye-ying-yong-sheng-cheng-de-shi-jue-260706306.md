---
title: 'UI2App: Benchmarking Visual Interaction Inference in Executable Web Application
  Generation'
title_zh: UI2App：可执行网页应用生成的视觉交互推理基准
authors:
- Grace Man Chen
- Litao Guo
- Yifan Wu
- Yiyu Chen
- Yenchi Tseng
- Sicheng Liu
- Yuyu Luo
- Ying-Cong Chen
affiliations:
- The Hong Kong University of Science and Technology (Guangzhou)
- The Hong Kong University of Science and Technology
arxiv_id: '2607.06306'
url: https://arxiv.org/abs/2607.06306
pdf_url: https://arxiv.org/pdf/2607.06306
published: '2026-07-06'
collected: '2026-07-22'
category: Eval
direction: 多模态代码生成 · 交互能力评估
tags:
- Multimodal LLM
- Benchmark
- UI Generation
- Code Generation
- Interaction Evaluation
one_liner: 推出首个仅基于UI截图推理交互的可执行网页生成基准与多维度评估框架
practical_value: '- 电商活动页/商品页AI自动生成场景，可复用IIS交互评估指标，无需对齐参考代码，仅验证功能正确性即可降低评测成本

  - 低代码Agent开发落地时，可引入「状态连贯性校验」逻辑，优先保障跨页状态传递、导航可达性等核心交互能力

  - 多模态模型选型做UI还原任务时，不要仅以视觉相似度为选型依据，视觉与交互实现能力存在明显mismatch，需额外测试交互落地性能'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM网页生成方案分为两类：文本驱动方案对用户prompt要求高、布局与跨页一致性表达能力有限；图像驱动方案对齐真实开发流程，但现有评估仅关注视觉保真度，缺失对生成产物交互能力的系统性评估，无仅靠静态截图还原应用行为的专用基准。

### 方法关键点
推出UI2App基准，包含327张UI截图，归为45组状态连贯的多路由可执行网页截图集；设计4维度端到端评估pipeline：可执行性、导航可达性、视觉保真度、交互推理能力，其中交互指标IIS仅评估功能正确性与状态管理复杂度，兼容任意有效实现，不要求匹配单一参考代码。

### 关键结果数字
6个前沿多模态模型测试显示：视觉重建与交互实现能力严重错配，视觉保真度排名第一的模型IIS得分仅7.5，排名第四，比IIS第一名低5.2倍；跨页状态等高复杂度交互是普遍瓶颈，半数被测模型在该维度得分为0，仅靠静态截图推理完整交互行为仍是核心挑战。
