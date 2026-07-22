---
title: 'ReViV: Reconstructing the Viewer and the View in 4D from Monocular Egocentric
  Video'
title_zh: ReViV：从单目第一人称视频中4D重建观察者与观测场景
authors:
- Xiaozhong Lyu
- Gen Li
- Zhiyin Qian
- Xucong Zhang
- Marc Pollefeys
- Siyu Tang
affiliations:
- ETH Zurich
- Delft University of Technology
- Microsoft Switzerland
arxiv_id: '2607.17790'
url: https://arxiv.org/abs/2607.17790
pdf_url: https://arxiv.org/pdf/2607.17790
published: '2026-07-19'
collected: '2026-07-22'
category: Other
direction: 第一人称视觉 · 4D多模态联合重建
tags:
- Egocentric Vision
- 4D Reconstruction
- Masked Generative Transformer
- Multimodal Learning
- Motion Estimation
one_liner: 首个单目第一人称视频统一4D重建框架，同时输出观察者运动与场景动态，精度效率双SOTA
practical_value: '- 多模态信号联合概率建模的思路可迁移至推荐系统多行为、多模态用户信号的统一建模，替代多任务独立建模的拆分方案

  - 单前向通路多任务输出的架构设计可借鉴至多目标排序模型优化，减少多模型级联带来的推理延迟

  - 若布局AR电商、可穿戴设备交互场景，该开源模型可直接用于用户动作、视线意图理解的底层能力搭建'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有第一人称4D重建方案依赖预计算相机轨迹等辅助输入，将场景感知与人体自运动建模拆分为独立任务，存在推理速度慢、缺乏统一端到端框架的问题。
### 方法关键点
1. 将4D重建任务建模为RGB视频、相机轨迹、视线方向、全身/手部运动、深度等多模态信号的联合概率分布学习问题
2. 基于Masked Generative Egocentric Transformer搭建单前向通路架构，单次推理即可输出时序一致的观察者与场景双侧4D重建结果
### 关键结果
在HoloAssist、HOT3D、ARCTIC等5个基准数据集上，全身/手部/视线重建、相机跟踪精度达到SOTA，深度估计性能极具竞争力，推理速度显著优于现有方案
