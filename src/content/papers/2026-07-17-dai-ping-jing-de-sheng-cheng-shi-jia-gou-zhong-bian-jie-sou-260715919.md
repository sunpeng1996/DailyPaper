---
title: On the Failure of Boundary-Seeking Distillation in Bottlenecked Generative
  Architectures
title_zh: 带瓶颈的生成式架构中边界搜索蒸馏失效问题研究
authors:
- Mohamed Amine Kina
affiliations:
- Universität Bremen
arxiv_id: '2607.15919'
url: https://arxiv.org/abs/2607.15919
pdf_url: https://arxiv.org/pdf/2607.15919
published: '2026-07-17'
collected: '2026-07-20'
category: Training
direction: 无数据知识蒸馏 · 生成式架构训练优化
tags:
- Knowledge Distillation
- Data-free Training
- Generative Model
- Autoencoder
- Model Compression
one_liner: 证明边界搜索蒸馏在带瓶颈生成架构上失效，提出流形感知合成作为无数据生成蒸馏有效基线
practical_value: '- 做VAE-based召回、语义ID生成等带瓶颈的生成式推荐模型无数据蒸馏时，不要直接套用分类器的边界搜索蒸馏方案，避免梯度冲突导致效果下降

  - 带隐空间压缩层的生成类业务模型做蒸馏，优先选择考虑隐空间流形几何结构的样本合成策略，可大幅降低训练冲突

  - 大生成式推荐模型压缩到低延迟推理场景时，可直接复用流形感知合成的无数据蒸馏基线，规避边界搜索的技术坑'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
无数据知识蒸馏可解决数据隐私受限、原始训练数据不可得场景下的模型压缩需求，现有分类器场景下有效的边界搜索蒸馏（如CAKE）能否迁移到带瓶颈的生成式架构尚不明确。
### 方法关键点
1. 将自编码器连续重建任务重定义为逐特征稠密分类任务，在MNIST数据集上直接验证CAKE在自编码器蒸馏中的适配性
2. 理论分析边界搜索目标的缺陷：带瓶颈生成架构的解码器是共享低维瓶颈约束的耦合特征级分类器阵列，独立采样对比目标会破坏隐空间流形几何，产生严重梯度冲突而非有效边界样本
3. 提出流形感知合成方案完全规避上述冲突
### 关键结果
边界搜索蒸馏在带瓶颈生成架构上本质不适配，完全失效；流形感知合成可作为无数据生成蒸馏的有效基线，无性能折损。
