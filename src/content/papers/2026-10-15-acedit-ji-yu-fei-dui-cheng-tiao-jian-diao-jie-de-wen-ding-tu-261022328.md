---
title: 'ACEdit: Stable Multi-Turn Image Editing via Asymmetric Conditioning'
title_zh: ACEdit：基于非对称条件调节的稳定多轮图像编辑方法
authors:
- Sara Dorfman
- Nir Goren
- Gal Barak
- Daniel Cohen-Or
- Or Patashnik
affiliations:
- Tel Aviv University
arxiv_id: '2610.22328'
url: https://arxiv.org/abs/2610.22328
pdf_url: https://arxiv.org/pdf/2610.22328
published: '2026-10-15'
collected: '2026-10-17'
category: Multimodal
direction: 多模态生成 · 多轮图像编辑优化
tags:
- Multi-turn Generation
- Diffusion Model
- Knowledge Distillation
- Image Editing
- Asymmetric Conditioning
one_liner: 提出非对称条件+蒸馏的ACEdit训练框架，解决多轮图像编辑的效果累积衰减问题
practical_value: '- 多轮交互类生成场景（如电商商品图多轮修图、Agent多轮内容生成）可复用Self-Forcing训练思路，训练阶段强制模型承接自身上一轮输出，缩小训推分布差

  - 当自生成轨迹偏离ground truth导致直接监督不可靠时，可借鉴锚定原始输入的teacher模型做蒸馏提供监督信号，无需依赖完整真值编辑序列

  - 非对称条件机制可直接迁移至多轮生成任务，学生走顺序迭代路径、teacher锚定原始输入做全局对齐，平衡迭代灵活性和生成稳定性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有图像编辑模型单轮生成效果优异，但多轮迭代过程中每轮产生的微小分布偏移会持续累积，导致训练时的输入分布与多轮推理的实际输入分布存在显著gap，编辑效果随轮次增加快速劣化。
### 方法关键点
1. 引入Self-Forcing训练范式，训练阶段直接让模型基于自身上一轮的输出做后续编辑，预演多轮推理的输入场景，对齐训推分布；
2. 针对自生成编辑轨迹偏离真值轨迹、直接监督不可靠的问题，采用蒸馏目标，引入锚定原始干净图像、接收复合编辑指令的teacher模型提供可靠训练信号；
3. 设计非对称条件机制：学生模型按顺序基于自身输出迭代编辑，teacher模型始终锚定原始输入做全局对齐，平衡迭代灵活性和生成稳定性。
### 关键结果
15轮长序列编辑场景下，相比基线FLUX.2 Klein，大幅降低细节丢失、色偏、伪影等劣化问题，同时保持单轮编辑质量和指令遵循度。
