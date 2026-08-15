---
title: 'DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation'
title_zh: DreamX-Phi 1.0：面向机器人操控的动作条件视频世界模型
authors:
- DreamX Team
- Rui Chen
- Xiangxiang Chu
- Geng Li
- Jifan Li
- Qingfeng Shi
- Datao Tang
- Jing Tang
- Jun Wang
- Pengfei Zhang
affiliations:
- DreamX Team
- AMAP-ML
arxiv_id: '2608.13489'
url: https://arxiv.org/abs/2608.13489
pdf_url: https://arxiv.org/pdf/2608.13489
published: '2026-08-12'
collected: '2026-08-15'
category: Other
direction: 机器人世界模型 · 动作条件视频生成
tags:
- WorldModel
- RoboticManipulation
- GeometricEncoding
- KnowledgeDistillation
- VideoGeneration
one_liner: 提出融合几何编码、视觉约束的动作条件视频世界模型，获WorldArena 2.0挑战赛冠亚军
practical_value: '- 多模态条件生成任务可借鉴PRoPE几何编码注入注意力的思路，将结构化位置/规则约束融入生成过程，提升电商文案/商品图生成的指令对齐度

  - 生成序列一致性优化可复用「冻结预训练大模型作为教师+掩码监督」的方案，小成本保障推荐/广告生成场景中核心对象属性不漂移

  - 高QPS生成场景可参考分布匹配蒸馏方法，将多步生成器压缩为少步学生模型，在精度损失极小的前提下提升推理速度'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有动作条件视频生成模型仅追求输出真实感，无法严格对齐输入动作指令、保持场景几何结构与操作对象属性一致性，易出现动作执行偏差、目标对象丢失等问题，无法满足机器人操控预演的决策要求。

### 方法关键点
1. 注意力层注入PRoPE风格的单臂SE(3)变换几何编码，保留机械臂身份与刚体运动结构，保障预测结果严格遵循指令指定的动作路径；
2. 新增轻量深度分支约束场景级几何特征，结合SAM3掩码与冻结V-JEPA教师模型做监督，保证抓取全流程中操作对象的属性一致性；
3. 采用分布匹配蒸馏方案，将多步生成器压缩为少步学生模型，大幅降低推理延迟适配端侧部署需求。

### 关键结果
在WorldArena 2.0挑战赛中斩获Track1第一名、Track2第二名。
