---
title: 'SMetric: Rethink LLM Scheduling for Serving Agents with Balanced Session-centric
  Scheduling'
title_zh: SMetric：面向Agent服务的会话中心平衡LLM调度策略
authors:
- Jiahao Wang
- Kaizhan Lin
- Kaixi Zhang
- Jinbo Han
- Xingda Wei
- Sijie Shen
- Chenguang Fang
- Wenyuan Yu
- Rong Chen
- Haibo Chen
affiliations:
- Shanghai Jiao Tong University
- Alibaba Group
- ShanghaiTech University
arxiv_id: '2607.08565'
url: https://arxiv.org/abs/2607.08565
pdf_url: https://arxiv.org/pdf/2607.08565
published: '2026-07-09'
collected: '2026-07-10'
category: LLM
direction: LLM服务调度 · 会话中心KV cache复用优化
tags:
- LLM Serving
- KV Cache
- Scheduling
- Agent
- Load Balance
one_liner: 针对Agent LLM服务场景提出会话级差异化调度策略，兼顾KV cache复用与集群负载均衡，大幅提升服务吞吐
practical_value: '- 运维Agent服务/LLM推理集群的团队可直接复用会话差异化调度逻辑：会话首请求按负载均衡打散，后续请求优先路由到同实例复用本地KV
  cache，在不损失缓存收益的前提下提升集群吞吐

  - 可借鉴无状态会话阶段识别方法，直接从请求携带的历史消息数推断会话轮次，无需调度器维护会话状态，完全兼容OpenAI风格无状态API，降低架构复杂度

  - 采用两级KV cache（本地GPU+全局CPU/RDMA）架构的团队，可复用过载实例检测、缓存驱逐判断的兜底策略，解决长尾会话堆积导致的负载不均问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM调度策略针对人类聊天场景设计，适配Agent服务场景时存在明显缺陷：Agent场景KV cache复用率超过80%（远高于聊天场景的54-62%），且Agent仅需完整响应、对单token延迟容忍度更高，核心目标是提升集群TPS。现有缓存感知调度为了KV复用过度优先路由到缓存命中实例，导致少数实例过载、其余空闲，集群吞吐被锁死；而单纯负载均衡策略又会丢失大量本地KV缓存复用收益，极端情况下会压垮全局缓存层。

### 方法关键点
- 依托两级KV cache架构：本地GPU tier+全局CPU/RDMA tier，未命中本地缓存时可从全局层拉取，平衡负载无需完全放弃KV复用
- 差异化调度策略：每个会话的首请求纯按负载均衡路由，打散会话分布；同会话后续请求优先路由到之前服务的实例复用本地KV cache，仅当目标实例过载超过阈值、或会话缓存已被驱逐时回退到负载均衡
- 无状态会话识别：直接从请求携带的历史消息数量推断会话轮次，调度器无需维护会话状态，架构轻量化易扩展，兼容现有标准LLM API

### 关键实验
基于阿里百炼BAILIAN的两个生产Agent服务Trace（编码大模型场景），对比BAILIAN生产调度器、SOTA LMetric、纯负载均衡等baseline：
- 预填充解码（PD）混部场景下，集群TPS比最优baseline高10-16%，P50首token延迟（TTFT）降低17%，P50单输出token延迟（TPOT）降低10%
- 预填充解码（PD）拆离场景下，预填充TPS比最优baseline高2-34%，P50 TTFT降低37%

面向Agent的LLM调度不需要在KV缓存复用和负载均衡中二选一，抓准会话首请求的路由即可同时拿到两者的收益。
