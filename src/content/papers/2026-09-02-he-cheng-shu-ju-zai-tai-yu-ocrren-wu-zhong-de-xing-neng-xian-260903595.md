---
title: How Far Can Synthetic Data Take Thai OCR?
title_zh: 合成数据在泰语OCR任务中的性能上限研究
authors:
- Kunat Pipatanakul
affiliations:
- Wayu Research
- Paxa Labs
arxiv_id: '2609.03595'
url: https://arxiv.org/abs/2609.03595
pdf_url: https://arxiv.org/pdf/2609.03595
published: '2026-09-02'
collected: '2026-09-14'
category: Multimodal
direction: 多模态 · 低资源语言OCR合成数据优化
tags:
- OCR
- Synthetic Data
- Low-resource Language
- Transfer Learning
- Multimodal
one_liner: 拆解合成数据对泰语OCR迁移效果的影响因子，训练无真实标注的高性能泰语OCR模型
practical_value: '- 面向东南亚小语种电商的商品图文字识别、商家资质/订单文档识别等场景，可优先用合成数据替代高成本人工标注，仅需重点优化字体多样性、二维结构、手写字形3个核心因子，忽略非文本上下文降本

  - 训练粒度可按需选择：页面级训练适配固定版式的同域场景（如平台标准订单、报关单识别），裁剪级训练适配版式多样的跨域场景（如商家自主上传的商品主图文字识别）

  - 低算力部署场景可复用中小参数多模态基座微调，实验验证0.9B参数的PaddleOCR-VL微调后性能超过7B参数竞品，推理成本大幅降低'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有开源OCR模型、数据集集中覆盖中英等高资源语言，泰语等低资源语言缺乏高质量标注数据，合成数据虽可低成本生成大规模标注样本，但影响其向真实场景迁移效果的核心因子未被明确拆解。
### 方法关键点
通过可控文档重建pipeline拆分合成数据的源域匹配、页面上下文、排版、空间结构、字形变异5类维度的影响，分别在页面级、裁剪级两种训练粒度下，测试打印体、手写体泰语OCR的迁移性能差异。
### 关键结果数字
非文本上下文对迁移效果无显著影响，字体多样性、二维结构、真实手写字形可显著提升迁移效果；仅用45723张合成页微调0.9B参数的PaddleOCR-VL基座，打印体中位数字错率从6.64%降至1.24%，手写体从74.87%降至20.55%，全5个测试集指标优于7B参数的Typhoon OCR v1
