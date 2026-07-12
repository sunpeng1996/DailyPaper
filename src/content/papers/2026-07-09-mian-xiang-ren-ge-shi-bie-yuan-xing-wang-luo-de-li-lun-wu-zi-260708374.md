---
title: Large-Language-Models-as-a-Judge in Theory-Agnostic Adaptive Metric-Alignment
  for Prototypical Networks in Personality Recognition
title_zh: 面向人格识别原型网络的理论无关自适应度量对齐LLM评判框架
authors:
- Jing Jie Tan
- Ban-Hoe Kwan
- Danny Wee-Kiat Ng
- Yan-Chai Hum
- Shih-Yu Lo
- Po-An Chen
- Noriyuki Kawarazaki
- Kosuke Takano
- Anissa Mokraoui
affiliations:
- Universiti Tunku Abdul Rahman, Malaysia
- National Yang Ming Chiao Tung University, Taiwan
- Kanagawa Institute of Technology, Japan
- Université Sorbonne Paris Nord, France
arxiv_id: '2607.08374'
url: https://arxiv.org/abs/2607.08374
pdf_url: https://arxiv.org/pdf/2607.08374
published: '2026-07-09'
collected: '2026-07-12'
category: LLM
direction: LLM-as-Judge · 无标签跨体系特征对齐
tags:
- LLM-as-a-Judge
- Metric Alignment
- Prototypical Network
- Cross-domain Alignment
- Unsupervised Representation Learning
one_liner: 提出理论无关的JAM框架，结合LLM-as-Judge实现无需预定义标签的跨体系人格识别
practical_value: '- LLM-as-Judge的前置+在环双配置可直接复用在推荐系统模糊样本标注、低质训练数据过滤场景，大幅降低人工标注成本

  - 跨源数据的CTH对齐策略（人工引导链接+机器共识）可迁移到多业务线用户偏好数据的统一特征建模，适配不同标签体系

  - 无预定义标签的原型网络聚类方法可用于冷启动用户/商品的隐含分群，无需依赖预设的用户画像/商品类目标签体系'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统人格识别高度依赖预定义心理学分类体系，标注异构且存在不一致性，泛化能力受限，无法挖掘不同体系下共通的潜在行为结构。
### 方法关键点
1. 提出JAM无理论依赖框架，将学习目标从适配预定义分类转向挖掘统一的潜在心理伪特征维度；
2. 基于注意力池化图原型网络在嵌入空间聚类，学习结构化通用心理表征，无需绑定特定分类体系即可从文本推导潜在心理画像；
3. 跨理论对齐（CTH）模块结合人工引导链接与机器共识，无需预定义标签即可统一异构数据集；
4. 引入LLM-as-Judge双机制：前置环节清洗数据、在环环节识别模糊样本引导自适应度量学习。
### 关键结果
跨心理学分类体系的泛化性显著提升，支持低资源人格理论的识别任务，已开源全部代码、模型权重及相关产物
