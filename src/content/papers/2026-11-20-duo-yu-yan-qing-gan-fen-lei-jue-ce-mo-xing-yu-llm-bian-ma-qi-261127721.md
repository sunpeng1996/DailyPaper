---
title: 'Decision Models for Multilingual Emotion Classification: A Comparative Study
  Against LLMs and Encoders'
title_zh: 多语言情感分类决策模型：与LLM、编码器的对比研究
authors:
- Alessandro Piccolo
- Francesco De Nicolò
- Francesco Manco
- Eufemia Lella
affiliations:
- Sirio – Research & Innovation, Sidea Group, Bari, Italy
arxiv_id: '2611.27721'
url: https://arxiv.org/abs/2611.27721
pdf_url: https://arxiv.org/pdf/2611.27721
published: '2026-11-20'
collected: '2026-11-23'
category: Eval
direction: 多语言情感分类 · 模型性能对比评测
tags:
- Emotion Classification
- Zero-shot
- Multilingual
- Decision Model
- Latency Optimization
one_liner: 对比多语言情感分类场景下决策模型、通用LLM、微调编码器的效果与latency表现
practical_value: '- 零样本无标注场景下，决策模型可作为短文本分类默认选型，效果仅比目标域微调编码器低1个macro-F1点，latency为同基座LLM的1/5，还可输出选项级概率，适配电商评论情感识别、用户意图分类等场景

  - 同参数规模专用决策模型比通用LLM在分类任务上高10个macro-F1点，业务分类类任务优先选专用微调模型而非通用LLM，性价比更高

  - 跨域迁移场景下，零样本决策模型比其他域微调编码器效果高8-15个macro-F1点，无目标域标注时可直接选用，无需额外做跨域微调'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：决策模型在闭集分类任务上具备低延迟、prompt鲁棒性优势，但此前无跨语言场景下决策模型、通用LLM、微调编码器的系统性对比研究，也未验证零样本分类方案是否可替代微调方案
**方法关键点**：对比3款决策模型（Jev、OpenAI Decisions、Strands Decider 2B）、2款通用LLM（GPT-6 Luna、Qwen3.5-2B）、2款微调多语言编码器，在5种语言10个社交媒体数据集上开展4类情感分类任务，采用配对差异、等价检验做统计验证
**关键结果数字**：最优零样本方案平均仅比目标域微调编码器低1个macro-F1点，比其他域微调编码器高8-15点，比最强公开情感模型高6点；OpenAI决策端点效果与同基座GPT-6 Luna持平，latency仅为1/5；2B参数决策模型比同规模通用LLM高10个macro-F1点，增益来自训练策略而非决策格式；仅在最大数据集GoEmotions上微调方案优势显著
