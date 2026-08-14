---
title: 'StreamTTT: Reconciling Real-Time Perception and Long-Term Memory in Streaming
  VLMs'
title_zh: StreamTTT：流式视觉大模型中实时感知与长期记忆的平衡
authors:
- Joya Chen
- Zeyun Zhong
- Mike Zheng Shou
affiliations:
- National University of Singapore
- Karlsruhe Institute of Technology
arxiv_id: '2608.13416'
url: https://arxiv.org/abs/2608.13416
pdf_url: https://arxiv.org/pdf/2608.13416
published: '2026-08-13'
collected: '2026-08-14'
category: Multimodal
direction: 多模态大模型 · 流式记忆优化
tags:
- VLM
- Streaming Perception
- Long-term Memory
- KV Cache
- Fast Weights
one_liner: 提出将流式VLM长期历史存入注意力上下文外的在线更新快权重，平衡实时感知与长程记忆能力
practical_value: '- 可复用「滑动KV cache存近期信息+外置快权重存长期历史」的架构，解决电商直播实时理解、长会话导购Agent的长序列注意力稀释问题

  - 离线长时序任务+实时任务联合训练的策略，可迁移到流式用户行为序列建模，兼顾短期点击感知与长期兴趣召回效果

  - 长短记忆拆分的思路可降低推荐系统长会话推理的显存与计算开销，适合端侧/低算力场景的流式推荐应用'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
流式VLM普遍存在实时感知与长程记忆的权衡问题：缩短上下文窗口可提升当前场景感知精度，但会牺牲历史内容召回能力；拉长上下文又会导致注意力稀释，降低实时推理效率。
### 方法关键点
1. 设计StreamTTT架构，将长程历史写入注意力上下文之外的在线更新快权重，不占用attention计算空间；
2. 保留短滑动KV cache专门存储近期帧数据，避免注意力分散；
3. 采用离线长视频QA与新构建的实时QA语料联合训练。
### 关键结果
在OVO-Bench上，StreamTTT-4B较同参数SimpleStream-4B，实时感知指标高1.4pt，回溯能力高3.7pt；性能与参数量2倍的SimpleStream-8B在StreamingBench的RTVU子集上表现相当。
