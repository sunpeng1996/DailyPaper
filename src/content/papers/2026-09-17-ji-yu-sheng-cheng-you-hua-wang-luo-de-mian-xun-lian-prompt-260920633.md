---
title: 'Refinement Is Inherently Editable: Training-Free Prompt-to-Prompt Image Editing
  with Generative Refinement Network'
title_zh: 基于生成优化网络的免训练Prompt-to-Prompt图像编辑方法
authors:
- Yulong Chen
- Ziqian Zhang
- Haoyu Zhang
- Ao He
- Senmao Li
- Kai Wang
affiliations:
- City University of Hong Kong (Dongguan)
- City University of Hong Kong
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2609.20633'
url: https://arxiv.org/abs/2609.20633
pdf_url: https://arxiv.org/pdf/2609.20633
published: '2026-09-17'
collected: '2026-09-18'
category: Other
direction: 多模态生成 · 免训练文本引导图像编辑
tags:
- Image Editing
- Training-free
- Generative Refinement Network
- Prompt-to-Prompt
- Text-guided Generation
one_liner: 提出免训练RefineEdit图像编辑框架，通过二值图像码全局优化实现精准编辑同时保留无关内容
practical_value: '- 电商商品主图/详情页批量改图场景可复用该免训练Prompt-to-Prompt编辑逻辑，无需额外标注训练数据即可完成属性修改，降低运营素材生产门槛

  - 自适应空间冻结+有限比特锁定的trick可迁移到商品图局部编辑场景（如改颜色、加配件），避免无关背景/主体被误改，提升编辑稳定性

  - 双分支概率差筛选可编辑区域的思路，可接入AI商品素材生成pipeline做局部修正，大幅提升素材产出效率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有文本引导图像编辑存在两类缺陷：diffusion类方法空间控制不准，易出现编辑不完整或篡改无关区域问题；自回归类方法受固定解码顺序限制，无法修正早期生成决策，亟需免训练的高精准编辑方案。
### 方法关键点
1. 基于生成优化网络搭建RefineEdit免训练框架，通过二值图像码全局优化耦合编辑定位与内容生成，随图像迭代动态重评估编辑证据
2. 从源图像中间状态初始化编辑分支复用原有布局，通过双分支对同源采样比特的概率差筛选可编辑位置，未选比特直接复用源图像状态
3. 引入自适应空间冻结、有限比特锁定机制稳定多步优化过程，无需依赖外部掩码或注意力控制
### 关键结果
在PIE-Bench的9类编辑任务中，背景保留相关指标PSNR、LPIPS、MSE、SSIM均为最优，同时全图与编辑区域的CLIP得分在所有参评方法中排名第一
