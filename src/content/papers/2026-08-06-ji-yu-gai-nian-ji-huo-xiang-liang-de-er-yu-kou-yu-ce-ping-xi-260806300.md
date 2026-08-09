---
title: Bias Analysis of L2 Speaking Assessment Systems Using Concept Activation Vectors
title_zh: 基于概念激活向量的二语口语测评系统偏差分析
authors:
- Arya Labroo
- Mengjie Qian
- Kate Knill
affiliations:
- University of Cambridge
arxiv_id: '2608.06300'
url: https://arxiv.org/abs/2608.06300
pdf_url: https://arxiv.org/pdf/2608.06300
published: '2026-08-06'
collected: '2026-08-09'
category: LLM
direction: 大模型可解释性 · 偏差检测
tags:
- Concept Activation Vector
- Sparse Autoencoder
- Fairness
- Interpretability
- Bias Detection
one_liner: 将CAV偏差分析拓展到BERT、Whisper类神经口语测评系统，验证稀疏自编码器对概念检测的影响
practical_value: '- 做电商推荐/广告打分模型的偏差审计时，可复用CAV方法，明确区分「概念是否被模型编码」和「概念是否实际影响预测输出」两个维度，避免误判偏差

  - 若在高维激活空间用CAV做偏差检测遇到线性不可分问题，可尝试用SAE在稀疏隐空间学习概念方向再映射回激活空间，提升概念可恢复性

  - 注意SAE会衰减原始激活空间的敏感度，尤其是低维层，做偏差检测时不能直接用SAE隐空间的敏感度代替原始模型的真实敏感度'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
基于Transformer的二语口语自动测评系统已广泛应用于高利害场景，但黑盒特性导致难以验证评分是否受母语、年龄等无关属性影响，现有CAV偏差分析方法多适配特征型测评系统，缺乏对神经大模型测评系统的适配方案。
### 方法关键点
1. 将CAV分析拓展到两类神经测评系统：文本型BERT打分器、语音+文本多模态Whisper打分器，用梯度敏感度指标量化无关概念对最终评分的实际影响
2. 引入稀疏自编码器(SAE)，在稀疏隐空间学习CAV后再映射回激活空间，解决复杂嵌入空间线性可分性差的问题
### 关键结果
- 概念可恢复性强依赖于被探测的模型表示与架构，而非仅由概念本身决定
- 模型对无关概念的敏感度同样存在架构依赖
- SAE可显著提升概念线性可恢复性，但会衰减原始激活空间的敏感度，低维层衰减幅度更大
