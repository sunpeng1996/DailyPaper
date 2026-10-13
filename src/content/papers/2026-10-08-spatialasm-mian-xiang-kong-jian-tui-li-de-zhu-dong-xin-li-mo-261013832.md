---
title: 'SpatialASM: Internalizing Active Mentalization for Spatial Reasoning'
title_zh: SpatialASM：面向空间推理的主动心理建模能力内化框架
authors:
- Yuhong Liu
- Shenxi Wu
- Junyi Chi
- Beichen Zhang
- Xuanlang Dai
- Jiaqi Wang
- Yuhang Zang
- Dahua Lin
affiliations:
- The Chinese University of Hong Kong
- Shanghai AI Laboratory
- Fudan University
- Shanghai Innovation Institute
- CPII under InnoHK
arxiv_id: '2610.13832'
url: https://arxiv.org/abs/2610.13832
pdf_url: https://arxiv.org/pdf/2610.13832
published: '2026-10-08'
collected: '2026-10-13'
category: Reasoning
direction: 多模态大模型 · 空间推理能力优化
tags:
- LVLM
- Spatial Reasoning
- Chain-of-Thought
- Active Mentalization
- Training Framework
one_liner: 提出SpatialASM训练框架，将主动空间心理建模能力内化进LVLM，提升多场景空间推理精度
practical_value: '- 多模态商品理解场景可复用主动视角规划思路，自动生成多视角空间推理CoT轨迹，降低人工标注成本，提升3D商品、AR试穿相关场景的推理精度

  - 具身导购/仓储Agent的空间能力训练可复用双监督范式：用显式推理轨迹教模型视角调度逻辑，搭配自动生成的视角采择任务强化场景想象

  - 稀缺推理监督数据的生成方法可迁移到其他多模态推理场景，比如商品摆放空间关系理解、虚拟导购路径规划等，快速扩充训练数据'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有LVLM在需要视角变换、跨视图对应、未观测区域推理的复杂空间任务上表现欠佳，缺乏人类具备的主动重构任务相关视角空间布局的Active Spatial Mentalization（ASM）能力，且空间类Chain-of-Thought（CoT）标注稀缺，难以支撑相关能力训练。
### 方法关键点
SpatialASM训练框架通过训练时空间模拟将ASM能力内化到LVLM：采用异中心新视角生成器锚定假设视角的视觉依据，输出两类互补监督信号：① 显式ASM轨迹，指导LVLM在推理时自适应调用视角规划与想象；② 自动构造的视角采择任务，强化视角条件下的场景想象能力。
### 关键结果
在7个覆盖感知导向空间理解、多图/跨视图/视角变换推理的基准测试上，4种主流LVLM backbone的平均推理精度均实现提升，同时保留原有通用视觉能力，ASM轨迹合成方案可有效缓解空间CoT监督稀缺问题。
