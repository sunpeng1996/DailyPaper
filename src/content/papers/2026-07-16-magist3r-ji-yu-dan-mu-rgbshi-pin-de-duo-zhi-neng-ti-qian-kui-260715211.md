---
title: 'MAGiSt3R: Multi-Agent Feed-forward 3D Reconstruction from Monocular RGB Videos'
title_zh: MAGiSt3R：基于单目RGB视频的多智能体前馈3D重建框架
authors:
- Ziren Gong
- Xiaohan Li
- Fabio Tosi
- Ninghui Xu
- Stefano Mattoccia
- Jianfei Cai
- Matteo Poggi
affiliations:
- University of Bologna
- The University of Hong Kong
- Southeast University
- Monash University
arxiv_id: '2607.15211'
url: https://arxiv.org/abs/2607.15211
pdf_url: https://arxiv.org/pdf/2607.15211
published: '2026-07-16'
collected: '2026-07-19'
category: MultiAgent
direction: 多智能体协同3D环境重建
tags:
- MultiAgent
- 3D Reconstruction
- Monocular Vision
- Pose Optimization
- Feed-forward
one_liner: 提出多智能体前馈3D重建框架，基于单目RGB视频实现近10FPS高精度重建与位姿跟踪
practical_value: '- 多Agent分层（intra/inter-agent）信息融合思路可迁移至电商多端/多场景用户行为数据的跨域合并，降低全局信息整合误差

  - 前馈推理链路+后置漂移校正的架构可借鉴到实时推荐系统，平衡低延迟需求与链路累积偏差问题

  - 近10FPS实时3D重建能力可落地AR电商场景，用于商品快速3D建模、虚拟试穿/试用的环境感知'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有单目3D重建方案难以同时满足实时性、多智能体协作精度要求，前馈链路存在相机位姿累积漂移问题，无法适配AR、自主导航等落地场景。
### 方法关键点
1. 基于3R系列前馈模型处理单目RGB视频，直接回归生成局部点云图
2. 设计MAGMA合并模型，在intra-agent、inter-agent两个层级融合局部点云，输出全局一致的点云地图
3. 新增位姿图优化模块，校正前馈pipeline的累积相机漂移误差
### 关键结果
在合成、真实世界数据集上，重建精度、相机跟踪精度均优于SOTA前馈方案，单目RGB视频重建推理速度接近10FPS
