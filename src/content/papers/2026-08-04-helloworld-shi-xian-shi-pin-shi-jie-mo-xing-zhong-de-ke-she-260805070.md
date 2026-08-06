---
title: 'HelloWorld: Enabling Socially Interactive Characters in Video World Models'
title_zh: HelloWorld：实现视频世界模型中的可社交交互角色
authors:
- Liangyang Ouyang
- Ruicong Liu
- Xuangeng Chu
- Kaipeng Zhang
- Yoichi Sato
affiliations:
- The University of Tokyo
- Alaya Lab
arxiv_id: '2608.05070'
url: https://arxiv.org/abs/2608.05070
pdf_url: https://arxiv.org/pdf/2608.05070
published: '2026-08-04'
collected: '2026-08-06'
category: Multimodal
direction: 多模态视频生成 · 虚拟角色实时交互
tags:
- Video World Model
- Social Interaction
- Self-Distillation
- DiT
- Video Generation
- Benchmark
one_liner: 提出支持用户与视频内角色实时社交交互的HelloWorld视频世界模型及配套评测基准
practical_value: '- 自蒸馏微调策略可直接复用在生成类模型优化流程中，用模型自身合成的带标注数据微调，大幅降低人工标注成本

  - 推理阶段修改DiT交叉注意力掩码实现时序局部生成可控的思路，可迁移到电商直播虚拟主播、生成式短视频推荐的实时交互触发场景

  - 针对业务核心场景自定义专项评测指标+通用指标的组合评估思路，可用于生成式推荐、Agent交互的效果量化'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频世界模型仅能生成固定时序的视频内容，不支持用户与场景内虚拟角色的实时社交交互，无法满足虚拟直播、互动内容生成等场景需求。
### 方法关键点
1. 提出自蒸馏微调流水线，用模型自身合成的同时包含社交交互动作和相机运动的样本微调，在学习相机姿态约束的同时不降低交互动作的生成质量；
2. 推理阶段引入免训练交互触发模块，用户触发交互时修改DiT的交叉注意力掩码，让交互相关文本prompt仅作用于触发窗口内的帧，实现交互响应的时序精准定位；
3. 构建含400个样本的HelloWorldBench评测基准，包含3个社交交互专项指标+3个传统生成质量指标，用于统一评估。
### 关键结果
交互效果全面超越各类基线模型，同时保持SOTA的画面美学效果和相机姿态跟随能力。
