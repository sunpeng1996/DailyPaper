---
title: 'TILDE: TILt-based Distributional Erasure for Concept Unlearning'
title_zh: TILDE：基于倾斜分布对齐的扩散模型概念遗忘方法
authors:
- Naveen George
- Naoki Murata
- Yuhta Takida
- Konda Reddy Mopuri
- Yuki Mitsufuji
affiliations:
- Indian Institute of Technology Hyderabad
- Sony AI
- Sony Group Corporation
arxiv_id: '2607.06432'
url: https://arxiv.org/abs/2607.06432
pdf_url: https://arxiv.org/pdf/2607.06432
published: '2026-07-07'
collected: '2026-07-08'
category: Training
direction: 扩散模型训练 · 概念遗忘
tags:
- Concept Unlearning
- Diffusion Model
- Distribution Alignment
- GFlowNet
- Model Safety
one_liner: 提出基于分布对齐的扩散模型概念遗忘框架TILDE，兼顾强遗忘效果与良性生成质量保留
practical_value: '- 电商生成式营销素材场景中，可复用该分布对齐思路实现版权IP、竞品标识等敏感概念的定向遗忘，规避合规风险的同时保留素材生成质量

  - 生成式推荐系统若搭载AIGC能力，可借鉴该无锚点能量倾斜方法，无需全量重训即可快速擦除违规内容生成能力

  - residual ∇-GFlowNet的残差校正训练范式可迁移至其他大模型微调场景，在最小改动原生模型的前提下实现指定能力调整'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有扩散模型概念遗忘方法虽能有效擦除目标概念，但普遍存在良性生成质量、多样性、语义覆盖度下降问题；从头训练无违规数据的基准模型成本极高，现有擦除目标未明确要求与基准分布对齐，保留效果完全依赖更新规则，不可控性强。
### 方法关键点
将概念遗忘转化为分布对齐问题，在遗忘约束下最小化擦除后模型与预训练模型的条件分布偏差；采用能量倾斜的无锚目标抑制含目标概念的图像生成，同时保留各prompt的良性生成相对概率；基于残差∇-GFlowNet训练，仅学习相对于预训练扩散模型的得分校正量，无需改动原模型主体。
### 关键结果
在物体、艺术风格、虚拟人物三类概念遗忘任务上，遗忘效果优于现有基线，同时良性生成的保留度、分布保真度均显著超越对比方法。
