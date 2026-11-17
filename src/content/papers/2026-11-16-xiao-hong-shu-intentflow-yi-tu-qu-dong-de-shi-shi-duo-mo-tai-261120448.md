---
title: 'IntentFlow: An Intent-Driven Real-Time Multimodal Search System with Image-Text
  Queries at Xiaohongshu'
title_zh: 小红书IntentFlow：意图驱动的实时多模态图文搜索系统
authors:
- Dongjia Zhao
- Yuchen Ma
- Chunsheng Shi
- Ziqiu Gui
- Chao Yuan
- Jianing Zhu
- Zhaoxing Zhang
- Yahui Liu
- Daoxin Zhang
- Yi Wu
affiliations:
- Xiaohongshu Inc
arxiv_id: '2611.20448'
url: https://arxiv.org/abs/2611.20448
pdf_url: https://arxiv.org/pdf/2611.20448
published: '2026-11-16'
collected: '2026-11-17'
category: RecSys
direction: 多模态搜索 · 意图驱动全链路优化
tags:
- Multimodal-Search
- Intent-Modeling
- Agentic-Data
- Representation-Learning
- Real-Time-System
one_liner: 基于分层意图建模串联多模态搜索全链路，落地小红书十亿级索引场景
practical_value: '- 多模态搜索业务可先搭建分层意图分类体系，为每个细分意图定义独立的相关性判断规则，统一召回、重排全链路的优化目标，避免前后链路目标不一致导致的效果损失

  - 可复用Agentic数据构造工作流：先做意图识别，再基于意图规则自动挖掘正负样本、补全校验证据，仅歧义点走人工审核，大幅降低多模态检索的标注成本

  - 十亿级以上大规模多模态索引迭代可采用Query侧LoRA+残差投影的优化方案，无需全量重刷文档向量，大幅降低索引更新成本，支持模型快速迭代

  - 多模态重排模块可接入上游意图识别结果，用小参数VLM做意图条件下的相关性分级，和现有排序策略做分层融合，在控制计算成本的同时提升排序效果'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
UGC社区多模态图文搜索场景下，同一参考图搭配不同文本query对应完全不同的用户意图（如同一T恤的query可能是找同款、找穿搭、找洗护方法），传统纯视觉相似度召回+重排的方案存在前后链路相关性标准不统一、符合意图的候选漏召回的问题，无法适配十亿级索引下的实时搜索需求。
### 方法关键点
- 设计两层意图分类体系：第一层分视觉搜索、信息寻求、意图不明3大类，第二层拆解为商品搜索、图片搜索、属性变体搜索、穿搭推荐等7个细分意图，每个意图定义0/1/2三级相关性判断规则
- 离线Agentic数据工作流：基于意图规则自动挖掘正负样本、校验证据，歧义点走人工审核，低成本生成梯度相关性标注和对比学习样本
- 多模态表示学习：融合意图感知对比学习、梯度排序、大模型蒸馏训练召回向量，Query侧加LoRA+残差专家门控适配，无需全量重刷文档索引即可快速迭代
- 意图条件重排器：基于上游预测的分层意图，用0.8B小参数VLM预测query-候选对的相关性等级，和现有排序策略分层融合
### 关键实验
线上A/B测试对比小红书原有纯视觉搜索基线，完整IntentFlow系统Top-4 QCTR相对提升28.17%，整体QCTR提升18.96%，用户搜索页平均停留时长提升12.56%，端到端P50 latency仅1.07s，满足十亿级索引的实时查询要求。
### 核心结论
多模态搜索的核心不是单纯提升跨模态相似度，而是先对齐用户意图，再用统一的意图相关性规则串联数据构造、召回、重排全链路。
