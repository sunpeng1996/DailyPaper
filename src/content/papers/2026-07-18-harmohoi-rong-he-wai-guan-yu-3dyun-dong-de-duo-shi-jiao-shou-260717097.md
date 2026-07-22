---
title: 'HarmoHOI: Harmonizing Appearance and 3D Motion for Multi-view Hand-Object
  Interaction Synthesis'
title_zh: HarmoHOI：融合外观与3D运动的多视角手物交互合成方法
authors:
- Lingwei Dang
- Juntong Li
- Zonghan Li
- Hongwen Zhang
- Liang An
- Wei Min
- Yebin Liu
- Qingyao Wu
affiliations:
- South China University of Technology
- Beijing Normal University
- Tsinghua University
- Shadow AI
arxiv_id: '2607.17097'
url: https://arxiv.org/abs/2607.17097
pdf_url: https://arxiv.org/pdf/2607.17097
published: '2026-07-18'
collected: '2026-07-22'
category: Multimodal
direction: 多模态生成 · 手物交互合成
tags:
- Diffusion Model
- 3D Motion Synthesis
- Multi-view Generation
- HOI
- Embodied AI
one_liner: 提出统一扩散框架HarmoHOI，可生成多视角一致的手物交互视频与全局对齐3D点轨迹
practical_value: '- 跨模态对齐的伪视频表示思路可复用：将3D结构化数据（如商品3D模型、用户空间行为轨迹）转为伪视频对齐大模型2D隐空间，大幅降低跨域适配成本

  - 小样本迁移的混合课程学习策略可借鉴：当目标场景多视角/多模态标注数据稀缺时，可先用单视图通用数据预训练再分步迁移到目标场景

  - 多模态联合生成的扩散框架思路可用于电商AR场景：同步生成2D视觉效果与3D运动轨迹，保证AR试穿、虚拟导购等交互的几何一致性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
多视角一致的手物交互（HOI）合成是动画制作、具身AI的核心基础能力，但现有方案受手部复杂运动、遮挡问题限制，难以保证多视角几何一致性，且多视角HOI标注训练数据极度稀缺。

### 方法关键点
1. 提出统一扩散框架HarmoHOI，联合建模2D RGB视频与3D点轨迹，在去噪过程中实现2D外观与3D运动的同步演化
2. 设计多视角扩散Transformer混合结构，将3D点轨表示为伪视频，对齐视频大模型的2D隐空间，缩小领域差异降低预训练先验适配成本
3. 引入全局运动对齐扩散模块，将粗点轨优化为全局对齐的公制尺度3D轨迹，进一步保障几何一致性
4. 采用混合数据课程学习策略，将单视图数据的通用先验迁移到多视角生成任务，解决数据稀缺问题

### 关键结果
在视觉质量、运动合理性、多视角几何一致性三个核心评估维度均达到SOTA性能
