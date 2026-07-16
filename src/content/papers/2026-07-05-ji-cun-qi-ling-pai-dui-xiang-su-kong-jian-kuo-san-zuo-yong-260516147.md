---
title: Registers Matter for Pixel-Space Diffusion Transformers
title_zh: 寄存器令牌对像素空间扩散Transformer的作用研究
authors:
- Nikita Starodubcev
- Ilia Sudakov
- Ilya Drobyshevskiy
- Artem Babenko
- Dmitry Baranchuk
affiliations:
- Yandex Research
arxiv_id: '2605.16147'
url: https://arxiv.org/abs/2605.16147
pdf_url: https://arxiv.org/pdf/2605.16147
published: '2026-07-05'
collected: '2026-07-16'
category: Other
direction: 扩散Transformer · 视觉生成性能优化
tags:
- Diffusion Transformer
- Register Token
- Pixel Space Generation
- ViT
- Image Generation
one_liner: 揭示寄存器对像素空间DiT的增益机制，提出寄存器引导技术提升生成视觉结构一致性
practical_value: '- 电商商品图/营销素材像素空间生成场景，可直接引入寄存器令牌优化高噪声阶段特征质量，降低生成畸变

  - 复用Register Guidance技术，放大结构相关寄存器贡献，解决服装、家居等商品生成时的结构错乱、部件错位问题

  - 若当前业务用latent空间DiT，可小范围测试寄存器增益，优先在像素空间生成场景落地该优化方案'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
ViT中寄存器令牌可有效解决高范数patch token异常导致的特征图质量下降问题，随着扩散模型大量采用Transformer架构、转向像素空间训练，寄存器对Diffusion Transformers（DiT）的作用机制及增益尚不明确。
### 方法关键点
1. 对比分析像素空间与隐空间DiT的中间表示，验证DiT不存在ViT的patch token异常问题，但仍可从寄存器获得增益
2. 定位增益核心来源：高噪声阶段寄存器可输出更干净的特征图，对像素空间生成的帮助远大于隐空间
3. 提出Register Guidance技术，放大负责优化视觉结构与连贯性的寄存器令牌的贡献
### 关键结果
寄存器对像素空间DiT的性能增益显著优于隐空间DiT，现有SOTA像素空间DiT隐含的类寄存器机制是其优异表现的核心原因之一
