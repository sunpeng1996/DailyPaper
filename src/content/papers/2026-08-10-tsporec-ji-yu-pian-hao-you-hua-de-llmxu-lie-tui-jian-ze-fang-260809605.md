---
title: 'TSPORec: Token Selection via Preference Optimization for LLM-Based Sequential
  Recommendation'
title_zh: TSPORec：基于偏好优化的LLM序列推荐Token选择方法
authors:
- Wenqiao Zhu
- Chao Xu
- Haipang Wu
- Ji Liu
arxiv_id: '2608.09605'
url: https://arxiv.org/abs/2608.09605
pdf_url: https://arxiv.org/pdf/2608.09605
published: '2026-08-10'
collected: '2026-08-11'
category: RecSys
direction: LLM序列推荐 · Token选择效率优化
tags:
- Sequential Recommendation
- LLM4Rec
- Token Selection
- Preference Optimization
- Inference Optimization
one_liner: 提出三阶段偏好优化Token选择框架，同步提升LLM序列推荐的效果与推理效率
practical_value: '- 电商商品文本表征可复用该Token选择逻辑：优先保留商品名、属性、核心卖点等名词/实体Token，过滤无意义介词、连接词，在同等Token预算下提升表征质量

  - LLM4Rec场景可复用三阶段训练Pipeline：先预训练基线LLM推荐模型，再接轻量Policy Head用偏好优化学习Token选择策略，最后用筛选后的Token重训模型，仅增加少量训练成本即可降低60%+推理成本

  - 偏好优化的Proxy Reward设计可迁移：用两个采样Token子集的InfoNCE Loss差作为奖励信号，无需人工标注偏好，自动学习任务相关的Token重要性'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM-based序列推荐为控制推理成本，通常仅截取商品文本前k个Token，丢弃了后半段有效信息，导致效果下降；如何在限制输入Token长度的前提下保留最高信息量的文本片段，是兼顾LLM4Rec效果与落地可行性的核心痛点。

### 方法关键点
- 三阶段训练Pipeline：第一阶段预训练基础LLM序列推荐模型（包含item LLM和user LLM）；第二阶段冻结LLM backbone，新增轻量Policy Head，基于自定义Proxy Reward训练Token选择策略；第三阶段用学到的策略筛选高信息量Token，重训推荐模型
- 分Chunk的Token选择：支持按连续Token Chunk做筛选，粒度可配置，Token级选择是Chunk size=1的特例
- 无标注Proxy Reward设计：对同一段文本采样两个不同Token子集，分别计算对应的InfoNCE Loss，Loss更低的子集对应奖励+1，反之-1，最大化奖励的过程自动学习高价值Token的选择策略

### 关键实验
在Amazon Books、Pixel两个公开数据集上对比SASRec、HLLM等6个基线，分别用Qwen3-Embedding-0.6B、TinyLlama-1.1B作为backbone验证，效果最高提升31.25%的NDCG，推理成本最高降低63.4%，仅用64个选中Token就能达到基线用256个Token的效果。

### 核心结论
LLM4Rec中输入Token的质量远重要于长度，优先保留高区分度的实体/属性Token，远好于无脑取文本前缀的默认策略。
