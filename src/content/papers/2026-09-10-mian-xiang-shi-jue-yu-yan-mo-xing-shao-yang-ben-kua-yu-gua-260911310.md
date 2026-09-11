---
title: 'Your Model Already Knows Don''t Teach It, Learn to Ask It: Soft Prompting
  for Few-Shot Adaptation of Vision-Language Models'
title_zh: 面向视觉语言模型少样本跨域适配的软提示优化方法
authors:
- Gautam Rajendrakumar Gare
- Siyi Li
- Hewei Wang
- Cesar Daniel Hernandez
- Wei Zhao
- Wolfgang M. Pauli
- John Galeotti
- Deva Ramanan
affiliations:
- Carnegie Mellon University
- Apple
arxiv_id: '2609.11310'
url: https://arxiv.org/abs/2609.11310
pdf_url: https://arxiv.org/pdf/2609.11310
published: '2026-09-10'
collected: '2026-09-11'
category: Multimodal
direction: 多模态大模型 · 少样本软提示适配
tags:
- Soft Prompting
- VLM
- Few-shot Adaptation
- LoRA
- Cross-domain Detection
one_liner: 通过优化软提示放置与初始化策略，以极少量参数实现VLM少样本适配效果匹配LoRA且无遗忘
practical_value: '- 电商多模态搜索/商品识别冷启动场景，可采用「跨模态边界放置软提示+空token初始化」方案替代LoRA，训练参数量减少4个数量级，且不破坏原模型通用能力

  - 多模态Agent跨垂直域任务适配时，可直接复用学到的软提示到新VLM版本无需重训，大幅降低模型迭代的适配成本

  - 需同时保留VLM通用能力+垂直域能力的业务场景（如兼顾通用VQA和电商商品检测），优先选择软提示而非LoRA，完全避免灾难性遗忘'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有VLM跨域少样本适配方案以离散提示优化、LoRA微调为主，前者效果上限低，后者参数开销高、易引发灾难性遗忘，亟需轻量无遗忘的适配方案。
### 方法关键点
1. 软提示注入位置选择视觉token与文本token的跨模态边界，优于NLP领域常用的前缀放置策略
2. 采用语义为空的space token初始化软提示，效果优于语义初始化、随机初始化
3. 全程冻结预训练主干权重，仅优化极少量连续提示token
### 关键结果
- 10-shot跨域检测任务上，仅1-3个提示token（平均7168参数）在Roboflow20-VL基准上mAP达14.2，匹配最优LoRA配置，训练参数量少20000×
- 无灾难性遗忘：同精度LoRA会导致NaturalBench VQA精度相对下降35%，软提示则完全不影响原模型性能
- 软提示可直接迁移到Qwen3.5-9B无需重训，mAP提升0.8，还可转写为可读提示，效果匹配DetPO、优于GEPA
