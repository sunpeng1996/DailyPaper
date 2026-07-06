---
title: Understanding How Humans Inject Knowledge into Machine Learning Workflows through
  Visual Analytics
title_zh: 基于可视化分析的人类知识注入机器学习工作流机制研究
authors:
- Yiwen Xing
- Philip Beaucamp
- Joyraj Chakraborty
- Afrah Farea
- Yuanzhe Jin
- Saiful Khan
- Gennady Andrienko
- Natalia Andrienko
- Min Chen
arxiv_id: '2607.00969'
url: https://arxiv.org/abs/2607.00969
pdf_url: https://arxiv.org/pdf/2607.00969
published: '2026-07-01'
collected: '2026-07-06'
category: Other
direction: 可视化分析 · 人机协同ML工作流优化
tags:
- VIS4ML
- Visual Analytics
- ML Workflow
- Human-in-the-loop
- Knowledge Injection
one_liner: 调研近10年200余篇VIS4ML论文，总结人类通过交互可视化向ML工作流注入知识的路径与价值
practical_value: '- 迭代推荐/搜索模型时，可参考本文总结的知识注入路径，在特征工程、超参调优环节引入交互可视化工具降低人肉debug成本

  - 搭建Human-in-the-loop的LLM4Rec/Agent系统时，可参考文中四维度编码框架设计人机交互接口，提升专家知识注入效率

  - 评估人机协同ML工作流收益时，可复用文中的信息论成本收益分析方法，量化可视化工具的投入产出比'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前ML工作流过度强调自动化，普遍忽视人类知识在数据标注、特征工程、模型调优等环节的核心价值，VIS4ML（可视化分析辅助ML）领域的知识注入机制缺乏系统性梳理。
### 方法关键点
收集近10年IEEE VIS会议的200余篇VIS4ML论文，从ML特性、可视化、交互、操作四个维度设计编码框架开展系统性文献调研，结合VA建模概念模型与信息论成本收益分析框架总结底层规律。
### 关键结果
明确了人类通过交互可视化向ML工作流注入知识的多条典型路径，实证了VA在ML工作流中的落地价值，所有调研论文清单与分析结果已全部开源。
