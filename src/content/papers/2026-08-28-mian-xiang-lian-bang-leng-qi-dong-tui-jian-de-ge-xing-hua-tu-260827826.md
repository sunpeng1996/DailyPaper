---
title: Personalized and Multi-View Representation for Federated Cold-Start Recommendation
title_zh: 面向联邦冷启动推荐的个性化多视图表示框架
authors:
- Jaehyung Lim
- Wonbin Kweon
- Woojoo Kim
- Junyoung Kim
- Dongha Kim
- Hwanjo Yu
affiliations:
- Pohang University of Science and Technology
- University of Illinois Urbana-Champaign
arxiv_id: '2608.27826'
url: https://arxiv.org/abs/2608.27826
pdf_url: https://arxiv.org/pdf/2608.27826
published: '2026-08-28'
collected: '2026-08-31'
category: RecSys
direction: 联邦推荐 · 冷启动优化
tags:
- Federated Recommendation
- Cold-Start Recommendation
- Multi-View Learning
- Personalized Recommendation
- Privacy Preserving
one_liner: 双边隐私约束下融合个性化生成器与多视图编码的联邦冷启动推荐框架，全面提升冷项推荐效果与公平性
practical_value: '- 冷启动场景可直接复用多视图编码器+item自适应门控的设计，搭配正交损失降低视图冗余、负载均衡损失避免视图塌陷，显著提升属性特征的语义表征能力

  - 隐私合规/联邦推荐场景可复用「协同与属性知识融合为单一交换表征」的设计，消除客户端对齐正则，降低跨端通信开销，同时避免原始属性/交互数据泄露

  - 个性化冷启可复用轻量线性+激活的用户专属表征生成器设计，通过闭式解避免迭代优化，兼顾个性化效果与工程落地效率

  - 长尾用户/小众需求推荐场景可复用个性化表征逻辑，降低零得分用户占比，提升用户级公平性，减少小群体推荐效果劣化'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
联邦推荐（FedRec）满足了用户交互数据不出域的隐私合规要求，但现有方案默认物品池固定，未覆盖新商品持续上架的冷项实战场景；同时受双边隐私约束（服务器无权限访问用户交互、客户端无法获取商品原始属性），现有方案存在三大缺陷：个性化缺失、异构语义压缩进单嵌入空间导致的组合性失效、协同与属性表征分别传输对齐带来的训练通信效率低下。
### 方法关键点
- 服务端为每个用户训练轻量化个性化表征生成器，采用闭式解求解避免迭代优化，支持服务端存参/客户端卸载存参两种部署模式，平衡存储与通信开销
- 全局多视图编码器搭配item自适应门控，通过正交损失降低视图冗余、负载均衡损失避免视图塌陷，精准捕获异构属性的互补语义
- 将协同知识与属性知识融合为单一交换item表征，客户端无需额外对齐正则，仅需传输单份表征矩阵大幅降低通信开销
- 原生支持(ε, δ)-LDP本地差分隐私，适配高隐私要求场景
### 关键结果
在CiteULike、3个不同规模XING公开数据集上，对比8个SOTA基线，冷项推荐相对最优基线最高提升7.56%；零得分用户占比最多降低4.3个百分点，用户级公平性（Gini系数）显著优化；加入LDP隐私保护后效果降幅远低于同类基线。
> 最值得记住：联邦冷启的核心瓶颈不是隐私约束，而是全局表征的个性化不足与语义表征能力的缺失
