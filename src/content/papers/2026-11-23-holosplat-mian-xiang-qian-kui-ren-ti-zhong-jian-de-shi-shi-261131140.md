---
title: 'HoloSplat: Real-Time Token Streaming for Feed-Forward Human Reconstruction'
title_zh: HoloSplat：面向前馈人体重建的实时令牌流框架
authors:
- Chaofan Li
- Qihan Ding
- Shihan Wang
- Zhehao Shen
- Boyu Shen
- Quanyu Chen
- Haoyu Wu
- Lan Xu
- Xin Lou
affiliations:
- ShanghaiTech University
arxiv_id: '2611.31140'
url: https://arxiv.org/abs/2611.31140
pdf_url: https://arxiv.org/pdf/2611.31140
published: '2026-11-23'
collected: '2026-11-28'
category: Other
direction: 三维人体重建 · 实时令牌流传输
tags:
- 3D Reconstruction
- Token Streaming
- Gaussian Splatting
- Real-time Rendering
- XR
one_liner: 提出低带宽高画质实时人体三维流框架，通过令牌编解码降低传输开销提升渲染质量
practical_value: '- 透明度引导剪枝+PCA降维+无损几何编码的令牌压缩组合策略，可直接迁移到3D商品模型、虚拟人等电商多媒体内容的低带宽传输场景

  - 服务端压缩+客户端超网络恢复的端云拆分架构，可复用在AR试穿、虚拟直播间等互动电商业务的3D内容渲染链路

  - 热身阶段一次性微调模型头的校准思路，可借鉴到多端适配的个性化渲染场景，避免逐帧计算额外开销'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
实时自由视角人体视频流是沉浸式XR、远程呈现的核心支撑技术，但现有方案生成的3D高斯数据量远超实际传输带宽限制，强压缩又会大幅降低渲染质量，无法同时满足实时重建、低带宽传输、轻量客户端解码的要求。
### 方法关键点
1. 将前馈重建网络在高斯头前拆分，设计服务端令牌压缩+客户端令牌恢复的多码率编解码架构；
2. 服务端采用透明度引导令牌剪枝、PCA降维、令牌锚点无损几何编码压缩数据量；
3. 客户端将特征重建超网络融合进高斯头，修复压缩带来的质量损失；
4. 新增神经会话校准机制，热身阶段利用传入相机视角在线微调高斯头，无逐帧开销即可适配新相机参数和采集条件。
### 关键结果
服务端4块RTX 5090帧率达32.2FPS，50Mbit/s带宽下，客户端RTX 3050Ti单帧解码耗时22.1ms，数据传输量比未压缩float32 3D高斯低22.8倍，校准解码后PSNR提升1.05dB
