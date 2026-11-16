---
title: 'Unlocking Cross-Attention in Label-Scarce Regimes: A Weakly Supervised Approach
  for Video Semantic Segmentation'
title_zh: 弱标签场景下激活交叉注意力：弱监督视频语义分割方法
authors:
- Andrea Marelli
- Alessandro Ardenghi
- Giacomo Boracchi
- Luca Magri
affiliations:
- Politecnico di Milano
- Bocconi University
arxiv_id: '2611.18324'
url: https://arxiv.org/abs/2611.18324
pdf_url: https://arxiv.org/pdf/2611.18324
published: '2026-11-13'
collected: '2026-11-16'
category: Other
direction: 弱监督视频语义分割 · 交叉注意力训练
tags:
- Weakly Supervised Learning
- Cross-Attention
- Video Semantic Segmentation
- Self-Supervision
- Transformer
one_liner: 提出MemCAM弱监督视频分割框架，通过特征空间自监督稳定时序交叉注意力训练，无需外部先验
practical_value: '- 弱标签场景下通过历史特征相似度传播构造伪监督信号的思路，可迁移至用户行为序列建模、稀疏点击场景的推荐模型训练，降低对高质量标注的依赖

  - 时序交叉注意力的自监督稳定训练方法，可复用在用户长序列推荐、多轮对话Agent的注意力模块训练中，解决弱标签下注意力学习不稳定的问题

  - 无需依赖外部先验、仅用隐空间特征相似度做对齐的设计，可降低短视频电商内容理解、多模态召回模块的工程计算开销'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
弱监督视频语义分割（WS-VSS）仅需视频级标签即可学习时序一致的语义对象掩码，但弱监督下直接训练时序交叉注意力权重不稳定，性能甚至低于单帧基线；现有方法依赖光流等外部先验，存在非语义、计算开销高、噪声大的问题，会退化监督信号质量。
### 方法关键点
提出MemCAM transformer框架，无需直接监督注意力权重或引入外部先验，通过特征空间自监督直接学习时序交叉注意力；设计CAM传播算法，基于隐空间patch级特征相似度传播历史CAM生成监督信号，新增预测CAM与传播CAM的一致性约束，稳定时序注意力训练。
### 关键结果
在YouTube-Objects v2.2与WS²数据集上，MemCAM的时序定位、分割性能均优于现有WS-VSS方案，验证了弱标签场景下通过内部自监督有效训练交叉注意力的可行性。
