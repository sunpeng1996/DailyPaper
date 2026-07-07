---
title: Enhancement of E-commerce Sponsored Search Relevancy with LLM
title_zh: 基于LLaMA2与LoRA的电商Sponsored Search广告相关性提升
authors:
- Md Omar Faruk Rokon
- Andrei Simion
- Weizhi Du
- Musen Wen
- Hong Yao
- Kuang-chih Lee
affiliations:
- Walmart AdTech, Sunnyvale, CA, USA
arxiv_id: '2607.03886'
url: https://arxiv.org/abs/2607.03886
pdf_url: https://arxiv.org/pdf/2607.03886
published: '2026-07-04'
collected: '2026-07-07'
category: RecSys
direction: 搜索广告相关性 · LLM参数高效微调
tags:
- LLaMA2
- LoRA
- Sponsored Search
- Relevance Classification
- E-commerce
one_liner: 用LoRA微调LLaMA2 7B实现<query,广告标题>三分类相关性判断，效果优于BERT系列与GPT-4
practical_value: '- 电商广告相关性场景可直接复用LoRA微调LLaMA2 7B的方案，同时给attention层和FFN层的投影层加LoRA适配，比仅调attention层效果更优，训练成本远低于全量微调，隐私性优于调用GPT-4等外部API

  - 相关性标注可采用三级分类（相关/部分相关/不相关），配合自动标注+少部分人工校验的方式降低标注成本，数据集采样时做分层抽样平衡类别分布，提升模型泛化性

  - 优先选择开源LLM做领域微调适配，效果远好于通用大模型few-shot，本文中微调LLaMA2 7B准确率比GPT-4 few-shot高26个百分点，推理速度更快，适合线上实时场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商 Sponsored Search 是平台核心收入来源，传统相关性匹配方法（如BERT双编码器、关键词匹配）难以捕捉用户查询的隐含意图，匹配偏差会直接损害用户体验、点击率与转化率；通用大模型如GPT-4的few-shot方案存在效果差、调用成本高、延迟高、数据泄露风险等问题，亟需适配电商场景的低成本、高性能相关性判断方案。

### 方法关键点
- 基座采用开源LLaMA2 7B，基于LoRA做参数高效微调，同时对attention层的q/k/v/o投影层、FFN层的gate/up/down投影层添加低秩适配矩阵，仅更新少量参数即可完成领域适配，训练成本远低于全量微调。
- 任务定义为<query, 广告标题>三分类任务，输出标签为相关、部分相关、不相关，采用交叉熵损失、Adam优化器训练。
- 配套搭建自动标注系统，结合人工校验生成高质量样本，大幅降低标注成本。

### 关键实验
数据集来自Walmart真实搜索日志，包含250K训练样本、56K验证/测试样本，采用分层抽样平衡三类标签分布，由第三方标注员多人投票生成Ground Truth。对比基线包括BERT双编码器、BERT交叉编码器、GPT-4 few-shot。核心结果：微调后模型测试集准确率89.43%，F1值89.41%，较BERT交叉编码器高3.16pp，较GPT-4 few-shot高26.41pp；NDCG@4达0.7142，较BERT交叉编码器提升0.0203。

### 核心结论
开源大模型做针对性领域微调，在垂直场景的效果、成本、隐私性上全面优于通用大模型few-shot调用，是电商搜索广告场景的最优选择。
