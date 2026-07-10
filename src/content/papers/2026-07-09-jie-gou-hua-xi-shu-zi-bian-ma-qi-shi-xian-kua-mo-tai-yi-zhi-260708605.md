---
title: When Structured Sparse Autoencoders Learn Consistent Concepts Across Modalities
title_zh: 结构化稀疏自编码器实现跨模态一致概念学习
authors:
- Weiduo Liao
- Yunqiao Yang
- Ying Wei
affiliations:
- Zhejiang University
- Nanyang Technological University
arxiv_id: '2607.08605'
url: https://arxiv.org/abs/2607.08605
pdf_url: https://arxiv.org/pdf/2607.08605
published: '2026-07-09'
collected: '2026-07-10'
category: Multimodal
direction: 多模态可解释性 · 稀疏自编码器优化
tags:
- Sparse Autoencoder
- VLM
- Cross-modal Learning
- Interpretability
- Regularization
one_liner: 针对VLM中普通SAE跨模态概念一致性差的问题，提出带结构化稀疏正则的S²AE，提升语义对齐与表征效率
practical_value: '- 多模态电商内容（图文商品、短视频）表征场景可复用S²AE的分组正则思路，基于注意力相似度+空间邻近度分组，提升跨模态表征的概念一致性，减少语义漂移

  - 多模态检索/推荐召回阶段可采用S²AE生成的稀疏特征，在保持99%以上重建精度的同时降低L0范数，提升大规模向量索引的检索效率

  - 多模态Agent的内容理解/推理模块可引入S²AE优化神经元单义性，降低跨模态任务幻觉，提升输出结果的可靠性与可解释性'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
Sparse Autoencoders (SAE)是大模型机制可解释性的主流技术，但在Vision-Language Models (VLM)中普通SAE无法学习跨模态一致概念，视觉模态的概念覆盖碎片化、语义对齐性差。
### 方法关键点
提出Structured Sparse AutoEncoder（S²AE）：1）基于Transformer注意力相似度与空间邻近度对图像patch分组；2）训练时加入结构化稀疏正则，组间独占稀疏实现概念解耦、组内稀疏保证组内概念一致性，驱动SAE latent神经元学习独立的语义接地概念。
### 关键结果
在Qwen2.5-VL-7B-Instruct上测试：语义对齐（mIoU）平均提升6.06%，表征效率（L0范数）达60.81（越低越优），重建解释方差保持99%以上；跨模态语义一致性平均提升3.08%，神经元单义性得分平均提升2.37%
