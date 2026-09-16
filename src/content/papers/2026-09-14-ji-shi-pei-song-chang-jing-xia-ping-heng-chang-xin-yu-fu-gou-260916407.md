---
title: 'Balancing Trial and Reorder: A Hybrid Sequential Transformer-GBDT Ranker for
  On-Demand Delivery'
title_zh: 即时配送场景下平衡尝新与复购的Transformer-GBDT混合排序系统
authors:
- Marcel Kurovski
- Attila Nagy
- Steffen Klempau
- Aleksandr Fedintsev
affiliations:
- Wolt (DoorDash, Inc.)
arxiv_id: '2609.16407'
url: https://arxiv.org/abs/2609.16407
pdf_url: https://arxiv.org/pdf/2609.16407
published: '2026-09-14'
collected: '2026-09-16'
category: RecSys
direction: 排序系统 · 多目标平衡与跨域统一
tags:
- Sequential Recommendation
- Learning to Rank
- Cross-domain Recommendation
- Transformer
- GBDT
- Multi-objective Optimization
one_liner: 提出Transformer-GBDT混合通用门店排序模型，统一多领域排序，平衡尝新复购并落地Wolt生产
practical_value: '- 架构选型可直接复用：Transformer做用户序列建模输出logit作为GBDT的输入特征，既充分利用长序列行为信号，又保留树模型对强规则/上下文特征的适配性，比端到端大模型稳定性更高、推理延迟更低，适合工业级排序场景落地。

  - 探索利用平衡技巧可迁移：训练时给尝新样本设置更高权重，通过调整w_new/w_rec的比值即可直接拉取尝新-复购的帕累托前沿，无需修改模型结构，业务上要提升新商家/新品曝光时可直接通过该系数快速调优，配合YetiRank
  Pairwise损失可定向提升top排序的NDCG效果。

  - 跨域模型统一方案可参考：用共享Transformer建模全领域用户行为，下游接领域专属GBDT排序器，既能实现跨域行为信号迁移，又适配不同领域的特征差异，可大幅降低维护多套垂直领域排序模型的运维成本。

  - 工程实现trick：Transformer单次请求前向生成全候选集logit，再通过gather操作取对应候选的分数，避免每个候选重复计算，可大幅降低推理延迟；每日重训练解决Transductive类embedding的新商家/新地域冷启动问题，适配本地生活动态候选集场景。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
即时配送平台的门店排序需同时满足用户复购熟店的需求与探索新店的预期，还要适配本地动态候选集（配送范围、实时运力、营业时间等约束），原生产环境分餐饮、零售维护4套独立排序模型，运维成本高，且难以平衡尝新和复购的多目标冲突。

### 方法关键点
- 两阶段混合架构：第一阶段用基于BERT4Rec改造的双向Transformer（仅掩码最近一次购买做预测）建模用户历史购买序列，输出全门店预测logit；第二阶段GBDT排序器将Transformer logit作为特征之一，融合门店属性、上下文、用户-门店交互特征做最终排序，下游分餐饮、零售两个领域专属GBDT适配特征差异。
- 多目标调优：Transformer训练时给尝新、冷启动、复购样本设置权重`w_new > w_cs > w_rec`，GBDT阶段采用优化NDCG的YetiRank Pairwise损失，通过调整`w_new/w_rec`比值可直接调节尝新与复购的trade-off。
- 跨域统一：Transformer共享全领域用户行为序列训练，餐饮与零售的行为信号可互相迁移，解决跨域用户冷启动问题，将原4套独立排序模型合并为1套通用架构。

### 关键结果
离线相比原生产模型，尝新MRR提升12%~30%，5/6国家复购MRR略有下降但全局CVR无统计显著下跌；线上A/B测试V1版商家尝新率+5.5%、全局CVR+0.16%，V2版尝新率再+0.45%，跨域V3版零售商家尝新率再+1.31%，全链路p99延迟60ms，替代原4套模型大幅降低运维成本。

**最值得记住的一句话**：工业排序无需盲目上端到端大模型，Transformer做序列特征提取+树模型做最终排序的混合架构，兼顾效果、可解释性、延迟与业务调优灵活性，是落地性价比极高的方案。
