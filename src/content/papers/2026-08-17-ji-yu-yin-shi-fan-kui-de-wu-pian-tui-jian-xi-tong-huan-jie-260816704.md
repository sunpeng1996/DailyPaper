---
title: Unbiased Recommender Systems with Implicit Feedback
title_zh: 基于隐式反馈的无偏推荐系统：缓解位置与流行度偏差
authors:
- Md Aminul Islam
affiliations:
- University of Illinois Chicago
arxiv_id: '2608.16704'
url: https://arxiv.org/abs/2608.16704
pdf_url: https://arxiv.org/pdf/2608.16704
published: '2026-08-17'
collected: '2026-08-18'
category: RecSys
direction: 推荐系统去偏 · 位置与流行度偏差缓解
tags:
- Implicit Feedback
- Position Bias
- Popularity Bias
- GNN
- Learning to Rank
- Debiasing
one_liner: 提出LTR位置偏差校正、GNN-CF流行度去偏等多套无偏方案，适配不同推荐场景需求
practical_value: '- 排序场景的位置偏差优化可直接复用CFC双阶段控制函数框架，无需修改原有排序目标、不需要 propensity 估计，适配各类非线性排序模型，落地成本低

  - 已上线的GNN-CF推荐系统可集成PPD后处理去偏方案，对预训练embedding做流行度分量投影去除，无需重训模型即可快速提升长尾商品曝光

  - 新训GNN-CF模型可采用DPAA消息传递去偏方案，交互级权重融合预训练+当前模型embedding、层间权重向深层倾斜，有效缓解流行度放大问题

  - 无偏验证标签缺失时，可采用残差去偏的验证点击策略做超参调优，避免选到被位置/流行度偏差误导的次优模型'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
隐式反馈（点击、收藏等）是推荐系统最易获取的训练数据，但天然存在位置偏差（高排位 item 点击量与真实相关性无关）、流行度偏差（热门 item 马太效应挤压长尾相关 item 曝光），直接训练会扭曲用户偏好，引发反馈循环，长期降低推荐精准度与生态多样性。现有去偏方法存在依赖 propensity 估计、线性假设限制、模型耦合度高、无法解决GNN消息传递的流行度放大问题等缺陷。

### 方法关键点
- 针对LTR场景位置偏差：提出CFC双阶段控制函数框架，一阶段建模历史排序过程生成残差（代表无法被特征解释的排序偏移，即偏差分量），二阶段将残差及与特征的交互项作为控制变量加入点击模型，无需修改排序目标、无需随机实验
- 针对已训GNN-CF的流行度偏差：提出PPD后处理去偏方案，计算交互级流行度得分（全局偏好扣除个性化偏好），构造embedding空间的流行度方向向量，直接对预训练embedding做投影移除流行度分量，无需重训
- 针对新训GNN-CF的流行度偏差：提出DPAA消息传递去偏方案，交互级权重融合预训练稳定embedding与当前训练动态embedding，层间权重向深层倾斜，降低消息传递过程中热门item的信号权重

### 关键结果
在3个公开基准数据集、1个工业级数据集上对比SOTA去偏基线，CFC在LTR场景下NDCG@10相对提升6.2%；PPD在GNN-CF场景下长尾item召回率提升18.7%，整体NDCG@5提升4.8%；DPAA在高流行度偏差场景下NDCG@10相对提升7.9%，同时热门item推荐效果无明显下降。

### 核心结论
无偏推荐的核心不是完全消除热门内容的曝光，而是把流行度信号和真实用户偏好信号分离，在不损失热门内容推荐效果的前提下提升长尾内容的精准触达。
