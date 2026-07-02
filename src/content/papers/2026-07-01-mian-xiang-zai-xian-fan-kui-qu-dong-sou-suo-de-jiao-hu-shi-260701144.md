---
title: Sequentially-Controlled Interactive Multi-Particle Flow-Maps for Online Feedback-Driven
  Search
title_zh: 面向在线反馈驱动搜索的交互式多粒子流图采样框架
authors:
- Binglin Ji
- Anindya Sarkar
- Hengchang Lu
- Jens Sjölund
- Yevgeniy Vorobeychik
affiliations:
- Washington University in St.Louis
- Uppsala University
arxiv_id: '2607.01144'
url: https://arxiv.org/abs/2607.01144
pdf_url: https://arxiv.org/pdf/2607.01144
published: '2026-07-01'
collected: '2026-07-02'
category: Other
direction: 反馈驱动搜索 · 多粒子采样优化
tags:
- IMPFM
- Flow-Map
- Online-Search
- Reward-Alignment
- Sampling-Efficiency
- SMC
one_liner: 提出IMPFM多粒子流图采样框架，大幅提升在线反馈驱动搜索的样本效率与结果多样性
practical_value: '- 电商搜索/推荐冷启动场景可复用多粒子吸引-排斥双力机制，平衡高转化内容探索与结果多样性，避免热门内容过度坍缩

  - 在线反馈驱动的生成式商品文案、营销素材生成场景，可借鉴流图后验样本共享机制，减少用户反馈交互次数，提升迭代效率

  - 工程上可复用交互感知重加权+ESS阈值重采样方案，缓解传统SMC采样的权重退化问题，提升生成结果的稳定性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有反馈驱动搜索方法普遍存在局部探索受限、模式坍缩、样本效率低等问题，难以适配先验偏好未知、仅能通过序列反馈迭代的业务场景（如电商冷启动推荐、交互式内容搜索）；传统SMC采样存在严重权重退化问题，RL微调则易受早期奖励模型偏差误导，亟需兼顾全局探索、样本效率与结果多样性的采样框架。
### 方法关键点
- 多粒子双力动态设计：每个粒子的漂移同时包含自身价值梯度的剥削项、其他粒子的核加权价值梯度吸引项、粒子间的排斥项，平衡高回报区域收敛与多样性保持
- 流图驱动的后验样本共享：所有粒子的后验样本集合用于校正每个粒子的漂移，最大化单样本的信息利用率
- 交互感知重加权方案：将价值与多样性梯度投影到基础模型的动态空间，避免样本偏离分布，配合ESS阈值触发的重采样，缓解权重退化
- 支持梯度-free的黑盒奖励优化，可直接适配点击、停留时长等不可微的业务反馈信号
### 关键实验
在ImageNet搜索、GenAI-Bench/T2I-CompBench++对齐任务上对比FKS、DAS、MFM等SOTA基线，相同反馈预算下奖励得分最高提升18%，LPIPS多样性得分提升22%，ESS有效样本量提升近2倍，低反馈预算下性能优势更突出。
### 核心结论
将粒子视为整体而非独立个体优化，通过全局信息共享的多粒子交互动态，是解决反馈驱动搜索中探索-利用矛盾的高效路径
