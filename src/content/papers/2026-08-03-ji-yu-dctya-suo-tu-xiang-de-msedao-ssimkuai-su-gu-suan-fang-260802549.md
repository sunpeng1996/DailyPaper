---
title: Estimating SSIM from MSE for DCT-Based Compressed Images
title_zh: 基于DCT压缩图像的MSE到SSIM快速估算方法
authors:
- Luc Trudeau
- Maria G. Martini
affiliations:
- Université du Québec à Rimouski
- Kingston University London
arxiv_id: '2608.02549'
url: https://arxiv.org/abs/2608.02549
pdf_url: https://arxiv.org/pdf/2608.02549
published: '2026-08-03'
collected: '2026-08-09'
category: Other
direction: 图像压缩 · 质量评估指标快速估算
tags:
- SSIM
- MSE
- DCT Compression
- Image Quality Assessment
- PSNR
one_liner: 仅使用参考图像局部统计量即可从全局MSE/PSNR近似DCT压缩图像SSIM，效果显著优于基线
practical_value: '- 电商商品主图/详情图批量JPEG压缩场景中，可替代逐像素SSIM计算，大幅降低算力开销

  - 短视频转码场景中，参考图像统计量可在同内容多批次编码中复用，进一步降低评估成本

  - 内容中台图像质量校验链路中，可替换原有高耗时SSIM计算方案，提升批处理吞吐'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有图像压缩场景中，PSNR/MSE计算简单但和人眼感知相关性弱，SSIM感知匹配度高但计算依赖局部误差数据，高复杂度不适合大规模批处理场景。

### 方法关键点
针对DCT类压缩（如JPEG）场景，通过参考图像的局部方差/标准差加权重分配全局MSE，得到近似局部MSE，无需访问压缩后图像的局部误差即可计算SSIM近似值。

### 关键结果数字
在Kodak、Xiph Subset1数据集的全JPEG质量等级下，两种加权方案的SSIM近似精度均显著优于全局MSE基线；框架可直接扩展到视频场景，同内容的参考图像统计量可在多轮编码任务中摊销计算成本。
