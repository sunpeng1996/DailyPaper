---
title: Vision-Language Grounding as Bidirectional Concept Correspondence
title_zh: 将视觉-语言定位建模为双向概念匹配任务
authors:
- Jieyu Zhang
- Ziqi Gao
- Luke Zettlemoyer
- Ranjay Krishna
affiliations:
- University of Washington
- Allen Institute for AI
- FAIR at Meta
arxiv_id: '2608.07886'
url: https://arxiv.org/abs/2608.07886
pdf_url: https://arxiv.org/pdf/2608.07886
published: '2026-08-07'
collected: '2026-08-11'
category: Multimodal
direction: 多模态 · 视觉语言双向定位对齐
tags:
- Vision-Language Grounding
- Multimodal Alignment
- Open-Vocabulary Detection
- Concept Correspondence
- Zero-shot Learning
one_liner: 提出双向视觉语言概念匹配框架ConCor-1，统一多类定位任务，性能大幅优于基线
practical_value: '- 电商商品多模态理解场景可复用双向匹配框架，无需提前指定文本片段即可自动对齐商品标题描述与图像中商品/属性区域，提升多模态召回准确率

  - 可复用bridge token设计实现跨模态特征对齐，降低多模态联合建模的工程复杂度，适配跨域零样本商品识别、多模态搜索等场景

  - 多任务统一数据集格式构建思路可迁移，将不同来源的商品图文标注数据转换为统一匹配格式，减少多任务数据标注成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有视觉-语言定位多为单向任务，需提前给定待匹配文本短语，无法自动识别文本中与视觉相关的片段，也无法同时完成文本分割、图像分割、跨模态对齐三类子任务。

### 方法关键点
将定位重新定义为图文对双向概念匹配任务，无需预设相关文本片段，即可自动恢复所有带视觉指代的文本片段与实例级图像区域的对应关系；基于预训练视觉语言模型搭建ConCor-1，引入可学习bridge token表征候选图文匹配对，为每个token预测文本掩码、图像掩码及匹配存在得分；将多类定位、分割数据集转换为统一匹配格式用于训练评估。

### 关键结果
长字幕数据集上匹配F1较基线提升48%，零样本LVIS数据集上匹配F1提升29%。
