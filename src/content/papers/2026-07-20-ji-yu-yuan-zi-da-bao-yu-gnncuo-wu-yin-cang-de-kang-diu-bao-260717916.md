---
title: Packet-Loss Robust 3D Gaussian Compression via Atomic Packaging and GNN-based
  Error Concealment
title_zh: 基于原子打包与GNN错误隐藏的抗丢包3D高斯压缩方法
authors:
- Yuxuan Tao
- Xuerui Ma
- Hao Zhang
- Chunhua Peng
affiliations:
- 中南大学
- 马栏山音视频实验室
arxiv_id: '2607.17916'
url: https://arxiv.org/abs/2607.17916
pdf_url: https://arxiv.org/pdf/2607.17916
published: '2026-07-20'
collected: '2026-07-26'
category: Other
direction: 3D高斯渲染 · 流传输抗丢包优化
tags:
- 3DGS
- GNN
- Compression
- ErrorConcealment
- Streaming
one_liner: 提出抗丢包3DGS传输框架，编码端优化打包策略，解码端双分支修复，20%丢包下PSNR仅降3dB
practical_value: '- 做3D商品展示、AR试穿等3D内容流传输的业务，可直接复用锚点级原子打包策略，避免单包丢包导致属性不一致的渲染崩溃

  - 分层随机分组分散丢包的思路可迁移至大体积3D内容分块传输，避免局部连续丢包造成的大面积显示异常

  - 解码端轻量GNN+插值双分支加置信度fallback的架构，可平衡修复效果与端侧推理延迟，适合端侧3D内容渲染场景'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
3DGS现有压缩方案（如HAC++）流传输时码流对丢包极敏感，传统方法将关联锚点属性拆分到独立流，单包丢包会导致锚点属性不一致，引发严重渲染artifacts。
### 方法关键点
1. 编码端：锚点级原子打包将单锚点所有属性封装在一起，把属性损坏故障转化为干净的锚点缺失；分层随机分组进一步将丢包分散到空间全域，避免大面积连续空洞
2. 解码端：将丢失锚点修复建模为先验感知的属性补全任务，先通过上下文感知残差插值（CARI）分支基于哈希网格先验和邻域残差构建鲁棒基线，再用带哈希网格先验交叉注意力的轻量两层GNN细化高频属性残差；属性级置信度控制在预测不可靠时回退到插值结果
### 关键结果
在BungeeNeRF、Mip-NeRF 360、Tanks and Temples数据集20%随机丢包场景下，相比无错误隐藏的传输方案效果大幅提升，相对无损HAC++参考的平均PSNR下降仅约3dB
