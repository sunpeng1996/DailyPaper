---
title: 'Code2Video-Compass: A Comprehensive Benchmark for General-Purpose Code-Based
  Video Generation across T2V, I2V, and V2V'
title_zh: Code2Video-Compass：覆盖T2V/I2V/V2V的代码驱动视频生成基准
authors:
- Zhenghan Chen
- Zekai Shao
- Xin Lin
- Leting Cheng
- Siming Chen
affiliations:
- Fudan University
- Sun Yat-sen University
arxiv_id: '2610.28416'
url: https://arxiv.org/abs/2610.28416
pdf_url: https://arxiv.org/pdf/2610.28416
published: '2026-10-19'
collected: '2026-10-24'
category: Eval
direction: 多模态大模型 · 代码生成视频评估
tags:
- Video Generation
- MLLM
- Benchmark
- Evaluation
- Code Generation
one_liner: 推出覆盖T2V/I2V/V2V的代码驱动视频生成通用基准，含2104个任务与主客观双层评估体系
practical_value: '- 电商营销短视频自动化生成业务，可复用该基准的主客观评估指标体系，量化代码生成带货/宣传短视频的效果

  - 电商Agent自动生成商品展示视频的链路中，可参考其任务复杂度分层规则设计不同难度的prompt工程，提升生成成功率

  - 落地代码驱动可控视频生成场景时，可优先参考该基准的测评结果选型MLLM，减少前期验证成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有代码驱动视频生成基准多面向专项任务，缺乏覆盖T2V/I2V/V2V全模态、全创作场景的通用评估体系，无法全面衡量MLLM将多模态需求转化为可执行视频生成代码的能力。
### 方法关键点
1. 构建包含2104个任务的通用基准，覆盖10个视频类别、24个子类，复杂度按结构搭建、动态动画、状态依赖三个维度分层
2. 设计双层评估框架：12项客观指标覆盖运行性能、视频质量、文本-视频对齐、参考保真度；5项主观指标采用MLLM评审，衡量指令遵循度、整体视频质量等维度
### 关键结果数字
对9个系列共15款主流开源/闭源MLLM测评显示，即使头部模型也难以稳定生成符合要求的高质量视频，性能随任务复杂度提升明显下降
