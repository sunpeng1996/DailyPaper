---
title: 'Multi-Resolution Flow Matching: Training-Free Diffusion Acceleration via Staged
  Sampling'
title_zh: 多分辨率流匹配：基于分阶段采样的免训练扩散模型加速方法
authors:
- Xingyu Zheng
- Xianglong Liu
- Yifu Ding
- Weilun Feng
- Junqing Lin
- Jinyang Guo
- Haotong Qin
affiliations:
- Beihang University
- Nanyang Technological University
- Institute of Computing Technology, Chinese Academy of Sciences
- University of Science and Technology of China
- ETH Zurich
arxiv_id: '2607.01642'
url: https://arxiv.org/abs/2607.01642
pdf_url: https://arxiv.org/pdf/2607.01642
published: '2026-07-01'
collected: '2026-07-03'
category: Multimodal
direction: 多模态扩散模型 · 免训练推理加速
tags:
- Diffusion Model
- Flow Matching
- Training-Free
- Inference Acceleration
- Multi-Resolution Generation
one_liner: 提出免训练分阶段多分辨率流匹配方法MrFlow，实现扩散模型最高25倍端到端加速且效果损失极小
practical_value: '- 电商素材生成场景可直接复用该框架，无需重训练文生图模型即可大幅降低推理成本，保障出图质量损失小于1%

  - 分阶段低→高分辨率生成+轻量GAN超分+低强度噪声注入的pipeline可迁移至生成式推荐的高清商品图/营销素材生成提速场景

  - 该方法可与时间步蒸馏等现有加速策略正交组合，可在已做蒸馏优化的生成模型基础上进一步提升加速比'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有免训练多分辨率扩散加速方法多在隐空间上采样+局部区域修改，易出现模糊或伪影，文生图推理速度与效果的平衡难以兼顾。
### 方法关键点
MrFlow采用四阶段pipeline：1）低分辨率快速生成主体结构；2）用轻量预训练GAN在像素空间做超分；3）注入低强度噪声支持高频重采样；4）高分辨率下细化细节，全程无需训练或运行时动态识别。
### 关键结果
在FLUX.1-dev、Qwen-Image上实现10倍端到端加速，OneIG指标与加速前差距小于1%，性能优于其他免训练加速策略；与预训练时间步蒸馏策略结合后最高可实现25倍加速。
