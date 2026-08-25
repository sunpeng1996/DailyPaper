---
title: Grounding Free-Form Instructions for Fashion Complementary Image Generation
title_zh: 面向时尚搭配场景的自由形式指令引导互补图像生成
authors:
- Matteo Attimonelli
- Claudio Pomo
- Alessandro De Bellis
- Danilo Danese
- Dietmar Jannach
- Tommaso Di Noia
affiliations:
- Politecnico di Bari
- Sapienza University of Rome
- University of Klagenfurt
arxiv_id: '2608.23302'
url: https://arxiv.org/abs/2608.23302
pdf_url: https://arxiv.org/pdf/2608.23302
published: '2026-08-24'
collected: '2026-08-25'
category: GenRec
direction: 生成式推荐 · 多模态时尚搭配生成
tags:
- Multimodal Generation
- Fashion Recommendation
- Flow Matching
- Text-to-Image
- RecSys Benchmark
one_liner: 提出支持自由文本指令的时尚搭配衣品生成模型StyleFlow及多粒度指令标注基准
practical_value: '- 电商服饰搭配场景可直接复用该架构，基于用户输入的自由穿搭需求+现有单品图生成符合要求的互补商品图，提升搭配推荐的交互性

  - 多粒度指令标注方法可迁移：用VLM自动生成低/中/高特异性指令再人工校验，大幅降低指令类数据集的标注成本

  - 单多模态Transformer联合建模种子图+指令的设计，相比多辅助模块方案推理成本更低，适合落地到C端实时交互场景'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有时尚互补图像生成（CIG）任务基准依赖刚性模板prompt，无法匹配真实场景下用户的自然穿搭查询需求，也无法验证模型对不同粒度语言指令的响应能力。
### 方法关键点
1. 定义自由形式指令驱动的CIG任务范式，输入为种子衣品图像+自然语言穿搭需求，输出风格匹配的互补商品图像；
2. 采用VLM自动生成低/中/高三种特异性指令，经人工校验后完成3个现有CIG基准数据集的增强；
3. 提出StyleFlow模型，基于Rectified Flow Matching架构，通过单个多模态Transformer同时对种子图像、文本指令做条件建模，无需额外辅助模块。
### 关键结果
跨图像质量指标、商品目录对齐分析、消融实验及人类评估结果显示，StyleFlow生成结果的指令对齐度、风格连贯性均优于基线方案，且架构复杂度更低，推理成本较辅助模块类方案显著降低。
