---
title: 'LightTAR: Light and Fast Target-Aware Representations for Multimodal Tabular
  Learning'
title_zh: LightTAR：面向多模态表格学习的轻量快速目标感知表示
authors:
- Eilam Shapira
- Alan Arazi
- Shoham Grunblat
- Roi Reichart
affiliations:
- Technion – Israel Institute of Technology
arxiv_id: '2611.17600'
url: https://arxiv.org/abs/2611.17600
pdf_url: https://arxiv.org/pdf/2611.17600
published: '2026-11-11'
collected: '2026-11-19'
category: Multimodal
direction: 多模态表格学习 · 目标感知特征提取
tags:
- Multimodal Tabular Learning
- Dimensionality Reduction
- PCA
- PLS
- Feature Engineering
one_liner: 用正则化PLS提取目标感知特征增强PCA，无需改动组件即可提升多模态表格学习性能
practical_value: '- 电商推荐场景中，商品标题/主图等多模态embedding的降维环节可引入LightTAR，在原有PCA特征基础上增加少量PLS提取的目标感知特征，几乎不增加推理耗时即可提升排序/召回模型效果

  - 无需修改现有预训练编码器、下游排序/召回模型结构，可直接嵌入现有特征工程管线，落地改造成本极低

  - 可同时提取预训练编码器中间层与最后层的embedding做PLS特征计算，挖掘预训练模型中与业务目标相关的隐藏信号'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
多模态表格学习场景下，现有方案通常用PCA对文本、图像的预训练embedding做降维，仅优先保留输入方差，容易丢失和下游预测目标强相关的关键信息。
### 方法关键点
- 提出轻量的LightTAR方案，在标准PCA生成的特征基础上，用正则化PLS从预训练编码器的最后层和中间层联合提取少量目标感知特征做增强
- 无需改动原有编码器或下游模型结构，可直接嵌入现有编码pipeline
### 关键结果
- 在21种表格模型（树集成、神经网络、表格基座模型）上测试，所有模型的平均预测性能均有提升
- 跨模型平均在几乎所有MulTaBench数据集上预测效果提升，总运行时间仅较PCA方案有小幅增加
