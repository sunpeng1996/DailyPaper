---
title: 'Nearest but Not Dearest: Shared Curator-Feedback Infrastructure for Content-Only
  Search and Recommendation'
title_zh: 面向纯内容搜索推荐的统一策展人反馈共享基础设施
authors:
- Matt Sandler
affiliations:
- Feed.fm, San Francisco, USA
arxiv_id: '2609.30568'
url: https://arxiv.org/abs/2609.30568
pdf_url: https://arxiv.org/pdf/2609.30568
published: '2026-09-24'
collected: '2026-09-28'
category: RecSys
direction: 统一搜索推荐 · 策展人反馈优化
tags:
- Unified Search and Recommendation
- Curator Feedback
- Content-only Retrieval
- Music Recommendation
- Embedding Reweighting
one_liner: 将检索失败拆分为音效/上下文两类路由到共享层处理，同时优化搜索推荐两路效果
practical_value: '- 召回错误可按「语义匹配类/业务规则类」拆分，前者路由到embedding重权/重训层，后者路由到前置规则过滤层，无需所有错误都依赖模型迭代，大幅降低优化成本

  - 搜索和推荐底层共享召回、表示层时，单路收集的反馈可自动同步到另一路，无需维护两套反馈回路，尤其适合冷启动、用户行为稀疏的业务场景

  - 无用户行为信号时，小批量专业标注（本文仅4名策展人、1200条标注）即可驱动可落地的效果提升，优先优化规则类错误的ROI远高于模型类优化'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
纯内容驱动的搜索推荐场景（如冷启动内容池、版权受限的音乐/音频平台、用户行为稀疏的垂直业务）无法依赖交互信号优化，仅靠预训练embedding余弦相似度召回的结果有近40%不符合专业审核要求，其中大量错误与内容本身的语义匹配度无关，是业务规则类冲突，且此前无统一方案同时优化搜索、推荐两条业务线的效果。

### 方法关键点
- 将召回错误拆分为两类：音效/语义匹配错误（Csound，包括风格、节奏、情绪不匹配，可通过表示层优化解决）、上下文规则错误（Cctx，包括语言、版权、节日属性、内容分级等与语义匹配无关的问题，可通过规则过滤解决）
- 反馈路由逻辑：Cctx类错误直接更新候选生成层的SQL规则过滤器，Csound类错误生成三元组训练线性投影重权头，冻结预训练CLAP embedding仅微调512维线性层，加入恒等正则防止小样本过拟合
- 两类优化都落在搜索、推荐分流前的共享层，一次反馈同时生效于语义搜索、标签搜索、种子推荐、艺术家推荐四类入口

### 关键结果
基于生产环境5.7万首版权曲库，用4名专业策展人标注的1200条召回结果评估：
- 基线（原始CLAP余弦召回）拒答率38.17%，上线双优化后拒答率降至28.83%，相对下降24.5%，统计显著（$p=2.2×10^{-6}$）
- 规则过滤贡献4.08pp的拒答率下降，模型重权贡献5.25pp的下降，两类优化效果接近，但规则开发成本仅为模型的数十分之一

### 核心洞见
不要把所有召回错误都丢给模型迭代解决，规则类优化的ROI远高于表示层优化，统一底层的搜索推荐架构可实现一次反馈多路生效
