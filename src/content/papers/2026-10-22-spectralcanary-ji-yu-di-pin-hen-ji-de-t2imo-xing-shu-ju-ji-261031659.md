---
title: 'SpectralCanary: Embarrassingly Simple Low-Frequency Traces for T2I Dataset-Use
  Auditing'
title_zh: SpectralCanary：基于低频痕迹的T2I模型数据集使用审计方法
authors:
- Sy-Tuyen Ho
- Anirudh Satheesh
- Soham Chawathe
- Huy Nghiem
- Yongkyun Lee
- Andrew Adams Schoen
- Furong Huang
affiliations:
- AllPurposeAI
- University of Maryland
arxiv_id: '2610.31659'
url: https://arxiv.org/abs/2610.31659
pdf_url: https://arxiv.org/pdf/2610.31659
published: '2026-10-22'
collected: '2026-10-24'
category: Multimodal
direction: 多模态生成 · T2I数据集版权审计
tags:
- Text-to-Image
- Dataset Auditing
- Watermarking
- Low Frequency Signal
- Copyright Protection
one_liner: 提出通过低通掩码将固定金丝雀图像融入数据集的T2I审计方案，兼顾图像保真度与检测精度
practical_value: '- 电商自有商品图、素材库可复用该低通水印方案，防止第三方未经授权用自有素材微调T2I生成竞品素材，可溯源盗版训练行为

  - 生成式商品图的版权溯源可复用该轻量检测逻辑，无需复杂模型即可快速定位生成模型的训练数据来源

  - 低频信号注入的思路可迁移到推荐场景的用户行为数据水印、流量反作弊埋点，不影响业务特征有效性同时支持数据泄露审计'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有T2I数据集使用审计方案需在可验证性、保真度、鲁棒性、可部署性之间做权衡，无法在不损坏原始数据质量的前提下，高效检测目标数据集是否被未经授权用于微调T2I模型。
### 方法关键点
1. 通过平滑低通掩码将固定金丝雀图像融合到数据集中每张图像，不修改文本标注，无需辅助生成或逐图优化；
2. 配套轻量验证器即可检测可疑T2I模型的生成结果中是否携带注入的低频审计信号。
### 关键结果数字
1% FPR下，跨2种架构、Pokemon数据集测试中单生成TPR达91.1%，30次生成的模型级检测准确率达94.8%；跨艺术/医疗/时尚等5类数据集+SD3.5测试，平均单生成TPR达92.4%，水印注入后图像SSIM达0.989、ΔFID仅0.05；对抗攻击下移除水印需付出ΔFID上升25以上的质量损失代价。
