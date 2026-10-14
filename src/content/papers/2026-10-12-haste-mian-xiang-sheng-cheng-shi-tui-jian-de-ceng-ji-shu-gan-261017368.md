---
title: 'HASTE: Hierarchical and Attribute-aware Supervision for Generative Recommendation'
title_zh: HASTE：面向生成式推荐的层级属性感知监督训练框架
authors:
- Tripti Shukla
- Shwetha Somasundaram
- Akshat Gupta
- Rohit Garg
- Paul Duff
- Ian Anderson
affiliations:
- Glance
arxiv_id: '2610.17368'
url: https://arxiv.org/abs/2610.17368
pdf_url: https://arxiv.org/pdf/2610.17368
published: '2026-10-12'
collected: '2026-10-14'
category: GenRec
direction: 生成式推荐 · 层级属性感知训练
tags:
- Generative Recommendation
- Semantic ID
- Training Loss
- Long-tail Recommendation
- LLM4Rec
one_liner: 为基于Semantic ID的生成式推荐引入层级与属性感知监督，同时提升训练效率与长尾推荐效果
practical_value: '- 训练Semantic ID生成式推荐时可直接复用层级损失设计：按SID从粗到细分配4:3:2:1的权重，加置信度门控和调度采样，能实现近2倍收敛加速同时提升效果，无需修改推理逻辑

  - 长尾物品优化可复用属性辅助损失方案：在SID细粒度预测层的隐藏态挂载轻量MLP头，用商品库的属性标注（颜色、材质等）做监督，对长尾物品加权，可显著提升长尾召回准确率，无额外推理成本

  - 生成式推荐的训练损失优化不需要修改模型架构或推理逻辑，仅通过调整损失权重、增加辅助监督就能拿到明显收益，ROI远高于改模型结构'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于Semantic ID的生成式推荐普遍采用平的因果交叉熵损失，既没有利用SID本身的层级结构，导致训练收敛慢、原始语义结构被破坏，也无法充分利用LLM的语义先验，长尾商品因交互数据稀疏表征质量差，推荐效果远低于头部商品。

### 方法关键点
- 层级损失：对4层SID从粗到细分配4:3:2:1的静态权重，加入上游预测置信度门控，训练前期用静态权重，后期逐渐切换到置信度加权，同时加入调度采样缩小训练推理的暴露偏差
- 属性感知辅助损失：在SID第2层（细粒度预测层）的隐藏态挂载轻量MLP头，用商品库的颜色、材质等标注做监督，对低频商品加大损失权重，辅助优化表征
- 总损失为层级损失加加权属性损失，全程无需修改SID结构或推理逻辑，仅调整训练目标

### 关键实验
在Amazon Beauty、Sports、Toys三个公开数据集、Fashion-140k及内部时尚数据集上验证，对比SASRec、BERT4Rec、TIGER、OneRec-Think等基线：层级损失比标准CE平均1.99倍加速收敛，Recall@10最高提升15.5%；结合属性损失后，长尾商品Recall@10最高提升24.2%，整体效果进一步提升2%-3%。

最值得记住的一句话：基于Semantic ID的生成式推荐训练目标要对齐SID本身的层级结构，结合商品属性的辅助监督可以用极低的成本大幅提升长尾效果和训练效率。
