---
title: L1 Augmented Attention as an Improved Vector Similarity Metric
title_zh: L1增强注意力：一种改进的向量相似度度量方法
authors:
- Kurt Godden
affiliations:
- Walsh College, Troy Michigan, USA
arxiv_id: '2607.18027'
url: https://arxiv.org/abs/2607.18027
pdf_url: https://arxiv.org/pdf/2607.18027
published: '2026-07-20'
collected: '2026-07-21'
category: LLM
direction: LLM基础组件 · 注意力机制优化
tags:
- Attention Mechanism
- Vector Similarity
- L1 Norm
- Transformer
- Perplexity Optimization
one_liner: 在标准缩放点积注意力中加入头专属可学习L1距离惩罚，提升向量相似度计算效果与语言模型困惑度
practical_value: '- 向量召回场景可复用该混合相似度思路：在内积得分基础上加入L1距离惩罚项，缓解高范数热门item/query过度拉高匹配分的问题，提升语义匹配精准度

  - 计算资源受限场景下，可先将query/key投影到8-16维低维子空间再计算L1距离，既降低计算开销，还可通过投影层学习适配业务场景的L1几何特征

  - 堆叠Transformer结构的生成式推荐/Agent系统可分层配置相似度策略：低层用L1增强注意力捕捉局部特征的细粒度差异，高层用常规注意力做全局语义聚合，平衡效果与推理效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
标准缩放点积注意力混淆了向量方向对齐与范数信息，会出现高范数低相似度向量匹配分高于低范数高相似度向量的异常，无法精准度量向量语义相似性，限制了Transformer类模型的表征效果。

### 方法关键点
- 注意力得分公式修改为「缩放点积得分 - 头专属可学习λ_h乘以query与key的L1距离」，混合点积的方向对齐奖励与L1的坐标偏差惩罚，互补捕捉向量几何信息
- 为降低L1计算开销，先通过无偏置线性层将query/key投影到低维子空间，投影矩阵跨头共享但各头仅更新对应切片，实现头级特征专业化
- λ_h初始化为0，各注意力头独立学习，自适应匹配不同层的表征统计特性，低层偏向放大L1惩罚捕捉局部差异，高层偏向降低L1权重做全局语义聚合

### 关键实验
在WikiText-2数据集上用参数量1.7M的小型Transformer训练，对比Vaswani原始注意力、RBF-L2核注意力：最优配置（query/key投影到8维）实现14.5%的困惑度降低，是RBF-L2方案提升幅度的3倍，仅增加29%的训练时间；分层混合方案（低层用L1增强、高层用RBF-L2）可实现7.1%的困惑度降低，训练开销仅增加13%。

### 核心结论
点积与L1分别捕捉向量相似度的方向对齐与坐标偏差特性，二者结合可构建更鲁棒的向量相似度度量，低维投影可进一步平衡效果与计算效率。
