---
title: Learning to Reason with Predictive Gains for Generative Recommendation
title_zh: 基于预测增益的生成式推荐推理优化框架GainReason
authors:
- Zhuoyang Li
- Teng Shi
- Jiakai Tang
- Weijie Yu
- Guofu Xie
- Xiao Zhang
- Lei Kou
- Yang Yu
- Lei Shen
- Xin Chen
affiliations:
- 中国人民大学高瓴人工智能学院
- 对外经济贸易大学人工智能与数据科学学院
- 阿里巴巴国际数字商业集团
arxiv_id: '2611.21441'
url: https://arxiv.org/abs/2611.21441
pdf_url: https://arxiv.org/pdf/2611.21441
published: '2026-11-16'
collected: '2026-11-17'
category: GenRec
direction: 生成式推荐 · 推理优化
tags:
- Generative Recommendation
- LLM
- Reasoning
- Semantic ID
- Reinforcement Learning
one_liner: 采用目标Semantic ID似然变化作为句级奖励优化生成式推荐推理，效果优于现有规则奖励方法
practical_value: '- 推理优化奖励设计可复用PG思路：无需基于最终推荐结果设计规则，直接用目标Semantic ID的log似然变化作为句级奖励，解决奖励稀疏、区分度低的问题，降低规则设计成本

  - 自定义因果注意力机制可直接落地：仅需1次前向即可计算所有推理步骤的PG，训练单步耗时仅比基线高1%，工程开销极低

  - PGRU辅助任务设计思路可借鉴：仅对净预测增益接近0的样本做推理条件下的预测微调，避免算力浪费在增益已足够或负增益的样本上

  - 解决推理反向拖累问题：采用PG优化可保证推理过程对推荐的正向贡献，避免工业场景中加推理反而效果下降的常见问题'
score: 10
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前推理增强的生成式推荐普遍基于GRPO搭配规则奖励优化，奖励仅由最终推荐结果决定，存在两个核心痛点：一是无法衡量推理内部各步骤的实际预测贡献，正负贡献的推理步骤获得相同的优化信号；二是组内奖励区分度极低，大量样本组的相对优势为0，优化效率极差，甚至普遍出现添加推理后推荐效果反而下降的问题。

### 方法关键点
- 定义Predictive Gain（PG）作为核心奖励：单句推理生成后，目标Semantic ID的log似然变化值，直接衡量单句推理对预测的贡献，理论证明最大化期望PG与Top-K排序目标严格对齐
- 提出PGRO优化策略：将句级PG作为奖励，采用GRPO风格的代理目标优化推理生成；设计自定义因果注意力机制，仅需1次前向即可计算所有推理步骤的PG，大幅降低计算开销
- 新增PGRU辅助任务：仅对净PG接近0的轨迹做推理条件下的预测微调，加强模型对推理信息的利用，避免负增益样本的干扰

### 关键实验
在Industrial、Movies、Yelp三个公开生成式推荐基准上，对比传统序列推荐、普通生成式推荐、推理增强生成式推荐三类共12种基线方法，相比最优基线：Industrial数据集NDCG@5提升7.7%，Movies提升3.1%，Yelp提升6.8%；训练单步耗时仅比规则奖励基线高1%，开销可忽略。

### 核心结论
优化生成式推荐的推理过程，与其依赖最终结果的粗粒度规则奖励，不如直接衡量每一步推理对目标预测的实际贡献，兼顾优化效率与推荐效果。
