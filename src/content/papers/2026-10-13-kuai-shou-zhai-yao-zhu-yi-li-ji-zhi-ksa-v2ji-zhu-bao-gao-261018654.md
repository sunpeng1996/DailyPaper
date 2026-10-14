---
title: Kwai Summary Attention V2 Technical Report
title_zh: 快手摘要注意力机制KSA V2技术报告
authors:
- OneRec Team
- Chenglong Chu
- Guohong Mu
- Guowang Zhang
- Hao Peng
- Hui Wang
- Jian Liang
- Jiangxia Cao
- Jiao Ou
- Jiaxin Deng
affiliations:
- Kuaishou
arxiv_id: '2610.18654'
url: https://arxiv.org/abs/2610.18654
pdf_url: https://arxiv.org/pdf/2610.18654
published: '2026-10-13'
collected: '2026-10-14'
category: LLM
direction: LLM长上下文推理 · KV缓存与注意力优化
tags:
- KV Cache
- Long Context LLM
- Attention Optimization
- Inference Acceleration
- Sparse Attention
one_liner: 复用已有Summary token，通过C-KSA、S-KSA模块实现KV缓存压缩与推理加速，长上下文性能损失极低
practical_value: '- 电商Agent/生成式推荐场景的长上下文LLM推理，可直接复用C-KSA分层压缩思路，在不降低用户历史、商品信息召回准确率的前提下，降低KV缓存占用，提升单卡并发量

  - S-KSA的Summary-guided块级稀疏注意力方案，可迁移到长序列用户行为建模的召回/排序模块，用分层摘要做粗筛后再精准匹配，降低长序列计算开销

  - 现有已训练的Hybrid KSA类模型可直接复用论文的轻量化适配方案（仅训练新增模块参数）升级，无需全量重训，业务迭代成本极低'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
长上下文LLM推理中KV缓存随序列长度线性增长、prefill阶段计算量呈平方级增长，原有Hybrid KSA架构存在压缩粒度固定、全注意力层计算冗余的痛点，无法同时兼顾长上下文性能和推理效率。
### 方法关键点
- **C-KSA**：将每km个连续的Summary KV聚合为层内Meta条目，分层压缩不改变原有Summary传输粒度，支持层间自定义压缩比，新增参数仅需少量适配训练
- **S-KSA**：复用现有Summary生成块级路由索引，仅召回Top-K相关原始文本块做注意力计算，避免全量注意力开销
- 完全兼容原有Hybrid KSA的3:1层布局，可通过轻量化适配直接升级已训模型，无需全量重训
### 关键结果
基于1.9B MHA、4B GQA两个Hybrid KSA backbone验证，对比Hybrid KSA baseline：128K序列下，KV缓存大小降低40.4%，prefill throughput提升1.51倍，decode throughput提升1.27倍，RULER长上下文平均准确率仅下降0.22pp，通用能力指标波动小于3pp。
### 核心结论
复用已有Summary token同时承担记忆压缩和稀疏索引两个角色，是兼顾长上下文性能与推理效率的低成本方案。
