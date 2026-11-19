---
title: 'LogT: Logically Think with Images for Visual Search'
title_zh: LogT：面向视觉搜索的图像逻辑推理框架
authors:
- Yanjun Fu
- Quanzeng You
- Jiadong Guo
- Yujie Lu
- Sai Charitha Akula
- Haiping Wu
- Miao Liu
- Sanghamitra Dutta
- Lu Yuan
affiliations:
- Meta Superintelligence Labs
- University of Maryland
arxiv_id: '2611.19200'
url: https://arxiv.org/abs/2611.19200
pdf_url: https://arxiv.org/pdf/2611.19200
published: '2026-11-13'
collected: '2026-11-19'
category: Agent
direction: VLM Agent · 视觉搜索工具调用优化
tags:
- VLM
- Tool Call
- SFT Data Engine
- Visual Search
- Reinforcement Learning
one_liner: 通过逻辑链引导的自动化SFT数据引擎，提升VLM视觉搜索的工具调用效率与推理性能
practical_value: '- 做工具调用类Agent的SFT数据集时，可复用本文逻辑链引导+人类推理策略模拟的范式，优先提升数据质量而非堆数据量，训练成本可降低1~2个数量级

  - 电商图搜、商品细粒度识别（如标签OCR、属性识别）场景，可直接复用LogT的Zoom-in训练范式，仅SFT即可超过现有SOTA，且工具调用次数减少2倍以上，降低推理时延

  - 对Agent做RL优化前先保障SFT数据质量，可大幅提升RL性能上限，无需设计复杂的工具专用奖励函数，通用的正确性+格式奖励即可达到最优效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有VLM做细粒度视觉搜索时，需调用Zoom-in工具补全视觉细节，但过往方案依赖SFT+复杂RL训练，存在推理逻辑混乱、工具调用冗余、训练成本极高的问题，核心瓶颈被错判为RL复杂度不足，实际是SFT数据质量差。

### 方法关键点
- 全自动SFT数据引擎LogT分两个模块：① 面向对象的QA合成：输入高清图+目标区域的上下文/聚焦裁剪图，生成针对细粒度细节的高难度QA，经VLM-as-Judge过滤后仅保留无工具时基座VLM正确率极低的难例；② 逻辑链引导的推理轨迹合成：模拟人类3种视觉推理策略（直接回答/多跳推理/穷举搜索）生成逻辑链骨架，再引导生成带规范Zoom-in调用的结构化推理轨迹。
- 训练仅需用LogT合成的7.1k条SFT数据微调基座，再叠加无工具专属设计的简单RL（仅正确性+格式奖励）即可。

### 关键结果
基于Qwen2.5-VL-7B基座，在7个视觉搜索基准上对比SOTA：① 仅用LogT-SFT，数据量少3.1×、GPU小时少120×的情况下，性能超过SOTA；② 叠加简单RL后，比SOTA平均高9.59个点，工具调用准确率达94.21%，调用次数减少2.3×。

> 最值得记住的话：对工具调用类Agent任务，高质量SFT数据的收益远高于堆数据量和复杂RL设计。
