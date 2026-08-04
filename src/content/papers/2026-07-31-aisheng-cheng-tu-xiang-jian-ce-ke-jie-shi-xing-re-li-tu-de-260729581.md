---
title: 'Explaining AI-Image Detection: What the Heatmap Actually Shows'
title_zh: AI生成图像检测可解释性：热力图的真实指示含义
authors:
- Leonid Kuturin
- Ilya Sotnikov
- Mark Khusnutdinov
- Mikhail Potemkin
- Pavel Baranas
- Aleksandra Korepanova
- Alexander Kalashnikov
affiliations:
- Sirius Educational Centre
- HSE University
arxiv_id: '2607.29581'
url: https://arxiv.org/abs/2607.29581
pdf_url: https://arxiv.org/pdf/2607.29581
published: '2026-07-31'
collected: '2026-08-04'
category: Multimodal
direction: 多模态内容风控 · 生成图像检测
tags:
- AI-generated Image Detection
- Explainable AI
- Heatmap Attribution
- E-commerce Moderation
- Compression Robustness
one_liner: 针对电商伪造评论图场景，量化压缩偏差对AI图检测的影响，验证各类归因热力图的实际效用
practical_value: '- 电商内容风控场景训练生成图检测模型时，需对齐真实图与生成图的最后一步编码格式，可大幅提升PR-AUC约0.17，避免压缩历史带来的评估虚高

  - 生成图检测的归因热力图选择上优先用扰动法，不推荐Gradient-CAM类方法，集成区域归因图兼顾效率与精度，比遮挡法快3倍左右

  - 上线检测模型前必须做跨编码格式的鲁棒性测试，避免用户上传时的压缩操作导致模型误判漏判'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
电商平台依赖用户上传的评论图处理退款申请，AIGC技术让伪造高逼真度评论图的成本趋近于0，现有AI生成图检测模型的性能评估普遍受压缩历史干扰存在虚高，作为检测证据的归因热力图的真实有效性也缺乏系统性量化验证。
### 方法关键点
基于186527张电商评论图构建测试集，通过控制正负样本的最终编码格式消除压缩偏差，对比5款公开检测模型与自研模型的鲁棒性，采用因果验证框架测试17种主流归因热力图的实际效用。
### 关键结果
原始训练的最优模型在产品不相交划分上PR-AUC达0.9999，对齐生成图与真实图的最终编码格式后，PR-AUC提升0.176±0.009；最优集成区域归因图生成速度为12.4s/张，比传统遮挡法快3.6倍，像素AP领先所有基线。
