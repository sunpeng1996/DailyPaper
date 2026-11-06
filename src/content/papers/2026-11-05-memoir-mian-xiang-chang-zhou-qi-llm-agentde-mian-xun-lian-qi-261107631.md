---
title: 'MEMOIR: A Training-Free Memory Lifecycle for Long-Horizon LLM Agents'
title_zh: MEMOIR：面向长周期LLM Agent的免训练内存生命周期框架
authors:
- Mayank Anand
- Subham Raj
- Aman Vaibhav Jha
- Sriparna Saha
affiliations:
- Indian Institute of Information Technology Allahabad
- Indian Institute of Technology Patna
arxiv_id: '2611.07631'
url: https://arxiv.org/abs/2611.07631
pdf_url: https://arxiv.org/pdf/2611.07631
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: 长周期LLM Agent · 内存生命周期管理
tags:
- LLM-Agent
- Memory-System
- Training-Free
- Long-Horizon
- Retrieval
one_liner: 提出免训练长周期LLM Agent内存框架，融合事后归因更新与事前安全门控压缩提升证据召回
practical_value: '- 电商客服Agent、个性化推荐Agent的长周期用户记忆系统可直接复用TRACE-UCB设计：基于历史召回贡献度动态更新记忆权重，搭配UCB探索避免高频记忆锁死，无需额外训练成本。

  - 内存压缩阶段可复用三门控校验逻辑，仅在确认信息无损失时合并冗余记忆，避免合并时丢失未来会用到的证据，离线执行不阻塞在线链路，适配大流量生产环境。

  - 可复用成本-效果权衡方案：默认选用低延迟的词法重叠归因（6.7ms P50），精度要求高的场景可切换到留一法反事实归因（67ms P50），根据业务 latency
  要求灵活选型。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
长周期LLM Agent现有内存系统存在两个核心缺陷：一是写入时分配的静态重要性分数不会随使用更新，导致召回持续偏好过时记忆；二是内存合并时无完整性校验，容易误删未来查询需要的关键证据，无法支撑跨会话的长周期任务需求。

### 方法关键点
- 在线路径采用TRACE-UCB机制：每次查询后通过词法重叠/反事实归因计算召回记忆对答案的贡献度，动态更新记忆重要性权重，搭配UCB探索项提升低曝光记忆的召回概率，避免反馈锁死；
- 离线周期执行门控合并：仅当事实完整性、检索覆盖率、压缩比例三门控全部通过时才合并冗余记忆，合并后的新记忆继承源记忆的最大重要性权重与曝光次数，避免冷启动；
- 全链路免训练，写入路径无LLM调用，合并操作离线异步执行不阻塞在线请求。

### 关键实验
在1905条去重LoCoMoQA数据集上，完整检索栈相比纯余弦检索证据Recall@5提升11.92个百分点；置信度门控反馈额外提升1.5个百分点，多跳查询场景下Oracle反馈可提升8.05个百分点；100次校验通过的内存合并可降低活跃存储1.42%，无观测信息损失，单侧95%上限损失率仅2.95%；写入路径P50延迟仅6.8ms。

### 最值得记住的一句话
内存生命周期管理的核心原则是「使用后归因重要性，压缩前校验留存性」。
