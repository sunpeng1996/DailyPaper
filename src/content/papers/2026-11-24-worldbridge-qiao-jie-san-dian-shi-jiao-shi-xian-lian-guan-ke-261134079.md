---
title: 'WorldBridge: Bridging Scattered Views for Coherent 3D World Generation'
title_zh: WorldBridge：桥接散点视角实现连贯可控3D世界生成
authors:
- Weilong Yan
- Jingyu Hu
- Hongli Xu
- Yifan Zhan
- Beibei Lin
- Anbang Wang
- Qinqian Lei
- Jingwei Huang
- Robby T. Tan
affiliations:
- National University of Singapore
- Tencent
- The Chinese University of Hong Kong
- The University of Tokyo
arxiv_id: '2611.34079'
url: https://arxiv.org/abs/2611.34079
pdf_url: https://arxiv.org/pdf/2611.34079
published: '2026-11-24'
collected: '2026-11-27'
category: Other
direction: 3D世界生成 · 散点视角一致性对齐
tags:
- 3D Generation
- Cross-View Consistency
- Test-Time Optimization
- Attention Mechanism
- Benchmark
one_liner: 提出基于低/无重叠散点图像生成连贯3D世界的WorldBridge框架及配套评测基准
practical_value: '- 多源低重叠信息全局编码思路可迁移到跨域用户行为建模，提升用户画像一致性

  - 即插即用的测试时优化策略可复用在生成式推荐输出的一致性校准环节

  - 时空注意力区分轨迹内/外参考的设计可借鉴到序列推荐长短期兴趣建模'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有3D世界生成方法要么无法处理低/无视觉重叠的散点输入图像，要么生成的跨视角几何一致性差，同时缺乏适配该场景的公开评测基准。
### 方法关键点
1. 将散点参考图像编码为全局场景上下文，统一引导全视角的几何与外观生成；
2. 设计时空参考注意力机制，同时保障目标轨迹内时序参考保真度、支持轨迹外灵活空间参考；
3. 提出即插即用的隐层参考一致性策略，通过重投影引导的测试时优化提升参考匹配度；
4. 发布WorldBridge基准套件，填补低重叠参考3D生成场景的评测空白。
### 关键结果
各项定性定量指标均超越现有SOTA，可支持稀疏视角重建、相机姿态引导布局控制、文本驱动unseen内容生成、跨虚实风格参考桥接等多类场景。
