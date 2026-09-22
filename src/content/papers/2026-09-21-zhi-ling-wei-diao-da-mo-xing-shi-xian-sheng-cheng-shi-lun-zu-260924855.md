---
title: 'Extracting Arguments, Not Just Classifying Them: Instruction-Tuned LLMs for
  Generative Component Detection'
title_zh: 指令微调大模型实现生成式论元组件检测：同步完成边界识别与分类
authors:
- Sofiane Elguendouze
- Erwan Hain
- Elena Cabrio
- Serena Villata
affiliations:
- Université Côte d'Azur
- CNRS
- INRIA
- I3S
arxiv_id: '2609.24855'
url: https://arxiv.org/abs/2609.24855
pdf_url: https://arxiv.org/pdf/2609.24855
published: '2026-09-21'
collected: '2026-09-22'
category: LLM
direction: 指令微调LLM · 生成式信息提取
tags:
- Instruction Tuning
- Large Language Model
- Argument Mining
- Sequence Generation
- Information Extraction
one_liner: 将论元组件检测重构为生成任务，通过紧凑指令微调LLM实现端到端检测，性能优于现有SOTA
practical_value: '- 可复用「将序列标注+分类的联合任务重构为生成任务」的思路，解决电商评论观点提取、商品属性抽取等场景的多步骤任务误差累积问题

  - 紧凑指令prompt的设计思路可迁移至LLM微调场景，降低推理时的token开销，适配高并发的业务调用需求

  - 对于需要同时做span识别+标签分类的信息抽取类Agent任务，可直接复用该框架的指令微调范式，省去预分段步骤'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有论元组件检测（ACD）多采用分段+分类的pipeline或简化序列标注方案，存在误差累积、依赖预分段输入的缺陷，端到端生成式方案研究较少。

### 方法关键点
提出ITFACD范式，将ACD重构为纯语言生成任务，基于指令微调LLM，用紧凑指令prompt引导模型直接从原始文本中输出论元span及对应类别（claim、premise等），无需前置分段预处理。

### 关键结果
在ACD标准基准上性能优于现有SOTA系统，是首个将ACD完全建模为生成任务的方案之一，验证了指令微调对复杂论元挖掘任务的适配性，代码与数据集已开源。
