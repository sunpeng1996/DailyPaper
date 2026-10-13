---
title: 'SAGE: Salient Factor Discovery and Generation with Visual Foundation Representations'
title_zh: SAGE：基于视觉基础表示的显著因子发现与生成
authors:
- Shuang Liang
- Lejun Liao
- Shiyuan Zhang
- Max C. Zhang
- Xiaolong Luo
- Han Wang
- Stefano Anzellotti
- Yuan Yuan
affiliations:
- HKU
- Boston College
- University of Virginia
- Harvard University
arxiv_id: '2609.39635'
url: https://arxiv.org/abs/2609.39635
pdf_url: https://arxiv.org/pdf/2609.39635
published: '2026-09-29'
collected: '2026-10-13'
category: Multimodal
direction: 多模态 · 无监督视觉因子分解与可控生成
tags:
- Visual Foundation Model
- Unsupervised Discovery
- Diffusion Transformer
- Controllable Generation
- Representation Disentanglement
one_liner: 提出SAGE框架，无需细粒度标签即可分解视觉显著因子，支持无监督子类型发现与可控生成
practical_value: '- 电商商品同款/相似款挖掘场景可复用该无监督因子分解思路，仅需正负两类数据集即可提取商品核心差异特征（如眼镜款式、服装图案），无需细粒度标注

  - 商品营销素材生成场景可借鉴显著因子条件扩散生成架构，固定商品核心属性的同时变化背景、角度等共性特征，低成本生成多版本合规素材

  - 推荐系统细粒度用户偏好建模可参考该因子解耦思路，从用户交互的视觉内容中分离通用偏好与细粒度特异性偏好，提升小众偏好召回准确率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有对比分析方法难以在无细粒度标签的前提下精准捕获目标数据集特有的细粒度特征，无法同时支持子类型发现与保留核心属性的可控生成。

### 方法关键点
1. 基于冻结的自监督视觉表示自编码器，在高维空间隐层直接将表示分解为数据集共有因子与目标特有显著因子；
2. 将参考图像的显著因子作为条件输入Diffusion Transformer，实现保留核心属性的可控生成。

### 关键结果
Digits-ImageNet数据集上无监督子类型探测精度达0.950，远超基线的0.281；显著因子条件生成的子类型准确率达90.5%，是未分解隐层方案的3.27倍，rFID低于2；FFHQ眼镜数据集可自动发现眼镜、墨镜细分类别，定位标注错误样本；视网膜OCT数据集仅靠正常/患病二类标签即可区分3种不同眼病。
