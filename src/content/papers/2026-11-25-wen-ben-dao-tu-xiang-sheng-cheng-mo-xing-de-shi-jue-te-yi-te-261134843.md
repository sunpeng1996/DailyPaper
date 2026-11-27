---
title: Probing Visual Idiosyncrasies in Text-to-Image Models
title_zh: 文本到图像生成模型的视觉特异特征探究
authors:
- Yongqian Peng
- Hongjie Li
- Yichao Zhou
- Chi Zhang
- Yixin Zhu
affiliations:
- Peking University
- PKU-Wuhan Institute for AI
- XS Vision
arxiv_id: '2611.34843'
url: https://arxiv.org/abs/2611.34843
pdf_url: https://arxiv.org/pdf/2611.34843
published: '2026-11-25'
collected: '2026-11-27'
category: Multimodal
direction: 多模态T2I模型属性检测与溯源
tags:
- Text-to-Image
- Visual Idiosyncrasy
- Model Attribution
- Multimodal
- Source Classification
one_liner: 发现前沿开源T2I模型输出存在隐式视觉特异特征，可实现100%准确的模型来源分类
practical_value: '- 电商生成商品营销图场景下，可利用T2I模型特异特征快速溯源盗版生成素材，保护自有生成内容版权

  - 开展生成式推荐素材的匿名A/B测试时，需规避模型特异特征泄露版本信息，避免人类偏好评估结果出现偏差

  - 可复用低阶纹理、布局/深度、隐式风格偏好三层特征分析框架，定位不同生成模型输出的差异化特征，优化素材生成选型'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前主流T2I模型生成图像的视觉质量趋同，其输出是否存在模型特异特征，对生成内容溯源、跨模型对比、匿名偏好评估等场景至关重要，现有研究未系统拆解这类特征的层级构成。
### 方法关键点
选取Text-to-Image Arena排名前4的开源T2I模型（HiDream-O1-Dev、FLUX.2-dev、HunyuanImage-3.0、Qwen-Image-2512）生成同prompt样本，用ResNet-50构建来源分类器，从低阶纹理、中阶布局/深度/反照率、高阶隐式风格偏好三个层级拆解可区分的视觉特异特征。
### 关键结果
ResNet-50在域外prompt的测试集上分类准确率达100%，人类pairwise判别任务准确率仅62.61%；仅用低阶纹理训练的轻量MLP即可达到ResNet-50同等性能，给出特征提示后人类判别准确率提升9.03个百分点。
