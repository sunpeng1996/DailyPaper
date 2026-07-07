---
title: 'UniSGR: Unified Framework for Semantic ID Generation and Ranking'
title_zh: UniSGR：语义ID生成与排序的统一生成式推荐框架
authors:
- Jiawei Sun
- Jun Yang
- Ziyue Guo
- Dongyue Xu
- Jianan Yan
- Lifang Deng
- Xiaoyi Zeng
affiliations:
- Alibaba International Digital Commerce Group
arxiv_id: '2607.04068'
url: https://arxiv.org/abs/2607.04068
pdf_url: https://arxiv.org/pdf/2607.04068
published: '2026-07-05'
collected: '2026-07-07'
category: GenRec
direction: 生成式推荐 · 语义ID统一召回排序
tags:
- Semantic ID
- Generative Recommendation
- MoE
- KV Cache
- Multi-Objective Optimization
one_liner: 统一语义ID生成与多目标排序的生成式推荐框架，兼顾效果与工业级推理效率
practical_value: '- 可复用两阶段训练范式：多场景预训练+单场景对齐，直接解决稀疏业务场景的生成式推荐冷启动问题，无需从零训练

  - 引入VA-PMTP按业务价值给不同行为加生成权重，无需改模型结构即可提升高价值目标（如下单）的召回率

  - STARK推理优化可直接迁移到所有语义ID类生成式推荐系统，将解码吞吐量提升200%，降低延迟50%以上

  - 生成与排序共享语义ID表示+TAT任务感知token的设计，可消弭多阶段目标错位，减少独立排序模块的研发与推理成本'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式检索仅负责召回候选，后续独立排序模块易产生目标错位，且多业务场景数据难以复用，传统beam搜索解码语义ID的冗余计算导致延迟过高，难以满足工业级上线要求。

### 方法关键点
- 两阶段训练范式：第一阶段用多业务场景混合行为数据做Next Token Prediction预训练，学习通用用户兴趣与item语义；第二阶段在目标场景做联合优化，VA-PMTP按业务价值加权做多token并行预测，同时接入共享表示的PLE多目标排序模块。
- 生成排序对齐设计：在解码器输入前加入TAT可学习任务token，对应click/ATC/pay目标，搭配漏斗感知对比学习约束token语义，生成与排序模块共享编码器、解码器、语义ID三层表示，排序梯度直接回传更新生成器。
- 推理优化：提出STARK策略，将beam搜索的batch维度扩展改为序列维度扩展，用树形注意力掩码隔离分支，重组织KV cache避免前缀重复计算。

### 关键实验
在Lazada首页猜你喜欢场景下，对比TIGER、OneRec等主流基线，HR@100相对OneRec提升2.04%；两阶段训练相比仅单场景对齐，Pay-HR@100提升32.4%；STARK将单batch QPS从119提升至219，吞吐量翻倍；在线A/B测试相对现有级联系统，IPV涨3.36%，GMV涨5.68%。

### 核心结论
生成式推荐落地的核心瓶颈不仅是效果，更是多目标一致性与推理效率的工业级优化。
