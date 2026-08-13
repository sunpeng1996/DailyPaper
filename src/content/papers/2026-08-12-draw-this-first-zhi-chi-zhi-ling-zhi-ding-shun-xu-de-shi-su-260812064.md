---
title: Draw This First
title_zh: 《Draw This First：支持指令指定顺序的矢量速写生成模型》
authors:
- Dazhi Zhong
- Rowan Bradbury
- Grant Davis
affiliations:
- Krea.ai
- Wand Technologies
- Bradbury Group
arxiv_id: '2608.12064'
url: https://arxiv.org/abs/2608.12064
pdf_url: https://arxiv.org/pdf/2608.12064
published: '2026-08-12'
collected: '2026-08-13'
category: Other
direction: 多模态矢量生成 · 文本指令控制
tags:
- Text-to-Sketch
- Vector Generation
- Flow Matching
- VAE
- Instruction Following
one_liner: 通过预测2D绘制顺序场，实现可遵循文本指定顺序的矢量速写生成与图像转矢量
practical_value: '- 电商手绘短视频/商品卖点草图生成场景，可复用文本指定绘制顺序的逻辑，生成符合用户认知的绘画过程类营销内容

  - 商品线稿矢量化场景，可借鉴VAE解码器输出顺序场+分割的架构，替代传统逐笔画自回归方案，降低推理延迟

  - 多模态指令对齐任务中，可复用「约束排列训练+程序化生成对应指令caption」的方案，大幅降低标注成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统速写生成采用逐笔画自回归预测范式，推理延迟高，且无法灵活指定绘制顺序，难以适配需展示绘画过程的内容生产场景；现有模型多基于低质量涂鸦数据集训练，生成效果达不到商用标准。
### 方法关键点
1. 反转传统生成逻辑，先预测定义笔画绘制顺序的2D场，而非逐笔画生成；2. 复用预训练隐空间流匹配Transformer提供图像先验，训练VAE解码器输出顺序场、笔画掩码、笔画分割三类结果；3. 预测分割结果矢量化为多段线后按顺序场排序得到最终有序矢量速写，训练时采用约束排列+程序化生成匹配指令的方案，支持文本指定任意绘制顺序。
### 关键结果数字
基于47318份高质量艺术家手绘作品数据集训练，支持文生有序矢量速写、图像转有序矢量两类任务，均可100%遵循文本指令调整绘制顺序
