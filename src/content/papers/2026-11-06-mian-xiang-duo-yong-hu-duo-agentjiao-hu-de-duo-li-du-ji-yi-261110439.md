---
title: Who Remembers What? Multi-Granularity Memory Extraction for Multi-User, Multi-Agent
  Interaction
title_zh: 面向多用户多Agent交互的多粒度记忆抽取框架MIXUA
authors:
- Yunzhe Wang
- Mesut Erhan Unal
- Sheng Zhang
- Shabnam Ghadar
- Peng Tang
affiliations:
- AWS Agentic AI
- University of Southern California
arxiv_id: '2611.10439'
url: https://arxiv.org/abs/2611.10439
pdf_url: https://arxiv.org/pdf/2611.10439
published: '2026-11-06'
collected: '2026-11-14'
category: MultiAgent
direction: 多Agent记忆 · 跨用户知识共享
tags:
- Multi-Agent
- Memory System
- Privacy Protection
- Knowledge Transfer
- Personalization
one_liner: 提出四级粒度多用户多Agent共享记忆系统MIXUA，兼顾知识迁移、个性化与隐私
practical_value: '- 可直接复用四级记忆粒度（PAIR/USER/AGENT/GLOBAL）设计，解决多租户Agent服务的隐私、个性化、知识复用三者平衡问题，例如电商商家端智能助理的用户偏好、工具技巧、公共知识分层存储

  - 双流式记忆写入（可复用流/隐私流）的工程实现可直接迁移，从机制上避免私有数据写入共享域，适合多用户推荐系统的用户行为记忆分层，防止用户隐私数据被跨用户召回

  - 定期记忆复审机制可借鉴，自动升降级记忆条目粒度、合并重复内容，解决长周期运行的Agent系统记忆冗余、检索准确率下降问题

  - CROSSLEARNBENCH的评估思路可复用，从效用、个性化、隐私三个维度同时评估多用户Agent系统，避免单独优化效用忽略隐私和个性化的问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有自进化Agent的共享记忆系统要么全量共享忽略用户隐私和个性化需求，要么完全隔离无法跨用户/Agent复用知识，无法支撑多用户多异构Agent共存场景下的集体进化，同时缺乏同时覆盖知识迁移、个性化、隐私的统一评估基准。

### 方法关键点
- 定义四级记忆粒度：PAIR（仅单个用户-Agent对可见）、USER（单个用户所有Agent可见）、AGENT（单个Agent所有用户可见）、GLOBAL（全量用户Agent可见），每条记忆的授权域为效用适用域与隐私披露边界的交集
- 双流式写入：交互轨迹拆分为可复用流和隐私流，分别由独立写入模块处理，隐私流仅可写入USER/PAIR域，从机制上避免隐私泄漏
- 定期记忆复审：自动调整记忆条目粒度，合并重复内容，淘汰失效记忆
- 检索时按当前用户-Agent对的权限从对应四级域召回相关记忆

### 关键结果
基于自研CROSSLEARNBENCH（覆盖5用户7异构Agent），对比无记忆、单粒度记忆等基线：任务通过率比无记忆高16pp，比单全局记忆高5pp，跨用户跨Agent的未知任务通过率比单全局记忆高4.6pp；用户偏好保留率最高达90%，隐私探针泄漏率最高仅0.02%；缺失AGENT/PAIR域时，个性化知识泄漏率从22%升至95%，Agent专属知识通过率从89%降至40%。

多用户多Agent集体进化场景下，明确记忆的归属和访问边界，比记忆本身的内容提取更重要。
