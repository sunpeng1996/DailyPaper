---
title: 'Gate3DGen: A Pre-processing Model that Selectively Purifies Real-World Images
  for 3D Generation'
title_zh: Gate3DGen：面向3D生成的真实图像选择性净化预处理模型
authors:
- Xiaolin Li
- Zihao Huang
- Fanpeng Meng
- Chen Yang
- Guanjun Wu
- Kai Zhang
- Jiemin Fang
- Qi Tian
affiliations:
- Tsinghua University
- Huawei Inc.
- Huazhong University of Science and Technology
arxiv_id: '2610.31649'
url: https://arxiv.org/abs/2610.31649
pdf_url: https://arxiv.org/pdf/2610.31649
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: 3D生成 · 输入预处理优化
tags:
- 3D Generation
- Image Preprocessing
- Synthetic Data Engine
- Router Network
- Computer Vision
one_liner: 提出带退化感知路由的3D生成前置图像净化框架，无需重训下游生成器即可提升真实图效果
practical_value: '- 电商商品3D建模场景可复用「路由+轻量化净化」预处理架构，干净输入直接跳过降低 latency，仅对模糊/暗光/遮挡的实拍商品图做净化，无需重训下游3D生成模型

  - 可复用合成退化数据引擎构造思路，基于自有3D商品资产渲染干净视图并叠加真实场景退化类型，生成配对训练数据优化预处理模型

  - 空间损失设计可迁移到商品图像修复场景，强制保留商品ID、轮廓、纹理等核心识别特征，避免过度修正导致商品信息失真'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
单图3D生成在 curated 基准上保真度很高，但面对存在光照不均、模糊、遮挡的真实世界图像时效果骤降，现有净化方案要么无差别处理浪费算力，要么易丢失3D生成所需的关键视觉特征，还需重训下游生成器。
### 方法关键点
1. 设计 degradation-aware router，自动判断输入是否干净，干净图直接透传下游，脏图则提取退化特征引导净化
2. 3D导向单步净化器基于退化特征修复输入，用空间损失约束保留物体ID、轮廓、纹理等3D生成必需线索
3. 自研合成数据引擎，渲染3D资产干净视图并合成复合退化样本，提供配对监督数据
### 关键结果
- 合成基准上平均仅需2.3s完成净化，使下游 TRELLIS.2 的网格距离相对退化输入降低61.5%
- VLM 评估和真实图人工偏好测试均验证其退化修正、身份保留能力优异
