---
title: 'InceptionGS: Generative Bootstrapping for Large-Scale Gaussian Splatting under
  Unstructured View Sampling'
title_zh: InceptionGS：非结构化视角采样下大规模高斯溅射的生成式自举方法
authors:
- Tianheng Lu
- Guangyu Wang
- Ruqi Huang
- Lu Fang
affiliations:
- Tsinghua University
arxiv_id: '2609.02747'
url: https://arxiv.org/abs/2609.02747
pdf_url: https://arxiv.org/pdf/2609.02747
published: '2026-09-02'
collected: '2026-09-04'
category: Other
direction: 3D高斯溅射 · 非结构化视角渲染优化
tags:
- Gaussian Splatting
- Novel View Synthesis
- 3D Reconstruction
- Neural Rendering
- Generative Prior
one_liner: 结合重建与自适应生成先验修复非结构化采样下高斯溅射的视角缺失区域，提升3D渲染质量
practical_value: '- 电商3D商品建模场景可借鉴「重建+生成先验」平衡思路，低成本修复实拍视角不足的商品3D模型区域，降低3D资产制作成本

  - AR/VR导购、虚拟逛街场景的大规模场景3D重建可复用其场景/视角自适应生成先验融合方案，保障非结构化采样下的3D内容一致性

  - 纯推荐排序、用户建模类业务无直接可迁移价值，仅适用于涉及3D内容生产的电商衍生场景'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
大规模3D场景数字化需要全视角一致的高质量渲染，但全视角采集受成本、场景复杂度、可达性限制难以落地，非结构化采样下部分区域必然存在视角不足问题；现有重建类方法在视角稀缺区域表现差，生成类方法存在可控性弱、3D一致性不足等缺陷。
### 方法关键点
提出InceptionGS框架，精准平衡重建与生成能力：以初始高斯溅射结果为基础，软融合场景自适应、视角自适应的生成先验，仅针对性修复视角稀缺导致的问题区域，其余区域保留原有重建精度，同时兼顾生成的合理性与重建的保真度。
### 关键结果
在真实大规模场景数据集上的实验证明，该方法处理非结构化影像的效果显著优于基线方法，可大幅提升高斯溅射的高保真渲染能力，补充可视化视频进一步验证其渲染的视觉一致性优势。
