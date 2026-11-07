---
title: Hierarchical Incremental Beta Splatting for Online Reconstruction
title_zh: 面向在线3D重建的分层增量Beta泼溅（HIBS）算法
authors:
- Linus Franke
affiliations:
- University of Würzburg
arxiv_id: '2611.08288'
url: https://arxiv.org/abs/2611.08288
pdf_url: https://arxiv.org/pdf/2611.08288
published: '2026-11-05'
collected: '2026-11-07'
category: Other
direction: 在线三维重建 · 核函数与层级优化
tags:
- 3DGS
- Beta Kernel
- Online Reconstruction
- LOD
- Rasterization
one_liner: 引入带置信度调控的Beta核优化在线3D高斯泼溅，同步提升重建精度与运行效率
practical_value: '- 可借鉴置信度感知的初始化思路：推荐冷启动场景中，依据多域行为信号的一致性置信度，设置item/用户embedding的初始可学习权重，高置信样本减少迭代开销，低置信样本留足优化空间

  - 错误驱动的资源复用策略可迁移到召回池更新：将长尾低曝光的候选item重分配到预测误差高的用户请求区间，提升候选池资源利用率

  - LOD分层保形合并思路可用于大模型多粒度索引构建：用闭形式合并方法生成不同精度的索引层级，兼顾推理速度与检索精度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有在线3D高斯泼溅（3DGS）每帧生成的基元仅能迭代数十次，难以修正初始化误差，且高斯核天生偏软，需大量重叠才能拟合实体表面，重建质量与优化效率存在明显瓶颈。
### 方法关键点
1. 用Beta核替代高斯核，其形状参数可在类高斯软轮廓到近不透明平面之间插值，作为几何置信度的调控开关；
2. 基于几何可观测性、多视图深度一致性做置信度感知的基元初始化，高置信区域生成实体基元，低置信区域生成可修正软基元；
3. 错误驱动的基元重定位机制回收stale基元到光度误差热点，支持精确tile裁剪加速光栅化，闭形式保形合并构建LOD层级适配快速优化与实时渲染。
### 关键结果
在Mip-NeRF 360在线重建协议下，PSNR最高提升0.8dB，优化耗时最高降低40%，LPIPS指标从0.429降至0.295。
