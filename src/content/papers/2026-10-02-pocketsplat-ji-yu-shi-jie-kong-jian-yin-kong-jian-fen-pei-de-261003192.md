---
title: 'PocketSplat: Mobile Gaussian Reconstruction via World-Space Latent Allocatio'
title_zh: PocketSplat：基于世界空间隐空间分配的移动端高斯重建
authors:
- Wenzhi Guo
- Xianda Chen
- Dongxuan Chen
- Guangchi Fang
- Bing Wang
affiliations:
- The Hong Kong Polytechnic University
arxiv_id: '2610.03192'
url: https://arxiv.org/abs/2610.03192
pdf_url: https://arxiv.org/pdf/2610.03192
published: '2026-10-02'
collected: '2026-10-05'
category: Other
direction: 移动端3D高斯重建资源优化
tags:
- 3D_Gaussian_Reconstruction
- On_Device_AI
- Mobile_AI
- Latent_Allocation
- Feed_Forward_Network
one_liner: 提出预算可控的移动端前馈高斯重建框架，可直接在iPhone端运行且优于基线
practical_value: '- 电商AR商品3D建模可借鉴其预算可控的高斯生成逻辑，按需控制输出3D资产大小，适配端侧存储/渲染性能

  - 多视图输入的特征融合可复用其cell级隐空间聚合方法，减少无效解码开销，提升端侧推理速度

  - 端侧AI应用可参考其资源约束下的优先级解码逻辑，仅对高价值特征做完整计算，避免超出设备内存阈值'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：移动端3D高斯重建需同时满足两个核心约束：推理过程不超出设备资源上限，输出高斯资产规模适配下游端侧存储、渲染需求。现有前馈高斯重建方法的输出规模由输入分辨率、视图数量隐式决定，无法灵活适配不同端侧的资源约束。
**方法关键点**：1. 支持预先指定输出预算，在预测的世界空间中组织几何感知的稠密隐候选，给局部隐单元分配精确整数容量，仅对保留的候选解码完整高斯属性，减少无效计算；2. 解码前通过单元条件隐融合聚合多视图重复证据，局部稀疏化后通过空间责任解码适配高斯支撑范围。
**关键结果**：在DL3DV及分布外基准上，质量-预算权衡表现优于所有前馈高斯重建基线；在Mip-NeRF 360数据集上可直接在iPhone端运行，构建更高质量紧凑高斯资产的速度较流式MVSplat变体有显著提升，原生MVSplat、DepthSplat均超出设备内存预算。
