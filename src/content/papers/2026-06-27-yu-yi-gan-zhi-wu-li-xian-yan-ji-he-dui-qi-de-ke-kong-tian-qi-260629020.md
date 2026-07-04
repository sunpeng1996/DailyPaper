---
title: Semantic-Aware, Physics-Informed, Geometry-Grounded Weather Video Synthesis
title_zh: 语义感知、物理先验、几何对齐的可控天气视频合成框架
authors:
- Chenghao Qian
- Nedko Savov
- Lingdong Kong
- Yeying Jin
- Rui Song
- Wenjing Li
- Zhun Zhong
- Jiaqi Ma
- Gustav Markkula
- Luc Van Gool
affiliations:
- University of Leeds
- INSAIT, Sofia University
- National University of Singapore
- University of California, Los Angeles
- Hefei University of Technology
arxiv_id: '2606.29020'
url: https://arxiv.org/abs/2606.29020
pdf_url: https://arxiv.org/pdf/2606.29020
published: '2026-06-27'
collected: '2026-07-04'
category: Other
direction: 可控视频生成 · 多信号解耦引导
tags:
- Video Synthesis
- Controllable Generation
- Physics-Informed
- Semantic Alignment
- Data Augmentation
one_liner: 提出语义-物理-几何三条件引导框架，生成高真实度可控天气视频，可提升下游视觉任务鲁棒性
practical_value: '- 多条件解耦引导生成的范式可迁移至多属性可控的广告/商品素材生成场景，将属性、动态、空间约束拆分为独立引导信号，提升生成可控性

  - 外挂领域规则（如物理模拟）引导预训练通用生成模型的思路，可降低业务定制化生成效果的训练成本，无需从头训练大模型

  - 合成稀有场景样本增强下游模型鲁棒性的验证流程，可复用至推荐系统中稀有样本/负样本的构造与效果验证环节

  - 针对户外品类商品的广告素材，可直接复用该框架快速生成不同天气下的场景化展示效果，提升素材生产效率'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有天气视频合成方法存在效果多样性不足、动态过程难控制的问题，依赖文本引导易缺失细节，通用视频编辑器优化目标偏向干净美观输出，难以生成雨雪等密集粒子类极端天气效果。

### 方法关键点
将合成任务解耦为三类独立条件信号分别引导：
1. 语义感知外观锚定，结合场景语义与用户输入确定天气视觉风格；
2. 物理先验动态模拟，基于重力、风力、湍流规则模拟高斯表示的粒子场运动过程；
3. 几何对齐合成，将模拟粒子与场景几何位置匹配后调用现成视频编辑器生成最终结果。

### 关键结果
生成的天气效果多样性、物理真实性、视觉真实度均优于现有方案，合成的天气数据可让自动驾驶语义分割模型在恶劣天气下的鲁棒性获得显著提升。
