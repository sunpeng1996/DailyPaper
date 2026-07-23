---
title: Evolving Cache Schedules for Fast Diffusion Policy Inference
title_zh: 面向扩散策略快速推理的动态缓存调度框架
authors:
- Siying Wang
- Kangye Ji
- Di Wang
- Fei Cheng
affiliations:
- Xidian University
- Tsinghua Shenzhen International Graduate School, Tsinghua University
arxiv_id: '2607.20293'
url: https://arxiv.org/abs/2607.20293
pdf_url: https://arxiv.org/pdf/2607.20293
published: '2026-07-22'
collected: '2026-07-23'
category: Other
direction: 扩散模型推理 · 无训练缓存调度优化
tags:
- Diffusion Policy
- Feature Cache
- Evolutionary Search
- Inference Acceleration
- Training-free
one_liner: 基于进化搜索的无训练扩散策略缓存调度框架，可在保性能前提下最高实现8.05倍推理加速
practical_value: '- 生成式推荐（如商品图/文案生成）场景用扩散模型时，可复用EVO无训练缓存调度思路，无需重训模型即可降低推理成本、提升响应速度

  - 针对多步迭代推理的系统（如多步推理Agent、迭代式生成模型），可借鉴冗余感知初始化+目标条件早停的进化搜索方案，快速定位最优缓存刷新策略

  - 生成类模型线上部署时，可离线预搜索得到最优缓存调度表直接嵌入预训练模型，无需改动现有线上推理逻辑即可实现提效'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
扩散策略通过迭代去噪实现强视觉运动控制效果，但迭代 denoising 计算开销极高，难以满足实时部署要求；现有无训练缓存方案对所有模块统一分配计算资源，忽略模块间的异构冗余特性，性能-效率 tradeoff 较差。
### 方法关键点
提出无训练加速框架EVO：
1. 将每个候选缓存策略编码为块-时间步网格的完整调度表，通过缓存复用跳过迭代去噪过程中的Transformer冗余计算，同时保障闭环推理性能
2. 引入冗余感知初始化生成优质初始候选，搭配目标条件早停机制大幅降低搜索开销
3. 离线优化得到的调度表可直接嵌入任意预训练扩散策略，无需重新训练
### 关键结果
在多类操作基准测试中几乎无损原有性能，最高实现8.05倍动作生成加速，推理FLOPs从15.77G降至最低1.96G。
