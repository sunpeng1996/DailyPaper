---
title: 'IWIBench: Evaluating Gradient-Free Model Driven Intra-weight Injection'
title_zh: IWIBench：无梯度模型驱动权内注入能力评估基准
authors:
- Chris von Csefalvay
- Pranav Doma
- Achyuthan Unni Krishnan
- Tamás Földi
affiliations:
- Robotics Intelligence CoE, HCLTech, Santa Clara, CA
arxiv_id: '2611.08647'
url: https://arxiv.org/abs/2611.08647
pdf_url: https://arxiv.org/pdf/2611.08647
published: '2026-11-04'
collected: '2026-11-10'
category: Eval
direction: 大模型权内注入能力评估
tags:
- Evaluation
- Gradient-Free
- Weight-Editing
- LLM
- Benchmark
one_liner: 提出首个无梯度权内注入能力评估基准IWIBench，量化大模型编辑小模型权重的能力
practical_value: '- 可尝试用无梯度权内注入快速更新推荐/广告场景LLM的商品知识、促销规则，无需全量finetune，大幅降低迭代成本

  - 权内注入的难易度分布可指导业务编辑优先级：优先落地alias绑定（如商品别名映射）、知识更新类需求，暂不投入资源到结构化输出强制、长度控制等高难度编辑场景

  - IWIBench的「目标达成度+原有能力保留度」双维度评估框架可直接复用，用来验证业务侧自研LLM权重编辑工具的效果'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
无梯度权内注入可直接编辑模型权重修改行为（如更新事实知识、调整输出规则），但此前无系统化评估体系量化不同大模型的编辑能力差异。

### 方法关键点
1. 构建IWIBench基准，设置10类文本编辑目标任务，要求大编辑器模型修改Gemma 3 4B IT小模型权重，仅开放4种权重读写工具、固定rollout生成与核验预算，需同时保留小模型原有能力；
2. 配套Validator模块在隔离环境应用补丁，对比编辑前后模型的目标达成度与能力保留度。

### 关键结果
1. Astra、GPT-6.1 Sol表现远超其他模型，该能力为近期训练新增（GPT-5.6 Sol几乎无对应能力）；
2. 任务难度差异极大：alias获取/重编码成功率最高，结构化响应任务全失败，回答长度控制仅1例成功；
3. 不同任务族的成功率相关性极低，权内注入能力发展极不均衡。
