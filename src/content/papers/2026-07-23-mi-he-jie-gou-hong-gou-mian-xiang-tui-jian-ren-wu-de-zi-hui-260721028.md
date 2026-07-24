---
title: 'Bridging the Structural Gap: Adapting Autoregressive Generation for Recommendation'
title_zh: 弥合结构鸿沟：面向推荐任务的自回归生成适配方法
authors:
- Junchao Zeng
- Junzhang Zhu
- Junyang Chen
- Yudong Li
- Wei Liu
- Chengxiang Zhuo
- Zang Li
affiliations:
- Tencent
- Shenzhen University
- Sun Yat-sen University
arxiv_id: '2607.21028'
url: https://arxiv.org/abs/2607.21028
pdf_url: https://arxiv.org/pdf/2607.21028
published: '2026-07-23'
collected: '2026-07-24'
category: GenRec
direction: 生成式推荐 · 自回归语义ID生成优化
tags:
- Generative Recommendation
- Semantic ID
- Autoregressive Generation
- Sequential Recommendation
- Beam Search
one_liner: 提出BARGE生成式推荐框架解决item边界丢失与语义漂移问题，已在腾讯业务落地提效
practical_value: '- 编码侧可直接复用ICA模块：对每个item的多token Semantic ID做跨注意力聚合+门控残差注入，无需修改主模型结构即可提升item级结构感知，参数和推理开销极低

  - 解码侧可复用HPR语义漂移优化：在beam search每一步加轻量化双塔路径打分，无需放大beam size即可减少层级解码漂移，推理 latency 增加不到10%

  - 多通道生成可参考DPD方案：通过OSQ-VAE正交拆分item embedding+两路独立解码+OR融合，在不增加单路推理成本的前提下，大幅提升长尾/冷启动item召回率

  - 工业落地验证充分：这套方案已在腾讯内容推荐场景上线，CTR+0.6%、点击UV+1.34%、阅读时长+1.7%，可直接迁移到电商/内容生成式推荐业务'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于分层Semantic ID的生成式推荐（GR）直接照搬NLP自回归生成范式，存在两个结构性缺陷：一是将每个item的多token语义ID拍平为序列，丢失item边界信息，将item级推荐退化为token级序列建模；二是层级解码时前缀错误会导致语义漂移，一旦进入错误子树就无法召回目标item，单纯放大beam size的方案成本过高，无法落地线上低延迟场景。

### 方法关键点
- **Item Context-Aware Attention (ICA)**：对每个item的多个语义ID token做跨注意力聚合得到item级上下文，通过门控残差网络融合回每个token，在保留原始token信号的同时补全item结构信息
- **Hierarchical Path Reranking (HPR)**：每步解码时计算用户历史全局表征和候选路径累积embedding的余弦相似度，与生成概率加权融合后重排序，无需放大beam size即可修正漂移路径
- **Dual-Path Decoding (DPD)**：用OSQ-VAE将item embedding正交拆分为两个独立子空间，生成两路互补语义ID，两路解码器独立生成后做OR融合，进一步降低单路漂移导致的漏召风险

### 关键结果
在Amazon Beauty、Sports公开数据集上，对比TIGER等SOTA生成式基线，R@10最高提升19.6%；腾讯百万级用户离线测试Hit@5比OneRec高10.2%；线上A/B测试实现CTR+0.6%、点击UV+1.34%、总阅读时长+1.7%的核心指标提升。

> 值得记住的结论：生成式推荐不能直接照搬NLP自回归生成范式，必须针对推荐任务的item级目标和分层语义ID的树状结构做定制化适配。
