---
title: Parallel Decoding Distillation for Fast Image and Video Generation
title_zh: 用于快速图像视频生成的并行解码蒸馏方法
authors:
- Neta Shaul
- Chao Liu
- Arash Vahdat
- Julius Berner
affiliations:
- NVIDIA
- Weizmann Institute of Science
arxiv_id: '2607.26004'
url: https://arxiv.org/abs/2607.26004
pdf_url: https://arxiv.org/pdf/2607.26004
published: '2026-07-27'
collected: '2026-07-29'
category: Multimodal
direction: 多模态生成 · 蒸馏推理加速
tags:
- Diffusion Model
- Knowledge Distillation
- Parallel Decoding
- Video Generation
- Inference Acceleration
one_liner: 提出兼容任意预训练扩散/流匹配模型的并行解码蒸馏PDD，4-8步NFE实现SOTA生成效果且显著提升样本多样性
practical_value: '- 电商商品/营销素材AI生成场景可复用PDD蒸馏方法，将预训练多模态生成模型压缩到4-8步推理，大幅降低生成时延，满足实时素材生成需求

  - 蒸馏训练时放弃难优化的VSD+对抗损失组合，改用PDD的轨迹式蒸馏框架，既能降低训练难度，还可缓解模式坍塌，提升生成素材的多样性

  - 针对需动态调整推理质量/速度的业务场景（如不同等级用户的素材生成服务），可复用PDD支持可变NFE采样的设计，无需训练多模型即可适配不同时延要求'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
扩散/流匹配模型的迭代采样推理速度极慢，现有主流加速方案依赖VSD+对抗损失进行蒸馏，优化难度极高且易出现模式坍塌，导致生成样本多样性差、视频运动信息缺失。
### 方法关键点
轨迹式蒸馏方法PDD的架构与训练流程兼容任意预训练扩散/流匹配模型，支持可变NFE采样；单次网络前向即可预测多步去噪结果，无需使用JVPs或有限差分近似回归速度导数，大幅降低训练复杂度。
### 关键结果
在LTX-2.3文生视频/音频、Wan 14B文生视频、Qwen-Image文生图任务上，仅用4-8 NFE即可达到SOTA效果，且生成视频的多样性得到显著提升。
