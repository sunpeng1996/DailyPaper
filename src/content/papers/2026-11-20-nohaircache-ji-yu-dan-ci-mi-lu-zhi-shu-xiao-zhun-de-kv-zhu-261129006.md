---
title: 'NoHairCache: Calibrate-Once KV Cache Eviction with One Power-Law Exponent'
title_zh: NoHairCache：基于单次幂律指数校准的KV Cache驱逐策略
authors:
- Shuyang Xiang
arxiv_id: '2611.29006'
url: https://arxiv.org/abs/2611.29006
pdf_url: https://arxiv.org/pdf/2611.29006
published: '2026-11-20'
collected: '2026-11-24'
category: LLM
direction: LLM推理优化 · KV Cache 驱逐
tags:
- KV_cache
- LLM_inference
- power_law
- eviction_policy
- NoHairCache
one_liner: 统一H2O与StreamingLLM为幂律家族，单次校准的KV Cache驱逐策略跨域通用
practical_value: '- 电商LLM导购/多轮对话Agent部署时，可直接复用幂律评分公式替换原有KV缓存驱逐逻辑，仅需对所用LLM做一次离线校准，无需跨业务场景调参，额外开销仅为1次标量乘法

  - 针对1B参数以上模型的长上下文推理场景（如长会话理解、长商品评价分析），当KV缓存预算为序列长度6%-50%时优先采用，可比StreamingLLM获得0.06-0.10的PPL下降，同时保留98%以上的全缓存QA准确率

  - 若校准资源不足，可直接采用α=0.5的理论默认值，性能接近校准最优值，无需额外成本，适合快速上线'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文LLM推理的KV缓存内存占用随序列长度线性增长，是推理延迟与成本的核心瓶颈；现有主流驱逐策略H2O、StreamingLLM为互相割裂的启发式规则，缺乏统一框架，且需针对不同场景调参，迁移成本极高。
### 方法关键点
- 提出统一幂律评分框架：token保留分数为$s_i = A_i \cdot (t-i)^{-\alpha}$，其中$A_i$为累计注意力值，$\alpha$为年龄惩罚指数，H2O对应$\alpha=0$、StreamingLLM对应$\alpha \to \infty$，两类策略实为同一框架的两个端点
- 证明$\alpha$是模型固有属性，仅需在单语料（如WikiText）上做1次离线校准，即可跨数据集、跨任务、跨缓存预算通用，校准得到的$\alpha$范围为0.2-0.7，符合无毛发定理约束
- 实现轻量化部署：预计算年龄惩罚查找表，在线推理仅比H2O多1次标量乘法，开销可忽略，支持全局固定$\alpha$、分层$\alpha$等多种部署档位
### 关键结果
在WikiText、PG19、arXiv三个数据集上对比H2O、StreamingLLM：
- 缓存预算512时，PPL比StreamingLLM低0.057-0.104（p<0.05），比H2O低0.72-2.39
- NarrativeQA长上下文QA任务中，25%缓存预算下保留98.2%的全缓存准确率，远高于StreamingLLM的91.1%
- 仅在缓存预算低于序列长度6%的极端压缩场景下，StreamingLLM表现更优
### 核心结论
KV Cache驱逐无需设计复杂启发式，平衡token累计重要性与年龄衰减的单次校准幂律指数，即可覆盖绝大多数主流场景
