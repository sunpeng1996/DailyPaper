---
title: 'Revisiting Avatar-As-Image: High-Fidelity Registration is All You Need'
title_zh: 重审图像化Avatar：仅需高保真配准即可实现高质量3D数字人
authors:
- Margaret Kostyrko
- Yuxuan Xue
- Garvita Tiwari
- Gerard Pons-Moll
affiliations:
- University of Tübingen
- Tübingen AI Center
- Max Planck Institute for Informatics
arxiv_id: '2609.11722'
url: https://arxiv.org/abs/2609.11722
pdf_url: https://arxiv.org/pdf/2609.11722
published: '2026-09-10'
collected: '2026-09-12'
category: Other
direction: 3D数字人 · 高保真表面配准
tags:
- DigitalHuman
- SurfaceRegistration
- SMPL
- 3DGeneration
- UVMapping
one_liner: 提出多阶段优化管线AvaImg，实现任意着装扫描的高保真SMPL(-X)+D配准，适配2D图像基础模型
practical_value: '- 电商虚拟试穿、3D数字人主播业务可直接复用AvaImg的三级效率级联优化方案，大幅降低3D人体配准的运行开销与存储成本

  - 「3D UV图对接2D预训练生成模型」的技术路径可迁移到电商数字人内容生成场景，复用成熟的2D图像生成能力降低研发成本

  - 基于有符号绕数实现的体在衣内约束方案，可直接用于优化3D人体建模流程的配准准确率，减少穿模等问题'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有基于UV纹理/位移图的3D着装人体表示可直接复用预训练图像网络能力，但高保真配准前提长期未被满足，导致生成质量受限，且无公开方案可实现任意着装扫描的高保真SMPL(-X)+D配准。

### 方法关键点
提出AvaImg多阶段优化管线：通过有符号绕数实现「身体在衣物内部」约束，搭配三级效率级联降低10倍运行时、节省95%存储，再通过粗到细的位移优化恢复精细表面细节，生成的UV图可直接对接冻结FLUX VAE复用2D生成先验。

### 关键结果
在6个数据集的人体拟合、形状估计、表面配准任务上全面超越基线，纹理配准PSNR达34.48dB，效果接近原始扫描；对接FLUX VAE后仅新增0.76mm Chamfer误差，生成的UV图符合自然图像分布。
