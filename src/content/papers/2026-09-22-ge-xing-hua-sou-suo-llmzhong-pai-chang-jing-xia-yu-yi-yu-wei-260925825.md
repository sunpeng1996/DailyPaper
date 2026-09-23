---
title: Robust Fusion of Semantic and Behavioural Signals for LLM Reranking in Personalised
  Search
title_zh: 个性化搜索LLM重排场景下语义与行为信号的鲁棒融合
authors:
- Aleksandr V. Petrov
- Nathan Stein
- Erik Lybecker
- Emma Schüldt
- Daniel Lazarovski
- Hugues Bouchard
- Mounia Lalmas
affiliations:
- Spotify
arxiv_id: '2609.25825'
url: https://arxiv.org/abs/2609.25825
pdf_url: https://arxiv.org/pdf/2609.25825
published: '2026-09-22'
collected: '2026-09-23'
category: RecSys
direction: LLM重排 · 行为信号鲁棒融合
tags:
- Cross-Encoder
- Reranking
- Behavioural Signal
- Cold Start
- Personalized Search
one_liner: 提出双样本特征dropout训练策略，解决LLM重排注入行为信号后的长尾冷启性能衰减问题
practical_value: '- 结构化行为特征（如CTR、历史转化率、query-item匹配率）注入LLM重排prompt时，先离散为very_low/medium/very_high等序数级文本token，无需修改模型架构，生产兼容度高

  - 训练时采用双样本特征dropout策略：每个样本同时生成带行为特征和不带行为特征的两个prompt，加权计算loss，α取0.5左右即可平衡头部性能与长尾/冷启鲁棒性，推理链路无任何额外开销

  - 评估注入强特征的LLM重排模型时，必须新增「特征移除诊断评估」+按流量头/尾/冷启分桶，避免只看整体指标掩盖长尾性能衰减的隐性问题

  - 电商搜索/推荐场景可直接复用该方案解决统计特征稀疏下的LLM重排退化问题，无需额外做冷启特征补全'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
个性化搜索LLM重排需同时融合语义匹配、用户上下文和历史行为信号，但直接把点击率、历史交互成功率这类强行为特征注入prompt会导致模型shortcut learning，过度依赖统计特征，在长尾query、冷启物品这类行为特征稀疏/缺失的场景性能大幅下降，工业界亟需兼顾头部性能和长尾鲁棒性的信号融合方案。

### 方法关键点
- 行为特征（QSS，query-item-国家维度的历史搜索成功率）离散为5档序数文本token注入prompt，无需修改LLM架构，可直接落地生产
- 采用双样本特征dropout训练：每个训练样本同时构造带QSS（x+）和删QSS（x-）两个prompt，共享标签，loss为两个样本交叉熵的加权和，α控制带特征样本的权重
- 推理阶段仅用单模型单前向，和普通重排链路完全一致，无额外 overhead

### 关键实验
基于Spotify 100万训练/1万评估的搜索交互日志，对比无QSS基线、直接注入QSS的基线模型；直接注入QSS全量流量NDCG@7提升13.3%，但QSS缺失场景性能下降4.3%；采用α=0.5的双样本训练后，全量流量NDCG@7仍保持13.3%的提升，QSS缺失场景性能仅下降0.5%，相对直接注入方案提升4%；线上AB测试两种QSS感知方案均提升搜索成功率约2%，冷启物品场景双样本训练比直接注入方案方向上有0.75%的优势。

### 核心结论
强行为特征注入LLM重排时，需同步评估特征存在/移除两类场景的性能，双样本特征dropout训练可在不改动推理链路的前提下兼顾头部收益与长尾冷启鲁棒性。
