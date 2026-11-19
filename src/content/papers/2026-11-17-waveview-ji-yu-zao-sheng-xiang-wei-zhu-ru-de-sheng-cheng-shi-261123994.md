---
title: 'WaveView: The Novel View Is in the Noise'
title_zh: WaveView：基于噪声相位注入的生成式新视角合成方法
authors:
- Kaiwen Wang
- Jan-Hendrik Pauls
- Yinzhe Shen
- Frank Bieder
- Christoph Stiller
affiliations:
- Karlsruhe Institute of Technology, Germany
- Parallel Domain, Germany
- FZI Research Center for Information Technology, Germany
arxiv_id: '2611.23994'
url: https://arxiv.org/abs/2611.23994
pdf_url: https://arxiv.org/pdf/2611.23994
published: '2026-11-17'
collected: '2026-11-19'
category: Multimodal
direction: 生成式新视角合成 · 扩散模型优化
tags:
- Diffusion Model
- Novel View Synthesis
- Wavelet Transform
- Inference Optimization
- Generative Vision
one_liner: 通过初始噪声相位注入实现无架构修改、低开销的高性能生成式新视角合成
practical_value: '- 扩散模型先验注入技巧可迁移：可将电商业务侧结构先验（如商品展示约束、广告合规规则）注入生成初始噪声相位，无需修改基座模型架构，大幅降低业务场景适配成本

  - 推理优化思路可复用：仅通过改造初始输入噪声提升生成效果，无额外推理模块开销，适合生成式推荐、商品素材生成等低延迟需求的业务场景

  - 双树复小波包变换的局部细粒度信号注入方法，可落地到电商商品视角调整、虚拟试穿视角生成等多模态生成控制场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有生成式新视角合成（NVS）的显式扭曲、隐式编码两类方法均需引入额外推理模块，存在推理开销高、生成布局易偏离真值的问题。

### 方法关键点
1. 无需修改预训练生成器架构，将扭曲后的源场景信号注入初始噪声的相位维度，新增推理开销可忽略
2. 采用双树复小波包变换（DT-CWPT）实现局部各向异性相位注入，在遮挡区域、极线沿线对生成器的约束更低，适配复杂场景生成需求

### 关键结果数字
- DL3DV基准所有重叠区间性能超过全部基线，最难区间共视区域PSNR比同基座的MetaView高0.84dB，推理速度快2.1倍
- 动态NVS场景下，用同款噪声注入方法微调AnyView，AnyViewBench零样本PSNR从11.58提升至12.35dB
