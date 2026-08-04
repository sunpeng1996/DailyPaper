---
title: 'GROVE: Growing and Reasoning over Temporally Stratified Memory from Streaming
  Video Experience'
title_zh: 面向流式视频的时间分层记忆生长与推理框架GROVE
authors:
- Sitong Gong
- Caixin Kang
- Tianyu Yan
- Guo Chen
- Bo Zheng
- Kaipeng Zhang
- Yunzhi Zhuge
- Xiang Ruan
- Huchuan Lu
- Yifei Huang
affiliations:
- 大连理工大学
- Alaya Lab
- 东京大学
- NVIDIA
arxiv_id: '2608.02392'
url: https://arxiv.org/abs/2608.02392
pdf_url: https://arxiv.org/pdf/2608.02392
published: '2026-08-03'
collected: '2026-08-04'
category: Agent
direction: 视频Agent 分层记忆构建与多场景推理
tags:
- VideoAgent
- StratifiedMemory
- StreamingVideo
- ProactiveAssistance
- MemoryRetrieval
one_liner: 训练无关的流式视频时间分层记忆框架，同时支持反应式QA和主动式辅助服务
practical_value: '- 可复用分层记忆架构到长周期用户行为建模：将行为数据按实时感知、秒级Moment、会话级Episode、跨周期Pattern分层存储，每层匹配对应召回能力，比平铺索引同时提升召回准确率20%+、推理效率20%+

  - 主动服务触发逻辑可迁移到电商主动推荐场景：将当前实时行为特征转化为检索query，拉取历史事件、模式层信息做匹配，判断是否需要主动推送优惠、补货提醒等服务，降低无效打扰

  - 训练无关的流水线设计可直接落地：无需微调大模型，仅通过prompt engineering完成记忆构建、分割、检索全流程，适合快速复用在多模态交互Agent场景'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有流式视频记忆系统多仅支持query驱动的被动召回，主动辅助场景普遍采用独立的记忆与控制机制，两套架构无法复用，且长周期视频下平铺记忆的检索准确率低、延迟高，亟需统一的记忆substrate同时支撑两类场景。

### 方法关键点
- 增量构建4层因果时间分层记忆：实时感知层（存帧caption + 结构化实体、属性、OCR文本）、Moment层（带时间戳的细粒度事件）、Episode层（语义连贯的活动片段）、Pattern层（跨周期重复行为模式），所有更新仅依赖历史观测，无需回溯未来数据
- 配套4种scale-native检索技能：对应每层分别是Perception Lookup、Moment Recall、Episode Replay、Pattern Traversal，Agent根据query语义自动选择检索路径，多轮迭代直到证据足够回答
- 统一接口兼容两类任务：被动QA由用户query触发检索决策流，主动辅助由当前实时感知特征自动生成检索query，拉取对应层信息判断是否需要触发服务

### 关键结果
在5个行业标杆benchmark上取得SOTA：MM-Lifelong长视频QA任务day/week/month维度得分23.50/22.75/19.98，较最优基线ReMA分别提升6.75/3.93/1.36；EgoServe主动服务任务Macro-F1达12.6，较次优方案高4.6；分层架构较平铺索引减少20%+推理轮次，端到端延迟降低近20%。

> 最值得记住：按时间粒度分层的记忆架构+对应粒度的检索能力，可同时适配被动查询和主动触发两类场景，同时提升长周期信息检索的效果与效率
