---
title: 'PluraMath: Extending Mathematical Reasoning Evaluation Beyond High-Resource
  Languages'
title_zh: PluraMath：将数学推理评估拓展至高资源语言以外
authors:
- Daryna Dementieva
- Nikolay Babakov
- Kathy Hämmerl
- Ilseyar Alimova
- Jindřich Libovický
- Shu Okabe
- Miras Baisbay
- Lukas Edman
- Abrorkhon Inomkhujaev
- Antonia Karamolegkou
affiliations:
- Technical University of Munich (TUM)
- Charles University
- Inria
- Indian Institute of Technology Kharagpur (IIT Kharagpur)
- Nazarbayev University
arxiv_id: '2607.05992'
url: https://arxiv.org/abs/2607.05992
pdf_url: https://arxiv.org/pdf/2607.05992
published: '2026-07-06'
collected: '2026-07-08'
category: Eval
direction: 多语言大模型数学推理能力评估
tags:
- LLM Evaluation
- Mathematical Reasoning
- Multilingual LLM
- Low-resource Language
- Benchmark
one_liner: 构建覆盖18种低资源语言的数学推理基准PluraMath，测评27款大模型揭示跨语言推理性能差距
practical_value: '- 跨境多语言电商Agent推理能力测评可复用「机器预翻译+母语者校验」的低成本数据集构建流程，降低小语种测试集制作成本

  - 面向小语种市场的LLM推理类应用（如智能导购价格计算Agent）可直接用PluraMath基准预筛模型，优先选择指令跟随能力强的底座

  - 多语言大模型微调可参考其高低资源语言性能差的结论，针对性补充小语种推理类指令数据，缩小跨语言性能gap'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有数学推理基准严重偏向英、中等高资源语言，已有的PolyMath基准仅覆盖18种高资源语言，低资源语言的大模型推理能力评估存在显著空白，无法支撑多语言大模型迭代优化。
### 方法关键点
基于PolyMath拓展构建PluraMath基准，覆盖6大语系的18种中低/极低资源语言，采用「机器预翻译+母语者全量校验」的人在环路流水线构建数据集，开源完整数据集、采集流程与评测框架；选取27款不同规模（小/中/大/闭源合集）的推理类LLM开展跨语言数学推理能力测评。
### 关键结果数字
高资源与低资源语言的数学推理性能存在显著差距，性能表现与模型指令跟随能力强相关；所有开源模型在极低资源语言上的准确率平均比英语低30%以上，闭源模型跨语言性能差距约为15%
