---
title: 'HySparse2: Hybrid Sparse Attention with Two-Level KV Sharing'
title_zh: HySparse2：支持双层KV共享的混合稀疏注意力架构
authors:
- Jianyu Wei
- Yizhao Gao
- Qihao Zhang
- Shimao Chen
- Zhengju Tang
- Yu Cheng
- Shengjie Zhou
- Zihan Jiang
- Yifan Song
- Hailin Zhang
affiliations:
- Xiaomi LLM-Core
arxiv_id: '2609.26368'
url: https://arxiv.org/abs/2609.26368
pdf_url: https://arxiv.org/pdf/2609.26368
published: '2026-09-22'
collected: '2026-09-23'
category: LLM
direction: LLM推理优化 · KV共享 稀疏注意力
tags:
- KV Cache
- Sparse Attention
- Long Context
- Agent Inference
- MoE
one_liner: 面向长轮次Agent场景的双层KV共享混合稀疏注意力架构，兼顾长程检索精度与推理效率
practical_value: '- 电商多轮导购Agent、长文档RAG场景可复用token级稀疏选择+强制最近窗口的设计，在固定注意力预算下提升长上下文历史召回精度，减少KV缓存存储

  - 工程侧可参考双层KV共享的预填充早退方案，预填充阶段仅运行self-decoder即可完成KV缓存构建，1M上下文下预填充FLOPs最高降5倍，适合大流量长上下文Agent场景降本

  - 推荐系统长用户序列建模可借鉴混合滑动窗口+全局稀疏注意力的设计，平衡局部短期行为和全局长期兴趣的建模精度，降低序列建模开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长轮次多交互Agent场景下，工具返回的长观测结果、多轮对话历史会大幅拉长上下文，现有稀疏注意力方案存在预填充计算量大、KV缓存占用高、长上下文检索精度不足的问题，亟需同时兼顾效率与效果的长上下文注意力架构。

### 方法关键点
- 外层KV Bridging：采用YOCO风格的self-decoder（混合全注意力+滑动窗口注意力）+ cross-decoder（混合全注意力+稀疏注意力）架构，仅将self-decoder全注意力层的隐态投影为cross-decoder全注意力层的KV缓存，预填充阶段跑完self-decoder即可早退，无需执行cross-decoder层
- 内层KV Reuse：在HySparse基础上做两点优化，一是将块级稀疏选择替换为token级选择，在相同注意力预算下提升长上下文检索精度；二是移除稀疏层独立的SWA分支，强制将最近窗口的token加入稀疏选择，兼顾局部建模的同时支持预填充早退

### 关键实验
基于80B-A3B MoE模型，对比HySparse、Hybrid SWA两个基线，轻量post-training后，MRCR-v2、RULER-v2得分较HySparse分别提升11.30、19.81个百分点；1M上下文场景下，预填充FLOPs较HySparse降2.92倍、较Hybrid SWA降5.02倍，KV缓存仅占2.69GB，为HySparse的40%、Hybrid SWA的22%。

**最值得记住的一句话**：针对Agent场景的长上下文优化，可通过跨层跨模块的KV共享设计，在不损失甚至提升效果的前提下大幅降低预填充和KV存储开销。
