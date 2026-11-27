---
title: 'SPARC: Geometry-Guided Attention Pruning for Long-Horizon Camera-Controlled
  Video Generation'
title_zh: SPARC：几何引导注意力剪枝实现长时序可控相机视频生成
authors:
- Zesong Yang
- Weikai Chen
- Liyuan Cui
- Yuan Li
- Jiaxin Huang
- Lutao Jiang
- Runze Zhang
- Yingda Yin
- Xiaoyang Huang
- Kai Yan
affiliations:
- State Key Laboratory of CAD&CG, Zhejiang University
- LIGHTSPEED
- HKUST(GZ)
arxiv_id: '2611.34064'
url: https://arxiv.org/abs/2611.34064
pdf_url: https://arxiv.org/pdf/2611.34064
published: '2026-11-24'
collected: '2026-11-27'
category: Multimodal
direction: 多模态生成 · 注意力剪枝优化
tags:
- AttentionPruning
- VideoGeneration
- DiffusionTransformer
- CameraControl
- InferenceOptimization
one_liner: 基于几何引导注意力剪枝实现无额外学习模块的长时序可控相机视频生成与推理加速
practical_value: '- 注意力剪枝的不对称设计思路可复用在长序列推荐场景：对已观测用户行为token限制关联历史对应token、未观测候选保留全量注意力，兼顾一致性与效果

  - 无额外模块的剪枝优化思路可迁移至大模型推理提速场景，通过业务先验（如用户行为时序关联、商品语义关联）指导注意力剪枝，在不新增参数的前提下降低推理延迟

  - 跨长时间gap的稳定检索思路可借鉴到长时序用户记忆建模场景，通过对应关系感知偏置与位置无关编码提升历史行为召回的稳定性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
长时序可控相机视频生成现有方案需新增额外控制或记忆模块，推理计算量大，难以支撑分钟级长视频生成，同时存在相机控制精度低、场景重访一致性差的问题。
### 方法关键点
1. 几何引导的注意力剪枝框架无需新增可学习模块，直接改造预训练视频扩散Transformer的原生自注意力机制，同时实现相机控制与场景记忆检索
2. 基于观测/未观测内容的不对称上下文需求设计剪枝策略：已观测token仅关联几何对应的历史token与局部时空上下文，未观测区域保留全量注意力
3. 引入对应关系感知注意力偏置、顺序无关历史定位策略，支撑长时序间隔下的稳定检索
### 关键结果数字
相机贴合度、场景重访一致性、视觉保真度均显著提升，结合四步蒸馏后推理提速超50×，可生成分钟级可控相机视频
