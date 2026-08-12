---
title: 'CapProbe: Evaluating Detailed Image Captions via Full-Scene Dense Question
  Answering'
title_zh: CapProbe：基于全场景密集问答的精细化图像字幕评估方法
authors:
- Mouxiao Huang
- Qiangyu Yan
- Borui Jiang
- Han Shu
affiliations:
- Huawei Technologies
arxiv_id: '2608.11074'
url: https://arxiv.org/abs/2608.11074
pdf_url: https://arxiv.org/pdf/2608.11074
published: '2026-08-11'
collected: '2026-08-12'
category: Eval
direction: 多模态内容评估 · VLM字幕评测
tags:
- VLM
- Image Captioning
- Evaluation Benchmark
- Question Answering
- Multimodal
one_liner: 提出区域对齐的全场景密集QA基准CapProbe，实现图像字幕的细粒度事实性校验与质量评估
practical_value: '- 电商多模态内容（商品图生成文案、直播截图字幕）的事实性评估可复用区域对齐+密集MCQ校验框架，替代传统语义相似度指标，降低
  hallucination 漏判

  - 生成式内容质量评估可借鉴Uncertain选项+Effective Accuracy设计，区分「未覆盖信息」和「错误信息」，更精准衡量生成内容的信息密度和准确率

  - 多模态大模型业务选型时可复用该评估范式，快速对比不同VLMs的图像信息提取、文案生成的细粒度能力，减少人工标注成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有VLM图像字幕评估的传统参考指标（CIDEr、SPICE）及LLM打分协议无法精准校验密集事实性错误，现有QA类评估方案存在探针密度低、领域覆盖窄、无图像区域对齐的缺陷，难以衡量字幕的信息密度与事实准确率。
### 方法关键点
1. 将图像拆分为覆盖前后景的语义区域，针对每个区域生成10个语义类别的MCQ问题，形成密集视觉事实校验清单；
2. 覆盖37个一级领域、219个二级子领域，设置Uncertain选项、Effective Accuracy区分未回答和错误回答，新增密度指标惩罚冗长无信息的字幕；
3. 将开放打分转为结构化MCQ判读，降低开放打分偏差，固定打分器下模型排名稳定性高。
### 关键结果数字
基准包含346张图像、1868个区域、25650个问题，单图平均74个QA对；在13个VLMs上测试发现不同模型覆盖率差距显著，存在明确的能力-效率权衡，可识别稀疏评估遗漏的失效模式。
