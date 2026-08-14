---
title: Thought-Level Beam Search for Reasoning
title_zh: 面向大模型推理任务的思想级束搜索框架Gambit
authors:
- Lijie Yang
- Hongyin Luo
- Jiawei Zhao
- Tri Dao
- Ravi Netravali
affiliations:
- Princeton University
- MIT CSAIL
- Meta AI
arxiv_id: '2608.08020'
url: https://arxiv.org/abs/2608.08020
pdf_url: https://arxiv.org/pdf/2608.08020
published: '2026-08-10'
collected: '2026-08-14'
category: Reasoning
direction: 大模型推理 · 测试时算力分配优化
tags:
- Beam Search
- Test-time Compute Scaling
- LLM Reasoning
- KV Cache
- Inference Optimization
one_liner: 提出思想级束搜索算法Gambit，固定硬件预算下动态分配算力到高潜力推理路径提效增准
practical_value: '- 电商Agent复杂推理（如用户需求拆解、优惠券最优发放计算）场景可复用Gambit的零和算力分配策略：固定活跃推理路径池，剪枝低质量路径后立即从高潜力前缀分支，兼顾硬件利用率与推理准确率，避免资源浪费

  - 推荐系统大模型推理（如个性化文案生成、长序列用户意图推理）可复用其轻量隐状态打分+warmup阈值设计：仅在推理达到足够深度后才启动剪枝/分支，减少早期打分噪声带来的误判，同时打分模块仅用2层MLP开销极低

  - 多路径推理场景（如搜索query改写多候选生成、活动规则合规校验）可复用其KV cache前缀共享机制：分支路径继承父路径KV cache，大幅降低多候选生成的token开销与latency，实测最多降68.5%
  token消耗'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
大模型推理性能提升高度依赖测试时算力缩放，但传统并行采样资源浪费严重（大量错误路径占用算力），剪枝类方法会导致硬件闲置、无法主动偏移输出分布，核心问题是未将算力动态分配到最有潜力的推理路径，固定硬件预算下效率极低。

### 方法关键点
- 提出Gambit思想级束搜索框架，将测试时推理建模为约束下的算力分配问题，维护固定大小的活跃推理路径池，执行零和剪枝-分支操作：每轮剪枝K条得分最低的路径，同时从K条最高得分前缀分支新路径，始终保持硬件满负载
- 加入warmup阈值设计：推理达到预设token长度前不执行打分与剪枝，避免早期推理信息不足导致的打分噪声误判
- 设计解耦内存管理架构：分离逻辑搜索视图与物理调度视图，内存不足时被调度器驱逐的路径转为“幽灵路径”仅保留逻辑位置，避免算力过度集中到少数路径导致的贪婪崩溃
- 打分模块可复用现有轻量隐状态探针，整体系统开销低于1%

### 关键实验
在AIME、HMMT、GPQA等数学/科学推理基准上测试，对比Self-Consistency、STEP、DeepConf等基线：相同硬件约束下，比剪枝基线HMMT-24准确率提升6.7%、AIME-25提升3.3%，比标准并行采样token消耗最多降低68.5%，推理路径吞吐量提升2倍以上。

### 核心结论
测试时算力优化的核心不是加多少算力，而是把算力分配到哪里，主动从高潜力前缀分支相比单纯剪枝能带来本质的效率与准确率提升
