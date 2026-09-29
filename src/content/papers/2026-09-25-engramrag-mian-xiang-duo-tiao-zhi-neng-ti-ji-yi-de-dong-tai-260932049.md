---
title: 'EngramRAG: Dynamic Usage-Weighted Topology and Synaptic Consolidation for
  Multi-Hop Agentic Memory'
title_zh: EngramRAG：面向多跳智能体记忆的动态加权拓扑与突触巩固机制
authors:
- Bhavyateja Potineni
- Lohit Giri
- Anu Jain
- Vadim Kutsyy
- Rajasekhar Pentakota
affiliations:
- Independent Researchers
arxiv_id: '2609.32049'
url: https://arxiv.org/abs/2609.32049
pdf_url: https://arxiv.org/pdf/2609.32049
published: '2026-09-25'
collected: '2026-09-29'
category: Agent
direction: Agent 多会话长期记忆优化
tags:
- Agentic Memory
- Graph RAG
- Hebbian Plasticity
- Personalized PageRank
- Synaptic Consolidation
one_liner: 提出分层双状态混合记忆架构，解决多会话Agent长期记忆的三大核心缺陷
practical_value: '- 电商导购/服务Agent的用户记忆模块可直接替换传统时间衰减规则为CATD拓扑衰减，按节点的拓扑负载权重计算留存半衰期，搭配N_grace≥4的冷启动保护期，避免用户核心偏好、身份信息、服务约束被误删

  - 跨会话多跳需求匹配场景可复用U-PPR扩散算法，融合语义相似度与历史共访问强度做图遍历，同时通过[:SUPERSEDES]有向边过滤过时的用户地址、偏好、商品规则，彻底解决新旧事实冲突的幻觉问题

  - 低延迟RAG架构可直接复用Waking/Dreaming双状态设计：在线路径做Dense Vector、BM25、图检索的动态加权RRF融合，异步离线时段做图聚类、权重更新、节点修剪，不影响在线响应，实测26.21ms检索延迟完全满足电商实时交互要求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前多会话LLM Agent的传统记忆架构存在三大致命缺陷：扁平向量索引无法跨会话遍历多跳关联依赖（关联失明）、按时间衰减的淘汰规则会误删用户身份与核心约束（脚手架遗忘）、静态图RAG不随实际使用动态更新拓扑，易出现新旧事实冲突的分裂脑幻觉，无法支撑长期连续交互场景。

### 方法关键点
- 双状态架构拆分：在线Waking状态负责低延迟摄入与检索，异步Dreaming状态（默认每6小时执行）离线做拓扑维护，读写路径完全解耦
- 提出U-PPR扩散算法，边权重通过赫布可塑性规则动态更新，按共检索次数调整关联强度，自动识别高中心度的核心认知枢纽节点
- 提出CATD拓扑衰减规则，仅在离线时段执行淘汰，按节点的拓扑负载权重计算留存半衰期，核心身份/偏好节点永久保护
- 三元混合检索：向量、BM25、U-PPR的召回结果通过动态意图加权的RRF融合，通过[:SUPERSEDES]有向边过滤过时事实

### 关键实验
在LoCoMo基准1982个多会话QA对测试中，相比纯向量RAG，Recall@5相对提升38.9%（53.21% vs 38.29%）、MRR相对提升43.1%；比BM25 Recall@5高4.55个百分点；比静态图RAG Recall@5高6倍以上。50个知识突变测试中，分裂脑幻觉率从70%降至0%；90天模拟部署核心信息留存率100%，平均检索延迟仅26.21ms。

### 核心洞察
Agent长期记忆的核心不是简单的历史存储，而是构建随使用动态演化的拓扑结构，让核心信息自然成为网络枢纽不被遗忘，过时信息被主动过滤。
