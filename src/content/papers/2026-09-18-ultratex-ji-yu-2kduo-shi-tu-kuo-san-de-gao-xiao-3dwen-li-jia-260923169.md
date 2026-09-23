---
title: 'UltraTex: Unleashing 2K Multi-View Diffusion for 3D Texturing'
title_zh: UltraTex：基于2K多视图扩散的高效3D纹理生成框架
authors:
- Yibo Zhang
- Ze Yuan
- Nan Cao
- Li Zhang
- Yan-Pei Cao
- Yuan-Chen Guo
- Rui Ma
affiliations:
- Jilin University
- Shanghai Innovation Institute
- The University of Hong Kong
- Tongji University
- VAST
arxiv_id: '2609.23169'
url: https://arxiv.org/abs/2609.23169
pdf_url: https://arxiv.org/pdf/2609.23169
published: '2026-09-18'
collected: '2026-09-23'
category: Other
direction: 3D生成 · 多视图扩散效率优化
tags:
- Diffusion Model
- 3D Generation
- Multi-View
- Efficient Inference
- High Resolution
one_liner: 提出UltraTex框架，通过冗余Token裁剪与稀疏注意力优化，实现2K分辨率3D纹理生成效率数十倍提升
practical_value: '- 背景Token丢弃+块稀疏注意力的长序列优化组合，可迁移到电商3D商品展示、AR试穿场景的高分辨率渲染任务，大幅降低显存占用与推理延迟

  - 前景感知VAE解码的设计思路，可复用在需要保留局部高频细节的生成场景，比如电商商品主图高清生成、商品营销素材的精细化渲染

  - 针对高分辨率生成任务构建大规模垂类数据集的思路，可借鉴到服饰、3C等品类的3D资产批量生成场景的训练数据准备流程'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有多视图扩散3D纹理生成方法受限于512/768低分辨率，无法保留高分辨率参考图的高频细节，直接扩容到2K分辨率时Token量超212K，显存与延迟成本过高。
**方法关键点**：1. 背景Token丢弃策略：在DiT backbone前移除无意义背景Token，压缩序列长度；2. 块稀疏注意力：降低前景序列的注意力计算量；3. 前景感知VAE解码：消除仅用前景推理带来的重构伪影；4. 构建G-buffer TexVerse数据集，覆盖26.8万3D资产的超高清多视图渲染数据，支撑2K模型训练。
**关键结果**：生成纹理保真度高、细粒度细节丰富，训练速度较基线提升20.6~91.1倍，端到端推理速度提升22.3~74.6倍
