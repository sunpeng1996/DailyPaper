---
title: Keep it Simple! A Multiple-Choice Task can Benefit Generative Recommendation
title_zh: 引入简单多选辅助任务提升基于Semantic ID的生成式推荐效果
authors:
- Wei-Hsiang Huang
- Jyun-Yu Jiang
- Pu-Jen Cheng
affiliations:
- National Taiwan University
- Coupang
arxiv_id: '2611.19320'
url: https://arxiv.org/abs/2611.19320
pdf_url: https://arxiv.org/pdf/2611.19320
published: '2026-11-14'
collected: '2026-11-17'
category: GenRec
direction: 生成式推荐 · 多任务辅助优化
tags:
- Generative Recommendation
- Semantic ID
- Auxiliary Task
- Sequential Recommendation
- BPR
one_liner: 为基于Semantic ID的生成式推荐引入轻量多选辅助任务，最高提升NDCG@10达79%
practical_value: '- 可直接复用该辅助任务设计：仅需在现有Semantic ID生成式推荐模型中新增3个特殊task token（主任务前缀、辅助任务前缀、历史/候选分隔符），总损失直接叠加主任务与辅助任务的负对数似然即可，无需改动模型主干架构，落地成本极低

  - 候选集优先采用均匀采样策略，无需设计复杂动态调度逻辑，候选数量设置为10左右性价比最高，候选数过大易引入假负样本导致效果饱和甚至下降

  - 主任务与辅助任务的训练样本比例建议设为1:1，无需额外调整损失权重，可适配绝大多数稀疏电商/内容推荐场景

  - 该辅助任务同时提升热门、中长尾商品的推荐效果，不会牺牲长尾表现，适合电商全品类推荐场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于Semantic ID的生成式推荐大多依赖语义对齐、复杂架构设计或大量超参数调优，训练阶段仅学习正样本的生成逻辑，没有显式建模正负样本的相对排序信号，不符合BPR的核心思想，存在OOD泛化能力弱、语义相似但行为模式不同的item区分度低等问题，在高稀疏推荐场景下表现受限。

### 方法关键点
- 新增多选辅助任务，与主生成任务共享全部模型参数，仅通过3个特殊token区分任务：主任务前缀p1、辅助任务前缀p2、分隔用户历史与候选集的p3，无额外架构改动
- 辅助任务候选集构造：每个训练样本采样nc-1个未交互负样本+1个正样本，随机打乱后拼在用户历史序列后，任务目标仍是生成正样本的Semantic ID，与主任务目标完全一致无冲突
- 总损失为主任务负对数似然与辅助任务损失的直接加和，每个训练样本每轮分别参与主、辅任务各1次

### 关键实验结果
在4个公开基准数据集（Amazon Scientific、Instruments、Yelp、MovieLens 1M）上，以经典生成式推荐模型TIGER为基线，设置nc=10时，NDCG@10相对基线提升4.9%~79%，性能超过LETTER、ETEGRec等主流SOTA生成式推荐模型，高稀疏数据集上提升幅度更显著；候选数达到10左右时效果饱和，主辅任务1:1的样本比例表现最优。

**最值得记住的一句话**：生成式推荐不需要盲目堆叠复杂架构与多模态对齐任务，补全缺失的正负样本相对排序信号，用极简辅助任务即可获得远超复杂方案的收益
