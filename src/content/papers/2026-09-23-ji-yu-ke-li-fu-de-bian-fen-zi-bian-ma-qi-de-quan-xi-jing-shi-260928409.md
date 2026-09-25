---
title: Learning Holographic Reduced Representations with Clifford Variational Autoencoders
title_zh: 基于克利福德变分自编码器的全息精简表示学习
authors:
- Mohamed Malek Abid
- P. Michael Furlong
affiliations:
- University of Zurich & ETH Zurich
- National Research Council Canada
- University of Waterloo
arxiv_id: '2609.28409'
url: https://arxiv.org/abs/2609.28409
pdf_url: https://arxiv.org/pdf/2609.28409
published: '2026-09-23'
collected: '2026-09-25'
category: Training
direction: 表示学习 · 向量符号代数嵌入
tags:
- VAE
- Vector Symbolic Architecture
- Representation Learning
- Clifford Algebra
- Embedding
one_liner: 提出Clifford-VAE生成适配VSA的嵌入，性能优于高斯、超球面VAE
practical_value: '- 电商召回/排序场景的Embedding可借鉴Clifford torus投影约束，提升嵌入的代数可操作性，支持后续符号化规则与模型打分融合

  - 多模态商品表示可复用该方法将图文感知数据映射到VSA空间，实现跨模态的符号化检索与精准匹配

  - 推荐系统Agent的记忆编码可采用该方法提升binding/unbinding性能，增强长短期记忆的结构化存取效率'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
向量符号代数（VSA）可通过高维向量的代数操作实现神经符号计算，但非结构化数据到VSA空间的嵌入尚无成熟方案，现有高斯、超球面VAE生成的表示无法适配VSA的绑定、解绑等运算要求。
### 方法关键点
提出Clifford-VAE变分自编码器，将输入数据直接投影到任意维度的Clifford torus空间，生成的表示天然适配全息精简表示（HRR）类VSA的运算规则，无需额外编码转换。
### 关键结果
- 半监督分类任务上，在MNIST、FashionMNIST、CIFAR-10数据集上性能与高斯VAE、超球面VAE持平
- VSA基准测试中，自绑定/解绑、角色填充恢复、bundle容量三项核心指标全面优于两类基线模型
