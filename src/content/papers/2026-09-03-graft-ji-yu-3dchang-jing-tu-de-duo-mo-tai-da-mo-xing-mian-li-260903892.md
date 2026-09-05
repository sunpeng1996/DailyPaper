---
title: 'GraFT: A Training-Free Framework for Spatial Reasoning in Multimodal Large
  Language Models via 3D Scene Graphs'
title_zh: GraFT：基于3D场景图的多模态大模型免训练空间推理框架
authors:
- Junqing Du
- Fernando Ropero
- Erkin Turkoz
- Yanfeng Zhang
- Lu Liu
affiliations:
- Riemann Lab, Huawei Technologies
arxiv_id: '2609.03892'
url: https://arxiv.org/abs/2609.03892
pdf_url: https://arxiv.org/pdf/2609.03892
published: '2026-09-03'
collected: '2026-09-05'
category: Reasoning
direction: 多模态大模型 · 免训练空间推理
tags:
- MLLM
- Spatial Reasoning
- 3D Scene Graph
- Training-Free
- BEV
one_liner: 提出免训练框架GraFT，基于3D场景图增强多模态大模型空间推理能力，性能超各类基线
practical_value: '- 线下商超、家居电商的3D场景导购Agent落地时，可复用「3D场景图+符号几何工具+BEV渲染」的组合方案，免微调提升空间类问答准确性，无需修改MLLM基座

  - AR试穿、家装布局推荐等需要空间感知的场景，可参考该框架「结构化3D信息+任务相关第一视角帧」的信息注入逻辑，降低MLLM空间类幻觉

  - 资源受限的落地场景可优先采用外挂结构化知识的免训练方案替代高成本基座微调，适配多类MLLM基座降低迁移成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

## 动机
现有MLLM空间推理能力薄弱，在几何测量、视角转换、细粒度视觉属性对齐任务上表现较差；现有优化方案依赖大规模标注微调或新增专用3D编码器，成本高且绑定特定基座，泛化性差。

## 方法关键点
提出免训练框架GraFT，通过轻量易维护的3D场景图（3DSG）向冻结MLLM注入缺失的3D结构信息，覆盖三类核心能力：1）通过符号工具实现确定性几何计算；2）通过BEV渲染输出全局空间布局；3）通过任务相关第一视角帧实现视觉属性对齐，全程无需微调MLLM参数。

## 关键结果
在ScanQA数据集上所有指标均优于同基座基线，CIDEr提升27%；在VSI-Bench数据集上，冻结MLLM性能最高提升65%，超过所有专有/通用开源基线及多个知名微调空间模型。
