---
title: Technical Manual for a Toolkit for Measuring Contextual Individuation in Transformer
  Language Models
title_zh: Transformer语言模型上下文词义区分能力测量工具包技术手册
authors:
- José Luciano Verçosa Marques
- Frederico Jorge Heitmann
- Daniel Omar Perez
- Marcelo Vinicius de Paula
- Tárcio André dos Santos Barros
affiliations:
- Center for Electric Mobility Research (CEMOBE) / Power Electronics Laboratories
  (LEPO), University of Campinas (Unicamp)
- Institute of Computing (IC), University of Campinas (Unicamp)
- Center for Logic, Epistemology and History of Science (CLE), University of Campinas
  (Unicamp)
arxiv_id: '2609.05333'
url: https://arxiv.org/abs/2609.05333
pdf_url: https://arxiv.org/pdf/2609.05333
published: '2026-09-04'
collected: '2026-09-07'
category: Eval
direction: LLM上下文语义编码能力评估工具
tags:
- Transformer
- LLM Evaluation
- Contextual Representation
- Open Toolkit
- Word Sense Disambiguation
one_liner: 开源可直接复用的Transformer语言模型上下文词义区分能力测量工具包，提供全流程实现与避坑指南
practical_value: '- 多义Query的语义编码效果评估可直接复用本工具的bridge form构造方法、领域成对轮廓系数计算逻辑，避免词义混淆、子词切分错位等常见坑

  - 电商场景下多义搜索词（如「苹果」可指水果/数码）的上下文语义区分能力验证，可直接复用本工具的全流程pipeline做AB测试

  - 构建RAG语义召回的评估数据集时，可参考本工具的跨领域同形多义词语料构造方法，提升召回准确率测试的有效性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
Transformer LM输入层为同形词分配固定的上下文无关向量，业界普遍认为模型深层会根据上下文区分词义，但长期缺乏标准化、可规避常见方法偏差的测量工具。

### 方法关键点
基于bridge form（跨多个领域出现、同形不同义的词）构造测量框架，全流程覆盖：bridge form与所属领域定义、Wikipedia语料获取、词出现位置定位、逐层表征提取、领域成对轮廓系数计算表征空间区分度、配对可视化协议；每个设计都针对性规避了类别标签过宽导致的词义污染、轮廓系数多组偏差、子词切分错位、降维可视化轴可比性偏差等常见问题。

### 结果
本手册为方法与实现参考，未公布特定模型/数据集的实测结果，工具包全源码、配套语料已通过持久化标识符公开，可直接用于相关实证研究。
