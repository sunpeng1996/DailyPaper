---
title: Evaluation of Phonetic Encoding Algorithms on Transcription Datasets
title_zh: 语音编码算法在语音转写数据集上的性能评估
authors:
- Can Özbey
- Emre Kaplan
- Berkin Deniz Kahya
affiliations:
- Huawei Turkey R&D Center
- Istanbul Technical University
arxiv_id: '2609.04391'
url: https://arxiv.org/abs/2609.04391
pdf_url: https://arxiv.org/pdf/2609.04391
published: '2026-09-03'
collected: '2026-09-08'
category: Eval
direction: 语音编码算法 · 性能评估方案设计
tags:
- Phonetic Encoding
- Evaluation Metric
- IPA Transcription
- String Similarity
- Orthographic Transparency
one_liner: 提出基于Hüllermeier-Rifqi指数的语音编码评估方案，可衡量编码与IPA转写匹配度及语言正字法透明度
practical_value: '- 电商语音搜索的同音Query纠错场景可复用该评估框架筛选最优语音编码算法，降低召回错误率

  - 多语言跨境电商的语音搜索/转写场景，可借鉴归一化编辑距离+随机基线校正逻辑优化语音相似度计算策略

  - 语音交互类Agent的意图识别模块，可复用碰撞率评估指标优化语音编码的召回准确率'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有语音编码算法缺乏与IPA（国际音标）转写真值对齐的统一评估方案，无法精准衡量编码对语音相似度的拟合程度，也难以实现跨语言、跨编码方案的横向性能对比。

### 方法关键点
1. 基于Hüllermeier-Rifqi指数设计评估框架，计算真值IPA转写对与对应语音编码对的归一化编辑距离的绝对差，得到不一致得分
2. 引入使用与被测编码器相同字符集的随机字符串生成器的得分作为基线，校正最终评估结果
3. 额外搭配碰撞率指标同步评估编码器的召回能力

### 关键结果
该方案可实现多语言数据集下各类语音编码器的横向性能对比，还可拓展用于衡量语言的正字法透明度，验证了框架的通用性
