---
title: 'PFA: Attention Can Be Progressively Focused in Long-Sequence Generative Recommendation'
title_zh: PFA：面向长序列生成式推荐的渐进式聚焦注意力框架
authors:
- Pengjie Zhou
- Weiqin Yang
- Haibo Xing
- Hao Deng
- Jinxin Hu
affiliations:
- Alibaba International Digital Commerce Group
- Zhejiang University
arxiv_id: '2610.39273'
url: https://arxiv.org/abs/2610.39273
pdf_url: https://arxiv.org/pdf/2610.39273
published: '2026-10-29'
collected: '2026-10-30'
category: GenRec
direction: 生成式推荐 · 长序列推理优化
tags:
- Generative Recommendation
- Long Sequence Modeling
- Sparse Attention
- KV Cache
- Beam Search
one_liner: 针对长序列生成式推荐解码延迟瓶颈，提出渐进式聚焦注意力框架实现效果与效率双重提升
practical_value: '- 可直接复用GR解码注意力特性观测：生成式推荐解码过程中注意力逐步聚焦、跨步骤token重要性排序一致性达0.7以上，无需每步/每beam独立做全量topk检索，大幅降低冗余计算

  - 工程落地可直接复用PFA核心架构：Step0做全注意力全局探索，Step1跨beam加权聚合得到共享token重要性排序，选中KV重排为连续内存布局，后续步骤按几何比例缩减token预算，避免非连续内存访问开销

  - 超参数可直接复用工业最优配置：初始token预算取历史长度的1/2，几何保留率取0.5，共享排序在Step1后构建，无需大量调参即可平衡效果与延迟

  - 长序列业务收益可落地：该方案支持用户行为序列从128扩展到512，推理延迟反而从15ms降至11ms，同时带动广告收入提升3.76%，解决长序列落地的延迟瓶颈'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
长用户行为序列可显著提升生成式推荐（GR）效果，但自回归beam search解码过程中，每步每beam都需要对全量历史做注意力计算，导致推理延迟随序列长度线性增长。现有静态历史压缩方案易丢失关键语义，动态top-k稀疏注意力则存在重复token选择、非连续KV cache访问开销大的问题，无法满足工业级低延迟要求。
### 方法关键点
- 前置观测得到GR解码两个核心特性：①渐进式注意力聚焦：解码越靠后，注意力越集中在少量核心token，Step3时前10%token即可捕获97.77%的注意力权重；②跨步骤排序一致性：核心token的重要性排序跨步骤斯皮尔曼相关系数达0.7以上，可复用早期排序结果
- 三阶段解码设计：Step0保留全注意力做全局偏好探索；Step1跨beam加权聚合注意力分布，得到共享的历史token重要性排序，选top-k token重排为连续KV缓存；后续步骤复用该排序，按几何比例缩减token预算，仅访问排序前缀的连续缓存
- 新增步骤感知KV投影，为每个解码步骤分配独立的KV投影参数，避免复用token导致的表征同质化
### 关键结果
在Kindle Store、Tmall公开数据集和阿里电商广告工业数据集上验证，对比GEMs、TIGER等SOTA基线：
- 离线效果：Recall@10平均相对提升5.75%，NDCG@10平均提升7.18%；工业数据集上较全注意力方案提速1.45×，Recall@10提升3.16%
- 7天线上A/B测试：用户行为序列长度从128扩展到512的前提下，广告收入（REV）提升3.76%，CTR提升0.34%，GMV提升2.56%，在线响应时间仅11ms，低于全序列方案的15ms
### 核心洞见
生成式推荐的自回归解码存在天然的注意力冗余，利用跨步骤、跨波束的注意力特性做结构化剪枝，是兼顾长序列效果和推理效率的高性价比路径
