---
title: 'Inherited, Not Invented: Tracing the Provenance of Wait in Reasoning Models'
title_zh: 推理模型反思标记“Wait”溯源：源于训练继承而非RL生成
authors:
- Zhizhuo Kou
- Sizai Hou
- Long Chen
- Jian Yang
- Junyu Luo
- Jingshu Peng
- Wenkai Zhang
- Sirui Han
- Yike Guo
affiliations:
- The Hong Kong University of Science and Technology
- Peking University
- Huawei Noah’s Ark Lab
arxiv_id: '2610.30882'
url: https://arxiv.org/abs/2610.30882
pdf_url: https://arxiv.org/pdf/2610.30882
published: '2026-10-22'
collected: '2026-10-23'
category: Reasoning
direction: LLM推理 · 反思标记起源与训练影响
tags:
- Reasoning Marker
- RL Tuning
- LLM Training
- Model Probe
- Interpretability
one_liner: 通过全训练谱系溯源证明推理模型的Wait反思标记来自训练数据而非RL主动生成
practical_value: '- 设计Agent推理监控规则时，不要将wait这类反思标记的出现频率作为RL带来推理能力提升的核心指标，这类标记本质来自训练数据继承，不会被RL凭空生成，避免无效特征研发

  - 训练需要输出反思类话术的推理Agent（比如电商导购、售后咨询）时，可直接在SFT阶段注入带反思标记的推理轨迹，远低于RL阶段优化的成本，且效果更稳定；若不需要这类冗余标记，选择KL-free
  GRPO训练即可自然消除，无需额外加惩罚项

  - 做LLM输出评估时不要完全依赖LLM-as-judge的行为标签，涉及话术类、反思类的判断极易出现与人类标注趋势相反的偏差，需补充规则类的直接标记测量作为兜底，比如电商场景的客服回复质量评估可大幅降低误判'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
此前业界普遍认为推理模型中出现的"Wait"等反思标记是RL训练让模型学会反思的标志性产物，即所谓的"aha moment"，但大量RL带来精度大幅提升的场景下并未出现这类标记，现有研究未验证标记的真实来源，也不清楚RL对标记的实际作用，容易导致对模型推理能力的误判、推理监控规则失效。
### 方法关键点
- 覆盖120个模型端点的全训练谱系分析，包含OLMo-3全训练阶段checkpoint、18组无标记基础模型的Zero-RL训练、14组无标记基础模型的推理轨迹微调实验，覆盖0.5B-32B多尺度模型
- 设计无标注的语言索引体系，从频率、位置、形式、用法四个维度量化标记的演化，搭配注入错误的告警测试衡量标记对错误的感知能力，全程无需人工或LLM标注
- 对比不同RL配方（RL-Zero、KL-free GRPO等）对已存在标记的影响，同时做标记移植实验验证来源
### 关键结果
- 18组从无Wait标记的基础模型开始的Zero-RL实验中，17组在MATH-500精度中位数提升42.9个点的情况下，Wait标记出现率始终低于0.05次/千token
- 14组基于无标记基础模型做推理轨迹SFT的实验中，13组成功获得Wait标记，出现率中位数达3.54次/千token
- 若基础模型已存在Wait标记，RL-Zero配方会将其频率放大2-3倍，KL-free GRPO则不会放大甚至可完全消除SFT注入的标记，SFT后再做RL对标记频率影响极小
- 测试的其中1个LLM judge对反思行为的标注完全反转人类趋势：其标注的revision率从26.0%降到12.9%，而人类共识标注是从1.3%升到15.9%
### 核心结论
推理模型的反思标记本质是训练数据的产物，RL只会改造已有的标记不会凭空生成，标记频率不能直接代表推理能力的提升
