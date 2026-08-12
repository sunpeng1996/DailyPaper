---
title: 'CausalSplat: Towards Comprehensive Hierarchical Reasoning in 3D Gaussian Splatting'
title_zh: CausalSplat：面向3D高斯泼溅的全面层次化推理
authors:
- Jiayu Ding
- Meilu Song
- Yun Chen
- Wei Gao
- Ge Li
affiliations:
- Peking University Shenzhen Graduate School
- North China Electric Power University
- Hunan University
- Guangdong Provincial Key Laboratory of Ultra High Definition Immersive Media Technology
arxiv_id: '2608.11150'
url: https://arxiv.org/abs/2608.11150
pdf_url: https://arxiv.org/pdf/2608.11150
published: '2026-08-11'
collected: '2026-08-12'
category: Other
direction: 3D场景理解 · 层次化推理
tags:
- 3D Gaussian Splatting
- Vision-Language Model
- 3D Scene Graph
- Hierarchical Reasoning
- Benchmark
one_liner: 构建3D高斯分割推理基准，提出融合VLM与3D场景图的CausalSplat实现SOTA推理性能
practical_value: '- 做家居/线下实体场景的AR导购/推荐时，可借鉴「显式结构感知+隐式逻辑推理」解耦架构，拆分3D场景实体识别和用户隐式需求推理步骤，降低任务复杂度

  - 多模态推理类推荐系统的效果评估可参考分层基准设计思路，从常识、空间、功能、反事实维度逐层校验模型对用户隐式需求的理解能力

  - 具身电商Agent的3D场景理解模块可复用3D场景图+VLM融合的技术路径，提升复杂空间约束下的商品匹配准确率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有3D Gaussian Splatting（3DGS）的开放词汇场景理解仅支持显式查询，无法处理具身交互所需的隐式意图、复杂空间约束、常识推理需求，落地能力受限。
### 方法关键点
1. 新增推理型3D高斯分割任务，构建Causal-LERF、Causal-ScanNet两个基准，覆盖常识、空间、功能可供性、反事实4类层级推理评估维度；
2. 推出CausalSplat框架，融合Vision-Language Model（VLM）与3D场景图，将显式结构感知与隐式逻辑推理解耦处理，降低复杂推理任务难度。
### 关键结果
在自研层级推理基准上取得SOTA性能，同时在标准指代、开放词汇3D分割任务上具备强泛化性；现有SOTA方法在新基准上表现普遍较差，推理能力存在明显短板。
