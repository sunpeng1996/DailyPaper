---
title: 'CRAFT: LLM-Based Iterative Refinement for Temporal Reasoning over Clinical
  Narratives'
title_zh: 《CRAFT：面向临床叙事时间推理的LLM迭代优化框架》
authors:
- Chengyang He
- Tahreem Arif
- Marko Zivkovic
- Lijing Wang
- Yue Ning
- Ping Wang
affiliations:
- Stevens Institute of Technology
- Genesis Research Group
- New Jersey Institute of Technology
arxiv_id: '2608.12779'
url: https://arxiv.org/abs/2608.12779
pdf_url: https://arxiv.org/pdf/2608.12779
published: '2026-08-13'
collected: '2026-08-15'
category: Reasoning
direction: 大模型时序推理 · 生成验证迭代优化
tags:
- Temporal Reasoning
- LLM Framework
- Iterative Refinement
- Constraint Verifier
- Clinical NLP
one_liner: 提出生成器+约束验证器的LLM迭代架构，解决无显式时间锚的临床叙事症状时序重构问题
practical_value: '- 可复用「生成器+约束验证器+迭代反馈」架构，用于电商场景下无显式时间戳的用户行为/消费轨迹重构，例如从用户零散评价、客服会话中还原商品使用的时序问题

  - 约束验证器的设计思路可迁移到RAG生成结构化内容的场景，通过规则校验+定向反馈迭代优化生成结果，提升电商用户时序画像、商品事件时间线的准确率

  - 时序标注benchmark的构建思路可复用，用于搭建电商用户行为时序推理任务的验证数据集，优化时序召回、时序推荐的效果'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
临床叙事普遍缺乏显式时间锚点，现有时间推理方法多聚焦多就诊、时间戳丰富场景下的成对关系分类，无法解决单份稀疏锚点报告的结构化症状时序轨迹重构问题。
### 方法关键点
提出CRAFT框架，配对生成器与基于约束的验证器，通过定向反馈迭代生成、优化分阶段的症状时间线；构建MedTempo基准数据集，包含5347条新冠疫苗不良事件叙事，其中3166条带有专家验证的时间阶段标注。
### 关键结果
在4种不同LLM backbone上测试，CRAFT均稳定提升时序排序准确率；消融实验验证了生成器、验证器组件在不同能力等级模型下的独立贡献度。
