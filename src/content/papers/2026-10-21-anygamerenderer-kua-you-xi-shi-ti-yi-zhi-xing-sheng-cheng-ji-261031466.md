---
title: 'AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an
  Entity-Level Benchmark'
title_zh: AnyGameRenderer：跨游戏实体一致性生成渲染及实体级基准
authors:
- Ruicong Liu
- Liangyang Ouyang
- Fengbo Lan
- Zhixiang Wang
- Kaipeng Zhang
affiliations:
- Alaya Lab
arxiv_id: '2610.31466'
url: https://arxiv.org/abs/2610.31466
pdf_url: https://arxiv.org/pdf/2610.31466
published: '2026-10-21'
collected: '2026-10-24'
category: Multimodal
direction: 多模态生成 · 实体一致性视频渲染
tags:
- Generative Rendering
- LoRA
- Video Generation
- Entity Consistency
- AI Agents
- Benchmark
one_liner: LoRA微调33B参考视频生成模型，实现低质游戏画面的实体一致高质量渲染
practical_value: '- 电商商品短视频/虚拟直播场景需保实体一致性的生成任务，可复用仅输入原始视频、LoRA微调参考条件视频生成模型的范式，无需额外接入引擎中间表示，降低适配成本

  - 多模态生成效果的实体一致性评估可参考该方案，构建带标注实体框的专用基准，替代主观评估，提升业务指标可量化性

  - 小样本多模态生成任务的数据集构建可复用混合范式：结合领域合成配对数据、真实数据弱监督重建配对数据，降低标注成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
AI 编码 Agent 可快速生成可玩小游戏，但输出仅为低质灰块、几何图元等「程序员美术」，现有生成渲染方案易丢失实体位置、时序、数量一致性，且依赖引擎 G-buffer 等复杂中间输入，落地成本高。
### 方法关键点
1. 视频到视频生成渲染 pipeline 仅需普通视频输入，无需额外复杂表示，适配塔防、赛车等多类游戏类型，渲染过程保留布局、相机、所有实体的位置与时序；
2. 基于 33B 参数 MiniMax-H3 ref2va 参考视频条件生成模型做 LoRA 微调；
3. 训练集包含约10k配对clip，来自Agent生成游戏多流渲染数据、Unreal Engine合成数据、真实游戏录屏3D框重建配对数据三类；
4. 配套含59个样例、753个实体的实体级基准用于一致性评估。
### 关键结果
相比基线模型，时序匹配率从50.9%提升至62.9%，实体数量变化漏检率从34.7%降至21.3%，实体幻觉、漏渲染问题显著减少。
