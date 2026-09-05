---
title: 'OctWorld: Long-Range World-Consistent Video Generation with Octree-Based 3D
  Mapping'
title_zh: OctWorld：基于八叉树3D映射的长范围世界一致性视频生成方法
authors:
- Zelong Lv
- Sicheng Xu
- Jianfeng Xiang
- Ruicheng Wang
- Yue Dong
- Yu Deng
- Guangzhong Sun
- Jiaolong Yang
affiliations:
- University of Science and Technology of China
- Microsoft Research Asia
- Tsinghua University
arxiv_id: '2609.03919'
url: https://arxiv.org/abs/2609.03919
pdf_url: https://arxiv.org/pdf/2609.03919
published: '2026-09-03'
collected: '2026-09-05'
category: Other
direction: 3D视频生成 · 稀疏八叉树内存设计
tags:
- Video Diffusion
- 3D Memory
- Sparse Octree
- TSDF Fusion
- World Generation
one_liner: 提出搭载稀疏八叉树3D内存OctMap的视频扩散框架，实现长轨迹视角下空间一致的视频生成
practical_value: '- 可复用OctMap动态稀疏八叉树内存设计，降低电商3D商品建模、虚拟场景漫游的显存开销，解决多视角回放一致性问题

  - 单图启动+自定义相机轨迹生成逻辑可直接复用在AR商品试穿、虚拟逛店场景的长序列3D内容生成链路

  - TSDF多帧融合的一致性对齐思路可迁移到多视角商品图生成、直播数字人背景动态切换的一致性优化中'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有长轨迹视频生成方案在相机重访已生成区域时空间一致性退化严重，固定分辨率3D内存开销高，无法适配开放场景多尺度内容生成需求。
### 方法关键点
1. 基于预训练自回归视频扩散模型实现长上下文时序建模，支持单图输入下沿用户指定相机轨迹自回归生成内容
2. 提出OctMap可扩展空间自适应3D内存，在动态稀疏八叉树中执行TSDF融合，渐进式将生成帧与对应深度图聚合为全局3D表示
3. 八叉树分辨率随图像证据动态调整，兼顾多尺度场景的几何、外观细节保留与低内存开销
### 关键结果
实验显示长范围空间一致视频生成效果全面优于现有基准方法，OctMap相比点缓存、固定分辨率TSDF体素方案在内存效率、空间一致性指标上均有显著优势。
