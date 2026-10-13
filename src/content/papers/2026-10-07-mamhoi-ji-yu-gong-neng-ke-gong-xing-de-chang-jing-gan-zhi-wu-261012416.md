---
title: 'MAMHOI: Factorizing Scene-Aware Human-Object Interaction through Affordances'
title_zh: MAMHOI：基于功能可供性的场景感知人-物交互分解生成方法
authors:
- Mingyuan Lei
- Yoonchang Sung
- Tat-Jen Cham
affiliations:
- Nanyang Technological University, Singapore
- College of Computing and Data Science
arxiv_id: '2610.12416'
url: https://arxiv.org/abs/2610.12416
pdf_url: https://arxiv.org/pdf/2610.12416
published: '2026-10-07'
collected: '2026-10-13'
category: Other
direction: 3D场景感知人-物交互生成
tags:
- HOI Generation
- Affordance
- Scene Understanding
- Motion Synthesis
- Factorized Learning
one_liner: 提出基于affordance的拆分式场景感知HOI生成框架，无需配对人-物-场景标注训练
practical_value: '- 电商3D虚拟试穿/虚拟导购场景可借鉴拆分式训练范式，分别用场景数据集、交互数据集训练两个模块，无需昂贵的配对标注

  - 生成3D场景内人机/人-物交互时可引入affordance中间层，先预判交互可行区域再生成动作，降低物理穿模等冲突问题

  - 多源异构数据训练任务可设计显式中间接口，解耦不同模块的数据源要求，大幅降低标注数据获取成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
3D场景下真实人-物交互（HOI）生成需同时具备环境交互可行性推理、真实动效合成两项能力，但大规模配对人-物-场景标注数据稀缺，现有方案要么仅适配简化场景，要么动效真实性、物理合理性不足。
### 方法关键点
1. 引入显式motion-affordance中间接口解耦场景理解、动效合成模块，拆分实现场景感知HOI生成
2. 第一阶段由场景条件模型预测交互可行的位置与执行方式，第二阶段由affordance条件HOI模型生成对应人-物交互动作
3. 两个模块可分别从无配对的人类-场景数据集、人类-物交互数据集独立训练，无需配对标注
### 关键结果
复杂室内场景实验显示，可有效降低物体-场景穿透率，同时保留人-物交互质量，生成的场景感知交互物理合理性、真实度均更优
