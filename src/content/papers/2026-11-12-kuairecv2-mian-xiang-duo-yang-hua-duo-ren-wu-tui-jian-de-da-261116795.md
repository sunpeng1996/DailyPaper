---
title: 'KuaiRecV2: Benchmarking Large-Scale Continual Learning for Diversified and
  Multi-task Recommendation'
title_zh: KuaiRecV2：面向多样化多任务推荐的大规模持续学习基准
authors:
- Chenxu Li
- Shuchang Liu
- Hantao Shu
- Wei Yuan
- Zhe Xu
- Guoqing Hu
- Yan Wang
- Biao Yang
- Xiang Li
- Cheng Ling
affiliations:
- University of Science and Technology of China
- Kuaishou Technology
arxiv_id: '2611.16795'
url: https://arxiv.org/abs/2611.16795
pdf_url: https://arxiv.org/pdf/2611.16795
published: '2026-11-12'
collected: '2026-11-13'
category: RecSys
direction: 推荐系统基准 · 持续学习多任务评估
tags:
- Continual-Learning
- Multi-task-Recommendation
- Recommendation-Benchmark
- Diversity-Evaluation
- Generative-Recommendation
one_liner: 发布快手工业级30天长周期推荐基准，支持持续学习、多任务、多样性多维度评估
practical_value: '- 动态候选池的7天滑动窗口设计可直接复用在短视频/电商新品快速迭代场景，解决冷启与旧品下线的流式训练问题

  - 持续学习场景下的遗忘缓解可优先采用5%历史样本Replay策略，比EWC LoRA更稳定，Day7的HR@50保留率提升15倍

  - 多任务训练优先采用SFT+RL交替方案，纯RL对分布shift鲁棒性差，商品池更新后性能会陡降

  - 多样性评估可新增Semantic ID分层的token级指标，比单纯item层面覆盖率更能反映语义多样性真实水平'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐基准普遍存在离线评估与线上效果不一致问题，未覆盖工业场景三大核心痛点：动态候选池下的持续学习、准确率与多样性的token级tradeoff、生成式推荐的多任务reward平衡，导致算法迭代的离线效果无法有效预判线上表现。

### 方法关键点
- **数据集设计**：发布两个子集，FullMonth包含12.4万用户30天共4.84亿交互、2490万多模态item，采用7天滑动窗口动态更新候选池，提供Semantic ID、多模态embedding等元信息；Small包含前两天数据用于快速算法验证
- **评估体系**：同时覆盖三类指标：检索精度（NDCG、HR）、token+item两级多样性（覆盖率、Gini、分层token熵等）、多任务效果（覆盖点击、点赞、评论等8类用户行为）
- **流式训练pipeline**：支持按天增量训练，保留跨天用户历史上下文，避免用户序列在天边界被人为截断，更贴合真实线上场景

### 关键结果
对比SASRec、GRURec等传统序列模型，以及LLaDA-Rec、MiniOneRec等生成式推荐模型：生成式模型效果显著优于传统模型，MiniOneRec的HR@50达62.63e-3，是SASRec的9.5倍；5%样本回放的持续学习策略在Day7时对Day1数据的HR@50保留3.20，比原生MiniOneRec高15倍；SFT+RL交替训练比纯RL在候选池更新后性能下降减少80%以上。

### 核心结论
只有同时提升精度、多样性、多任务三类指标的算法迭代，才是可落地的有效改进，单一指标提升往往是无法在线上复用的缺陷进步。
