---
title: Task-Adaptive Grounded 3D-Programmers Using 2D VLMs
title_zh: 基于2D多模态大模型的任务自适应落地3D编程框架3D-Prog
authors:
- Arman Raayatsanati
- Sombit Dey
- Anna-Maria Halacheva
- Jan-Nico Zaech
- Luc Van Gool
- Danda Pani Paudel
affiliations:
- TextQL
- INSAIT, Sofia University
- ETH Zurich
arxiv_id: '2610.02021'
url: https://arxiv.org/abs/2610.02021
pdf_url: https://arxiv.org/pdf/2610.02021
published: '2026-10-01'
collected: '2026-10-03'
category: Multimodal
direction: 多模态大模型 · 3D理解与生成
tags:
- VLM
- 3D Understanding
- Visual Grounding
- Zero-shot
- Feedback Loop
one_liner: 提出CCF统一坐标框架与TAF反馈机制，无需重训2D VLM即可实现多场景3D理解与生成
practical_value: '- 可复用CCF统一坐标框架思路，解决电商3D商品多视角展示的坐标对齐、尺度不一致问题，提升3D商品渲染一致性

  - TAF任务自适应动态反馈机制可迁移至多模态推理链路，无需重训基座即可适配AR场景下的商品3D修改、自定义生成需求

  - 无需重训基座大模型的跨模态适配思路可降低3D电商场景的模型迭代成本，快速落地open-vocabulary的3D商品理解功能'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有2D VLM具备极强的泛化与推理能力，但3D理解能力受限于训练数据规模、多样性与推理容量，直接将2D VLM扩展到3D模态成本高、效果差。
### 方法关键点
1. 提出Canonical Coordinate Framing（CCF）作为统一视觉表示，将输入输出锚定到共享欧几里得坐标系，解决3D grounding常见的轴歧义、度量尺度不一致、参考系浮动问题；
2. 提出Task-Adaptive Feedback（TAF）任务自适应动态反馈机制，闭合推理环路，支持2D VLM在原生视觉上下文内执行各类开放词汇任务；
3. 搭建3D-Prog框架，无需对2D VLM进行任何重训，即可融合CCF与TAF能力。
### 关键结果
可在物体级、场景级任务上实现开放词汇3D理解、编辑与生成，在各类3D任务上均取得一致、可解释的高质量结果。
