---
title: 'HGenPush: A Heterogeneous Generative Recommendation Architecture for Industrial
  Push Notification Systems'
title_zh: HGenPush：面向工业推送场景的异构生成式推荐架构
authors:
- Xiao Liang
- Jiali Feng
- Xin Feng
- Yiqing Wang
- Baolin Ye
- Siyao Feng
- Zhihui Deng
- Cunyi Zhang
- Huajin Sun
- Xuanping Li
affiliations:
- Kuaishou Technology
arxiv_id: '2607.03362'
url: https://arxiv.org/abs/2607.03362
pdf_url: https://arxiv.org/pdf/2607.03362
published: '2026-07-03'
collected: '2026-07-07'
category: GenRec
direction: 生成式推荐 · 异构内容联合生成
tags:
- Generative Recommendation
- Semantic ID
- Multi-token Prediction
- Preference Alignment
- Push System
one_liner: 提出端到端异构生成式推送架构，优化多token生成效率，快手上线后DAU提升0.181%
practical_value: '- 可直接复用Chained-MTP多token生成方案，在保留语义依赖的前提下，比DeepSeek-MTP提升33.86%推理QPS，解决生成式推荐落地的效率瓶颈

  - 异构内容双分支联合生成设计可迁移到电商「商品+店铺」、内容平台「笔记+博主」的联合推荐场景，统一建模用户多维度需求

  - 跨场景行为融合方案可直接复用：将推荐域长短序列、推送域点击/曝光序列联合输入，解决推送场景行为稀疏问题

  - UCPA模块的GSISPO强化学习方法，基于会话后多维度反馈做序列级奖励，避免样本重加权对主目标的负向影响，可直接落地到所有生成式推荐的偏好对齐阶段'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐大多仅支持单类型内容生成，且普遍采用自回归范式生成Semantic ID，推理效率低，无法满足工业级推送系统的高吞吐要求；同时内容平台用户不仅需要优质内容，还偏好信任的创作者/商家，异构推荐需求未被充分满足。

### 方法关键点
- 混合用户行为理解模块：融合feed域长短行为、推送域点击/曝光序列、用户静态特征，通过decoder-only架构输出视频、作者两个分支的全局兴趣表征
- 异构生成模块：双分支分别生成视频、作者的Semantic ID；提出Chained-MTP方法，以全局兴趣表征为锚点，通过前序语义ID的累积嵌入建模依赖，放弃自回归范式大幅提升效率；作者分支新增行为级表征对齐，解决同领域作者的偏好区分问题
- UCPA偏好对齐模块：基于点击后会话的多维度用户反馈（播放、互动、负反馈等）构建奖励，提出GSISPO序列级强化学习算法，在不损失主指标的前提下对齐长期用户体验

### 关键实验
在快手4亿+日活的推送系统数据集上，离线对比SASRec、TIGER基线，视频分支HitRate@100达0.3915，作者分支达0.4848；Chained-MTP较DeepSeek-MTP吞吐量提升33.86%，效果基本持平；在线A/B测试全量版本较基线DAU提升0.181%，CTR提升1.577%，转发率提升7.57%。

生成式推荐落地工业场景的核心是平衡效果、效率与长期用户价值，异构多目标联合生成+轻量化生成范式+反馈对齐是可行路径。
