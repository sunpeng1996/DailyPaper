---
title: 'Squaring-the-Sphere: Distortion-Free and Seamless Panorama Generation via
  CubeAtlas'
title_zh: Squaring-the-Sphere：基于CubeAtlas的无畸变无缝全景生成
authors:
- Xuhui Zuo
- Chenjie Cao
- Tengfei Wang
- Junta Wu
- Yisu Zhang
- Chunchao Guo
affiliations:
- Tencent
arxiv_id: '2610.31565'
url: https://arxiv.org/abs/2610.31565
pdf_url: https://arxiv.org/pdf/2610.31565
published: '2026-10-22'
collected: '2026-10-24'
category: Multimodal
direction: 多模态生成 · 360°全景图像合成
tags:
- Diffusion Transformer
- Sparse Attention
- Panorama Generation
- CubeAtlas
- Multimodal Generation
one_liner: 提出CubeAtlas全景表示与布局感知稀疏注意力，实现低计算量的无畸变无缝360°全景生成
practical_value: '- 布局感知稀疏注意力的设计思路可迁移到商品360°全景图生成场景，仅保留几何相关token交互，降低计算量同时保证内容一致性

  - 无需修改预训练扩散Transformer backbone、仅优化输入表示适配下游任务的思路，可复用在商品AR建模、虚拟场景生成等AIGC业务，降低微调成本

  - 无训练超分+空间融合方案可直接复用到电商商品全景图高清化场景，无需额外训练即可提升细节质量'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有360°全景生成方案存在两难：等距柱状投影（ERP）支持无缝建模但畸变严重、与预训练图像生成器存在域差；立方图保留透视几何但易出现面间不一致、可见接缝，计算成本较高。
### 方法关键点
1. 新型全景表示CubeAtlas将所有立方图面展开为单一紧凑画布，排列方向对齐的旋转极地区域与赤道面，同时保留立方图几何特性与无缝拼接所需的跨面关联
2. 布局感知稀疏注意力掩码仅保留全景连续性所需的token交互，移除几何无关配对，无需修改预训练扩散Transformer backbone与位置编码即可单步生成完整全景
3. 无训练超分与融合方案，在无畸变透视空间增强细节后生成最终ERP全景
### 关键结果
多基准测试显示，相比ERP建模方案，CubeAtlas在降低注意力计算量的同时，几何保真度、跨视角一致性、高分辨率视觉质量均有明显提升
