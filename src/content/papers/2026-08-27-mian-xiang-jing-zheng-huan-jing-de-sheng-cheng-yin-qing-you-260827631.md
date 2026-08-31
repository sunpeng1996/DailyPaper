---
title: 'Beyond the Vacuum: Combinatorial Strategy Selection for Competitor-Aware Generative
  Engine Optimization'
title_zh: 面向竞争环境的生成引擎优化（GEO）组合策略选择框架
authors:
- Vaibhav Sourirajan
- Yao Zhang
- Himanshu Kumar
- Sahil Wadhwa
- Mann Patel
- Amirfarrokh Iranitalab
affiliations:
- Capital One, AI Foundations
arxiv_id: '2608.27631'
url: https://arxiv.org/abs/2608.27631
pdf_url: https://arxiv.org/pdf/2608.27631
published: '2026-08-27'
collected: '2026-08-31'
category: LLM
direction: 生成式搜索引擎优化 · 竞争感知
tags:
- GEO
- Bayesian Optimization
- DPO
- LoRA
- Preference Tuning
one_liner: 提出两阶段竞争感知GEO框架，结合贝叶斯优化与偏好微调适配动态竞争内容环境
practical_value: '- 电商商详页、商品卖点文案优化可直接复用论文提出的15种GEO改写策略组合，针对生成式搜索场景定向提升商品内容的引用优先级，尤其是结构化排版、统计数据补充、简洁性等策略的组合效果远优于单策略

  - 多竞品共存的优化场景可复用论文的硬负样本挖掘方法：基于统计显著性筛选效果差异显著的策略对，再按汉明距离选和最优策略最接近的硬负样本，搭配DPO微调策略选择模型，比固定策略的效果提升18%以上

  - 跨域内容优化场景可借鉴「score-grounded推理迹+SFT+DPO」的微调范式，仅需少量通用领域标注就能实现零样本跨域迁移，论文中在电商数据集上零样本PAWC比SOTA基线高8%以上

  - 做生成式搜索反作弊的团队可参考论文中的GEO策略特征，识别恶意优化的低质内容，规避内容权重作弊，保障搜索结果的公平性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有GEO方法均为孤立优化单条内容，未考虑竞品也在同步做内容优化的真实场景：当大量内容采用相同GEO策略时，单策略的收益会快速衰减，本质是零和博弈，亟需能感知竞争环境的动态策略选择方法。
### 方法关键点
- 两阶段Pipeline：第一阶段采用Bayesian Optimization of Combinatorial Structures（BOCS）在15种改写策略的32768种组合空间中高效搜索最优策略，收集不同组合的内容可见性黑盒观测数据；
- 偏好微调阶段：首先基于Welch's t-test统计显著性+汉明距离做硬负样本挖掘，生成效果差异显著、策略相似度最高的<最优-次优>策略对；其次用教师LLM生成基于文档内容的推理迹（屏蔽BOCS分数特权信息）；最后对学生模型做SFT+DPO微调，仅输入query和全量竞争corpus即可输出最优策略组合。
### 关键实验
在原生geo-bench和新增的带不同竞争强度的geo-benchcomp数据集上，对比15种单策略、AutoGEO、AgenticGEO等17个基线：
- 原生geo-bench上PAWC达32.62，比SOTA AgenticGEO高4.67，达到BOCS理论上限的84%；
- 竞争环境geo-benchcomp上PAWC达29.93，比AgenticGEO高18%以上，竞品优化率从0升至0.8时效果仅下降11.4%，远低于基线的衰减幅度；
- 零样本迁移到电商数据集，PAWC达37.78，比SOTA基线高8%以上。

生成式引擎优化本质是相对竞争问题，孤立优化的收益会随竞品GEO adoption率提升快速衰减，只有感知全量竞争corpus的动态策略选择才能维持稳定收益
