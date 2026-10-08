---
title: 'AdSpark: A Large-Scale Dataset and Benchmark for Product-Centric Advertisement
  Video Generation'
title_zh: AdSpark：面向商品中心广告视频生成的大规模数据集与基准
authors:
- Zhifei Yang
- Zhao Jiang
- Keyang Lu
- Honghe Zhu
- Zheng Zhang
- Jingjing Lv
- Changping Peng
- Ching Law
- Zhen Xiao
affiliations:
- Peking University
- JD.com
arxiv_id: '2610.10047'
url: https://arxiv.org/abs/2610.10047
pdf_url: https://arxiv.org/pdf/2610.10047
published: '2026-10-06'
collected: '2026-10-08'
category: GenRec
direction: 生成式广告 · 数据集与评估基准
tags:
- Advertisement Generation
- Dataset
- Benchmark
- E-commerce
- Video Generation
one_liner: 发布30万样本的电商商品广告视频生成数据集AdSpark及配套多维度评估基准
practical_value: '- 可直接复用AdSpark-Bench的6维度评估框架，重点参考产品保真度、卖点呈现、广告效果3个业务专属维度，快速搭建自家商品推广视频生成效果的量化评估体系，无需从零设计指标。

  - 训练电商广告视频生成模型时，可参考AdSpark的结构化标注范式，给训练数据补充产品身份、核心卖点、创意分镜、对齐音频脚本4类标签，能大幅提升生成内容的业务适配性。

  - 现有开源视频生成模型适配电商场景时，优先选择LoRA在垂直广告数据集上微调，实测该方案可将跨镜头产品一致性提升181%、叙事连贯性提升166%，投入产出比远高于从零训练模型。'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
当前电商广告视频生产依赖专业人工团队，成本高、周期长，无法满足海量SKU的推广需求；通用视频生成模型仅关注画质、语义对齐等通用能力，无法满足商品广告“保留产品细粒度身份特征、清晰呈现卖点、多镜头叙事连贯”的核心业务需求，且业内缺乏大规模电商广告专属数据集和面向商业效果的评估体系，导致该方向落地困难。

### 方法关键点
- 发布AdSpark-300K数据集：包含10万真实广告+20万合成广告样本，共30万组参考图-提示词-视频三元组，覆盖40个商品大类、3000+子类，总时长651小时，每样本标注产品身份、卖点、创意分镜、对齐音频脚本4类结构化信息。
- 配套AdSpark-Bench评估基准：从视觉质量、产品保真度、指令遵循度、时序连贯性、音频对齐度、广告效果6个维度，提供20+细分量化指标，支持多镜头广告的场景化评估。
- 数据集构建采用双管线：真实数据用SAM2做产品跟踪过滤、Qwen3-VL做质量校验，合成数据用大模型生成结构化创意脚本后生成视频，经人工校验后入库。

### 关键实验
在220个跨品类、SKU互不重叠的测试用例上，对比了18个主流开源/闭源视频生成模型，结果显示通用模型普遍存在产品特征漂移、卖点呈现不足的问题；用AdSpark-300K对LTX-2做LoRA微调后，跨镜头产品一致性从33.30提升到93.59，分镜结构对齐度从46.29提升到77.53，叙事连贯性从33.77提升到89.89，广告相关能力提升显著。

### 核心结论
面向电商场景的生成式内容落地，垂直场景的结构化标注数据集和业务导向的评估体系，比通用大模型本身的性能提升对业务效果的贡献更直接。
