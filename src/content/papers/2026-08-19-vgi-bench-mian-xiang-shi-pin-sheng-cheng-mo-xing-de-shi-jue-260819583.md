---
title: 'VGI-BENCH: Probing Visual Intelligence in Video Generation Models'
title_zh: VGI-BENCH：面向视频生成模型的视觉智能探测基准
authors:
- Xuan He
- Cong Wei
- Yuhao Cheng
- Linrui Ma
- Yuxuan Zhang
- Zuojun Li
- Yuhao Wen
- Zeyi Liu
- Yuren Hao
- Songcheng Cai
affiliations:
- University of Illinois Urbana Champaign
- Tsinghua University
- University of Waterloo
- Massachusetts Institute of Technology
- Microsoft Research
arxiv_id: '2608.19583'
url: https://arxiv.org/abs/2608.19583
pdf_url: https://arxiv.org/pdf/2608.19583
published: '2026-08-19'
collected: '2026-08-27'
category: Eval
direction: 生成式视频 · 视觉智能评测基准
tags:
- Video Generation
- Evaluation Benchmark
- Visual Reasoning
- Denoising Process
- Zero-shot Capability
one_liner: 构建含27项任务810实例的分层评测基准，探测视频生成模型视觉推理能力并定位现有模型瓶颈
practical_value: '- 电商商品/广告短视频生成团队可复用该基准的分层任务设计，验证生成视频的时序逻辑合理性（如商品使用流程、场景演化是否符合常识），避免单帧合理但整体逻辑矛盾的问题

  - 可借鉴其失败模式、输入敏感度分析方法，定位短视频生成bad case根因，针对性优化微调数据集与prompt模板

  - 视频生成模型后期去噪仅优化细节不修正推理错误，工程上可将逻辑校验前置到生成初始阶段，减少无效计算'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有视频生成模型的视觉推理能力缺少可靠评测方案，以往基准仅校验最终帧合理性，未考虑时序演化逻辑，也未匹配现有模型的视觉先验与能力边界，任务难度区分度差。
**方法关键点**：构建VGI-BENCH，包含27项细分视觉推理任务、810个评测实例，采用「任务域-技能标签」双层分类体系支持细粒度能力评估；除最终帧合理性外，额外校验视频时序演化过程的合法性，同时校准任务难度保证评测区分度。
**关键结果**：现有最强视频生成模型Seedance 2.0的评测准确率仅为51.0%，整体能力远未达到可靠水平；分析发现模型自校正能力极弱，后期去噪步骤仅优化细节、无法修正前期生成的逻辑错误，同时对输入条件敏感、合成微调的能力迁移边界有限。
