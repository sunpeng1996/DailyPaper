---
title: Text-Driven 3D Indoor Scene Synthesis in Non-Manhattan Environments
title_zh: 非曼哈顿环境下文本驱动的3D室内场景合成
authors:
- Xianhui Meng
- Zirui Song
- Yuchen Zhang
- Li Zhang
- Yongxuan Lv
- Xiuying Chen
- Kun Wang
- Yan Luo
- Kai Chen
- Hangjun Ye
affiliations:
- University of Science and Technology of China
- Xiaomi EV
- Mohamed bin Zayed University of Artificial Intelligence
- Georgia Institute of Technology
- Nanyang Technological University
arxiv_id: '2607.02407'
url: https://arxiv.org/abs/2607.02407
pdf_url: https://arxiv.org/pdf/2607.02407
published: '2026-07-02'
collected: '2026-07-04'
category: Other
direction: 文本驱动3D场景生成 · 非曼哈顿环境适配
tags:
- Text-to-3D
- Layout-Optimization
- Non-Manhattan
- LLM-Guided-Generation
- 3D-Scene-Synthesis
one_liner: 提出SPG-Layout框架结合统计先验与分层布局策略，解决非曼哈顿环境3D室内场景合成的几何违规问题
practical_value: '- 分层优先级排布策略可迁移至推荐排序流程，先定位高权重核心商品位置再优化长尾商品排布，降低整体布局违规率

  - 引入领域统计先验引导生成模型训练的思路，可复用至电商文案、商品展示位生成场景，减少不符合业务规则的错误输出

  - 若业务涉及AR家装、3D看房类电商场景，可直接复用SPG-Layout框架生成符合用户文本描述的非规整户型室内布局'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有LLM驱动的3D室内合成方案仅适配正交结构的曼哈顿环境，无法建模非正交空间关系，在非曼哈顿场景下几何违规率高、物理保真度低，与真实建筑复杂度存在明显gap。

### 方法关键点
1. 推出SPG-Layout文本驱动3D生成框架，引入物体分布统计先验指导训练，提升模型对复杂空间的理解能力与生成保真度；
2. 模拟人类设计流程采用分层布局策略，优先放置大型物体，从流程上大幅降低布局冲突概率，实现语义真实度与物理合理性的平衡优化；
3. 构建包含500个多样非曼哈顿环境的专用评测基准，填补复杂场景评测数据缺口。

### 关键结果
在曼哈顿、非曼哈顿两类场景下，SPG-Layout各项指标均显著优于现有SOTA方法，代码即将开源。
