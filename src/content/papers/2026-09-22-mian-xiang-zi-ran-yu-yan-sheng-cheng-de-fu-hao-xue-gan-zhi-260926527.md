---
title: A Semiotics-Aware Framework for Evaluating Fidelity and Coverage in Natural
  Language Generation
title_zh: 面向自然语言生成的符号学感知保真度与覆盖度评估框架
authors:
- Lorenzo Zangari
- Davide Picca
affiliations:
- University of Lausanne
arxiv_id: '2609.26527'
url: https://arxiv.org/abs/2609.26527
pdf_url: https://arxiv.org/pdf/2609.26527
published: '2026-09-22'
collected: '2026-09-23'
category: Eval
direction: NLG评估 · 符号学对齐指标
tags:
- NLG
- Evaluation
- LLM
- Semiotics
- Fidelity
- Coverage
one_liner: 提出基于符号学特征的NLG评估框架，输出保真度与覆盖度指标，解决传统指标表意偏差检测失效问题
practical_value: '- 电商生成式推荐/营销文案评估可复用该框架，对比生成文案与人工标注稿的符号学对齐度，避免生成内容偏离商品核心定位和用户心智

  - Agent对话生成场景可引入Semiotic Fidelity/Coverage指标优化采样温度：低温度场景优先匹配人类话术逻辑，高温度创意场景控制对齐度下限

  - 搜索Query改写/自动补全效果评估可引入该指标，检测改写后Query是否保留原意图的核心语义和指代关系，避免语义漂移'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统基于词汇重叠、全文相似度的NLG评估指标无法检测相同表述下的表意框架差异，易忽略语义漂移、指代偏差等问题，无法满足LLM生成内容的精细化评估需求。
### 方法关键点
1. 构建Semiotic Profile（符号学特征画像），同时建模文本的上下文语义、突出的话语指代信息
2. 输出两个量化指标：Semiotic Fidelity衡量待评估文本对基准文本特征画像的支持程度，Semiotic Coverage衡量待评估文本对基准文本特征画像的还原比例
### 关键结果
- 相同文本对的覆盖度得分通常低于保真度
- LLM生成内容与人工标注数据的对齐度在低采样温度下最高，温度升高时对齐度持续下降
