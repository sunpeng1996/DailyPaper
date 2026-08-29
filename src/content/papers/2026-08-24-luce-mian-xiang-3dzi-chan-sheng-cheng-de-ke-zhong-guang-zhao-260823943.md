---
title: 'Luce: Relightable Gaussians for 3D Asset Generation'
title_zh: Luce：面向3D资产生成的可重光照高斯表示
authors:
- Mayank Singh
- Michele Stoppa
- Alvise Memo
- Rui Yu
- Harsha Kalli
- Srimanth Gunturi
- Muhammad Ahmed Riaz
- Behrooz Shahsavari
- Waleed Abdulla
- David E. Jacobs
affiliations:
- Apple
arxiv_id: '2608.23943'
url: https://arxiv.org/abs/2608.23943
pdf_url: https://arxiv.org/pdf/2608.23943
published: '2026-08-24'
collected: '2026-08-29'
category: Other
direction: 单图像转3D资产生成 · 可重光照高斯表示
tags:
- 3D Generation
- Gaussian Splatting
- PBR
- Rectified Flow
- VAE
one_liner: 提出融合PBR材质的多模态高斯3D表示，单图生成可重光照高精度3D资产
practical_value: '- 电商商品3D素材生产：可直接复用单图转可重光照3D资产的pipeline，替代传统人工建模，大幅降低AR商品展示、虚拟试穿场景的素材生产成本

  - 推荐素材自动生成：可基于商品主图快速生成多光照、多角度3D渲染图，丰富商品信息流、广告推荐的素材池，提升素材多样性

  - 细粒度特征对齐trick：可借鉴预训练编码器多层特征拼接注入生成模型的方法，提升生成内容的细节还原度，适配电商场景下商品logo、参数文字的保留需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
高保真单图转3D任务需要同时捕捉几何与外观的3D表示，且需支持PBR材质、可重光照，适配标准渲染管线，现有方案在材质还原、细粒度细节保留上存在明显短板。
### 方法关键点
1. 提出Luce体素化多模态高斯云表示，为albedo、金属粗糙度、表面法线等PBR模态分别设置专属高斯基元，统一几何与物理材质表达；
2. 用VAE将该表示压缩为感知材质属性的统一隐空间；
3. 整流流Transformer以预训练图像编码器的多层特征为条件（同时保留语义上下文与空间细粒度信息），从单图生成对应隐向量，解码后得到可重光照PBR高斯，可选输出带切线空间法线的纹理网格。
### 关键结果
- Toys4K数据集上取得SOTA单图转3D效果，FID比最强基线提升28%；
- 自建AI生成图基准上，CLIP图像对齐分数达0.8519，优于最优基线的0.8299，可完好保留文字、logo、铭文等细粒度细节
