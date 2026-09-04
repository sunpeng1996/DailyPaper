---
title: 'Autoregressive Mosaics: Probing 2D Spatial Reasoning in Text-Only Language
  Models'
title_zh: 自回归马赛克基准：探测纯文本大语言模型的二维空间推理能力
authors:
- Ashwin Nedungadi
- Stefan Oehmcke
- Stefan Lüdtke
affiliations:
- Institute for Visual & Analytic Computing, University of Rostock
arxiv_id: '2608.30751'
url: https://arxiv.org/abs/2608.30751
pdf_url: https://arxiv.org/pdf/2608.30751
published: '2026-08-31'
collected: '2026-09-04'
category: Reasoning
direction: 大语言模型 · 空间推理能力评测
tags:
- Spatial Reasoning
- LLM Benchmark
- Code Generation
- Model Probing
- SVG
- Autoregressive Generation
one_liner: 提出AM-Bench基准拆解纯文本LLM空间表达与代码生成能力，探明2D空间推理性能核心影响因素
practical_value: '- 做Agent生成电商可视化物料（如商品SVG示意图、自定义装修素材）时，优先指定LLM输出原始SVG而非过程式代码，可显著提升布局准确率

  - LLM选型时不能仅用代码生成能力评估空间推理水平，针对海报生成、自定义布局等场景需单独做开放式布局任务评测

  - 长序列生成类Agent可借鉴激活探查思路，提前抽取粗粒度生成计划，优化生成过程的一致性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
纯文本/代码预训练LLM可生成可识别图像的绘图代码，但无法区分该能力来自内部2D空间布局表征，还是仅为空间描述到代码的翻译能力，缺乏拆解两类能力的基准。

### 方法关键点
AM-Bench基准设置两类任务：一是翻译任务，给定完整几何描述prompt输出对应绘图代码；二是布局任务，给定非完备prompt自主组合生成图像；同时开展输出介质ablation对比过程式代码与原始SVG的效果，通过模型激活探查推理过程。

### 关键结果
8个开源纯文本/代码LLM的翻译任务均表现稳定，但开放式布局任务性能差异显著，排除代码生成能力单独影响；替换为SVG输出后所有模型布局得分均明显提升；激活探查显示生成前仅存在prompt对应粗粒度布局计划，生成过程中模型实时跟踪几何状态而非执行固定初始计划。
