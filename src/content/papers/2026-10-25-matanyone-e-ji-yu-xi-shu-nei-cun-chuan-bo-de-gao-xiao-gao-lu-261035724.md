---
title: 'MatAnyone-E: Sparse Memory Propagation for Efficient High-Resolution Video
  Matting'
title_zh: MatAnyone-E：基于稀疏内存传播的高效高分辨率视频抠图
authors:
- Shuyun Wang
- Shangchen Zhou
- Peiqing Yang
- Yuekun Dai
- Xin Yu
- Chen Change Loy
affiliations:
- The University of Queensland
- S-Lab, Nanyang Technological University
- University of Adelaide
arxiv_id: '2610.35724'
url: https://arxiv.org/abs/2610.35724
pdf_url: https://arxiv.org/pdf/2610.35724
published: '2026-10-25'
collected: '2026-10-29'
category: Other
direction: 高分辨率视频抠图·推理性能优化
tags:
- Video Matting
- Sparse Memory
- High Resolution
- Inference Optimization
- Lightweight Decoder
one_liner: 提出稀疏内存传播+轻量解码器的高清视频抠图方案，4K下7.4倍速显存仅为原方案7.6%
practical_value: '- 电商直播/商品高清视频抠图换背景场景可直接复用稀疏计算逻辑：先低分辨率定位待处理区域再做高分辨率计算，大幅降本提效

  - 大模型长上下文匹配、视频帧记忆召回等全局匹配成本高的场景，可借鉴「低分辨率粗筛+高分辨率精排」两段式匹配思路，压缩计算量

  - 核心模块优化可参考：先定位运行时瓶颈再做轻量化替换，通过知识蒸馏对齐原模块输出，兼顾推理速度与效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
高分辨率视频抠图需同时兼顾发丝、透明区域等细节保留与帧间一致性，传统基于内存的匹配方法随分辨率提升，计算、显存成本激增，现有方案处理4K输入易出现显存不足、细节丢失问题。
### 方法关键点
1. 稀疏内存传播（SMP）：先执行低分辨率传播识别不确定性区域及关联记忆候选，仅对该区域做高分辨率匹配，其余区域复用低分辨率结果，同时减少匹配点位与检索内存量
2. 轻量解码器（LD）：针对实测运行时瓶颈设计，通过蒸馏对齐原解码器表征，进一步降低高清蒙版生成成本
### 关键结果
4K分辨率下效果与MatAnyone 2相当，推理速度提升7.4倍，峰值GPU显存仅为原方案的7.6%；单NVIDIA H200 GPU开启编译推理时，1080p分辨率达73.07FPS、4K分辨率达28.62FPS
