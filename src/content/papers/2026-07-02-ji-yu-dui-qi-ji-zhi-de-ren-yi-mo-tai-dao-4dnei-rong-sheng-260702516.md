---
title: Alignment Is All You Need For X-to-4D Generation
title_zh: 基于对齐机制的任意模态到4D内容生成通用框架
authors:
- Qiaowei Miao
- Kehan Li
- Yawei Luo
- Yi Yang
arxiv_id: '2607.02516'
url: https://arxiv.org/abs/2607.02516
pdf_url: https://arxiv.org/pdf/2607.02516
published: '2026-07-02'
collected: '2026-07-04'
category: Multimodal
direction: 多模态生成 · 4D内容对齐优化
tags:
- Multimodal Generation
- 4D Generation
- Diffusion Model
- Alignment
- Content Creation
one_liner: 提出Align4D多阶段对齐框架，实现任意模态输入到4D动态内容的SOTA生成
practical_value: '- 电商AR/VR商品动态展示场景可复用三阶段对齐方案，解决多模态输入生成4D商品的几何、运动一致性问题

  - 异步优化训练策略可迁移至多模态生成类任务，解耦不同属性模块的训练流程，降低训练难度同时提升生成保真度

  - 多模态融合的基准数据集构建思路可参考，用于搭建自有商品3D/4D生成效果评测数据集'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有4D生成方法仅支持单模态输入，数据集构建成本高、扩展性差，生成内容普遍存在几何结构失真、时序运动不一致等缺陷，无法满足任意模态输入的4D内容生成需求。
### 方法关键点
1. Align4D通用框架以视频信号引导4D运动生成、3D数据约束4D几何结构，支持任意模态输入生成连贯的视频-3D配对4D内容；
2. 配套三大核心对齐优化技术：对象距离对齐（搜索VAOD/MAOD协调4D渲染结果与视频、多视角扩散模型先验）、运动-几何联合对齐（同步视频与3D输入约束已知/未知视图，保障生成一致性）、异步优化（解耦高斯属性与形变网络训练，提升运动与几何保真度）；
3. 同步开源X4D基准数据集，融合prompt、图像、视频、3D多模态数据用于4D生成任务评测。
### 关键结果
在X4D、Consistent4D公开基准上取得SOTA的4D生成质量与一致性表现。
