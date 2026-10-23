---
title: Bezier-Guided Adaptive Flow for Cross-domain Sequential Recommendation
title_zh: 贝塞尔引导的自适应流跨域序列推荐框架
authors:
- Ziang Lu
- Yu Zhang
- Xinzhe Jiang
- Lei Sang
- Yiwen Zhang
affiliations:
- Anhui University, China
arxiv_id: '2610.30825'
url: https://arxiv.org/abs/2610.30825
pdf_url: https://arxiv.org/pdf/2610.30825
published: '2026-10-22'
collected: '2026-10-23'
category: RecSys
direction: 跨域序列推荐 · 个性化知识迁移
tags:
- Cross-domain Recommendation
- Sequential Recommendation
- Flow Matching
- LLM
- Bezier Curve
one_liner: 提出贝塞尔引导的自适应流框架，实现用户粒度跨域序列推荐的个性化知识迁移
practical_value: '- 跨域推荐场景可复用「LLM推理用户分域兴趣→计算跨域兴趣重叠度→个性化控制迁移强度」的链路，解决全局对齐导致的负迁移问题

  - 贝塞尔曲线+残差流的语义迁移范式可替代传统线性插值/特征拼接，适配需要平滑渐进特征转换的跨域、冷启动场景

  - 双域预训练阶段可直接复用profile对齐、item语义对齐、CORAL正则三个辅助损失，快速构建分布一致的跨域语义空间

  - 基于推荐任务梯度构造流匹配监督信号的方法无需额外标注，适合工业界低资源落地需求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
跨域序列推荐旨在通过跨域知识迁移缓解数据稀疏和冷启动问题，但现有方案普遍采用全局对齐或粗粒度迁移策略，忽略了用户跨域偏好一致性的个体差异，容易引入无关信息导致负迁移，缺少用户粒度的迁移强度控制和语义自适应调整机制。

### 方法关键点
- 先用LLM推理用户分域兴趣画像，通过ID-文本双塔结构做双域预训练，加入profile对齐、item语义对齐、CORAL正则三个辅助损失，构建分布一致的统一跨域语义空间
- 基于用户跨域兴趣原型的JS散度计算偏好重叠度，为每个用户预测个性化迁移horizon，控制知识迁移的程度
- 以用户画像为控制点构造二次贝塞尔曲线作为迁移的几何参考，学习状态自适应的残差流动态修正迁移轨迹，加入任务梯度引导的流匹配损失和轨迹平滑正则优化

### 关键结果
在亚马逊公开数据集Movie-Book、Sport-Cloth上对比17个SOTA基线（含单域、传统跨域、扩散、LLM增强类），HR@10、NDCG@10相对最优基线提升3.91%~16.62%，其中电商类Sport-Cloth场景两个域的指标提升均超过14%。

最值得记住的一句话：跨域知识迁移不能搞「一刀切」，基于用户兴趣匹配度的个性化动态调整是降低负迁移、提升效果的核心。
