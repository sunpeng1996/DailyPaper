---
title: 'Vinci2: Providing Proactive Assistance in Continuous Egocentric Videos'
title_zh: Vinci2：面向连续第一视角视频的主动智能辅助系统
authors:
- Gong Sitong
- Tianyu Yan
- Caixin Kang
- Bo Zheng
- Xiang Ruan
- Huchuan Lu
- Kaipeng Zhang
- Yoichi Sato
- Yifei Huang
affiliations:
- Dalian University of Technology
- Alaya Lab
- The University of Tokyo
arxiv_id: '2607.11523'
url: https://arxiv.org/abs/2607.11523
pdf_url: https://arxiv.org/pdf/2607.11523
published: '2026-07-13'
collected: '2026-07-16'
category: Agent
direction: 主动式Agent · 多模态记忆增强
tags:
- Proactive Agent
- Memory Augmentation
- Egocentric Vision
- RAG
- Benchmark
one_liner: 提出首个第一视角主动辅助基准EgoServe与免训练记忆增强Agent EgoMemo，实现场景感知的主动干预决策
practical_value: '- 免训练记忆增强架构可直接复用，多模态/时序场景下可落地多尺度时序摘要+语义KG+嵌入库的三级存储结构，无需额外训练即可快速上线

  - 主动干预决策逻辑可迁移到电商导购Agent，结合用户浏览/消费时序上下文判断是否触发主动推送（如补货提醒、专属优惠触达），降低用户骚扰率

  - 跨时间窗的任务分级思路可用于推荐系统长短期兴趣建模，将用户行为划分为即时、短期、中期、长期四类 horizon 分别召回，提升推荐精准度'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有第一视角智能辅助系统要么被动等待用户查询，要么对所有检测到的事件无差别响应，未结合用户历史行为、当前活动判断辅助需求，易造成无效打扰。
### 方法关键点
1. 发布业界首个大规模第一视角主动辅助基准EgoServe，包含3000+服务实例，覆盖4类时间记忆窗口、10个服务类别，适配从即时安全告警到长期习惯指导的全场景需求
2. 提出免训练记忆增强Agent EgoMemo，维护多尺度时序摘要、语义知识图谱、视觉嵌入库三类互补记忆表示，每个时间步通过RAG判断是否需要干预，输出上下文贴合的响应
### 关键结果
EgoMemo在EgoServe基准上建立强基线性能，同时在现有公开第一视角任务benchmark上保持竞争力
