---
title: 'REBASE: Reference-Background Subspace Elimination for Training-Free In-Context
  Segmentation'
title_zh: REBASE：面向免训练上下文分割的参考背景子空间消除方法
authors:
- Mantha Sai Gopal
- Jaison Saji Chacko
- Harsh Nandwana
- Sandesh Hegde
- Debarshi Banerjee
- Uma Mahesh
affiliations:
- CamCom Technologies Private Limited
arxiv_id: '2607.09082'
url: https://arxiv.org/abs/2607.09082
pdf_url: https://arxiv.org/pdf/2607.09082
published: '2026-07-09'
collected: '2026-07-21'
category: Other
direction: 计算机视觉 · 免训练小样本图像分割
tags:
- Training-Free
- One-Shot Segmentation
- SAM
- Feature Subspace
- Semantic Matching
one_liner: 提出免训练框架REBASE，通过消除参考图背景子空间提升小样本分割精度
practical_value: '- 电商同款搜图场景可复用背景子空间消除思路：对用户上传的参考图提取低秩背景特征子空间，将参考、候选图特征投影到正交空间，过滤背景干扰提升跨图语义匹配准确率

  - 电商新品类商品抠图、素材自动化生产可直接复用REBASE免训练框架：无需标注重训即可基于单张参考图完成新类目商品分割，降低素材处理的人力与时间成本

  - 多模态推荐/多模态Agent的图像理解模块可借鉴相似性加权最远点采样方法：生成更精准的目标区域prompt，提升二手、定制类非标商品的识别准确率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有免训练上下文分割方案结合视觉基础模型与SAM实现单参考图新类目分割，无需类增量学习的重训与内存开销，但参考与query图像的共享背景会在非目标区域产生虚假高相似性，大幅降低prompt定位精度。
### 方法关键点
1. 从参考图像中识别低秩背景特征子空间，将参考、query特征闭式投影到该子空间的正交补集，过滤虚假上下文匹配，得到更干净的语义匹配结果；
2. 采用相似性加权最远点采样生成正点prompt，搭配优化后的稠密相似性先验，进一步提升定位精度。
### 关键结果
无需任何训练或参数更新，在PACO-Part、FSS-1000及ISIC2018等跨域数据集上取得免训练分割方法的新SOTA。
