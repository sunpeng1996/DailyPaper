---
title: 'From Synthesis to Removal: Physics-Grounded Reflection Simulation and Diffusion-Based
  Video Dereflection'
title_zh: 《从合成到去除：物理驱动反射模拟与扩散式视频去反射》
authors:
- Zepeng Wang
- Jiagao Hu
- Fuhao Li
- Yuxuan Chen
- Fei Wang
- Daiguo Zhou
affiliations:
- MiLM Plus, Xiaomi Inc.
arxiv_id: '2608.11562'
url: https://arxiv.org/abs/2608.11562
pdf_url: https://arxiv.org/pdf/2608.11562
published: '2026-08-11'
collected: '2026-08-13'
category: Other
direction: 视频修复 · 扩散模型落地
tags:
- Diffusion Model
- Video Restoration
- Reflection Removal
- Data Synthesis
- Benchmark
one_liner: 提出包含物理反射合成、扩散去反射模型及专用基准的闭环视频去反射框架
practical_value: '- 电商商品素材处理场景可直接复用该去反射能力，优化隔玻璃拍摄的商品视频/图片画质，提升素材利用率

  - 缺标注配对数据时可参考「物理规则约束+生成模型渲染」的合成思路，低成本生成高质量训练数据，降低标注成本

  - 预训练扩散模型适配下游任务时，可采用「任务感知隐层适配+轻量后处理」的方案，兼顾效果与推理速度，适配线上低延迟需求

  - 业务场景无公开评估基准时，可参考S2R-Bench的设计，同时覆盖自动指标评估与真人感知评估，统一效果衡量标准'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
隔玻璃拍摄的视频普遍存在反射伪影，会降低视觉质量、干扰下游视觉任务；现有视频去反射方向研究不足，核心痛点为缺乏配对训练数据、时序一致性的去除模型、专用评估基准。
### 方法关键点
提出闭环S2R框架，包含三大核心模块：
1. S2R-Synthesis合成管线：基于物理规则模拟玻璃粗糙度模糊、厚度重影、反射率变化等特征，结合视频扩散渲染器生成配对的含反射/无反射视频；
2. S2R-Removal去反射模型：首个基于扩散的视频去反射模型，基于预训练视频扩散先验做反射感知隐层适配，加一步像素几何精修，单步去噪即可输出干净视频；
3. S2R-Bench评估基准：首个视频去反射专用基准，同时支持全参考自动评估与真人感知评估。
### 关键结果
在S2R-Bench和多个公开图像基准上达到SOTA性能，推理速度优于非扩散类基线方案，验证了合成数据方案的有效性。
