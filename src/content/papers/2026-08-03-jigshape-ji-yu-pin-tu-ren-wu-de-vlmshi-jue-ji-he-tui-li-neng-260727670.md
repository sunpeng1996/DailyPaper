---
title: 'JigShape: Evaluating Visual-Geometric Reasoning in VLMs through Jigsaw Puzzles'
title_zh: JigShape：基于拼图任务的VLM视觉几何推理能力评估基准
authors:
- Shawn Li
- Wei Yang
- Jike Zhong
- Jiate Li
- Jiawei Yang
- You Qin
- Ryan Rossi
- Franck Dernoncourt
- Roger Zimmermann
- Yue Wang
affiliations:
- University of Southern California
- National University of Singapore
- Adobe Research
- Texas A&M University
- Rice University
arxiv_id: '2607.27670'
url: https://arxiv.org/abs/2607.27670
pdf_url: https://arxiv.org/pdf/2607.27670
published: '2026-08-03'
collected: '2026-08-12'
category: Eval
direction: 多模态大模型 · 视觉几何推理能力评估
tags:
- VLM
- Geometric Reasoning
- Evaluation Benchmark
- Multimodal
- Jigsaw Puzzle
one_liner: 提出带凹凸互锁拼图的VLM几何推理评估基准，验证当前VLM存在几何推理规模悬崖
practical_value: '- 做多模态商品理解、3D商品建模、家装搭配推荐等空间相关任务时，不可默认现有VLM具备强几何推理能力，需针对几何约束做专项微调

  - 开发多模态Agent（如虚拟试穿、商品空间布局推荐）时，需额外引入独立几何规则校验模块，弥补VLM空间推理短板

  - 评估多模态模型的空间推理能力时，可复用JigShape的凹凸互锁拼图设计，规避矩形切割带来的真值歧义问题'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLM几何推理评估基准多采用矩形切割拼图，纹理重复区域易出现真值歧义，无法准确衡量模型视觉内容与几何约束的联合推理能力。
### 方法关键点
提出JigShape基准，采用带凸榫与凹槽的互锁拼图块，几何约束结合视觉内容确保真值唯一，覆盖4×4到16×16共4种网格密度，合计95K测试实例。
### 关键结果
- 零-shot场景下仅GPT-5.5在4×4拼图任务上超过随机基线，其余前沿VLM准确率均为随机水平
- 监督微调后4×4任务准确率可达97%以上，但所有模型均存在「规模悬崖」：GPT-5.5在8×8任务上准确率从70%降至接近随机，微调模型在12×12任务上准确率低于5%，说明当前架构无法随约束数量增长维持稳定推理能力
