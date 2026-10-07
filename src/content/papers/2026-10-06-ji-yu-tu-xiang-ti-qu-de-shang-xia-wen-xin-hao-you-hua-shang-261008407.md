---
title: 'Seeing the Context: Enhancing Recommender Systems with Image-Derived Contextual
  Signals'
title_zh: 基于图像提取的上下文信号优化上下文感知推荐系统
authors:
- Tal Cordova
- Tomer Geva
- Moshe Unger
affiliations:
- Tel Aviv University
arxiv_id: '2610.08407'
url: https://arxiv.org/abs/2610.08407
pdf_url: https://arxiv.org/pdf/2610.08407
published: '2026-10-06'
collected: '2026-10-07'
category: RecSys
direction: 上下文感知推荐 · 多模态信号融合
tags:
- Context-Aware Recommendation
- Multimodal Fusion
- VLM
- Graph Contrastive Learning
- Recommender Systems
one_liner: 提出从评论图像提取三类上下文的ICE-Fuse管道，作为现有推荐系统的互补信号
practical_value: '- 电商/本地生活场景可复用该思路，从用户晒图、评价图中提取场景上下文（如到店消费的氛围、穿搭的使用场景等），仅需训练阶段注入到用户/物品表征，推理无需依赖图片，无线上性能负担

  - 可复用ICE-Fuse的门控融合机制，针对多源上下文信号动态分配权重，适配不同用户/交互场景的上下文贡献差异，替代人工设定的固定权重

  - 图像上下文即使单独表现不如现有信号，只要提供互补信息（如文本遗漏的场景细节），叠加后的微小RMSE下降在大规模业务流量下也能带来显著的GMV或点击率提升'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有上下文感知推荐系统的信号主要来自时间、位置、评论文本，图像仅被用于丰富用户/物品表征，从未被用于提取场景上下文；而图像是用户消费过程中实时拍摄的，可捕获文本事后回忆遗漏的场景细节（如消费氛围、社交场景、环境属性等），是待挖掘的优质上下文源。
### 方法关键点
- 将图像上下文划分为物理（环境、时间、氛围）、社交（同行人数、场景类型）、模态（消费目的、情绪）三类，针对每类设计专用prompt调用VLM提取结构化文本描述，再编码投影至与用户/物品embedding相同维度
- 提出ICE-Fuse管道，通过关联用户/物品表征的门控网络动态分配三类上下文的融合权重，而非使用固定权重，适配不同交互场景的上下文贡献差异
- 改造RGCL图对比学习推荐模型，训练阶段将融合后的图像上下文嵌入用户/物品表征，推理阶段无需输入图片，直接用预训练好的表征完成评分预测，无额外推理开销
### 关键实验
基于TripAdvisor公开的欧洲5城餐厅评论数据集（3.9w条评论、1.4k用户、1.3k商家），对比无上下文、城市日期特征、评论文本上下文、CLIP直接图像embedding四类基线：
1. 单独使用图像上下文RMSE为0.910，优于无上下文基线的0.954，但弱于城市日期（0.903）、文本上下文（0.899）
2. 图像上下文与现有信号叠加后，城市日期+图像RMSE降至0.902（p<0.001），CLIP embedding+图像降至0.903（p<0.001），文本上下文+图像降至0.896，均有提升
3. 语义分析显示图像与文本上下文仅存在少量重叠，图像可捕获灯光、户外座位等文本未覆盖的场景细节，互补性极强
### 核心结论
图像上下文不需要单独超越现有信号，只要提供互补信息，叠加后的微小准确率增益在大规模推荐场景下也能产生可观的业务价值。
