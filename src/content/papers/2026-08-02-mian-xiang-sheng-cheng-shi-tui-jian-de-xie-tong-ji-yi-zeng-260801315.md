---
title: Collaborative Memory Augmentation for Generative Recommendation
title_zh: 面向生成式推荐的协同记忆增强框架OMEGA
authors:
- Enze Liu
- Zhen Tian
- Wayne Xin Zhao
affiliations:
- Renmin University of China
- ByteDance
arxiv_id: '2608.01315'
url: https://arxiv.org/abs/2608.01315
pdf_url: https://arxiv.org/pdf/2608.01315
published: '2026-08-02'
collected: '2026-08-04'
category: GenRec
direction: 生成式推荐 · 记忆增强
tags:
- Generative Recommendation
- Memory Bank
- Retrieval Augmentation
- Collaborative Filtering
- Seq2Seq
one_liner: 为生成式推荐引入可插拔协同记忆框架，显式利用跨用户协同信号提升推荐效果
practical_value: '- 可作为可插拔组件直接接入现有T5架构的GenRec基线，无需重构整体流程即可获得10%~23%的核心指标提升，适合快速迭代的电商/内容推荐业务

  - 序列压缩trick可复用：用2~3个可学习query token即可将变长用户行为序列压缩为固定长度embedding，存储开销下降90%以上，同时保留核心语义信息，适合构建亿级规模的用户行为记忆库

  - 检索融合方案可直接落地：目标感知双加权检索（序列相似度+目标item相似度）+门控交叉注意力过滤噪声，仅新增7%的参数量，推理延迟仅提升1%，完全满足线上SLA要求

  - 训练范式可复用：两阶段微调（先冻住backbone对齐交叉注意力，再全参数联合优化），可避免外部记忆引入的语义漂移问题，训练稳定性远高于直接端到端训练'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐（GR）仅基于单用户历史序列建模，全局跨用户协同信号全部压缩在固定模型参数内，存在固有信息瓶颈，在稀疏用户、冷启动、长序列场景下效果受限，需要显式引入外部协同知识补全用户偏好信号。
### 方法关键点
- 三阶段架构OMEGA：① 潜在上下文压缩：输入序列前拼接C个可学习query token，经GR encoder编码后取前C位作为序列压缩表示，大幅降低存储开销；② 目标感知记忆检索：用轻量序列推荐模型（如HSTU）做召回，加权计算序列相似度+候选目标item相似度作为检索得分，提升召回相关性；③ 上下文感知融合：用检索得分生成门控系数过滤噪声记忆，再通过交叉注意力将协同记忆与用户本地序列融合后输入解码器。
- 训练采用两阶段微调：先冻住GR backbone仅优化交叉注意力层对齐语义，再全参数联合优化，避免语义漂移。
### 关键结果
在Amazon 2023、MovieLens-1M等5个公开数据集测试，对比SASRec、TIGER、Pctx等14个SOTA基线：基于TIGER接入OMEGA后NDCG@5最高提升23.68%，基于Pctx接入后NDCG@5最高提升15.38%；仅新增7%参数量，推理延迟仅增1%，记忆银行仅用1%容量即可达到全量99%以上的效果。

最值得记住的一句话：生成式推荐的效果提升不一定需要全量重训，可插拔的外部协同记忆是低开销提效的高性价比路径。
