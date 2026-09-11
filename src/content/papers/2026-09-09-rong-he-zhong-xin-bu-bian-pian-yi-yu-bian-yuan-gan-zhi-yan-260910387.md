---
title: Enhanced Deformable Convolution with Center-invariant Offset and Edge-aware
  Mask
title_zh: 融合中心不变偏移与边缘感知掩码的增强型可变形卷积
authors:
- Yixiao Li
- Xiaoyuan Yang
- Jin Jiang
- Minghao Zou
- Guanghui Yue
- Baoquan Zhao
- Jun Liu
- Wei Zhou
affiliations:
- 北京航空航天大学数学科学学院
- 上海航天技术研究院
- 卡迪夫大学计算与数学科学学院
- 深圳大学医学部生物医学工程学院
- 中山大学人工智能学院
arxiv_id: '2609.10387'
url: https://arxiv.org/abs/2609.10387
pdf_url: https://arxiv.org/pdf/2609.10387
published: '2026-09-09'
collected: '2026-09-11'
category: Other
direction: 计算机视觉 · 可变形卷积优化
tags:
- Deformable Convolution
- Semantic Segmentation
- Spatial Modeling
- Edge Detection
- Computer Vision
one_liner: 提出融合中心不变偏移与边缘感知掩码的增强可变形卷积，性能超过现有SOTA可变形卷积变体
practical_value: '- 中心不变偏移的核心锚定思路可迁移到用户行为序列建模，固定核心交互行为权重，降低无关行为的偏移干扰

  - 边缘感知掩码的选择性加权思路可复用在多模态推荐的商品图特征提取阶段，优先保留商品主体等高信息密度区域特征

  - 大核+核心固定的卷积设计可直接用到序列推荐的卷积类召回/排序模型，平衡长程兴趣捕获和核心兴趣稳定性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
可变形卷积在语义分割等CV任务中动态空间建模能力突出，但存在偏移密度高、长距离依赖不足的缺陷，无法生成精准适配目标的形变特征。
### 方法关键点
提出增强型可变形卷积网络EDCN，解码器侧集成两个核心模块：
1. 中心不变偏移模块COM：采用大卷积核，固定核中心位置不发生形变，从更丰富的空间信息中生成更贴合目标的偏移量
2. 边缘感知掩码模块EMM：通过Sobel边缘检测判断图像内容重要性，仅对高价值区域施加形变，过滤低信息区域的干扰
### 关键结果
在主流语义分割数据集上，EDC性能全面超过Deformable ConvNets V1-V4等所有SOTA可变形卷积变体；两个核心模块的有效性均经消融实验验证，且方案可扩展到大核图像分类任务。
