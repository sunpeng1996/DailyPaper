---
title: 'CARA: Concept-Aware Risk Attention for Interpretable Collision Anticipation'
title_zh: CARA：面向可解释碰撞预判的概念感知风险注意力框架
authors:
- Zhishan Tao
- Ruoyu Wang
- Yucheng Wu
- Enjun Du
- Yilei Yuan
- Sherwin Ho
- Yue Su
- Jinbo Su
- Yi Hong
affiliations:
- Shanghai Jiao Tong University
- The University of Hong Kong
- Fudan University
- The Hong Kong University of Science and Technology (Guangzhou)
- Renmin University of China
arxiv_id: '2607.22494'
url: https://arxiv.org/abs/2607.22494
pdf_url: https://arxiv.org/pdf/2607.22494
published: '2026-07-24'
collected: '2026-08-02'
category: Other
direction: 自动驾驶 · 可解释动态风险预判
tags:
- Interpretable Prediction
- Concept Learning
- Spatio-temporal Model
- Autonomous Driving
- Collision Anticipation
one_liner: 提出融合动态风险概念轨迹的可解释时空碰撞预判框架，同步提升预测精度与预警提前量
practical_value: '- 可借鉴「将语义概念作为中间推理证据而非事后解释」的思路，优化电商风控、虚假流量识别等对可解释性要求高的业务链路

  - 动态概念轨迹对齐多模态时序输入的方法，可迁移到时序用户行为序列的语义归因、用户兴趣演化建模任务

  - 从领域文本提取先验概念再对齐多模态特征的范式，可复用在多模态内容推荐的可解释性模块设计中'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
自动驾驶碰撞预判需同时满足预警准确率、预警提前量与可解释性要求，现有方法存在三类缺陷：特征驱动模型为黑盒、事后解释保真度不足、基于概念的方法仅适配静态识别场景，无法适配动态驾驶场景。
### 方法关键点
1. 从事故叙事文本中提取领域原生风险概念，通过图文相似度与时序视频帧对齐，构建动态演化的概念轨迹；
2. 将概念轨迹作为显式风险证据，直接引导空间注意力、时序注意力计算与风险预判流程，实现可解释性与预测过程的深度耦合。
### 关键结果
在3个公开碰撞预判基准上，CARA相较强基线持续提升预判准确率与预警提前量，同时输出稀疏、具备语义支撑的概念级解释证据。
