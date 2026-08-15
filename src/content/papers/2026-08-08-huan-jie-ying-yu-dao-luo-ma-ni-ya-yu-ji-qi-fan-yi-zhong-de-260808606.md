---
title: Mitigating Gender Bias in English to Romanian Machine Translation
title_zh: 缓解英语到罗马尼亚语机器翻译中的性别偏见问题
authors:
- Ioana Grigore
- Sergiu Nisioi
affiliations:
- University of Bucharest
- Human Language Technologies Research Center
- Faculty of Mathematics and Computer Science, University of Bucharest
arxiv_id: '2608.08606'
url: https://arxiv.org/abs/2608.08606
pdf_url: https://arxiv.org/pdf/2608.08606
published: '2026-08-08'
collected: '2026-08-15'
category: Other
direction: 机器翻译偏见缓解 · LLM+NMT混合架构
tags:
- Gender Bias
- Machine Translation
- LLM
- Fine-tuning
- Transformer
one_liner: 结合LLM性别分类与标签感知NMT的混合管线，将英译罗性别翻译准确率提升超40pct
practical_value: '- 跨境电商多语言文案翻译场景下，对职业、用户称谓等性别敏感词汇可插入前置hint标签，避免翻译输出默认阳性引发的用户反感，提升本地化适配效果

  - 当需要修正生成模型的固有偏见时，无需端到端重训大模型，可复用「前置语义识别打标+下游轻量微调模型感知标签生成」的低本高效管线

  - 面向源语言语义隐含、目标语言要求显式语法属性对齐的生成任务，可直接借鉴该混合架构思路，兼顾大模型语义理解能力与小模型生成可控性'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
从性别中立的英语翻译到需要显性语法性别一致的罗马尼亚语时，现有机器翻译系统常默认输出阳性形式，强化性别刻板印象，且暂无针对该语言对的专项性别偏见缓解方案。
### 方法关键点
1. 构建3个用于性别消歧与翻译的新数据集支撑任务训练与评测
2. 混合管线架构：首先微调LLaMA识别英文句中目标词的指代性别，插入inline性别提示标签；再将带标签句子输入微调后的标签感知Transformer NMT模型，生成形态正确的罗马尼亚语译文
### 关键结果数字
在WinoMT、WinoGender基准上，性别翻译准确率较基线MT系统提升超40个百分点，是首个结合LLM推理与标签感知翻译的英译罗性别偏见优化方案
