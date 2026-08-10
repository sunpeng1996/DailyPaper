---
title: 'When Activation Oracles Learn Not to Read: Concept-Specific Blind Spots in
  Fine-Tuned Oracles'
title_zh: 《激活Oracles的“选择性失明”：微调后出现的概念特定盲点》
authors:
- Tobias Bersia
- Tatiana Gaintseva
affiliations:
- BAISH
- Queen Mary University of London
arxiv_id: '2607.23379'
url: https://arxiv.org/abs/2607.23379
pdf_url: https://arxiv.org/pdf/2607.23379
published: '2026-07-24'
collected: '2026-08-10'
category: LLM
direction: 大模型可解释性 · Activation Oracle可靠性
tags:
- Activation Oracle
- Model Interpretability
- Fine-tuning
- Blind Spot
- LLM Probe
one_liner: 发现微调后的Activation Oracle会对训练阶段持续出现的特定概念产生选择性读取失效，动摇可解释性接口可靠性
practical_value: '- 做LLM4Rec可解释性分析时，不要完全依赖训练得到的激活探针输出，需搭配LogitLens、层消融等底层分析交叉验证结果

  - 微调用于模型内部状态检测的专用LLM时，要额外增加目标概念召回率校验环节，避免探针本身出现特定概念的读取盲区

  - 开展Agent安全审计时，如果用专用模型读取目标Agent内部状态，需交叉验证关键敏感概念的读取准确性，避免漏判风险'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
Activation Oracle（AO）作为读取LLM内部激活信息的灵活可解释性接口，此前被默认是模型内部表征的中立读出工具，但AO本身也是通过学习得到的系统，其输出受训练数据、优化目标的影响，实际可靠性未经过系统验证。
### 方法关键点
在受控的禁忌词猜测场景下开展对照实验：先微调被检测模型使其内部使用隐藏概念但不对外输出，再基于该模型的激活数据微调AO，测试AO对隐藏概念的读取能力，同时结合LogitLens、层消融技术定位失效原因。
### 关键结果
1. 微调后的AO未成为预期的专业读取工具，反而对训练阶段持续存在的目标概念产生选择性读取失效，成为「概念特定反阅读器」
2. 失效并非源于概念未被AO表征，目标概念在AO内部仍可被解码，故障出现在AO的最终读出通路
3. 模型行为泄漏、表征层可解码性、AO可输出性三者可完全分离，AO类学习型可解释性接口存在本质可靠性风险
