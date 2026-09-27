---
title: 'OneTrans-V2: Unifying Retrieval, Pre-rank, and Fine-rank with One Transformer
  in Industrial Recommender'
title_zh: OneTrans-V2：用单个Transformer统一工业推荐召回预排精排全级联
authors:
- Hannan Cao
- Jun Guo
- Haolei Pei
- Zhaoqi Zhang
- Tianyu Wang
- Ziyang Wang
- Youchen Sun
- Yue Xue
- Yucheng Mao
- Lintao Yan
affiliations:
- ByteDance
arxiv_id: '2609.28589'
url: https://arxiv.org/abs/2609.28589
pdf_url: https://arxiv.org/pdf/2609.28589
published: '2026-09-23'
collected: '2026-09-27'
category: RecSys
direction: 工业推荐 · 全级联架构统一
tags:
- MoE
- Generative Retrieval
- Cascade Recommendation
- Semantic ID
- Knowledge Distillation
one_liner: 用单个Transformer统一推荐三级级联，实现计算复用、联合优化与多目标整合
practical_value: '- 架构层面可复用级联统一思路：只编码1次用户行为序列作为共享上下文，各阶段附加专属token和参数，既能减少重复计算，又保留各阶段的特征定制能力，适合存量级联架构迭代

  - 多目标召回可借鉴DCGR设计：在生成Semantic ID前增加决策前缀（如转化、客单价、新品偏好等），通过在线调整偏移量即可切换业务目标，无需新增独立召回通道，大幅降低多目标召回的运维成本

  - 训练效率优化可直接复用SNT方案：按用户聚合样本，单次编码全量行为序列，多个曝光/阶段复用编码结果，可获得4.4倍训练加速，适合长序列推荐大模型训练场景

  - 大模型扩缩容可复用μP+MoE组合：用稀疏MoE扩容模型容量不增加激活计算量，结合μP参数化规则，无需逐次调整超参即可稳定扩缩模型规模，降低大模型迭代成本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐系统传统召回、预排、精排三级级联各阶段独立训练部署，存在重复编码用户序列、优化目标孤立、工程迭代成本高、模型容量分散等问题；之前的单阶段统一方案未覆盖全级联，端到端生成式推荐又会损失精排阶段的丰富特征收益，亟需兼顾级联保留和架构统一的方案。
### 方法关键点
- 级联统一架构：将三阶段作为单个因果Transformer的三个任务，用户行为序列编码为共享上下文，各阶段附加专属token，用阶段可见性掩码隔离跨阶段token，避免特征干扰，同时支持联合训练和精排到预排的内置知识蒸馏
- 多目标统一召回DCGR：生成Semantic ID前先预测包含转化等级、客单价、新品偏好、广告属性的决策前缀，推理时通过调整业务偏移量即可引导生成符合不同目标的物品，无需新增召回通道
- 高效训练与扩容：用稀疏MoE扩展主干容量，结合μP参数化保证不同规模模型训练稳定性；提出Sequence-Native Training（SNT）按用户聚合样本，单次编码行为序列多曝光复用，训练加速4.4倍
### 关键结果
在字节电商大规模工业推荐系统全级联落地，相比原有级联架构，GMV提升9.74%，相同硬件下QPS达原架构的3.2倍；离线召回HR@10提升6.2%，预排/精排AUC平均提升2.1%。
> 推荐级联统一的核心是拆分可共享的用户上下文计算和阶段专属的候选建模，而非强行替换原有级联的业务逻辑。
