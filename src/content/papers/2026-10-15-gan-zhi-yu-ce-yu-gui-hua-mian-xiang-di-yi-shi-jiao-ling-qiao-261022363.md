---
title: 'Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous
  Manipulation'
title_zh: 《感知、预测与规划：面向第一视角灵巧操作的统一世界动作模型》
authors:
- Zirui Wu
- Chen Guo
- Tianjian Jiang
- Zeren Jiang
- Zeming Li
- Lingchen Yang
- Longteng Duan
- Ying Xue
- Handi Yin
- Shenyuan Gao
affiliations:
- HKUST (GZ)
- Primatix
- ETH Zurich
- University of Oxford
- HKUST
arxiv_id: '2610.22363'
url: https://arxiv.org/abs/2610.22363
pdf_url: https://arxiv.org/pdf/2610.22363
published: '2026-10-15'
collected: '2026-10-19'
category: Other
direction: 世界模型 · 多任务统一训练
tags:
- World Model
- Diffusion Transformer
- Multi-task Training
- Mixture of Transformers
- 3D Perception
one_liner: 提出融合感知/预测/规划能力的P³-WAM统一模型，在第一视角灵巧操作多任务上优于专用基线
practical_value: '- 共享基础权重+模态特定适配的混合Transformer架构，可迁移至多任务推荐/Agent模型，大幅降低多任务训练与部署成本

  - 随机模态可见性训练策略，可让单一模型支持多种输入输出组合，适配多模态推荐、Agent交互的多样化场景需求

  - 统一训练优于单任务训练的结论，可指导多目标排序、Agent决策类模型的训练范式设计，实现多任务效果协同提升'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有第一视角灵巧操作相关模型多为单任务专用设计，感知、动作预测、规划能力相互割裂，无法支撑复杂具身任务的全链路需求。
### 方法关键点
1. 提出P³-WAM统一世界动作模型，覆盖三大任务模式：从视频重建3D手部/相机轨迹的感知模式、给定动作生成未来视频的预测模式、给定初始图像+文本指令生成动作与对应视频的规划模式
2. 采用混合Transformer架构，共享基础权重+模态特定适配，加入双向视觉-动作注意力，将结构化3D动作表征注入预训练视频扩散Transformer
3. 随机模态可见性训练策略，让视频、3D动作可在不同模式下灵活作为条件输入或预测目标
### 关键结果
统一训练相比单模式训练全任务效果提升，在4个数据集上3D手部重建、动作条件视频预测任务超越专用基线；规划任务的VLM评分在指令遵循、动作进程等维度均优于常规视频生成基线。
