---
title: Intent-Aware Caching for Efficient LLM Serving
title_zh: 面向多轮对话LLM服务的意图感知KV缓存驱逐优化方法
authors:
- Kazi Hasan Ibn Arif
- JinYi Yoon
- Dimitrios S. Nikolopoulos
- Hans Vandierendonck
- Deepu John
- Bo Ji
affiliations:
- Virginia Tech
- Inha University
- Queen's University Belfast
- University College Dublin
arxiv_id: '2611.09715'
url: https://arxiv.org/abs/2611.09715
pdf_url: https://arxiv.org/pdf/2611.09715
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: LLM服务优化 · KV缓存策略
tags:
- KV cache
- LLM serving
- cache eviction
- multi-turn conversation
- prefix caching
one_liner: 结合用户意图与轮次信号优化KV缓存驱逐策略，大幅提升缓存命中率降低服务时延
practical_value: '- 多轮对话类Agent、电商导购/客服LLM服务可直接复用「意图+轮次」分组思路优化KV缓存驱逐策略，替换原有LRU/ML-based策略，训练开销低性能提升明显

  - 意图分类可采用轻量方案：冻结E5 embedding+3层MLP头即可实现20ms延迟、75%分类准确率，且缓存效果对分类噪声鲁棒，30%噪声下性能下降平缓，落地成本极低

  - 缓存驱逐优先级设计可直接复用：「是否在预计复用窗口内→后续轮次概率→缓存大小的三级优先级，适配时延敏感的对话类服务可直接替换SGLang等框架原生驱逐逻辑

  - 线上服务可采用轻量周期统计替代复杂ML预测模型，天然适配业务负载漂移，无需频繁重训即可保持效果稳定'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM多轮对话服务依赖prefix caching复用KV状态降低prefill计算开销，但传统LRU、GDSF等驱逐策略仅依赖通用访问信号，未捕捉不同用户任务的交互行为差异，缓存命中率极低；已有的ML-based策略仅预测对话续接概率，未考虑轮次间隔差异，且频繁重训成本高，适配负载漂移能力差，与oracle策略性能差距显著。

### 方法关键点
1. 轻量意图分类器：离线通过TnT-LLM做意图发现得到30个细粒度类别，基于冻结的E5-Large-Inst embedding加3层MLP头训练分类器，推理延迟仅20ms，分类准确率75%，对噪声鲁棒
2. 在线轻量统计：按（意图，轮次）分组，周期性统计每个分组的后续轮次概率，拟合对数正态分布得到轮次间隔中位数作为复用窗口，适配负载漂移
3. 驱逐策略：模仿TB+S oracle策略，按三级优先级排序驱逐：①是否在复用窗口内 ②后续轮次概率 ③缓存大小，优先级最低的先驱逐

### 关键实验
在WildChat、ShareChat真实多轮对话数据集测试，对比LRU、LPC（SOTA ML-based策略基线：
- 140K token容量下缓存命中率达34.6%，较LRU提升183.6%，较LPC提升84%
- Qwen-1.5-110B上TTFT降低至3.76s，较LRU降46.1%，较LPC降32%
- 10req/s负载下平均时延3.41s，较LRU降51.4%，较LPC降37.3%；相同缓存命中率下节省53%GPU内存

### 核心结论
多轮对话KV缓存优化无需依赖复杂ML模型，仅结合用户意图的细粒度分组统计就能大幅提升缓存效率，落地成本远低于端到端学习方案
