---
title: 'AViTS: Adaptive Spatiotemporal Token Selection for Efficient Dynamic-Resolution
  Generation'
title_zh: AViTS：面向高效动态分辨率生成的自适应时空Token选择
authors:
- Haoran Qin
- Zhengan Yan
- Shikang Zheng
- Xiaobing Tu
- Jiacheng Liu
- Yuqi Lin
- Chang Zou
- JinShan Liu
- Peiliang Cai
- Xiantao Zhang
affiliations:
- Shanghai Jiao Tong University
- Alibaba Cloud
- Shandong University
- Jilin University
- Xi'an Jiaotong University
arxiv_id: '2608.17995'
url: https://arxiv.org/abs/2608.17995
pdf_url: https://arxiv.org/pdf/2608.17995
published: '2026-08-18'
collected: '2026-08-19'
category: Multimodal
direction: 多模态生成 · 扩散模型推理加速
tags:
- DiT
- Token Selection
- Diffusion Acceleration
- Dynamic Resolution
- FLOPs Reduction
one_liner: 针对DiT动态分辨率采样冗余问题，提出时空融合Token选择策略，大幅降低推理FLOPs且兼容其他优化手段
practical_value: '- 电商商品图、广告素材生成场景可复用时空Token选择逻辑，仅对和query语义相关的核心区域（如商品主体）做高分辨率渲染，降低生成成本同时保证核心信息质量

  - 该优化与蒸馏、量化、KV cache等现有主流推理优化手段完全正交，可直接叠加到现有生成服务链路，无需重构底层优化逻辑

  - 多模态Agent的实时图像生成/编辑交互场景，可借鉴Token优先级判别思路，在不损失核心信息的前提下大幅降低推理延迟，提升用户交互流畅度'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
Diffusion Transformers（DiT）生成质量优异但迭代采样推理成本极高，动态分辨率采样通过早期低分辨率降噪降本，但分辨率切换时统一上采样所有隐层Token会引入冗余计算，还可能损失细粒度细节一致性；现有部分上采样策略依赖局部隐层结构或单步统计，无法同时捕获Token-文本语义相关性、跨扩散步的Token表征动态变化。
### 方法关键点
提出AViTS自适应时空Token选择框架，通过隐层-文本注意力建模空间重要性，通过跨扩散步的Token级特征变化建模时间重要性，融合两者实现时空感知的选择性上采样：优先对关键Token做分辨率细化，延迟处理非重要Token，减少高分辨率冗余计算。
### 关键结果
- 在FLUX上实现最高6.34倍加速，在Qwen-Image-Edit、FLUX.1-Kontext-dev上实现近9倍FLOPs降低
- 与蒸馏、量化、特征缓存等优化手段正交，叠加蒸馏模型可达到14.76倍加速
