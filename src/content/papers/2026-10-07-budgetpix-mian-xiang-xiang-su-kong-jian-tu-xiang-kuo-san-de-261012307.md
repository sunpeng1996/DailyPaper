---
title: 'BudgetPix: Compute-Adaptive Tokenization for Pixel-Space Image Diffusion'
title_zh: BudgetPix：面向像素空间图像扩散的计算自适应分词方法
authors:
- Ozgur Kara
- Yujia Chen
- Daniel Watson
- David Forsyth
- James Matthew Rehg
- Wen-Sheng Chu
- Du Tran
affiliations:
- University of Illinois Urbana-Champaign
- Google
arxiv_id: '2610.12307'
url: https://arxiv.org/abs/2610.12307
pdf_url: https://arxiv.org/pdf/2610.12307
published: '2026-10-07'
collected: '2026-10-13'
category: Multimodal
direction: 多模态图像生成 · 推理效率优化
tags:
- Diffusion Model
- Adaptive Tokenization
- Inference Optimization
- Text-to-Image
- Compute Efficiency
one_liner: 提出计算自适应分词框架BudgetPix，大幅优化像素空间图像扩散的质量效率比
practical_value: '- 电商商品图/营销素材生成场景可复用熵引导四叉树的自适应算力分配逻辑，端侧低算力环境下优先保障商品主体生成质量，降低推理成本

  - 多模态推荐系统的图文生成模块可参考单checkpoint适配多算力预算的设计，无需针对不同算力环境训练多个模型，降低运维成本

  - 端侧Agent的多模态生成能力可复用可变token调度逻辑，边缘设备有限算力下优先保障核心视觉信息生成效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有图像扩散模型采用均匀分词策略，静态给等大图像块分配相同算力，无法适配推理端不同资源约束，对简单背景、复杂细节投入同等算力，质量成本比低下。
### 方法关键点
1. 自适应编码器基于熵引导四叉树+多尺度patch嵌入，将固定尺寸图像映射为可变长度token序列；
2. 尺度感知解码器可从多尺度token集合重建固定分辨率图像；
3. 灵活训练采样策略支持像素空间去噪器适配可变token数，可无缝接入现有扩散架构，单checkpoint覆盖多算力档位。
### 关键结果
文本生成图像任务上仅用25%原始算力，即可达到MiniT2I-L 512²、PixelDiT 1024²的同等保真度；基于MeanFlow的类别条件生成任务仅用60%算力即可实现近无损生成，FID仅上升0.8；人工与VLM评估均验证其质量-效率tradeoff显著优于基线。
