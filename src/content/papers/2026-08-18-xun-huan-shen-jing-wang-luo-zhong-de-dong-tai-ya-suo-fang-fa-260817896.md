---
title: Dynamic Compression in Recurrent Networks
title_zh: 循环神经网络中的动态压缩方法
authors:
- Jyothish Pari
- Ryan Bahlous-Boldi
- Pulkit Agrawal
affiliations:
- Improbable AI Lab, Massachusetts Institute of Technology
arxiv_id: '2608.17896'
url: https://arxiv.org/abs/2608.17896
pdf_url: https://arxiv.org/pdf/2608.17896
published: '2026-08-18'
collected: '2026-08-19'
category: LLM
direction: LLM长上下文优化 · 循环网络动态压缩
tags:
- Recurrent Network
- Dynamic Compression
- Long Context
- Memory Efficiency
- Computation Tradeoff
one_liner: 提出循环网络动态压缩机制，通过选择性回溯修正状态，大幅降低长序列任务所需内存开销
practical_value: '- 长上下文Agent/推荐场景可借鉴该思路，无需高保真存储全量用户历史在KV cache中，低优先级历史留原始记录，需要时再召回重算，平衡内存与计算开销

  - 基于RNN的序列用户建模场景，可引入选择性回溯机制，检测到当前请求关联早期历史时，重新读取原始行为序列更新状态，降低固定用户向量存储压力

  - 推荐大模型推理服务显存不足时，可复用该计算-内存权衡思路，通过少量额外计算降低KV cache占用，提升单卡服务并发量'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有循环网络采用单轮因果遍历模式压缩历史为固定大小状态，压缩时无法预知后续信息使用需求，必须均匀高保真保留所有历史片段，导致状态大小随序列长度快速膨胀，内存效率极低。

### 方法关键点
提出动态压缩机制，保留完整原始序列副本，允许循环网络在后续任务处理时，选择性回溯与当前任务相关的历史片段，通过额外循环更新修正当前固定大小状态；无需提前高保真存储全量历史信息，仅在需求触发时重扫对应片段补全信息。

### 关键结果
在上下文多函数复用少样本任务中，达到相同准确率所需的循环状态大小降低60%以上；当序列中存储的函数数量提升10倍时，性能退化幅度仅为单通循环模型的1/3，验证了通过增加少量回溯计算可大幅降低固定状态内存开销的可行性。
