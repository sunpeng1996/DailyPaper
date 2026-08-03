---
title: 'Small Is Enough: Per-User Style Rewriting of AI-Edited Text via LoRA Adapters'
title_zh: 小模型足够：基于LoRA适配器的AI编辑文本单用户风格重写
authors:
- Antorweep Chakravorty
affiliations:
- University of Stavanger, Norway
arxiv_id: '2607.29238'
url: https://arxiv.org/abs/2607.29238
pdf_url: https://arxiv.org/pdf/2607.29238
published: '2026-07-31'
collected: '2026-08-03'
category: LLM
direction: 个性化文本改写 · LoRA小模型微调
tags:
- LoRA
- Small Language Model
- Text Style Transfer
- Parameter Efficient Fine-Tuning
- Personalized NLP
one_liner: 提出隐私优先的单用户风格重写系统InMyStyle，用小模型+LoRA实现推理无需提示的个性化文本改写
practical_value: '- 电商个性化文案生成场景可复用该范式：针对商家/达人历史文案，用小模型+LoRA微调专属风格适配器，推理无需额外prompt即可生成符合账号风格的推广文案、商品详情，效果比通用prompt工程更稳定

  - 低算力需求的个性化任务可优先尝试0.5B-7B量级小模型，风格匹配类任务存在性能天花板，小模型足够达到 plateau，无需盲目堆叠大模型参数，可大幅降低推理与微调成本

  - 缺乏标注对的个性化微调场景可借鉴「本地辅助LLM生成配对样本」的方案，无需人工标注即可构建训练语料，适合C端用户个性化、商家个性化等冷启动场景'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
AI辅助编辑生成的文本易丢失用户独有的措辞、句式与表达风格，现有个性化改写方案要么推理需要输入复杂风格prompt，要么数据隐私性差、算力成本过高，缺乏面向单用户的轻量隐私友好落地方案。
### 方法关键点
1. 用多个本地辅助LLM将用户原始文本转换为AI改写变体，自动构造<AI改写文本, 用户原始文本>配对训练语料，无需人工标注；
2. 仅对0.5B-7B量级小基座微调LoRA适配器，采用response-only loss约束优化目标为符合用户风格的目标token；
3. 内置长度感知生成预算与自动分块机制，适配不同长度输入。
### 关键结果
- 219组科学论文评估对测试中，所有模型尺寸的自动综合得分均稳定在0.69（满分1），greedy与采样解码下无明显差异，性能出现明显天花板；
- 5个LLM评委的400次评分显示，InMyStyle输出的AI感知度比输入的AI生成文本低20%以上，同系列内模型尺寸越大AI感知度越低
