---
title: Evaluating the accuracy of KV cache reuse techniques
title_zh: KV缓存复用技术的准确性评估
authors:
- Samuel Cestola
- Tianxiang Xia
- Pengfei Zheng
- Weiyan Zheng
- Bo Wang
- Yi Zhao
- Diego Didona
affiliations:
- Huawei Technologies Ltd.
- ETH Zurich
arxiv_id: '2609.31415'
url: https://arxiv.org/abs/2609.31415
pdf_url: https://arxiv.org/pdf/2609.31415
published: '2026-09-25'
collected: '2026-09-28'
category: LLM
direction: LLM推理优化 · KV缓存复用评估
tags:
- KV cache
- RAG
- Evaluation
- LLM Inference
- Benchmark
one_liner: 指出现有KV缓存复用评估的系统性偏差，提出无歧义评估方法和Boxoffice专用测试集
practical_value: '- 业务侧上线KV缓存复用前，先用论文提出的「有意义子集」过滤规则筛选测试query：排除全prefill答错、参数记忆可答、低信息二选一样本，避免高估复用方案的准确率保留能力

  - 电商RAG/Agent场景下，同一个商品/订单chunk会出现在不同上下文的query中，优先选择支持多版本KV缓存的方案，根据当前查询的上下文匹配最优缓存版本，避免缓存陈旧导致的准确率暴跌

  - 可复用Boxoffice的合成逻辑，构造业务专属的KV缓存压力测试集，模拟高频复用、上下文冲突等真实场景，提前验证方案的鲁棒性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
位置无关KV缓存复用是降低RAG系统prefill延迟的核心技术，但现有评估方法存在两大缺陷：一是用全量数据集的聚合F1作为指标，混入大量无效样本，系统性高估复用准确率；二是常用公开QA数据集缺乏跨query chunk复用场景，无法有效评估warm类KV缓存复用方案的真实性能。

### 方法关键点
1. 提出「有意义子集」过滤规则：仅保留三类query——full prefill能正确回答、模型无上下文无法回答、答案难以随机猜测，排除三类混淆因素：基线答错的样本、参数记忆可答的样本、低信息二选一问题
2. 开源Boxoffice合成测试集：基于虚构电影库构造查询任务，天然避免参数记忆泄露，保证所有评估query的chunk均已在热身阶段出现，还可控制「缓存陈旧」场景（同chunk在热身和查询时的角色相反）
3. 以norm-F1（复用方案F1 / 全prefill F1）为核心指标，覆盖cold、warm离线、warm在线四类主流KV缓存复用方案

### 关键结果数字
- 在LongBench-QA数据集上，现有方法的聚合F1最高有42%来自全prefill根本答不对的query，过滤后真实准确率比报道值低31%~42%
- 在Boxoffice测试集上，单版本warm方案LMCache在缓存完全对齐时norm-F1达0.98，缓存完全错位时直接降到0；多版本方案CC-M4+Q平均norm-F1达0.53，但对齐场景下性能反而不如单版本方案

### 核心结论
评估KV缓存复用的核心是测量其保留全prefill准确率的能力，任何脱离上下文匹配的复用优化都会在高动态真实场景下出现准确率暴跌。
