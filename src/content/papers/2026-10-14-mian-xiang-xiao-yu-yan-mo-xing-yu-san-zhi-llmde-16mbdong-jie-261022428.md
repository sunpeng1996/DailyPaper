---
title: Embeddings Are Overpriced? A Frozen 16 MB Vocabulary for Small and Ternary
  Language Models
title_zh: 面向小语言模型与三值LLM的16MB冻结词表压缩方案
authors:
- Sai Kiran Bathula
affiliations:
- QLNI, New South Wales, Australia
arxiv_id: '2610.22428'
url: https://arxiv.org/abs/2610.22428
pdf_url: https://arxiv.org/pdf/2610.22428
published: '2026-10-14'
collected: '2026-10-19'
category: LLM
direction: 小语言模型 · 词表压缩 推理加速
tags:
- Small Language Model
- Embedding Compression
- BitNet
- Inference Acceleration
- Frozen Vocabulary
one_liner: 用预训练词嵌入降维二值化生成16MB冻结词表，大幅压缩小模型体积、提升推理速度且效果损失可控
practical_value: '- 端侧电商/推荐小模型（比如端侧个性化导购Agent、实时推荐理由生成）可直接复用该冻结词表方案，将占比60%+的词嵌入参数从数百MB压缩到16MB，大幅降低端侧内存占用，适配CPU运行

  - 场景定制小LLM（比如电商类目专属query理解、营销文案生成小模型）需新增领域词时，可直接通过子词编码平均生成新token的冻结编码，无需重新训练词表，仅损失3%左右效果即可快速适配新领域

  - BitNet三值量化+冻结词表的组合可作为端侧Agent底座优先选型：实验中46MB三值模型在笔记本CPU上推理速度达615~740 token/s，是8bit量化同结构模型的5~6倍，内存仅为1/7，可支撑高吞吐低延迟的端侧推荐交互需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
小语言模型中词嵌入表通常占总参数量的60%以上，现有量化方案均保留16bit词嵌入，导致压缩后大部分模型体积仍被词表占用，严重制约端侧部署的内存占用与推理速度；此前的无训练词表方案缺乏严格对照实验，效果收益不明确。

### 方法关键点
- 基于Gemma 3 270M预训练词嵌入矩阵，中心化后取Top 512主成分投影，对投影结果取符号得到每个token的512bit二值编码，总大小仅16MB，无任何训练参数
- 输入侧新增512→640线性映射、输出侧新增640→512线性映射适配模型隐层维度，仅新增0.65M训练参数；输出打分阶段加入token单字频率先验，优化长尾词表现
- 可搭配BitNet b1.58三值模型结构，整体训练参数量仅为原结构的37%

### 关键结果
- 训练数据为2.05B FineWeb-Edu tokens，对照基线为带可训练词表的原生Gemma 3 270M
- 冻结词表+浮点体模型在LAMBADA上领先基线1.6pp，HellaSwag、PIQA与基线持平，仅ARC-Easy低3.4pp；三值+冻结词表模型总大小仅46MB，LAMBADA、PIQA仍与基线持平
- 笔记本CPU上三值模型推理速度达615~740 token/s，是8bit量化基线的5.3~6.4倍，内存占用仅为基线的1/7；新增10000个领域词时，冻结词表模型仅损失3%左右效果，可训练词表模型效果暴跌43%

> 最值得记住的话：小模型可训练词嵌入带来的效果收益远低于其参数与部署成本，冻结预训练词嵌入二值编码是端侧小模型部署的高性价比替代方案
