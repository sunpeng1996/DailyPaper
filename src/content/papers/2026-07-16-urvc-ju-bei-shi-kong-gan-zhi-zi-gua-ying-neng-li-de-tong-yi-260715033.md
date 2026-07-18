---
title: 'URVC: A Unified Real-Time Neural Video Coding Model with Temporal, Spatial,
  and Perceptual Adaptivity'
title_zh: URVC：具备时空感知自适应能力的统一实时神经视频编码模型
authors:
- Xihua Sheng
- Chang Wen Chen
arxiv_id: '2607.15033'
url: https://arxiv.org/abs/2607.15033
pdf_url: https://arxiv.org/pdf/2607.15033
published: '2026-07-16'
collected: '2026-07-18'
category: Other
direction: 神经视频编码 · 实时自适应优化
tags:
- Neural Video Coding
- Real-Time Coding
- Rate Control
- Adaptive Prediction
- Perceptual Adaptation
one_liner: 提出兼具时空、感知自适应的统一实时神经视频编码模型URVC，解决现有方案动态环境适配性差问题
practical_value: '- 多候选架构+目标直接耦合的思路可迁移到推荐动态多策略选择场景，不同流量/用户群下可自适应切换召回/排序策略无需重训

  - 特征分解+独立量化的细粒度分配方法可复用至广告/短视频推荐的流量预算、算力资源动态分配场景

  - 主干模型+次级模块库的切换方案可借鉴实现推荐多目标（GMV/点击率/时长）零成本切换，无需部署多套模型'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有实时神经视频编码方案为满足速度要求舍弃动态适配能力，存在三大缺陷：无法根据运动复杂度、码率约束自适应调整时序预测；空间码分配策略训练后固定，测试时无法响应用户动态需求；不同质量偏好需部署独立模型，灵活度极低。
### 方法关键点
1. 率感知自适应时序预测：通过多候选架构生成多套预测候选，将候选选择直接与率失真优化耦合
2. 基于分解的空间码率控制：通过特征分解+独立量化实现细粒度空间码分配，支持测试时零重训直接调整空间码分布
3. 感知切换机制：仅需在主干帧生成器外训练次级模块库，即可实现信号保真/感知质量两种模式自由切换
### 关键结果
URVC在帧内周期-1设置下YUV420 PSNR优于SOTA实时编码方案DCVC-RT，感知质量大幅提升，同时支持零样本ROI编码
