---
title: From Global to Factor-Wise Expert Composition in Discrete Diffusion Models
title_zh: 离散扩散模型从全局到因子维度的专家组合方法
authors:
- Haozhe Huang
- Yudong Xu
- Abhijoy Mandal
- Alán Aspuru-Guzik
affiliations:
- University of Toronto
- Vector Institute for Artificial Intelligence
- Canadian Institute for Advanced Research (CIFAR)
arxiv_id: '2607.11758'
url: https://arxiv.org/abs/2607.11758
pdf_url: https://arxiv.org/pdf/2607.11758
published: '2026-07-13'
collected: '2026-07-15'
category: Training
direction: 离散扩散模型 · 专家组合优化
tags:
- Discrete Diffusion
- Expert Composition
- Dynamic Routing
- Generative Model
- ARC-AGI
one_liner: 提出离散扩散的FactorDiff因子级组合框架，分因子动态路由专家，效果显著优于全局加权方案
practical_value: '- 多专家融合场景可借鉴分因子路由思路替代全局加权，比如推荐中用户/物品/上下文特征分别路由对应领域专家，降低跨域干扰

  - 离散生成任务（如GenRec的Semantic ID生成、营销文案生成）可将输出拆解为独立因子，每个因子适配最优生成专家，提升生成一致性

  - 扩散模型落地时无需重新训练大模型，通过因子级动态路由即可组合多个小领域专家，降低训练成本覆盖长尾场景'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有离散扩散模型的多专家组合方案仅支持全局逐样本加权，未利用不同专家的空间/功能专长属性，在需要逻辑一致性、空间解耦的复杂任务上性能存在明显瓶颈。
### 方法关键点
提出FactorDiff因子级组合框架，无需修改预训练专家结构：1）将待生成样本拆解为多个独立的小因子（如空间像素、语义维度等）；2）采样过程中动态将每个因子路由到最匹配的对应专家生成。
### 关键结果
在ARC-AGI基准测试中，因子专属路由方案在需逻辑一致性、空间解耦的任务上，性能持续优于复杂的全局标量加权方案，无额外训练成本即可获得稳定提升。
