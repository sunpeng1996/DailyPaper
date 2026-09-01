---
title: 'ICEGR: An Intent-Coherent End-to-End Generative Retrieval Framework for E-commerce
  Search'
title_zh: 面向电商搜索的意图一致性端到端生成式检索框架ICEGR
authors:
- Jiayi Tuo
- Hehan Li
- Dongjun Fu
- Xin Lu
- Ling Zhuang
- Fuwei Zhang
- Meifang Li
- Peizhi Xu
- Hanmeng Liu
- Shuanglong Li
affiliations:
- 中国科学技术大学
- 百度
- 北京航空航天大学
- 中国人民大学
arxiv_id: '2608.29652'
url: https://arxiv.org/abs/2608.29652
pdf_url: https://arxiv.org/pdf/2608.29652
published: '2026-08-30'
collected: '2026-09-01'
category: GenRec
direction: 生成式检索 · Semantic ID全链路意图对齐
tags:
- Generative Retrieval
- Semantic ID
- E-commerce Search
- Preference Optimization
- Synthetic Query
one_liner: 全链路对齐query意图的电商生成式检索框架，线上GMV提升7.53%
practical_value: '- SID构造可直接复用思路：在静态商品表征基础上，融合query共点击图传播信息、商品历史关联query的加权表征后再量化，大幅提升Semantic
  ID与用户检索意图的匹配度

  - 长尾商品召回提升trick：基于商品结构化属性生成多粒度合成query，先做合成query到SID的SFT，再用真实query微调，可补全长尾商品的监督信号，低曝光商品Recall最高提升36%

  - 偏好优化避免意图漂移方案：做DPO时仅在语义相关的候选间构造偏好对，根据正负对综合评分差动态调整DPO温度系数，可在提升GMV的同时不损失query相关性

  - 工程落地参考：0.5B参数的生成式检索模型配beam size 50，在L20 GPU集群可支撑2200QPS、156ms平均延迟，满足电商搜索的生产级性能要求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式检索有望解决电商搜索多阶段级联架构的召回天花板问题，但现有方案全链路无法保持query意图一致性：静态Semantic ID仅依赖商品属性无法编码检索意图关联，低曝光长尾商品缺少真实query交互监督导致召回效果差，业务导向的偏好优化容易向高价值/热门商品偏移，破坏query-商品相关性，难以落地到工业场景。

### 方法关键点
- 意图感知SID构造：基于点击日志预训练对齐query-商品表征，引入共点击商品图传播挖掘意图关联的商品关系，融合商品对应的历史点击query表征后，通过残差KMeans量化生成分层SID
- 合成query增强统一SFT：从商品SPU、品牌、类目、属性等结构化信息生成多粒度合成query，先基于合成query-to-SID任务训练覆盖全量商品，再用真实交互query微调对齐用户真实检索分布
- 相关性校准偏好优化：偏好对仅在语义相关候选中构造，根据正负对的相关性+业务指标综合评分差动态调整DPO权重，保留SFT辅助损失，平衡业务收益与query相关性

### 关键实验
离线基于百度12.8M query、14.6M商品的3个月搜索日志，对比生产级生成式检索基线，Recall@20提升21.7%，NDCG@20提升26.6%；线上A/B测试20%流量，CTR提升3.52%，订单量提升15.96%，GMV提升7.53%；0.5B参数模型在L20 GPU集群上实现平均延迟156ms、峰值2200QPS，满足生产要求。

### 核心结论
生成式检索的落地收益不仅来自架构统一，更要保证query意图在SID构造、监督训练、偏好优化全链路的一致性，才能将离线相关性提升转化为线上业务增长。
