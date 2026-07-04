---
title: Rethinking Generic Object Tracking Toward Human-Level Perceptual Intelligence
title_zh: 面向人类级感知智能的通用目标跟踪研究重思考
authors:
- Shih-Fang Chen
affiliations:
- National Yang Ming Chiao Tung University
- Institute of Computer Science and Engineering
arxiv_id: '2607.01395'
url: https://arxiv.org/abs/2607.01395
pdf_url: https://arxiv.org/pdf/2607.01395
published: '2026-07-01'
collected: '2026-07-04'
category: Other
direction: 通用目标跟踪 · 类人感知能力优化
tags:
- Object Tracking
- Computer Vision
- Perceptual Intelligence
- Online Adaptation
- Generalization
one_liner: 借鉴人类视觉感知机制，系统性提升通用目标跟踪的判别、适配与推理能力
practical_value: '- 在线自适应能力优化思路，可迁移到推荐系统实时适配用户兴趣漂移、流量分布变化的场景

  - 小样本/未见类别泛化提升方法，可参考用于冷启动商品、小众垂类内容的召回排序建模

  - 类人感知的先验知识+上下文融合框架，可复用至直播商品跟踪、多模态商品检索的Agent感知模块'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有通用目标跟踪（GOT）仅依赖首帧目标边界框初始化，需在动态视频流中持续定位目标，但泛化与在线自适应能力存在瓶颈：当目标发生严重形变、遭遇复杂干扰、环境大幅变化或属于训练未见类别时，跟踪可靠性会显著下降，与人类视觉感知能力存在较大差距。

### 方法关键点
借鉴人类视觉系统整合先验知识、空间几何、语义上下文的感知机制，通过系列方法系统性优化跟踪模型三大核心能力：目标判别能力、鲁棒适配能力、几何推理能力，缩小机器跟踪系统与人类视觉感知的差距。

### 关键结果
相关核心成果已发表于计算机视觉顶会，在通用目标跟踪基准集上的跨场景、跨类别跟踪精度与鲁棒性实现显著提升。
