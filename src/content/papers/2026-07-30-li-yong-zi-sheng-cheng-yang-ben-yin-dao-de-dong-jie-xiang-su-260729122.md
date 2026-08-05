---
title: A Frozen Pixel-Space Diffusion Model Can Guide Itself with Its Own Samples
title_zh: 利用自生成样本引导的冻结像素空间扩散模型优化方法
authors:
- Zixuan Fu
- Chong Wang
- Lanqing Guo
- Kailai Zhou
- Jiahao Nie
- Bihan Wen
affiliations:
- Nanyang Technological University
arxiv_id: '2607.29122'
url: https://arxiv.org/abs/2607.29122
pdf_url: https://arxiv.org/pdf/2607.29122
published: '2026-07-30'
collected: '2026-08-05'
category: Training
direction: 参数高效微调 · 扩散模型自引导优化
tags:
- Diffusion Model
- Parameter-efficient Tuning
- Self-guidance
- Adapter
- Image Generation
one_liner: 为冻结预训练像素扩散模型加轻量头，用自生成样本做自引导，低算力提升生成质量
practical_value: '- 大模型微调场景可复用：冻结主干仅加中间层轻量头，用不到1%全模型训练算力即可实现效果提升，适合电商商品图生成、营销素材生成等场景的低成本迭代

  - 训练数据构造可复用：无需真实标注数据，用模型自身生成样本即可训练adapter，尤其适合缺少高质量标注的垂类生成场景（如定制化商品图、专属营销海报生成）

  - 推理增强可参考：利用中间层粗预测与最终层细预测的偏差做自引导，可迁移至多模态生成任务的采样阶段效果增强，无需引入额外外部引导模型'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
像素空间扩散模型可端到端直接生成原始像素图像，无需VAE压缩latent的两阶段流程，但现有效果优化方案均需从头训练模型，算力成本极高。

### 方法关键点
1. 发现预训练像素扩散Transformer的中间层可解码出捕捉低频全局结构的粗预测，最终层负责细化高频局部细节；
2. 冻结主干权重，仅在中间层接入轻量预测头，采样时用中间层与最终层预测的偏差作为自引导方向；
3. 训练轻量头无需真实图像，模型自生成样本训练效果更优，尤其能补全像素扩散易欠拟合的高频分量。

### 关键结果
轻量头训练成本不到全模型训练的1%；无CFG的JiT变体FID降低超50%；带CFG的强基线也显著提升，JiT-H/16 FID从1.86降至1.67，PixelREPA-H/16 FID从1.81降至1.59。
