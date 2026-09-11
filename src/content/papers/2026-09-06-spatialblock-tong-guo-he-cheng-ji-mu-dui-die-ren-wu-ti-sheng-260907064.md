---
title: 'SpatialBlock: Enhancing Spatial Intelligence in LVLMs via Synthetic Block-Stacking
  Problem'
title_zh: SpatialBlock：通过合成积木堆叠任务提升LVLM空间智能
authors:
- Soohyun Ryu
- Sohee Kim
- Eunho Yang
affiliations:
- KAIST
- AITRICS
arxiv_id: '2609.07064'
url: https://arxiv.org/abs/2609.07064
pdf_url: https://arxiv.org/pdf/2609.07064
published: '2026-09-06'
collected: '2026-09-11'
category: Multimodal
direction: 多模态大模型 · 空间推理能力增强
tags:
- LVLM
- Spatial Reasoning
- Synthetic Dataset
- 3D Perception
- Multimodal Training
one_liner: 构造15k合成积木堆叠数据集训练LVLM，低成本提升空间推理能力并可泛化到真实场景
practical_value: '- 做电商多模态商品理解（如堆叠商品识别、不同视角下商品匹配）时，可先构造低成本结构化合成任务数据集做增量训练，替代高成本真实标注

  - 构造多模态训练数据时可加入可控颜色锚点等显式视觉提示，降低模型在复杂视觉场景下的推理难度，提升任务准确率

  - 开发线下电商导购、仓管拣货等需要空间交互的Agent时，可先用积木类结构化合成数据预训练空间能力，再迁移到真实场景，大幅降低数据成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有LVLM空间智能薄弱，无法基于2D图像精准推理3D场景结构；现有真实场景空间QA数据集标注成本高、噪声大，高度依赖外部感知模块，落地门槛高。
### 方法关键点
受人类认知发展规律启发，提出通过结构化积木操作任务学习基础空间能力的范式；构建15k规模的SpatialBlock合成数据集，覆盖3D转2D投影、视角转换、结构组合三类核心空间任务，额外加入可控颜色调制作为视觉锚点提示，支持直接问答、推理预测两种训练模式。
### 关键结果
仅用该小型合成数据集训练的LVLM，空间推理性能显著优于基线模型，且无需额外微调即可直接泛化到真实世界空间任务。
