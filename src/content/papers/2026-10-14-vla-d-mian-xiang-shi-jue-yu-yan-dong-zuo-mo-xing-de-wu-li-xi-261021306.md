---
title: 'VLA-Δ: Learning Physical State Transition for Vision-Language-Action Models'
title_zh: VLA-Δ：面向视觉-语言-动作模型的物理状态转换学习
authors:
- Qi Lu
- Jiarun Li
- Ce Zhang
- Miao Pan
- Yi Pan
- Xu Wang
- Wenqi Zhang
- Xuhong Zhang
affiliations:
- Zhejiang University
- Central South University
- OmniAI Group of ZJU ACES Lab
arxiv_id: '2610.21306'
url: https://arxiv.org/abs/2610.21306
pdf_url: https://arxiv.org/pdf/2610.21306
published: '2026-10-14'
collected: '2026-10-18'
category: Agent
direction: 具身Agent · VLA模型优化
tags:
- VLA
- Embodied Agent
- State Transition
- Multimodal Pretraining
- Robot Control
one_liner: 为视觉-语言-动作模型引入物理状态转换显式监督，提升泛化性且无额外推理开销
practical_value: '- 序列决策类Agent（如导购Agent、用户路径规划Agent）训练时可引入状态变化显式监督，避免仅拟合观测-动作对应关系导致的过拟合问题

  - 多模态Agent训练可增加中间状态转换标注作为辅助损失，无需额外推理开销即可提升模型跨场景泛化性能

  - 针对决策类任务，构建覆盖任务语义+行为变化的细粒度标注，信号有效性优于纯端到端的输入-输出直接监督'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLA模型直接将观测映射为演示动作，缺乏中间物理状态变化的显式监督，易过拟合观测-动作对应关系；已有引入中间推理/未来状态预测的方法，未对物理状态转换本身做显式监督。
### 方法关键点
1. 提出VLA-Δ通用框架，将当前与未来状态的物理变化作为核心显式学习目标
2. 构建大规模预训练数据集，生成覆盖任务相关语义、视觉运动变化的物理状态转换标注，为连续动作生成提供更直接的监督信号
3. 推理阶段无需额外计算开销，可直接基于当前观测生成动作
### 关键结果
在LIBERO、RoboTwin基准上性能与SOTA持平，真实机器人实验中性能优于$\pi_{0.5}$。
