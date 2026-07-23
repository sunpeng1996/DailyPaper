---
title: 'LKValues: Aligning Large Language Models with Sri Lankan Societal Values'
title_zh: LKValues：面向斯里兰卡社会价值观的大语言模型对齐方案
authors:
- Nethmi Muthugala
- Supryadi
- Surangika Ranathunga
- Nisansa de Silva
- Ruijie Tao
- Ovindu Gunatunga
- Pengyun Zhu
- Shaowei Zhang
- Jingting Zheng
- Deyi Xiong
affiliations:
- Tianjin University
- Massey University
- University of Moratuwa
- Johns Hopkins University
- University of Colombo
arxiv_id: '2607.20410'
url: https://arxiv.org/abs/2607.20410
pdf_url: https://arxiv.org/pdf/2607.20410
published: '2026-07-22'
collected: '2026-07-23'
category: LLM
direction: 大语言模型 · 跨文化价值对齐
tags:
- Value Alignment
- Low-resource LLM
- Cross-cultural LLM
- Instruction Tuning
- Evaluation Benchmark
one_liner: 首个面向斯里兰卡语境的LLM价值观对齐资源套件，含150k指令语料与千级评估基准，适配低资源文化对齐场景
practical_value: '- 针对出海小众市场的LLM Agent/内容生成场景，可复用「本地调研+LLM抽取本土价值观→指令微调+专项Benchmark评估」的全流程，解决文化适配问题

  - 多语言跨境推荐场景下，可参考文中低资源语言指令语料构造方法，基于本土新闻生成场景化对齐样本，降低跨语言输出偏差

  - 价值对齐微调效果存在模型家族依赖，落地时优先在同基座多尺度模型上做验证，再选定最优基座迭代，减少试错成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM价值对齐普遍偏向西方规范，缺乏斯里兰卡等低资源多语言文化的对齐基准与语料，无法适配本土文化语境的推理与生成需求。

### 方法关键点
1. 基于205名受访者的三语调研，融合通用价值框架与LLM抽取的本土概念，梳理出40个得到多数认可的斯里兰卡社会价值观
2. 构建15万条场景化僧伽罗语-英语指令微调语料LKvaluesIT，以及含1000条样本的价值敏感评估基准LKvaluesBench
3. 对Qwen3.5-4B/9B、Aya-Expanse-8B三款开源基座做对齐微调

### 关键结果数字
大模型仍存在显著的低资源文化对齐缺口，LKValues微调可降低Qwen系列模型的无效输出与跨语言偏差，对齐增益存在明显的模型家族依赖
