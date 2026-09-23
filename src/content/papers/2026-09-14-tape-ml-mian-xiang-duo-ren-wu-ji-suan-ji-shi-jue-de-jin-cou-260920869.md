---
title: 'TAPe+ML: A Compact Structured Representation for Multi-Task Computer Vision'
title_zh: TAPe+ML：面向多任务计算机视觉的紧凑型结构化表示
authors:
- Sergey Kurinov
- Alexey Upatov
affiliations:
- Comexp Research Lab
- TAPe + ML Project
arxiv_id: '2609.20869'
url: https://arxiv.org/abs/2609.20869
pdf_url: https://arxiv.org/pdf/2609.20869
published: '2026-09-14'
collected: '2026-09-23'
category: Other
direction: 多任务计算机视觉 · 紧凑型结构化表示
tags:
- Computer Vision
- Multi-Task Learning
- Parameter Efficient
- Structured Representation
- Low Compute Deployment
one_liner: 基于TAPe结构化感知表示，实现参数量<100k的高性能多任务计算机视觉系统
practical_value: '- 可复用「将部分建模负担前置到输入结构化表示」的思路，在多任务推荐场景提前预编码用户/物品语义关联，大幅降低下游多目标模型参数量

  - 多任务模块化协调架构可迁移到推荐系统多目标优化场景，共享底层统一表示的同时为每个优化目标保留轻量专属子模型，平衡效果与效率

  - 小参数量高性能的设计思路适合端侧推荐、直播内容实时审核等低资源部署场景，可在有限算力下保障核心任务效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有多任务CV系统依赖像素张量输入，需同时学习视觉结构与求解下游任务，存在参数量大、算力/数据开销高的痛点

### 方法关键点
1. 基于TAPe主动感知理论构建结构化输入表示，预编码视觉感知元素间的相似性、关联关系，无需下游模型从零挖掘视觉结构
2. 采用模块化多任务架构，共享TAPe底层表示的同时，整合背景轮廓处理、局部目标定位、原型分类、子模型协调器四个模块，支持分类、检测、分割多任务

### 关键结果数字
总参数量<100k；COCO目标检测mAP50达84.7、mAP50-95达65.3，实例分割mask mAP50达80.7；ImageNet-Real Top-1准确率89.9%；1小时视频场景检测索引仅需10-11s，索引体积<1MB
