---
title: Sequential Modality Dropout for Robust Multi-Modal Sequential Recommendation
title_zh: 面向鲁棒多模态序列推荐的序列模态丢弃方法
authors:
- Guanqun Yang
- Wenlong Zhang
affiliations:
- Stevens Institute of Technology
arxiv_id: '2608.10240'
url: https://arxiv.org/abs/2608.10240
pdf_url: https://arxiv.org/pdf/2608.10240
published: '2026-08-10'
collected: '2026-08-12'
category: RecSys
direction: 多模态序列推荐 · 鲁棒性优化
tags:
- Sequential Recommendation
- Multi-modal Recommendation
- Robustness
- Modality Dropout
- E-commerce
one_liner: 4行代码的架构无关模态丢弃插件，大幅提升多模态序列推荐模态缺失鲁棒性且基本无损全模态精度
practical_value: '- 直接复用论文开源的4行PyTorch SMD实现，插入现有多模态序列推荐的模态融合层前，无需修改原有架构和超参，即可快速提升模态缺失场景的鲁棒性

  - 电商场景如果存在大量商品缺图、缺描述的情况，默认取模态丢弃概率p=0.3，平衡全模态精度和鲁棒性，避免全模态效果下降过多

  - 若业务模态缺失率超过50%，可额外叠加轻量跨模态重建损失，λ取0.01即可，进一步提升高缺失场景下的精度保留率

  - 不需要额外做模态补全的特征工程，SMD训练时模拟真实场景的整序列模态缺失，比逐item随机丢弃更贴合电商整类目缺模态的实际情况'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态序列推荐默认所有物品都具备完整的图文模态，但真实电商商品册中平均26%-48%的商品存在缺图、缺描述的问题，训练时基于全模态数据训练的模型，推理时遇到模态缺失会出现HR@10暴跌至原精度22%-73%的问题，现有模态缺失优化方法均未适配序列推荐的时序结构，落地效果差。

### 方法关键点
- 提出Sequential Modality Dropout（SMD）：训练时对每个 batch 样本的图像、文本模态流独立按概率p整序列置零，同一用户交互序列内所有物品共享同一个模态掩码，匹配真实场景中整类目、整批次模态缺失的模式，而非逐item随机丢弃
- SMD是架构无关的黑盒插件，仅4行PyTorch代码，插入模态融合层前即可生效，无需修改原有模型结构、优化器、超参数
- 可选跨模态重建辅助损失：训练两个模态投影层互相预测，推理时可通过存活模态隐式恢复缺失模态，仅在简单加法融合架构+高模态缺失率场景下启用

### 关键实验结果
在4个Amazon品类数据集、4个主流多模态序列推荐 backbone（MM-SASRec、IISAN、MISSRec、fMRLRec）上验证：
- SMD将文本模态缺失下的HR@10保留率提升1.0~3.2倍，全模态精度平均仅下降0.8%
- 极端95% item模态缺失场景下，SMD保留61%的HR@10，远高于无SMD的22%
- 叠加重建损失后，高缺失率场景下加法融合架构的保留率可从90%进一步提升至98%

### 核心结论
多模态序列推荐的模态缺失鲁棒性优化，不需要复杂的特征补全或者架构重构，仅需在训练时模拟真实缺失模式做整序列模态丢弃，即可用极小的成本获得极显著的效果提升
