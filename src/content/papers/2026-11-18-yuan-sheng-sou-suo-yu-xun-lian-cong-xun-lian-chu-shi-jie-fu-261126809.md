---
title: 'Search From the Start: Search-Native Pretraining for Language Models'
title_zh: 原生搜索预训练：从训练初始阶段赋予大模型搜索调用能力
authors:
- Kaustubh Ponkshe
- Gyung Hyun Je
- Stefan Taga
- Colin Raffel
- Martin Jaggi
affiliations:
- EPFL
- University of Toronto
arxiv_id: '2611.26809'
url: https://arxiv.org/abs/2611.26809
pdf_url: https://arxiv.org/pdf/2611.26809
published: '2026-11-18'
collected: '2026-11-23'
category: Training
direction: 大模型预训练 · 原生搜索能力注入
tags:
- Pretraining
- Tool Calling
- Search Augmentation
- Knowledge Intensive Task
- Small Language Model
one_liner: 在预训练阶段注入搜索能力，小模型可超越数倍参数量的无搜索大模型在知识密集任务的表现
practical_value: '- 电商导购/搜索Agent场景可复用该预训练范式：无需仅靠SFT注入搜索能力，用少量种子数据微调标注模型即可批量生成搜索增强语料，低成本把搜索调用能力灌进小模型，适配低算力/端侧场景的轻量化Agent需求

  - 训练损失trick可直接复用：仅对原文档、搜索query计算损失，搜索结果部分屏蔽损失，既让模型学会基于检索结果生成，又无需额外算力训练模型生成检索结果，降低训练成本

  - 成本优化方案可复用：可通过调整搜索插入频率、检索结果长度平衡效果与训练成本，比如每篇文档仅保留Top2最高相关性的搜索插入，仅需增加不到60%的额外算力即可拿到70%以上的原生搜索能力增益

  - 适配电商信息高频更新场景：该方法训练的模型更依赖检索到的实时信息，而非参数记忆的过时内容，可大幅降低商品价格、活动规则等动态信息的回答错误率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有大模型的搜索能力普遍在 post-training 阶段注入，预训练阶段仅针对静态文本做 next token 预测，导致小模型参数存储的 factual knowledge 容量有限、易过时，且后训练注入的搜索能力始终无法达到原生学习的效果，小模型在知识密集任务上的表现远不如大模型。

### 方法关键点
- 标注流水线：先用1万篇Wikipedia文档做种子数据，微调一个小型标注模型，可自动在大规模预训练语料中识别搜索插入点、生成对应搜索query，插入频率通过概率阈值控制
- 语料增强：对每个生成的query，用BM25从Sphere公开web语料库检索结果，插入到原文本对应位置，整体语料规模超100B token
- 损失设计：仅对原文档文本、搜索query、特殊搜索标记计算损失，搜索结果部分token完全屏蔽损失，既让模型学会基于检索结果生成，又降低训练 overhead

### 关键实验
在Wikipedia、DCLM-Edu两个语料上训练360M~3.3B参数的QueryLM，对比FLOP匹配的普通预训练基线、SmolLM3-3B、Qwen2.5-3B等开源模型：1.4B QueryLM在8个知识密集QA任务上的表现持平甚至超过FLOP匹配的3.3B基线；400M QueryLM加搜索的QA准确率超过无搜索的SmolLM3-3B，预训练算力仅为后者的1/6700；即便两类模型都做了搜索相关SFT，QueryLM的优势仍然保留，反事实证据测试中QueryLM遵循检索结果的比例比基线高8~12pct。

> 最值得记住：搜索能力预训练的增益无法被后训练完全覆盖，小模型通过原生搜索注入可用极低成本获得远超参数记忆的知识处理能力
