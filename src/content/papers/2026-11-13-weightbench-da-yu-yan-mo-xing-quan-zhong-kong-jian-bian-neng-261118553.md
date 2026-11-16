---
title: 'WeightBench: Evaluating Language Models as Weight-Space Programmers'
title_zh: WeightBench：大语言模型权重空间编程能力评估基准
authors:
- Aayush Marasini
- Barsat Khadka
- Nick Rahimi
affiliations:
- The University of Southern Mississippi
arxiv_id: '2611.18553'
url: https://arxiv.org/abs/2611.18553
pdf_url: https://arxiv.org/pdf/2611.18553
published: '2026-11-13'
collected: '2026-11-16'
category: Eval
direction: LLM能力评估 · 权重空间编程
tags:
- Weight-Space Programming
- LLM Evaluation
- Benchmark
- Model Editing
- Model Compression
one_liner: 推出含5赛道42项任务的WeightBench，量化评估LLM直接操作神经网络参数的WSP能力
practical_value: '- 可复用其开源OS-level sandbox框架，测试LLM直接编辑推荐模型小参数模块（如召回塔head、排序bias层）的可行性，适配轻量化调优场景

  - 参考其5类WSP任务设计思路，拓展内部LLM4Rec能力评估维度，例如验证LLM能否直接修复冷启动场景下小样本排序模型的权重错误

  - 当前前沿LLM仅能处理2K级小参数量模型的权重操作，业务侧暂不适合投入资源做7B级推荐大模型的直接权重编辑，可先在小模块试点'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前LLM已展现无需梯度下降、直接操作神经网络参数的权重空间编程(WSP)能力，但缺乏系统性评估该能力的统一基准，无法量化不同LLM的WSP水平差异。
### 方法关键点
推出WeightBench基准，覆盖5类赛道共42项WSP任务：权重读取、权重修复、权重生成、不可行编辑识别、无数据压缩，任务涉及的模型参数量覆盖2K级控制策略到7B级大语言模型，配套开源沙箱环境与实时排行榜。
### 关键结果数字
前沿LLM中GPT-6.1-sol在38项任务上得分0.568，Claude Opus 5.5全42项任务得分0.535，Sonnet 5.5、Haiku 5.5、DeepSeek v4-flash得分分别为0.466、0.402、0.215；当前模型仅能完成小网络读取、控制策略生成任务，暂不支持大模型补丁、无数据压缩、不可行编辑识别类任务。
