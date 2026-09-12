---
title: 'LoopVAE: Recurrent Depth Across Scales for Visual Tokenization'
title_zh: LoopVAE：面向视觉令牌化的跨尺度循环深度优化方法
authors:
- Zhiying Lu
affiliations:
- University of Science and Technology of China
arxiv_id: '2609.11516'
url: https://arxiv.org/abs/2609.11516
pdf_url: https://arxiv.org/pdf/2609.11516
published: '2026-09-10'
collected: '2026-09-12'
category: Multimodal
direction: 多模态 · 视觉令牌化参数共享优化
tags:
- VAE
- Visual Tokenization
- Parameter Sharing
- Recurrent Depth
- Multimodal Preprocessing
one_liner: 提出跨尺度循环参数共享的视觉令牌化模型LoopVAE，大幅降参同时保持优异图像重建性能
practical_value: '- 电商商品图生成、AIGC素材生产等多模态生成场景可复用跨尺度参数共享思路，在端侧/边缘等推理资源受限场景降低VAE部署的参数量开销

  - 多模态召回/排序的视觉特征压缩环节可参考LoopVAE的循环深度设计，在特征编码精度损失可控的前提下减小存储、传输成本

  - 训练侧可复用其两阶段训练策略，在有限训练epoch下快速达成视觉重建性能与参数量的权衡'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有分层视觉令牌化器为不同空间尺度分配独立处理模块，参数量冗余大，且参数与张量尺度强耦合，部署灵活性差。

### 方法关键点
提出跨尺度参数共享机制，同尺度内和跨尺度间复用带尺度、循环条件的核心处理块，仅分辨率转换模块保持独立；4个核心块可在单编码器/解码器内完成28次执行，兼容卷积、Transformer算子，支持单/多分辨率潜空间接口。

### 关键结果数字
ImageNet-256数据集上，29M参数量卷积版LoopVAE仅训练约30epoch，rFID达0.28、PSNR达32.54dB，参数量较84M基准VAE降低65%；非对抗Transformer消融版本在全局参数共享下PSNR、SSIM表现具备竞争力；参数量降低的tradeoff为运算量增加、推理时延上升。
