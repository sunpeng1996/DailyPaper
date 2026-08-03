---
title: 'MOT-SR: Multi-Objective Tool-Augmented Scientific Equation Discovery with
  Large Language Models'
title_zh: MOT-SR：多目标工具增强的大语言模型科学方程发现框架
authors:
- Boxiao Wang
- Runxiang Wang
- Kai Li
- Chongming Li
- Zhiwei Chen
- Yifan Zhang
- Jian Cheng
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- University of the Chinese Academy of Sciences
- Goethe University Frankfurt
- National Key Laboratory of Cognition and Decision Intelligence for Complex Systems
- National Lab of Pattern Recognition
arxiv_id: '2607.29561'
url: https://arxiv.org/abs/2607.29561
pdf_url: https://arxiv.org/pdf/2607.29561
published: '2026-07-31'
collected: '2026-08-03'
category: Other
direction: 大语言模型 · 符号回归 多目标优化
tags:
- LLM
- Symbolic Regression
- Multi-Objective Optimization
- Tool-Augmented LLM
- Pareto Front
one_liner: 结合外部分析工具与多目标帕累托优化，双LLM协作实现高性能符号回归
practical_value: '- 多目标优化动态维护帕累托最优解的思路可直接迁移到推荐系统多目标（点击率/转化率/客单价/用户体验）排序场景，解决单目标优化易陷入局部最优的问题

  - 双LLM协作（策略生成器+内容生成器）的闭环迭代架构，可复用到Agent工具调用、生成式推荐候选生成链路，提升生成效率与结果合理性

  - 引入外部工具提取先验知识引导生成的思路，可落地到RAG、LLM4Rec场景，降低生成幻觉同时提升结果相关性'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有LLM驱动的符号回归（SR）存在两大缺陷：一是无专门数据分析机制挖掘变量依赖，方程发现效率低；二是仅以拟合误差为单优化目标，忽略结构复杂度与泛化性，易过早收敛到局部最优，无法充分探索方程空间。
### 方法关键点
提出MOT-SR统一框架：集成外部分析工具提取结构先验引导方程生成，通过多目标评估模块动态维护帕累托前沿，联合优化准确率、复杂度、泛化性三大目标；采用双LLM协作架构：Meta Strategy Generator基于帕累托最优方程选择工具、生成结构优化策略，Equation Generator据此生成候选方程，系统闭环迭代持续优化策略与方程结构。
### 关键结果
在40个标准SR任务上，准确率、泛化性、效率均优于现有SOTA方法；在空间引力波天文学极端质量比旋进轨道建模任务上，发现的可解释修正项在未见过的配置上实现最低轨迹级积分误差。
