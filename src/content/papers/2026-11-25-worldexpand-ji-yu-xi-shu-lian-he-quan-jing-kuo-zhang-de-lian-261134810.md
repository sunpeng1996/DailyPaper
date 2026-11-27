---
title: 'WorldExpand: Building Coherent 3D Worlds via Sparse Joint Panoramic Expansion'
title_zh: WorldExpand：基于稀疏联合全景扩张的连贯3D场景构建方法
authors:
- Yuyang Yin
- Chenjie Cao
- Xuhui Zuo
- Yuning Gong
- Pengfei Wang
- Junta Wu
- Zhenwei Wang
- Yao Zhao
- Tengfei Wang
- Yunchao Wei
affiliations:
- Beijing Jiaotong University
- Tencent Hunyuan
arxiv_id: '2611.34810'
url: https://arxiv.org/abs/2611.34810
pdf_url: https://arxiv.org/pdf/2611.34810
published: '2026-11-25'
collected: '2026-11-27'
category: Other
direction: 3D场景生成 · 全景扩散模型
tags:
- 3D_Reconstruction
- Diffusion_Model
- Gaussian_Splatting
- View_Synthesis
- Panorama_Generation
one_liner: 提出稀疏联合全景生成框架，从单张全景图高效生成高一致性高分辨率3D场景，性能速度超SOTA
practical_value: '- 电商虚拟逛店场景可复用Coverage-Guided View Selection方法，优先生成高信息密度视角，降低渲染算力消耗

  - 多视角一致性生成逻辑可迁移到3D商品建模场景，解决多视角渲染内容冲突问题

  - 全局-局部注意力调度策略可直接复用至高分辨率生成任务，兼顾效果的同时降低训练推理成本

  - 虚拟人直播背景生成可借鉴该框架，用单张背景图快速生成连贯3D空间，降低场景搭建成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
单张全景图构建完整3D场景存在大量未观测区域，现有稠密序列生成方法存在冗余度高、长轨迹误差累积、跨视角内容冲突等问题，无法满足高精度3D重建需求。
### 方法关键点
1. 将单全景场景扩张任务转化为稀疏互补高分辨率全景观测生成问题，把生成算力集中到高信息密度场景区域；
2. 提出Coverage-Guided View Selection，基于场景自适应象限和warp-based覆盖分数筛选高价值目标观测位；
3. 联合全景扩散模型借助Gaussian-splatting几何warp，生成4个位姿对齐、跨视角一致的高分辨率全景图；
4. 采用诊断引导的全局-局部注意力调度，仅在敏感层保留全局注意力，大幅降低高分辨率联合生成的训练推理成本。
### 关键结果
跨多个数据集的新视角合成、下游3D重建指标均优于基线方法，推理速度显著快于SOTA全景视频方法，跨视角一致性、输出分辨率更高，可稳定泛化到多样真实场景。
