---
title: 'Weight Pair Encoding: Inducing a Smaller Grammar in Neural Network Weights'
title_zh: 权重对编码：在神经网络权重中诱导生成更小语法结构
authors:
- Irene Tallini
- Daniele Solombrino
- Alberto Cazzaniga
- Emanuele Rodolà
affiliations:
- Area Science Park
- Sapienza University of Rome
- Université Côte d'Azur
- Inria
- Paradigma
arxiv_id: '2609.31564'
url: https://arxiv.org/abs/2609.31564
pdf_url: https://arxiv.org/pdf/2609.31564
published: '2026-09-25'
collected: '2026-09-28'
category: Training
direction: 神经网络权重压缩 · 语法诱导训练
tags:
- Weight Compression
- Quantization
- Grammar Induction
- Straight-Through Estimator
- QAT
one_liner: 提出WeightPE方法，将有损Re-Pair压缩器嵌入Straight-Through Estimator微调权重，生成远小于int8 QAT的权重语法
practical_value: '- 大模型端侧/边缘侧部署的权重压缩场景，可复用WeightPE的语法压缩思路，在可接受精度损失下进一步降低权重存储开销，适配端侧推荐/Agent推理的存储约束

  - 量化感知训练（QAT）流程中可引入Straight-Through Estimator嵌套压缩模块的范式，在全局L2误差约束下对齐相似权重组，平衡压缩率与精度损失

  - 该方法微调得到的权重可直接兼容LZ78、SEQUITUR等多种语法压缩器，无需针对特定压缩算法适配，降低多部署环境的适配成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有神经网络权重压缩方案多采用固定大小码本，无法利用权重的分层重复结构，压缩率存在天花板，且极少将语法尺寸作为显式训练目标优化。

### 方法关键点
1. 将int8量化后的权重展平为字符串，嵌入基于Straight-Through Estimator的有损Re-Pair压缩模块；
2. 在全局L2误差预算内将相似的Re-Pair模式强制对齐为完全相同，支持训练过程中梯度反向传播；
3. 利用语法的可变长度模式与分层复用特性，实现比固定码本更高的压缩效率。

### 关键结果数字
在CIFAR-10微调的ViT-B/16、ViT-L/16的MLP权重上，WeightPE生成的Re-Pair语法尺寸仅为同级别int8 QAT方案的0.43倍、0.38倍，对应精度损失仅1.9、1.1个百分点，且效果可迁移到未微调适配的LZ78、SEQUITUR等其他语法压缩器。
