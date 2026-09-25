---
title: 'TOLA: Text-aware One-Step Latent Adaptation for Diffusion-based Text Image
  Super-Resolution'
title_zh: TOLA：面向扩散文本图像超分辨率的文本感知单步隐空间适配框架
authors:
- Yike Xu
- Yue Shi
- Yong Guo
- Jiezhang Cao
affiliations:
- Shanghai Jiao Tong University
- University of Chinese Academy of Sciences
- Shanghai AI Laboratory
arxiv_id: '2609.29240'
url: https://arxiv.org/abs/2609.29240
pdf_url: https://arxiv.org/pdf/2609.29240
published: '2026-09-24'
collected: '2026-09-25'
category: Multimodal
direction: 多模态 · 文本图像超分辨率优化
tags:
- Diffusion Model
- Text Image Super-Resolution
- Latent Adaptation
- OCR Conditioning
- Low Latency Inference
one_liner: 提出无需迭代的单步扩散文本超分辨率框架TOLA，解决多步推理延迟、语义错误累积问题，性能达SOTA
practical_value: '- 电商场景可复用置信度加权OCR条件注入方法，优化低清商品图/广告素材的文字超分预处理流程，减少OCR识别错误

  - 轻量隐空间残差校正模块可直接迁移至多模态输入的低清文本增强任务，在不显著增加推理耗时的前提下提升细节还原度

  - 单步扩散优化思路可复用至对推理 latency 敏感的端侧OCR、商品图像修复等业务场景，大幅降低部署成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有基于扩散的文本图像超分辨（TSR）依赖多步迭代预测，推理延迟极高；且错误文本先验会在迭代中被反复注入，导致语义错误不断放大，最终生成视觉清晰但字符识别错误的结果。
### 方法关键点
1. 构建无迭代的单步隐空间适配框架TOLA，规避多步扩散的性能损耗
2. 置信度加权文本条件模块仅构造1次语义条件，提前过滤不可靠OCR预测，避免污染图像重建过程
3. 轻量隐空间残差校正模块显式估计修正结构化残差，精准还原缺失或扭曲的笔画细节
### 关键结果
在CTR-TSR-Test（×4）、RealCE-200两个基准数据集上全指标达到SOTA，相比现有扩散类TSR方法在CTR-TSR-Test上PSNR至少提升2.72dB
