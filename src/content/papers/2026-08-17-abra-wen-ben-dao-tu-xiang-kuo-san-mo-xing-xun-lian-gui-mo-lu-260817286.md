---
title: 'Abra: Scaling Diffusion Image Training'
title_zh: 《Abra：文本到图像扩散模型训练规模化规律研究》
authors:
- Kyle Chickering
- Wei-An Lin
- Swayam Bhanded
- Dan Saunders
- Akshat Tripathi
- Jiaming Song
- Shyamal Buch
- Xinchen Yan
affiliations:
- Luma AI
arxiv_id: '2608.17286'
url: https://arxiv.org/abs/2608.17286
pdf_url: https://arxiv.org/pdf/2608.17286
published: '2026-08-17'
collected: '2026-08-19'
category: Training
direction: 扩散模型训练 · 计算最优缩放规律
tags:
- Diffusion Model
- Scaling Law
- Text-to-Image
- Training Optimization
- Flow Matching
one_liner: 系统研究文本到图像扩散模型缩放规律，明确其最优训练数据量为同规模LLM的10倍
practical_value: '- 电商AI商品图/营销海报生成团队训练扩散模型时，可参考200 image tokens/参数的最优配比，相比LLM多配10倍训练数据

  - 扩散模型对过训练鲁棒，算力有限时优先提升训练数据规模而非盲目增大模型参数量，降低训练成本

  - 扩散模型的训练曲线、最优CFG参数、生成质量均可预测，可提前预估不同算力预算下的产出效果，合理分配训练资源'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
LLM领域已有成熟的计算最优缩放定律指导训练，但文本到图像扩散模型领域的规模化规律缺乏系统研究，过往研究覆盖的算力范围有限，无法指导大预算下的模型训练资源分配。

### 方法关键点
基于自研Abra系列流匹配Transformer架构，在10^19到10^22 FLOPs跨三个数量级的算力区间开展对照实验，严格控制变量分析模型参数量、训练数据量与训练效果的关联。

### 关键结果数字
1. 扩散模型和LLM一样缩放规律可预测，但最优数据配比为200 image tokens/参数，是LLM Chinchilla准则的10倍；
2. 扩散模型对过训练鲁棒，同算力下优先增加数据规模比增大模型参数量效果更优；
3. 缩放规律可延伸到生成质量、最优CFG设置、训练曲线形态等多个维度，预测性极强。
