---
title: 'Once Generated, Ranked: End-to-End Generative Slate Recommendation with Unified
  Semantic-Collaborative IDs'
title_zh: 基于统一语义协同ID的端到端生成式Slate推荐框架OGR
authors:
- Yang Hu
- Jiayi Guo
- Jingui Ma
- Ning Li
- Jiangling Qin
- Yanming Li
- Yang Deng
- Xiaoshuang Chen
- Kaiqiao Zhan
affiliations:
- Kuaishou Technology
- Peking University
- Nanjing University
arxiv_id: '2608.17613'
url: https://arxiv.org/abs/2608.17613
pdf_url: https://arxiv.org/pdf/2608.17613
published: '2026-08-18'
collected: '2026-08-19'
category: GenRec
direction: 生成式推荐 · Semantic ID 端到端Slate推荐
tags:
- Generative Recommendation
- Semantic ID
- Slate Recommendation
- Listwise Optimization
- Preference Alignment
one_liner: 提出OGR端到端生成式slate推荐框架，统一语义协同ID与列表级规划，直接输出有序推荐序列
practical_value: '- SID构造可复用TUSID设计：MLLM多模态特征+品牌/类目/供需标签的门控交叉注意力融合，搭配CountSketch加权局部共现的协同信号注入，根据物品交互用户数动态调整协同信号权重，天然适配冷启场景

  - 生成式slate推荐可采用列表级偏好规划+位置级SID流水线解码架构，将序列依赖深度从O(KD)降至O(K+D)，兼顾列表级排序效果和推理效率，无需走传统多级召回排序链路

  - 训练可叠加双监督信号：曝光序列保持分布拟合，反馈序列注入用户偏好；后训阶段采用主业务奖励（如GMV、有效观看）+辅助奖励（如多样性）的校准机制，搭配保守策略优化，避免生成结果偏离既有分布，降低上线风险

  - 快手全链路落地验证了生成式推荐的工业可行性，可复用其偏好对齐思路降低上线试错成本'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有slate推荐依赖召回-排序级联链路，优化空间受候选池限制，且多阶段目标不一致；现有基于Semantic ID的生成式推荐要么SID缺少推荐感知的语义+协同信号融合，要么用Next Token Prediction优化，和slate级列表优化目标不匹配，无法直接生成有序推荐列表。

### 方法关键点
- 设计TUSID语义协同ID构造框架：先通过MLLM多模态特征和品牌/类目/供需标签做门控交叉注意力融合，得到推荐感知语义表征；再用CountSketch压缩距离加权的用户行为局部共现信息，根据物品的 distinct 交互用户数动态调整协同信号权重，最后通过RQ-KMeans量化为层级SID
- 提出GL2P全局列表级偏好规划架构：先对用户历史交互SID编码，再通过因果掩码Transformer做列表级偏好规划，每个位置的偏好表征生成后即可流水线式解码对应SID，无需等上一个位置的SID完全生成，大幅降低推理延迟；训练用曝光序列+反馈序列双监督，同时拟合曝光分布和用户偏好
- 新增SPA slate级偏好对齐后训阶段：基于主业务奖励和辅助奖励做校准，主辅奖励方向一致时才叠加辅助奖励，再用保守策略优化，避免生成结果偏离既有分布

### 关键结果
离线在快手工业数据集和公开KuaiRec数据集上，NDCG@5相对baseline分别提升48.2%、27.2%；推理吞吐量比TIGER、OneRec的beam解码模式提升2.4倍以上；线上A/B测试在快手3%流量下，有效观看提升1.120%，评论提升2.954%，点赞提升0.505%。

### 最值得记住的一句话
生成式slate推荐不需要沿用传统「先生成候选再排序」的级联思路，通过推荐感知SID、列表级规划和流水线解码，可实现「生成即排序」的端到端优化，兼顾效果、效率和上线稳定性。
