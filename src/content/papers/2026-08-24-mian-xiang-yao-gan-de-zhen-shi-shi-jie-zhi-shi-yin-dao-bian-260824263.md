---
title: Real-World Knowledge-Guided Change Data Synthesis for Remote Sensing
title_zh: 面向遥感的真实世界知识引导变化数据合成方法
authors:
- Yaoyi Qi
- Xingxing Weng
- Chao Pang
- Yongkang Cui
- Xiangyu Hao
- Xiaokang Zhang
- Guibo Zhu
- Gui-Song Xia
affiliations:
- 武汉大学人工智能学院
- 武汉人工智能研究院
- 中国科学院大学自动化研究所
- 武汉大学数学与人工智能研究院
arxiv_id: '2608.24263'
url: https://arxiv.org/abs/2608.24263
pdf_url: https://arxiv.org/pdf/2608.24263
published: '2026-08-24'
collected: '2026-09-08'
category: Other
direction: 遥感数据合成 · 知识引导生成
tags:
- Synthetic Data Generation
- Knowledge-Guided Synthesis
- Vision-Language Model
- Remote Sensing
- Change Detection
one_liner: 提出KnowChange知识引导合成框架，用预训练多模态模型生成高质量遥感变化检测训练数据
practical_value: '- 合成训练数据时可借鉴用预训练多模态模型替代人工规则设计样本转换逻辑，提升生成样本多样性与下游任务效果

  - 知识引导的样本生成模块可无缝嵌入现有数据增强pipeline，无需重构全流程即可优化生成数据质量

  - 小体量高质量合成数据效果优于大体量低质量合成数据，数据增强阶段可优先优化生成质量而非单纯堆量'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有变化数据合成依赖人工规则模拟变化，类别转换覆盖范围有限，导致生成数据多样性不足，预定义转换设计适配不同变化类型的灵活性差。
### 方法关键点
1. 以预训练视觉语言模型为知识源，可基于变化前场景与目标变化类型，推理得到合理的变化位置与类别转换逻辑
2. 知识引导的变化模拟与可泛化合成模型深度融合，同一框架下支持灵活生成多种类别的变化数据
### 关键结果
同等紧凑数据规模下，生成数据在合成到真实迁移、合成数据增强任务上效果均一致优于现有合成数据集，知识引导模块可无缝嵌入现有合成管线，提升生成数据的下游效用
