---
title: 'EmoHarness: Boosting Multimodal Emotion Understanding with Meta-Harness Evolving'
title_zh: EmoHarness：基于元线束演化的多模态情感理解增强方法
authors:
- Fenghai Li
- Bingxuan Li
- Jiawen Zhang
- Yifan Shen
- Jiateng Liu
- Yutong Zhang
- Yue Guo
affiliations:
- University of Illinois Urbana-Champaign
- University of California, Davis
- Stanford University
arxiv_id: '2611.11994'
url: https://arxiv.org/abs/2611.11994
pdf_url: https://arxiv.org/pdf/2611.11994
published: '2026-11-08'
collected: '2026-11-11'
category: Multimodal
direction: 多模态大模型 · 零微调性能优化
tags:
- Multimodal Emotion Recognition
- Prompt Engineering
- Zero Fine-tuning
- LLM Optimization
- Model Alignment
one_liner: 通过结构化证据组织与离线元线束演化，零微调提升小多模态模型的情感识别精度
practical_value: '- 小模型任务性能优化可优先引入多模态补充证据（如语音转写、韵律特征），无需微调即可获得大幅增益，适合电商直播情感分析、用户反馈语义理解等场景

  - 可复用「结构化证据锚定+候选标签对比校验」的Prompt模板，降低多模态信号冲突时的识别错误率，可迁移至商品评论情感分类、客诉意图识别任务

  - 离线用大模型基于错误案例迭代优化Prompt/调用逻辑的方案，可在不泄露测试集的前提下实现小成本性能提升，适合业务快速迭代'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
小多模态模型在文本、语音、视觉信号冲突时极易出现情感识别误判，微调成本高且场景适配慢，需要零微调的性能增强方案。

### 方法关键点
1. 引入harness封装层：包含Prompt、调用配置、校验逻辑，冻结底层小多模态模型（student），初始人工编写的scaffold模板将视觉观测、语音转写、韵律特征编号为可引用证据，引导模型基于证据对比候选情感标签。
2. 设计Meta-Harness Evolving（MHE）机制：用更强的大模型（Builder）离线读取student的错误案例与执行轨迹，迭代编辑harness逻辑，通过静态校验、验证门控筛选有效编辑，全程不接触测试集避免数据泄露。

### 关键结果
在5507条MME-Emotion测试集上，相对单视频输入baseline，EmoHarness为4个不同student模型带来7.6~13.4个百分点的macro识别精度提升；其中语音转写+韵律特征贡献5.38~10.71的核心增益，scaffold模板带来最高2.54的增益，演化编辑最多带来0.95的增益；情感上下文可迁移至IntentQA任务，3个student模型获得小幅提升
