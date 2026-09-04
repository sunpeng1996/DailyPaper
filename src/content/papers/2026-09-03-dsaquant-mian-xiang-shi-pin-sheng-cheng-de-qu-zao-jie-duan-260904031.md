---
title: 'DSAQuant: Denoising-Stage-Aligned Quantization-Aware Training for Video Generation'
title_zh: 'DSAQuant: 面向视频生成的去噪阶段对齐量化感知训练'
authors:
- Shuaiting Li
- Zelin Gao
- Haibin Shen
- Yujun Shen
- Haotong Qin
- Yinghao Xu
affiliations:
- Robbyant
- ZJU
- PolyU
- HKUST
arxiv_id: '2609.04031'
url: https://arxiv.org/abs/2609.04031
pdf_url: https://arxiv.org/pdf/2609.04031
published: '2026-09-03'
collected: '2026-09-04'
category: Training
direction: 扩散模型 · 量化感知训练优化
tags:
- QAT
- Video Diffusion Model
- Model Compression
- Denoising Stage
- Low-bit Quantization
one_liner: 针对视频扩散模型量化后细节损失问题，提出去噪阶段对齐的QAT框架，显著提升低比特量化下的生成效果
practical_value: '- 电商短视频/主图生成等场景的扩散类模型量化优化，可复用分阶段训练思路：早期保留教师蒸馏保证全局结构稳定，后期侧重细节重建优化

  - 扩散模型推理阶段可按去噪阶段动态调整CFG开关，避免低比特量化引入的高频噪声被放大，平衡推理速度与生成质量

  - 生成式模型低比特量化部署时，不要直接套用通用QAT方案，结合迭代生成的阶段特性做适配可大幅降低效果损失'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
视频扩散模型(VDM)内存、计算成本极高，严重阻碍落地；常规量化感知训练(QAT)虽能压缩模型，但会严重损失生成视频的细节、纹理保真度与清晰度，根源是传统量化流水线忽略了VDM去噪的阶段特性：早期去噪负责全局结构与运动生成，中晚期去噪负责局部外观与高频细节优化。
### 方法关键点
提出DSAQuant框架：训练阶段采用去噪阶段定向监督，早期保留教师蒸馏保证结构生成稳定，后期切换为目标驱动优化提升细节重建能力；推理阶段采用去噪阶段门控引导，最终去噪步关闭CFG，避免量化误差被放大为高频伪影。
### 关键结果
在Wan、CogVideoX系列模型的W4A4、W3A3低比特量化设置下，效果持续优于SOTA QAT基线，W3A3设置下VBench平均得分最高提升6.60，同时保留优秀的文本-视频对齐能力。
