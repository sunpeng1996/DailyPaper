---
title: 'Mitigating Matthew Effect: Multi-Hypergraph Boosted Multi-Interest Self-Supervised
  Learning for Conversational Recommendation'
title_zh: 多超图增强多兴趣自监督对话推荐框架 缓解推荐系统马太效应
authors:
- Yongsen Zheng
- Ruilin Xu
- Guohua Wang
- Liang Lin
- Kwok-Yan Lam
affiliations:
- Nanyang Technological University
- Digital Trust Centre Singapore
- Sun Yat-sen University
- South China Agricultural University
- Peng Cheng Laboratory
arxiv_id: '2607.18609'
url: https://arxiv.org/abs/2607.18609
pdf_url: https://arxiv.org/pdf/2607.18609
published: '2026-07-21'
collected: '2026-07-22'
category: RecSys
direction: 对话推荐 · 马太效应缓解
tags:
- Conversational Recommendation
- Hypergraph
- Self-supervised Learning
- Matthew Effect
- Multi-interest Modeling
one_liner: 构建三类型三通道超图建模多级用户兴趣，缓解对话推荐场景动态反馈下的马太效应
practical_value: '- 可复用多维度超图构建思路：从item/知识实体/对话关键词三个维度，叠加群体社交/好友同购/陌生用户同购三个渠道建模用户兴趣，直接迁移到电商交互式推荐场景提升推荐多样性

  - 工程实现可直接借鉴超图优化trick：将超图构建移至数据预处理阶段，采用稀疏图存储、多卡并行拆分超图计算，解决超图训练效率低的问题

  - 可直接复用马太效应评估指标体系：Coverage@K + 推荐物品平均热度 + 长尾物品曝光占比，这套指标组合可直接用于业务场景的公平性、多样性效果评测

  - 无标注场景可复用自监督训练方案：采用InfoNCE损失做多兴趣表示对齐，不需要额外标注数据，适合冷启动用户的兴趣挖掘'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有缓解推荐系统马太效应的方法大多针对静态离线场景，未考虑对话推荐中用户与系统动态交互的反馈循环会持续放大热门物品曝光、压制长尾内容，且传统单通道超图只能捕捉单一类型的用户交互模式，无法覆盖多层级隐性兴趣，从根源上限制了推荐多样性。

### 方法关键点
- 构建三类三通道超图：分别搭建面向item、知识实体、对话关键词的三类超图，每类超图均覆盖群体社交、好友同购、无社交关联同购三个渠道，基于motif生成超边捕捉多节点高阶交互关系
- 多兴趣自监督学习：通过超图卷积分别学习item级、实体级、词级的用户兴趣表示，经Attention融合得到最终多兴趣向量，采用InfoNCE损失做自监督训练，无需额外标注数据
- 双任务联合优化：将多兴趣表示同时输入推荐模块做候选item排序、对话模块生成回复，联合优化两个任务的交叉熵损失

### 关键实验
在REDIAL、TG-REDIAL、OpenDialKG、DuRecDial 4个公开对话推荐数据集上对比18个SOTA基线，推荐任务在REDIAL数据集上R@10达0.2192，较最优基线提升11.5%；对话任务Dist-2指标较GPT-3提升62.9%；马太效应相关指标中，Coverage@k平均提升8.2%，推荐物品平均热度降低17.3%，长尾物品曝光占比更均衡。

**最值得记住的一句话**：缓解对话推荐马太效应的核心不是强制推送长尾物品，而是通过多维度交互建模挖掘用户未被捕捉的隐性兴趣，在不损伤用户体验的前提下扩大推荐覆盖范围
