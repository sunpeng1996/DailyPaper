---
title: 'ReflectWorld-MM: An Entity-Oriented Multimodal Memory System for Open-Ended
  Video Streams'
title_zh: 面向开放视频流的实体导向多模态记忆系统ReflectWorld-MM
authors:
- Xiaokang Ma
- Yifan Sun
- Zhihong Jin
- Jie Gu
- Yudong Luo
- Shenyi Shao
- Chu Tang
- Jingmin Chen
- Li Pu
affiliations:
- Rightly Robotics
- Hangzhou Institute for Advanced Study, UCAS
- Zhejiang University
arxiv_id: '2607.09759'
url: https://arxiv.org/abs/2607.09759
pdf_url: https://arxiv.org/pdf/2607.09759
published: '2026-07-13'
collected: '2026-07-21'
category: Agent
direction: 多模态Agent 长时实体记忆优化
tags:
- Multimodal-Agent
- Long-Term-Memory
- Entity-Centric
- Video-Understanding
- Cognitive-Memory
one_liner: 提出融合三层认知记忆结构的实体导向开放视频流多模态记忆系统，在6个长视频基准上全部取得SOTA
practical_value: '- 实体导向分层记忆架构可直接迁移到电商多模态用户行为记忆系统：将用户/商品作为核心实体，拆分 episodic（浏览/交互事件）、semantic（用户偏好/商品属性）、procedural（运营规则）三层存储，召回时按需匹配层级，可大幅降低长序列检索成本

  - 感知前注入历史上下文的设计可优化直播/短视频内容理解流程：处理长直播流时，提前注入已识别的商品/主播实体历史、场景上下文，避免片段理解的信息割裂，提升直播商品挂载、内容标签生成的准确率

  - 可更新语义记忆加固规则可复用到用户画像迭代：对用户/商品属性设置重复观测加权加固机制，新观测属性初始权重低可修改，经多次验证后权重趋近1不可轻易变更，平衡画像的灵活性和准确性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有长视频多模态记忆系统要么将记忆存在模型上下文、KV cache中，仅支持定长视频，要么采用平铺特征存储，按帧/Token组织而非围绕核心实体，无法长期追踪跨时间出现的人/物，难以支撑开放流场景下的长时记忆推理需求。

### 方法关键点
- 感知前端：将原始音视频流切割为活动连贯片段，检测并重识别实体，感知前注入三层上下文（bounded工作记忆、单相机场景语义上下文、已识别实体的历史记忆），支持上层Agent主动引导感知聚焦目标
- 分层长时记忆：参考人类认知理论拆分三类记忆：① episodic记忆分实体观测、片段摘要、叙事章节三级抽象，支持不同粒度的事件召回；② 实体中心semantic记忆支持增删改操作，实体每出现5次触发一次知识合并，重复验证的事实按γ=0.2的速率加固权重，最高趋近1；③ procedural记忆存储用户规则，触发时经解析器去重冷却后再推送，避免重复告警
- 工程实现：记忆全部持久化到索引数据库，对外暴露通用API，支持任意视频流接入和下游Agent调用，单片段处理成本不随流长度增长

### 关键实验
在6个长视频/终身记忆基准上测试，对比M3-Agent、WorldMM、GPT-5等基线全部取得最优准确率：相比M3-Agent在M3-bench-web提升10.4个百分点、M3-bench-robot提升9.1个百分点，相比WorldMM在LVBench提升7.5个百分点，EgoLife-QA准确率达46.8%，超过人工标注ID描述的45.5%基准；仅4.6%~6.8%的问题需要回查原视频，远低于WorldMM的34%。

### 核心结论
持久化多模态记忆应该作为独立的活跃系统组件存在，而非模型的附属缓存，它需要参与感知过程、围绕实体组织经验，才能支撑通用Agent在长周期视觉流上的推理和行动。
