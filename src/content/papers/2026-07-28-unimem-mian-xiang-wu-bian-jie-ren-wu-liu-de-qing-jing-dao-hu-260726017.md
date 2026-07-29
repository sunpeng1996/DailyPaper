---
title: 'UniMem: Complementary Episodic-to-Parametric Memory for Boundary-Agnostic
  Task Streams'
title_zh: UniMem：面向无边界任务流的情景到参数互补记忆框架
authors:
- Siyu Xia
- Chenheng Zhang
- Yanting Wu
- Haoxuan Li
- Jiajun Chai
- Xiaohan Wang
- Guojun Yin
- Wei Lin
- Zhouchen Lin
- Haifeng Zhang
affiliations:
- 中国科学院自动化研究所
- 中国科学院大学
- 北京大学
- 美团
- 伦敦大学学院
arxiv_id: '2607.26017'
url: https://arxiv.org/abs/2607.26017
pdf_url: https://arxiv.org/pdf/2607.26017
published: '2026-07-28'
collected: '2026-07-29'
category: Agent
direction: Agent 流式任务互补记忆优化
tags:
- LLM Agent
- Memory System
- Streaming Task
- RAG
- PEFT
- Task Routing
one_liner: 受人类互补记忆机制启发，提出自路由双通路记忆框架解决无边界流式任务的稳定性-可塑性矛盾
practical_value: '- 可复用「情景记忆+参数记忆」双通路架构：电商场景下长尾低频用户query/任务用RAG缓存响应，高频重复模式自动聚类后转KV缓存/LoRA固化，既降低推理开销又避免参数冗余

  - 可直接借鉴路由令牌+置信度判定机制：用轻量路由向量做任务/用户意图分类，低于置信度阈值的请求走RAG兜底，降低错误路由带来的效果损失

  - 无标注流式数据聚类策略可复用：对无标签的用户交互/query流，用NCD距离+HDBSCAN做无监督聚类，自动发现新的任务/用户分群，无需人工标注任务边界'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
现有LLM Agent记忆方案存在明显缺陷：RAG类外部记忆可塑性强但推理开销高、无法内化高频重复模式；PEFT类参数记忆执行稳定高效，但依赖显式任务边界和固定参数预算，在无边界、持续演化的流式业务场景（如电商多轮客服、实时个性化推荐任务流）下存在严重的稳定性-可塑性两难问题。

## 方法关键点
- 受人类互补学习系统理论启发，设计情景→参数的双通路记忆架构，用可学习路由令牌作为控制器，自动为每个请求选择记忆通路
- 路由层同时包含已知任务令牌和novelty哨兵令牌，仅当已知任务路由置信度同时超过哨兵概率和设定阈值时，才激活对应参数记忆，否则请求进入情景缓冲区走RAG执行
- 支持无监督增量扩展：情景缓冲区存满后自动对存储的未知请求做NCD距离计算+HDBSCAN聚类，仅高频、高内聚的有效簇会被固化为新的参数记忆单元，稀疏长尾任务保留在缓冲区

## 关键实验
在Super-Natural Instructions（最多100个流式任务）、SuperGLUE混合流两个基准上测试，覆盖5个不同规模的LLM backbone，对比Zero-Shot、标准RAG、Replay LoRA、TOKMEM四类基线，平均EM值跨3个生成式任务backbone比基线高4.0个点；在LLaMA-3B SuperGLUE混合流上平均准确率达85.95%，比次优基线高6.97个点；16000个流样本下仅按需新增76个参数记忆单元，无参数爆炸风险。

> 最值得记住的一句话：流式场景下记忆不需要二选一，低频长尾靠检索降成本，高频模式靠参数固化提效率，自动路由即可平衡稳定性与可塑性。
