---
title: Adaptive Convolutional Sparse Coding via Information Bottleneck for Robust
  Visual Signal Representation
title_zh: 基于信息瓶颈的自适应卷积稀疏编码实现鲁棒视觉信号表征
authors:
- Meng'en Qin
- Yinchen Liu
- Mingxuan Cui
- Youlu Xing
affiliations:
- 深圳高等技术大学计算机科学与人工智能学院
- 电子科技大学数学科学学院
- 山东大学数学学院
arxiv_id: '2609.19122'
url: https://arxiv.org/abs/2609.19122
pdf_url: https://arxiv.org/pdf/2609.19122
published: '2026-09-16'
collected: '2026-09-17'
category: Other
direction: 视觉表征 · 自适应稀疏编码
tags:
- Convolutional Sparse Coding
- Information Bottleneck
- Visual Representation
- Robustness
- FISTA
one_liner: 将卷积稀疏编码的稀疏系数设为可微分变量联合学习，结合信息瓶颈提升视觉表征抗扰动鲁棒性
practical_value: '- 多模态搜广推的视觉特征提取环节，可复用自适应稀疏编码思路压缩冗余视觉信息，提升模糊商品图、带水印图等噪声输入下的特征鲁棒性，降低对排序/召回效果的影响

  - 特征压缩场景可借鉴信息瓶颈的trade-off优化逻辑，将压缩强度超参数设为可微分变量与主模型联合训练，免去人工调参成本

  - 面对脏输入的线上场景，可复用无标签后训练调整压缩强度的策略，固定主参数即可快速适配低质输入，无需全量重训'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
传统卷积稀疏编码（CSC）的稀疏系数需人工设置、固定不变，无法灵活平衡信息保留与压缩的trade-off，生成的视觉表征在输入存在扰动时鲁棒性差。
### 方法关键点
1. 用Fast Iterative Shrinkage-Thresholding Algorithm（FISTA）展开CSC优化过程，将稀疏系数设为可微分变量，与网络参数联合训练；
2. 从信息瓶颈视角设计目标函数，稀疏项驱动表征紧致，重建项+任务损失保留任务相关信息；
3. 新增无标签后训练策略，固定主网络参数即可针对受损输入调整压缩强度。
### 关键结果
在CIFAR、ImageNet数据集上，干净数据识别效果达同期SOTA同级，不同输入扰动下的鲁棒性实现大幅提升
