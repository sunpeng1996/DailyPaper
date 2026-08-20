---
title: 'EfficientSync: Real-Time Lip Synchronization via Deformation-Based Reference
  Texture Mixing'
title_zh: EfficientSync：基于形变的参考纹理混合实现实时唇形同步
authors:
- Fa-Ting Hong
- Runzhen Liu
- Luchuan Song
- Hongmin Cai
- Chuhua Xian
arxiv_id: '2608.18832'
url: https://arxiv.org/abs/2608.18832
pdf_url: https://arxiv.org/pdf/2608.18832
published: '2026-08-19'
collected: '2026-08-20'
category: Multimodal
direction: 多模态音视频处理 · 实时唇形同步
tags:
- LipSynchronization
- RealTimeGeneration
- TextureFusion
- Multimodal
- VideoEditing
one_liner: 提出基于形变的实时唇形同步框架，单GPU166FPS同时实现SOTA视觉质量与身份保留
practical_value: '- 电商直播虚拟人/数字人场景可复用Dynamic Texture Mixer的通道加权融合思路，利用参考帧保留主播真实唇纹、牙齿细节，避免生成失真影响用户信任

  - STAR Sampling零开销预处理方法可直接迁移到虚拟人动态素材检索流程，快速筛选最优参考帧降低推理成本

  - 局部编辑+背景先验分离的架构思路可借鉴到电商短视频/直播实时特效场景，既保证局部生成质量又不破坏原有画面信息'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有音频驱动唇形同步方案依赖大计算量GAN/扩散解码器重建全下半脸，推理延迟高，且易生成伪造的口腔内细节，无法保留用户真实纹理，身份一致性表现差。

### 方法关键点
1. 设计Dynamic Texture Mixer，将多参考帧融合转为通道级选择任务，通过全局上下文评估空间对齐的参考帧，经通道加权求和聚合，低成本保留纹理完整性
2. 提出时空偏移自适应掩码，将源帧拆分为唇形生成条件与独立背景先验，抑制下半脸信息泄露，实现生成嘴部与背景无缝融合
3. 推出零开销STAR Sampling预处理流程，检索最清晰、拓扑多样性最高的参考帧，提升形变质量上限

### 关键结果
在HDTF、VFHQ数据集上视觉质量、身份保留效果达SOTA，单GPU推理速度可达166FPS
