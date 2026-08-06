---
title: 'M-GATE: Multilingual Grammar, Accuracy in Translation, and Efficiency Benchmark
  for Large Language Models'
title_zh: M-GATE：面向大语言模型的多语言语法、翻译准确率与效率基准
authors:
- Tomáš Burkert
- Angelika Peljak-Łapińska
- David Zelený
affiliations:
- RWSTrainAI
arxiv_id: '2608.03803'
url: https://arxiv.org/abs/2608.03803
pdf_url: https://arxiv.org/pdf/2608.03803
published: '2026-08-04'
collected: '2026-08-06'
category: Eval
direction: 大语言模型多语言能力评测
tags:
- Multilingual LLM
- Benchmark
- Translation Evaluation
- Grammatical Error Detection
- Tokenizer Efficiency
one_liner: 推出覆盖30种高低资源语言的多语言能力评测基准M-GATE，含语法检测、回译、分词效率三类任务
practical_value: '- 跨境电商多语言内容生成、多语种客服Agent团队可复用M-GATE的任务范式评测自研/开源多语言LLM的实际语言能力，避免仅依据生成流畅度选型踩坑

  - 商品标题/详情、广告文案等多语言翻译场景可优先开启LLM推理链，可稳定提升翻译质量，语法审核类任务需根据模型特性判断是否开启推理

  - 低资源小语种的商品内容生成/翻译任务，补充对应语种预训练数据占比可直接有效提升效果，二者对数相关性达0.86'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有多语言LLM评测多聚焦特定任务完成度，混淆生成流畅度与实际语言掌握能力，缺乏针对语言本身熟练度的系统化基准。

### 方法关键点
构建覆盖30种类型差异大、涵盖高低资源的多语言能力基准M-GATE，包含三类任务：1. 语言学家构造的对抗性语法错误检测，聚焦各语言独有难点语法现象；2. 统一英语源的29种目标语言回译评测，采用经过专业标注验证的3家LLM评委组合打分；3. 补充分词效率维度评测。共完成50+模型的80+配置测试。

### 关键结果数字
- 模型流畅度与实际语言能力显著分离：翻译能力达标的模型在对抗语法检测任务上接近随机水平，最高MCC仅0.36，且错误倾向为漏判ungrammatical文本
- 翻译质量与预训练中对应语言的数据占比强相关（r=0.86，与Common Crawl占比对数相关），低资源语种效果惩罚显著但随模型迭代差距收窄
- 开启推理可稳定提升翻译效果，但对语法检测效果影响小甚至部分模型表现负向，最优配置随任务调整
