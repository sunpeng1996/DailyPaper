---
title: 'ARDY: Autoregressive Diffusion with Hybrid Representation for Interactive
  Human Motion Generation'
title_zh: ARDY：基于混合表征的自回归扩散交互式人体动作生成方法
authors:
- Kaifeng Zhao
- Mathis Petrovich
- Haotian Zhang
- Tingwu Wang
- Siyu Tang
- Davis Rempe
affiliations:
- NVIDIA
- ETH Zürich
arxiv_id: '2607.08741'
url: https://arxiv.org/abs/2607.08741
pdf_url: https://arxiv.org/pdf/2607.08741
published: '2026-07-08'
collected: '2026-07-11'
category: Other
direction: 生成式动作建模 · 实时交互式生成
tags:
- Diffusion Model
- Autoregressive Generation
- Hybrid Representation
- Interactive Generation
- Motion Synthesis
one_liner: 提出兼顾可控性与实时性的流式人体动作生成框架，支持文本、多类运动学约束下的长序列生成
practical_value: '- 电商虚拟人实时导购场景可直接复用该框架，实现文本/用户操作控制的虚拟人动作低延迟生成

  - 生成类任务可借鉴「显式关键特征+隐式整体嵌入」的混合表征设计，平衡可控性与生成效率

  - 流式生成场景可复用可变历史上下文的自回归Transformer去噪器设计，兼顾长序列约束与推理速度'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有离线人体动作生成方法可控性高，但推理速度无法满足交互式场景要求；在线实时生成方案则普遍存在可控性不足、上下文窗口小的问题，难以适配复杂文本语义与长时域生成目标。
### 方法关键点
1. 采用混合表征架构，结合显式根节点特征与隐式人体嵌入，平衡轨迹控制精度与生成学习效率；
2. 设计两阶段自回归Transformer去噪器，支持可变历史上下文与灵活长时域运动学约束；
3. 基于大规模动捕数据集端到端训练，直接对齐文本标签与真实姿态采样的运动学约束。
### 关键结果
4步扩散推理平均时延仅33ms，在HumanML3D、Bones Rigplay基准上动作质量与约束贴合度表现优异，支持文本控制、关键帧约束、路径跟随、键鼠交互等多类交互场景。
