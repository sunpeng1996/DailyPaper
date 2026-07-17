---
title: 'VideoChat3: Fully Open Video MLLM for Efficient and Generalist Video Understanding'
title_zh: VideoChat3：全开源高效通用视频多模态大模型
authors:
- Xinhao Li
- Yuhan Zhu
- Xiangyu Zeng
- Yuhao Dong
- Haoning Wu
- Zhiqiu Zhang
- Yuandong Yang
- Changlian Ma
- Qingyu Zhang
- Yansong Shi
affiliations:
- Nanjing University
- Shanghai AI Laboratory
- Nanyang Technological University
- Peking University
arxiv_id: '2607.14935'
url: https://arxiv.org/abs/2607.14935
pdf_url: https://arxiv.org/pdf/2607.14935
published: '2026-07-15'
collected: '2026-07-17'
category: Multimodal
direction: 多模态大模型 · 通用视频理解
tags:
- Video-MLLM
- Multimodal Understanding
- I3D-ViT
- Efficient Inference
- Video Perception
one_liner: 提出全开源4B参数视频MLLM VideoChat3，兼顾泛化性与计算效率，性能超过同/更大参数开源模型
practical_value: '- 电商短视频/直播理解场景可直接复用I3D-ViT+自适应帧分辨率设计，大幅降低视频处理推理成本，适配短视频内容标签生成、直播内容审核等业务

  - 可参考其可扩展视频数据合成pipeline，低成本构建电商商品短视频、直播片段等垂域微调数据集，提升垂域视频MLLM效果

  - 4B小参数视频MLLM的优化思路可迁移到端侧/边缘部署的视频导购Agent，兼顾性能与部署成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有开源视频MLLM存在三大痛点：跨视频类型泛化性差、计算成本高限制规模化落地、核心组件（训练代码/策略/数据集）不完全开源，阻碍迭代与落地。
### 方法关键点
1. 效率优化：提出Inflated 3D Vision Transformer（I3D-ViT）+ 流视频感知自适应帧分辨率方案，实现高效时空表征，降低训练与推理阶段视频处理开销；
2. 效果优化：搭建可扩展视频数据合成pipeline，生成覆盖通用、长视频、流视频三类场景的高质量训练数据集，提升跨域泛化能力。
### 关键结果数字
仅4B参数的VideoChat3在通用、长视频、流视频三类benchmark上，性能全面超越同参数或更大参数的开源SOTA模型，同时推理效率更高。
