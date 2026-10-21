---
title: Neighborhood-Aware Unlearning for Generative Recommendation
title_zh: 面向生成式推荐的邻域感知高效遗忘方法
authors:
- Pierre Lubitzsch
- Yubao Tang
- Maarten de Rijke
- Sebastian Schelter
affiliations:
- TU Berlin
- University of Amsterdam
- BIFOLD
arxiv_id: '2610.27232'
url: https://arxiv.org/abs/2610.27232
pdf_url: https://arxiv.org/pdf/2610.27232
published: '2026-10-19'
collected: '2026-10-21'
category: GenRec
direction: 生成式推荐 · 模型遗忘优化
tags:
- GenRec
- Unlearning
- Semantic ID
- Sequential Recommendation
- Machine Unlearning
one_liner: 针对SID类生成式推荐的遗忘溢出问题，提出邻域管控的高效遗忘方案，效果接近重训且保留95%以上效用
practical_value: '- 现有SID-based GenRec业务处理spam删除、用户隐私删除请求时，可直接复用NAU的损失框架，无需改动原模型和SID体系，迁移成本极低，运行效率比重训高3个数量级

  - 邻域概率管控的思路可直接适配业务场景：spam清理场景设λn>0，保留邻域合法物品的推荐效果；用户请求删除敏感物品时设λn<0，连带抑制同类敏感品曝光

  - 评估GenRec遗忘效果不能只看全局NDCG，必须补充目标物品邻域的效用、曝光指标，避免全局指标正常但相关品类推荐效果隐性下降的问题

  - NAU的超参在不同数据集、不同tokenizer下泛用性强，无需针对每个场景反复调参，适合工业界落地'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前基于Semantic ID（SID）的生成式推荐（GenRec）已在工业界落地，但传统遗忘方法存在严重溢出问题：由于语义相近的物品共享SID token，删除spam互动、响应用户隐私删除请求时，更新会波及邻域物品，全局NDCG等指标看似正常，但邻域推荐效用会出现大幅下降，而全量重训成本过高，无法支撑高频删除需求。
### 方法关键点
- 设计item级完整SID生成概率损失，对齐遗忘请求的物品粒度，替代原生token级训练损失
- 组合三类基础损失：retain集修复保留全局推荐效用、forget集梯度上升消除目标物品的训练影响、对比分离项避免目标物品在非关联场景下仍被高优排序
- 新增邻域概率管控项，通过调整权重λn的正负：spam删除场景设λn>0，保留邻域合法物品的生成概率；敏感品删除场景设λn<0，连带抑制邻域同类物品的曝光
### 关键实验结果
基于TIGER GenRec backbone，在亚马逊Beauty、Sports、Toys三个公开数据集、4种SID tokenizer下测试，对比7个主流遗忘基线：spam删除场景下，保留95%以上的重训NDCG@10，目标物品曝光与重训的差值比最优基线低30%以上，邻域效用比Forget+Repair基线高21个百分点，运行速度比重训快3个数量级；敏感品删除场景下，请求用户的敏感品曝光降低40%，且不影响其他用户的推荐效果。
### 核心结论
SID-based GenRec的遗忘效果不能仅依赖全局指标评估，必须显式管控目标物品邻域的概率重分布，才能避免隐性的局部推荐效用损失。
