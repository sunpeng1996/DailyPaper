---
title: 'From Sketch to Scene: Relightable Garment Reconstruction from Marked Sketches'
title_zh: 《从草图到场景：基于标记草图的可重光照服装三维重建》
authors:
- Ahmet Neçirvan Doğan
- Eren Acar Başaran
- Metin Sezgin
- Zahra Montazeri
affiliations:
- Koç University, Türkiye
- University of Manchester, UK
arxiv_id: '2610.21865'
url: https://arxiv.org/abs/2610.21865
pdf_url: https://arxiv.org/pdf/2610.21865
published: '2026-10-15'
collected: '2026-10-19'
category: Other
direction: 草图驱动 · 可重光照3D服装重建
tags:
- Sketch-to-3D
- 3D Garment Reconstruction
- Relightable Generation
- Multimodal Input
- Generative Modeling
one_liner: 利用带高光阴影标记的服装草图与纹理文本提示，生成可重光照编辑的带纹理3D服装网格
practical_value: '- 电商3D服装商品建模、虚拟试衣场景可复用稀疏标注方案：仅需用星/月符号标记高光阴影位置，大幅降低设计师标注成本

  - 可参考「草图结构输入+属性文本提示」的多模态生成范式，快速生成符合设计意图的3D商品素材，缩短上新周期

  - 生成的可重光照3D模型可直接适配不同电商活动页、直播间的打光需求，无需重复建模渲染，降低素材生产成本'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有草图转3D服装管线无法捕获设计师的光影设计意图，会把草图上绘制的明暗效果直接固化到纹理层，生成的3D模型无法调整光照，复用性极低，无法满足多场景渲染需求。
### 方法关键点
1. 先通过艺术生用户调研，确定星（高光）、月（阴影）为接受度最高的两种稀疏标记符号；
2. 输入带标记的服装草图+纹理描述文本提示，模型分两路预测：一是场景平行光参数，二是服装表面位移场，通过调整曲面形态让标记区域自然对应光照下的高光/阴影位置，而非将明暗绘制到纹理上；
3. 最终输出带纹理的3D网格，支持后续任意重光照、形态编辑操作。
### 关键结果
生成的3D服装模型完全匹配设计师标记的光影意图，纹理还原度符合文本提示要求，光照调整无 artifacts，较传统管线的3D素材复用率提升100%。
