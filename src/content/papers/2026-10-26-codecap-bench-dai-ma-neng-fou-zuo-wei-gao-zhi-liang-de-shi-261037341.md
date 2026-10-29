---
title: 'CodeCap-Bench: Can Code Serve as a Good Video Caption?'
title_zh: CodeCap-Bench：代码能否作为高质量的视频字幕？
authors:
- Jiafu Tang
- Yifan Xu
- Eric Tang
- Junjie Zhao
- Shipeng Luo
- Te Sun
- Haoxuan Hu
- Yiyan Ji
- Xinlong Chen
- Zihao Wang
affiliations:
- NJU
- Kling AI
- TJU
- SJTU
- CASIA
arxiv_id: '2610.37341'
url: https://arxiv.org/abs/2610.37341
pdf_url: https://arxiv.org/pdf/2610.37341
published: '2026-10-26'
collected: '2026-10-29'
category: Multimodal
direction: 多模态视频表示 · 大模型评测
tags:
- Multimodal LLM
- Video Caption
- Benchmark
- Code Generation
- Evaluation
one_liner: 提出代码作为视频字幕的新范式，推出CodeCap-Bench评测多模态大模型的代码字幕生成能力
practical_value: '- 电商商品动态展示视频、直播画面的结构化归档，可参考代码字幕范式，用可执行代码精确存储空间布局、时序动作信息，降低存储成本同时提升检索召回精度

  - 短视频推荐场景下的用户兴趣建模，可借鉴代码字幕的细粒度结构化表示能力，提取视频中商品的运动轨迹、布局变化等特征，提升对动态内容的理解准确率

  - 多模态Agent处理视频类用户查询时，可将代码字幕作为中间表示，相比自然语言字幕减少歧义，提升QA回答的推理精度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频字幕依赖自然语言，描述细粒度空间结构、时序动态时冗长且歧义多，无法满足高精度下游任务需求。

### 方法关键点
1. 提出可执行代码作为视频字幕的新范式，通过图元、布局规则、时序函数存储视频信息；
2. 构造CodeCap-Bench评测基准，包含5类结构化2D内容共323个视频，配套细粒度标注与多层级评估框架，衡量MLLM生成可信代码字幕的能力；
3. 在下游QA、视频重建任务上对比代码字幕与自然语言字幕的效果。

### 关键结果数字
代码字幕相比自然语言字幕，推理精度、重建保真度均更优；头部闭源MLLM代码字幕生成能力表现尚可，但捕捉复杂时序动态的准确率仍不足，开源MLLM性能较闭源差距显著。
