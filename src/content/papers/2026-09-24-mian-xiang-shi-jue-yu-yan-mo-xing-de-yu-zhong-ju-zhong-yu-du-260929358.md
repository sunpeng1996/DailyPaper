---
title: Domain Recentering and Confidence-Weighted Prior Calibration for Vision-Language
  Models
title_zh: 面向视觉语言模型的域重居中与置信度加权先验校准方法
authors:
- Youngeun Seol
- Jimin Shin
- Heeseo Yoon
- Uiwon Hwang
affiliations:
- Ewha Womans University
arxiv_id: '2609.29358'
url: https://arxiv.org/abs/2609.29358
pdf_url: https://arxiv.org/pdf/2609.29358
published: '2026-09-24'
collected: '2026-09-25'
category: Multimodal
direction: 多模态模型 · 分布偏移校准
tags:
- CLIP
- Distribution Shift
- Training-free Calibration
- Gaussian Mixture Model
- Vision-Language Model
one_liner: 提出无需训练的DRC校准方法，基于无标注目标数据缓解CLIP在分布偏移下的嵌入漂移问题
practical_value: '- 电商多模态搜推场景中跨域商品图像的CLIP嵌入对齐可复用DRC免训练校准方案，无需微调大模型即可缓解分布偏移导致的召回/排序准确率下降，节省算力成本

  - 无标注域的特征校准可替换硬聚类偏移修正方案，采用高斯混合后验加权的均值偏移方法，大幅降低聚类边界样本的校准误差

  - 目标域类别先验估计可复用置信度加权预测的思路，无需标注数据即可完成先验校正，适配冷启动场景的多模态分类、召回需求'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
CLIP等视觉语言模型零样本分类性能优异，但遭遇分布偏移时视觉嵌入会与固定文本embedding发生漂移，现有免训练校准方法采用硬聚类为样本分配单簇偏差，边界样本校准误差高。
### 方法关键点
1. 提出免训练的DRC校准方案，仅需无标注目标域图像即可完成CLIP适配，无需标注或反向传播
2. 拟合高斯混合模型，为每个嵌入减去后验加权的分量均值偏移，替代硬聚类修正逻辑
3. 基于置信度加权的预测结果估计目标域类别先验，通过log先验校正消除残余类别偏好
### 关键结果
跨域数据集平均准确率为对比方法最优，ViT-B/16、ResNet-50 backbone下分别比零样本CLIP高出4.13、5.07个百分点，ImageNet分布偏移场景下提升效果稳定
