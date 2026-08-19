---
title: 'From Corpora to Co-Evolving Capabilities: Capability-Centric Data Design for
  Generalist Image Generation'
title_zh: 面向通用图像生成的能力中心化数据设计：从语料到能力协同演化
authors:
- Xingjian Wang
- Zhao Wang
- Taihang Hu
- Jun Zheng
- Qing Jin
- Qinye Zhou
- Zhengtao Wu
- Yongchao Du
- Zuan Gao
- Chao Lin
affiliations:
- Alibaba Group
arxiv_id: '2608.18076'
url: https://arxiv.org/abs/2608.18076
pdf_url: https://arxiv.org/pdf/2608.18076
published: '2026-08-17'
collected: '2026-08-19'
category: Multimodal
direction: 多模态图像生成 · 数据基建与课程训练
tags:
- Multimodal Diffusion
- Data Curation
- Curriculum Learning
- Text-to-Image
- Image Editing
one_liner: 提出能力驱动的多引擎数据基建与课程调度框架，支撑通用图像生成多任务能力协同提升
practical_value: '- 电商AI美工、商品图生成业务可复用三引擎数据构建逻辑，分别对齐文图匹配、图编辑、商品实体关联三类任务的监督数据

  - 大模型训练可借鉴按能力依赖顺序的课程调度策略，从低阶到高阶逐步提升任务难度、数据质量、分辨率，提升训练效率

  - 可复用能力感知的闭环评估逻辑，针对模型能力缺口定向补采重采样数据，降低无效数据标注与训练成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有图像生成数据 pipeline 孤立优化单任务数据集，未按生成能力依赖关系组织异质监督信号，限制通用多任务生成效果。
### 方法关键点
1. 搭建能力驱动的数据基建，包含三个可协同的数据引擎，分别构建文图对齐、跨图转换、图-知识关联三类互补监督，由caption专家对齐跨任务跨粒度的T2I与编辑监督
2. 设计多阶段课程训练机制，按能力习得依赖顺序逐步迭代任务组合、视觉概念分布、数据质量、图像分辨率，搭配能力感知评估通过定向检索、专家标注、缺口感知重采样形成闭环
### 关键结果
累计构建440M T2I语料、120M编辑对、27M+图像-实体对，用该数据从头训练3B/6B规模多模态扩散模型，在CPI-Bench及多类T2I、编辑场景验证了覆盖度、渲染能力、跨能力迁移效果的显著提升
