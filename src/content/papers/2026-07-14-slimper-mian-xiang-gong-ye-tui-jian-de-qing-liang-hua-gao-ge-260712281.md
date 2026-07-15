---
title: 'SlimPer: Make Personalization Model Slim and Smart'
title_zh: SlimPer：面向工业推荐的轻量化高效个性化排序模型
authors:
- Siqi Wang
- Xianjie Chen
- Shaofeng Deng
- Albert Chen
- Romil Shah
- Jiawei Huang
- Zhaoqin Wang
- Zhang Zhang
- Yiqun Liu
- Meilei Jiang
arxiv_id: '2607.12281'
url: https://arxiv.org/abs/2607.12281
pdf_url: https://arxiv.org/pdf/2607.12281
published: '2026-07-14'
collected: '2026-07-15'
category: RecSys
direction: 工业推荐 · 轻量化排序 长序列用户建模
tags:
- Personalized Ranking
- Long Sequence Modeling
- Lightweight RecSys
- Transformer Optimization
- Industrial Deployment
one_liner: 将个性化排序重构为紧凑知识库迭代优化，实现低算力开销的长序列用户建模
practical_value: '- 架构设计上可借鉴排序任务重构思路，将<用户-物品>匹配抽象为紧凑知识库迭代更新，脱离模型深度与用户历史长度的绑定，大幅降低长序列建模的计算、内存开销

  - 工程落地可复用请求级优化方案，同一推荐请求内多候选物品共享用户侧token副本，在不损失效果的前提下削减推理内存占用

  - 特征融合可参考其单backbone统一处理稀疏、稠密、序列特征的设计，简化现有多类型特征融合的推荐模型架构，降低维护成本'
score: 9
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前工业推荐广泛采用的Transformer架构原生适配自回归生成任务，需维护随序列长度线性增长的大尺寸中间张量，与推荐任务仅需输出单组<用户-物品>相关度分数的需求不匹配，长序列用户建模的算力、内存开销过高，限制模型深度与建模效果。
### 方法关键点
1. 重构个性化排序为紧凑统一<用户-物品>知识库的迭代优化过程：每层仅选择性查询原始多模态用户侧token、计算显式匹配分数、更新知识库，每层复杂度为O(N)且中间表征尺寸固定，实现模型深度与用户历史长度完全解耦
2. 新增请求级优化：同一请求下所有候选item共享单份用户侧token副本，进一步降低推理内存占用
3. 单backbone统一融合稀疏、稠密、序列三类特征，自带注意力可解释性
### 关键结果
部署在Instagram Reels和Feed场景，用户参与度获得可测量提升，可支持10k+细粒度用户历史事件的高效建模
