---
title: 'Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation'
title_zh: Embodied-Navigator：基于点选、思考、记忆、对齐的高效具身导航框架
authors:
- Hongyan Feng
- Sunlai Chen
- Xuanyu Liu
- Miao Pan
- Yangfan Xie
- Yuxiang Cui
- Zhongxiang Zhou
- Rong Xiong
- Wenqi Zhang
- Jianwei Yin
affiliations:
- OmniAI Group of ZJU ACES Lab
- School of Software Technology, Zhejiang University
- Zhejiang Humanoid Robot Innovation Center Co., Ltd.
arxiv_id: '2608.17512'
url: https://arxiv.org/abs/2608.17512
pdf_url: https://arxiv.org/pdf/2608.17512
published: '2026-08-17'
collected: '2026-08-19'
category: Agent
direction: 具身Agent · 多模态导航优化
tags:
- VLM
- Embodied Agent
- Navigation
- GRPO
- Memory Mechanism
one_liner: 提出适配VLM 2D预训练先验的TAMP-Nav具身导航框架，实现SOTA性能与高样本效率
practical_value: '- 多模态任务输出空间适配思路可复用：搜索推荐多模态理解任务无需强行改造模型输出层，可通过后处理映射实现预训练能力和业务逻辑的对齐，大幅降低适配成本

  - 选择性记忆机制可迁移到用户行为序列建模：仅保留核心交互节点的高维特征，冗余行为压缩为轻量时空指标，降低长序列建模的存储和计算开销

  - 双层奖励对齐范式可用于推荐RL排序优化：叠加点击转化等全局reward和曝光停留等过程reward，大幅提升RL训练的样本效率和最终效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM落地具身导航存在三大核心问题：被迫适配不符合2D预训练先验的动作空间，搭配刚性推理逻辑与低效内存管理，部署难度高。

### 方法关键点
1. Pixel-to-3D动作范式：VLM仅输出2D像素点选结果，后处理映射为3D坐标交给SLAM底层控制，适配VLM原生2D视觉能力
2. 选择性推理+锚点轨迹记忆：关键节点动态触发Chain-of-Thought推理、留存高保真记忆，冗余轨迹压缩为轻量时空指标，兼顾历史信息保留和时空感知效率
3. 基于GRPO的双层对齐范式：叠加全局结果奖励和细粒度过程奖励，实现Agent认知规划和环境反馈的紧密对齐

### 关键结果
在R2R-CE数据集上SR达66.2%，取得SOTA性能，仅需90k训练轨迹，运行效率与样本效率均显著优于现有方案
