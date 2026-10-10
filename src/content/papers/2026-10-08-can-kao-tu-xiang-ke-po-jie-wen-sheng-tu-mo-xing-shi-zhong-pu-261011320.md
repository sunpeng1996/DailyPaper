---
title: 'It''s Always 10:10: Reference Images Break a Bias That Prompts Only Dent'
title_zh: 参考图像可破解文生图模型时钟普遍输出10:10的固有偏差
authors:
- Luca Cazzaniga
affiliations:
- Independent Researcher, AI-Assisted Visual Production
arxiv_id: '2610.11320'
url: https://arxiv.org/abs/2610.11320
pdf_url: https://arxiv.org/pdf/2610.11320
published: '2026-10-08'
collected: '2026-10-10'
category: Multimodal
direction: 多模态文生图 · 训练偏差消解
tags:
- Text-to-Image
- Bias Mitigation
- Multimodal Model
- Prompt Engineering
- Reference Image
one_liner: 验证文生图模型的时钟10:10生成偏差，证明添加参考表盘比文字提词消偏效果好，准确率提升37个点
practical_value: '- 电商手表/配饰类商品图生成场景，若有精准属性要求，可加入简单参考图替代纯文字提词，大幅降低训练数据带来的固有偏差，提升生成准确率

  - 多模态生成类Agent的指令优化，当文字prompt（数字/结构化描述）效果不达预期时，优先补充轻量参考素材，投入产出比远高于纯prompt调优

  - 生成内容质检流程可针对高频训练偏差（如广告类商品的常见默认样式）预设校验规则，提前拦截不符合要求的生成结果'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
文生图模型会复刻训练数据的固有习惯，极端案例是手表广告普遍采用10:10时间，导致模型即便被要求生成其他时间也大概率输出10:10，纯prompt调优的消偏效果未被量化验证。
### 方法关键点
在52款Magnific平台文生图模型、12款Higgsfield平台模型上测试4种提词方案：无时间要求（A）、数字标注时间（B）、文字描述指针位置（C）、文字+参考表盘图（D），要求生成3个分别显示2:35、6:50、11:20的时钟，双盲标注1799张生成图，标注一致性达96%以上。
### 关键结果
无时间要求时67%生成图的全部时钟为10:10；20款当前主流模型上，B方案全准确率34%、C方案30%、D方案75%，D比B准确率高37个百分点（95%CI 28-45）；跨平台复现结果一致，D方案全准确率达81%，几乎消除全10:10的错误生成。
