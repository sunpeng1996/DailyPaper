---
title: Fine-Grained Action Recognition with Cross-Attentive Latent Sparse Experts
title_zh: 基于交叉注意力隐式稀疏专家的细粒度动作识别
authors:
- Imtiaz Ul Hassan
- Tasweer Ahmad
- Nik Bessis
- Ardhendu Behera
affiliations:
- Edge Hill University
arxiv_id: '2608.13458'
url: https://arxiv.org/abs/2608.13458
pdf_url: https://arxiv.org/pdf/2608.13458
published: '2026-08-13'
collected: '2026-08-14'
category: Other
direction: 细粒度动作识别 · 多模态融合稀疏MoE
tags:
- Fine-grained Action Recognition
- Mixture-of-Experts
- Cross-Attention
- Multimodal Fusion
- Sparse Routing
one_liner: 推出跨模态融合+稀疏MoE的FineX框架，无文本监督/大模型预训练下实现细粒度动作识别SOTA
practical_value: '- 多模态特征融合可借鉴pairwise cross-attention对称信息流交换方案，避免单模态关键信息丢失，适配搜索推荐场景下用户/物品多模态特征融合需求

  - 稀疏MoE路由可参考「按内容选择共享专家+负载均衡正则」的设计，有效提升长尾分布场景下的分类/预测精度

  - 无需大模型预训练/文本监督的细粒度分类思路，可直接迁移到电商细粒度商品分类、用户细粒度行为识别、短视频内容标签化等业务场景'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
细粒度人体动作识别（FHAR）需区分视觉高度相似的动作，差异仅体现在肢体配置、时序、局部外观；现有单模态方案存在固有缺陷：RGB特征易丢失关节级几何信息，骨架特征易丢失dense空间细节，长尾场景下分类精度表现较差。
### 方法关键点
FineX框架拆分三类细粒度特征：RGB外观、姿态热图几何、骨架图拓扑；先通过pairwise cross-attention实现跨模态对称信息交互，全程保留各模态独立特征流；再引入流级隐式稀疏MoE，根据内容将特征路由到共享专家子集，搭配负载均衡正则优化路由效果。
### 关键结果
在Gym99、Gym288、Diving48数据集达到SOTA；长尾分布的Gym288数据集上，平均类准确率从68.6%提升至76.2%，涨幅7.6个点，全程无需文本监督或大规模视觉语言预训练。
