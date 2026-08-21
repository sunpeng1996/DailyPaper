---
title: Auditing Cross-Lingual Fairness in Language Model Watermarking
title_zh: 大语言模型水印的跨语言公平性审计
authors:
- Alexander Nemecek
- Osama Zafar
- Debargha Ganguly
- Vikash Singh
- Vipin Chaudhary
- Erman Ayday
affiliations:
- Case Western Reserve University
arxiv_id: '2608.20047'
url: https://arxiv.org/abs/2608.20047
pdf_url: https://arxiv.org/pdf/2608.20047
published: '2026-08-20'
collected: '2026-08-21'
category: Eval
direction: LLM水印 · 跨语言公平性评估
tags:
- LLM-Watermark
- Cross-Lingual-Fairness
- Evaluation-Framework
- Fairness-Audit
- Multilingual-LLM
one_liner: 提出4组件跨语言LLM水印公平性评估框架，验证性能差异由语系结构特性决定
practical_value: '- 跨境电商多语言AI文案、多语言Agent回复场景部署水印时，需按语系分别校准检测阈值，避免小语种漏检/误检

  - 评估跨语言水印效果可复用三类度量范式（分布/配对语义/参考困惑度），规避单度量带来的结论偏差

  - 多语言生成内容的合规性审计可直接复用该框架的广义熵差异分解方法，快速定位性能差异根因'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有LLM水印方案几乎仅在英文场景下完成评估，其默认检测阈值、狭窄的质量度量集在跨语言部署时会产生严重偏差，无法保障不同语言场景下的水印效果公平性。
### 方法关键点
提出4组件跨语言公平性评估框架：① 按部署场景经验校准的检测阈值；② 可区分校准失败与检测失败的阈值无关辅助度量；③ 三类互不重叠的质量度量范式（分布、配对语义、参考困惑度）；④ 基于语系划分的跨语言差异广义熵分解方法。
### 关键结果
在6种水印方案、3种开源生成模型、覆盖4种文字8个语系的11种语言、基座/指令微调两种模型范式下测试，可检出单语言单范式评估无法发现的失效模式，跨语言性能差异主要来自语系间结构差异，而非单一语言的特有属性。
