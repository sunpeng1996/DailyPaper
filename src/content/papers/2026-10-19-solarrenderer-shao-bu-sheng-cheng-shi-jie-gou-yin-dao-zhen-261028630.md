---
title: 'SolarRenderer: Few-Step Generative Reference Rendering'
title_zh: SolarRenderer：少步生成式结构引导真实感视频渲染引擎
authors:
- Guian Fang
- Shengju Qian
- Dongyue Lu
- Junchao Huang
- Lutao Jiang
- Xin Wang
- Yiren Song
- Li Jiang
- Mike Zheng Shou
affiliations:
- NUS
- LIGHTSPEED
- CUHK(SZ)
- SLAI
- HKUST(GZ)
arxiv_id: '2610.28630'
url: https://arxiv.org/abs/2610.28630
pdf_url: https://arxiv.org/pdf/2610.28630
published: '2026-10-19'
collected: '2026-10-21'
category: Other
direction: 可控视频生成 · 少步加速泛化
tags:
- Video Generation
- LoRA
- Controllable Generation
- Distribution Matching
- Real-time Rendering
one_liner: 基于双轻量LoRA适配冻结大视频backbone，4步实现跨结构实时渲染，泛化到11种训练未见结构
practical_value: '- 做可控生成类任务（如电商商品短视频生成、Agent交互内容生成）时，可复用「条件输入注入预训练模型原生参考通路+匹配RoPE位置+文本描述约束规则」的设计，无需额外新增ControlNet分支，仅用轻量LoRA即可实现跨类型条件控制，大幅降低适配新条件类型的成本

  - 少步加速场景可借鉴「先训练控制模块再冻结控制模块训练加速模块」的解耦训练范式，配合条件引导的分布匹配蒸馏，既保留控制精度又实现数倍提速，适合实时交互类生成场景落地

  - 条件生成任务的训练数据建设优先做对齐校验（如时序、空间对齐检查），高对齐度的小样本效果远优于低对齐度的大样本，无需盲目堆数据量，可大幅降低数据采集和标注成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有结构引导的视频渲染器存在三大痛点：一是绑定特定引擎的结构表示，适配新结构需要重新训练模型，泛化性差；二是需要几十步去噪采样，速度慢无法支持交互场景；三是训练数据帧对齐度低，控制精度不足，难以落地到Agent驱动内容生成、电商短视频批量生产、游戏开发等场景。
### 方法关键点
- 架构设计：冻结MiniMax-H3 33B预训练视频backbone，仅新增两个轻量LoRA分别实现结构控制和采样加速，无额外定制化分支；结构视频直接输入原生参考通路，每个结构帧匹配对应目标帧的RoPE位置，不添加类型标识符，仅通过固定文本描述结构的约束规则，单控制LoRA即可适配任意结构表示
- 训练范式：解耦控制与加速任务，第一阶段训练控制LoRA学习结构对齐，第二阶段冻结控制LoRA，基于结构引导的分布匹配蒸馏训练加速LoRA，放大结构信号避免蒸馏后画质和控制精度下降
- 工程优化：块因果注意力+KV cache支持流式输出，768p视频渲染帧率最高达28FPS，满足实时交互需求
- 数据建设：构建136K帧对齐的结构-视频对语料（共243小时），覆盖8个来源，提前通过时空对齐校验过滤低质量样本
### 关键结果
在覆盖16种结构表示的泛化基准（含11种训练未见结构）和分布内测试集上，4步渲染效果达到SOTA，速度是50步采样的12.3倍；流式变体的渲染效果超过所有现有同类型流式渲染器。
### 核心结论
可控生成任务中，复用预训练模型原生能力+轻量适配器的设计，既能实现跨类型条件泛化，又能大幅降低训练和落地成本
