---
title: Transparent by Design, Usable in Practice? A Formative Usability Study of a
  Conversational Product Advisor
title_zh: 设计原生透明的对话式商品导购实际可用吗？形成式可用性研究
authors:
- Kevin Schott
- Dagmar Kern
- Daniel Hienert
affiliations:
- GESIS – Leibniz Institute for the Social Sciences
arxiv_id: '2607.21513'
url: https://arxiv.org/abs/2607.21513
pdf_url: https://arxiv.org/pdf/2607.21513
published: '2026-07-23'
collected: '2026-07-24'
category: Eval
direction: 生成式推荐 · 对话式导购可用性评估
tags:
- Conversational Recommendation
- Usability Testing
- Explainable AI
- Transparent AI
- Human-Centered AI
one_liner: 通过7用户可用性测试输出透明对话式商品导购的优先级问题集与设计优化方向
practical_value: '- 做对话式电商导购的可解释性设计时，避免暴露「惩罚分」这类系统内部的负向、技术化指标，统一用正向匹配度表述，将多商品叠加雷达图替换为分组柱状图，可大幅降低用户理解成本

  - 对话式推荐系统不能仅提供纯对话交互，需补充轻量化直接操作控件（如筛选滑块、自定义排序按钮），平衡自动化效率与用户掌控感，有效提升用户信任

  - 可解释性设计要主动将系统推断的隐性需求暴露给用户确认/修改，避免因隐性规则的扣分项引发用户困惑

  - 电商对话导购的信任建设可复用3个经验：所有生成内容标注来源、避免阿谀式迎合话术、给用户开放信息来源选择权限（如专家评测/用户评价）'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM驱动的对话式商品导购交互流畅，但排序逻辑、推荐依据常隐藏在自然语言回复中，用户难以理解、信任和调整结果。设计原生透明的系统被视为核心解决方案，但透明设计是否能被用户实际感知、理解，以及用户对控制权的真实需求尚未得到实证验证，亟需落地的设计指导。
### 方法关键点
- 评估对象为笔记本电脑导购Chatbot，采用混合架构：确定性排序器负责基于商品属性的过滤打分，约束LLM生成 grounded 于商品库的内容避免幻觉；支持按需查看排序解释、多商品对比，主动回应用户需求的理解结果
- 采用形成式有声思维可用性测试，招募7名英国用户完成3个搜索任务（自由搜索、游戏本定向搜索、工作本需求迭代搜索），采集任务后易用性、满意度评分，编码交互行为得到带严重度的可用性问题集
### 关键结果
- 量化指标：3个任务的平均易用性（SEQ）得分分别为6.14/7、5.43/7、6.14/7，平均满意度分别为6.0/7、6.14/7、6.43/7；BUS-11可用性量表平均得分4.36/5，响应性得分最高达4.86/5
- 核心发现：最严重的可用性问题是排序解释难理解，4名用户对负向「惩罚分」表述、多商品叠加雷达图存在认知障碍；5名用户反馈功能可发现性差，4名用户希望补充直接操作的筛选、排序控件
### 核心结论
设计原生的透明性只是必要条件而非充分条件：暴露系统内部逻辑不等于用户能理解，可解释性设计必须站在用户认知视角而非系统实现视角
