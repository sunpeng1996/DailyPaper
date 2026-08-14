---
title: 'SNM-VFI: Symmetric Nonlinear Motion-Guided Generative Video Frame Interpolation'
title_zh: SNM-VFI：对称非线性运动引导的生成式视频插帧
authors:
- Jisoo Jeong
- Hong Cai
- Jamie Menjay Lin
- Hanno Ackermann
- Hyeonjun Sim
- Yinhao Zhu
- Yunxiao Shi
- Fatih Porikli
affiliations:
- Qualcomm AI Research
- Qualcomm Technologies, Inc.
- Google
arxiv_id: '2608.13460'
url: https://arxiv.org/abs/2608.13460
pdf_url: https://arxiv.org/pdf/2608.13460
published: '2026-08-13'
collected: '2026-08-14'
category: Other
direction: 生成式视频插帧 · 免训练框架
tags:
- Video Diffusion
- Optical Flow
- Frame Interpolation
- Training-free
- Generative Video
one_liner: 基于预训练光流与视频扩散的免训练运动可控视频插帧框架
practical_value: '- 电商商品短视频、直播切片的帧率提升场景可直接复用，免训练即可低成本获得高流畅度的插帧效果

  - 多模态广告/内容生成场景可借鉴「预训练模型先验引导+置信度分区域融合」架构，降低定制训练成本

  - 生成视频优化可复用光流约束扩散的思路，缓解运动畸变、时序不一致等常见问题'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有光流插帧依赖线性运动假设，处理非线性运动、遮挡、物体边界效果差；传统扩散插帧从随机噪声生成，时序一致性弱，且训练成本高。
### 方法关键点
1. 采用免训练架构，直接复用预训练光流模型与视频扩散模型；
2. 先通过光流模型生成多帧非线性流中间帧与置信度图，作为隐先验初始化、迭代引导扩散生成，保留稠密运动对应关系；
3. 基于置信度图融合光流输出的可靠结构与扩散生成的遮挡、边界等不确定区域的细节。
### 关键结果
在DAVIS、Sintel、KITTI三类基准测试中，感知质量、重建精度、多运动场景下的时序一致性均达到业内领先水平。
