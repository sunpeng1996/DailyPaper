---
title: 'GistRank: Gist-Compressed Listwise Ranking with Large Language Models'
title_zh: GistRank：基于要点压缩的大模型列表式重排序算法
authors:
- Guo Chen
- Wenhan Liu
- Reed Li
- Qianwen Ma
- Yu Lu
- Haibo Shi
- Bingbing Xu
- Junjie Huang
affiliations:
- Southwest University
- Renmin University of China
- Yuanbao Team, Tencent
- Institute of Computing Technology, Chinese Academy of Sciences
arxiv_id: '2610.39610'
url: https://arxiv.org/abs/2610.39610
pdf_url: https://arxiv.org/pdf/2610.39610
published: '2026-10-29'
collected: '2026-10-30'
category: RecSys
direction: 列表式重排序 · gist软压缩优化
tags:
- ListwiseRanking
- GistCompression
- LLMReranking
- EfficiencyOptimization
- InformationRetrieval
one_liner: 通过三阶段训练的gist软压缩实现高效listwise排序，较全量方案提速14倍，nDCG@10仅低0.89
practical_value: '- 电商/搜索重排序场景可直接复用K=4 gist token的软压缩方案，单文档压缩为固定长度软token，比BM25硬摘要多保留6~7分nDCG效果，rank阶段上下文长度降低6.8倍，线上延迟更稳定可控

  - 三阶段训练范式可低门槛迁移：第一阶段无监督预训练压缩能力，第二阶段用用户点击/未点击的隐式反馈做pairwise微调增强判别性，第三阶段适配listwise目标，额外标注成本极低

  - 线上部署可预计算离线商品/内容的gist KV cache，多query复用进一步降本，rank阶段耗时仅占端到端总耗时的7%，核心优化点可放在压缩阶段

  - 超参选择可直接复用K=4的最优配置，为效率-效果tradeoff的拐点，无需额外大量调参'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM原生listwise排序效果优于pointwise/pairwise方案，可捕捉跨候选对比信号，但输入长度随候选数、文档长度线性增长，推理延迟极高；滑动窗口方案存在重复编码开销，硬压缩会丢失排序所需的细粒度判别信息，现有通用gist压缩未针对排序的相对偏好信号优化，效果掉点显著。

### 方法关键点
- 三阶段训练范式：
1. 预训练阶段：半双向注意力约束下，用海量搜索query-passage对做无监督训练，让gist token充分吸收文档信息，仅通过gist预测对应query
2. 判别性微调阶段：用搜索引擎点击/未点击的pairwise隐式反馈训练，强化gist对正负样本的区分能力，注入排序所需的判别信号
3. listwise适配阶段：query前置到passage前生成query感知的gist，注入各层KV cache做非自回归排序，用ListMLE损失优化排序目标
- 单文档压缩为K=4个gist token，rank阶段直接复用压缩后的KV做打分，无需重新编码全文

### 关键结果
在TREC DL19/20、5个BEIR子集上测评，平均nDCG@10达59.17，仅比最强全上下文基线低0.89；端到端P50延迟为1625ms（DL19），较全文本one-shot排序提速14.05倍，较滑动窗口方案提速26.65倍；rank阶段耗时仅占总耗时的7%。

**最值得记住的一句话**：针对排序任务优化的gist软压缩可在几乎不损失效果的前提下大幅降低listwise重排序延迟，K=4是效率与效果的最优拐点。
