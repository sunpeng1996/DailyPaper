---
title: 'GNM Head: A Generative aNthropometric Model of the human head'
title_zh: GNM Head：人类头部生成式人体测量参数模型
authors:
- Stylianos Ploumpis
- Jan Bednarik
- Gaspard Zoss
- Ruslan Guseinov
- Luca Prasso
- Prashanth Chandran
- Oliver Boyne
- Vasileios Choutas
- Timo Bolkart
- Daoye Wang
affiliations:
- Google
arxiv_id: '2607.23687'
url: https://arxiv.org/abs/2607.23687
pdf_url: https://arxiv.org/pdf/2607.23687
published: '2026-07-25'
collected: '2026-07-30'
category: Other
direction: 3D生成·人体头部参数化建模
tags:
- 3DMM
- Generative Model
- Parametric Model
- 3D Reconstruction
- Computer Graphics
one_liner: 开源覆盖头脸颈眼口舌的高精度3D头部参数模型，拟合性能达SOTA
practical_value: '- 电商虚拟主播/数字人直播业务可直接复用该开源模型，大幅降低高精度3D头部建模的研发成本

  - 美妆、眼镜、首饰类AR试戴场景可利用模型的眼、口部精细结构，提升试戴贴合度与真实感

  - 商品3D建模场景可借鉴其「扫描数据+人工高质量样本混合训练+子模型拆分」的思路，提升3D生成精度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有公开3D头部参数模型解剖覆盖范围有限，仅建模外部几何，忽略口内、眼部结构，且受低质输入数据集限制，几何精度不足，无法满足大视觉生成模型的高精度空间控制需求。
### 方法关键点
1. 提出覆盖头部、面部、颈部、眼球、牙齿、舌头全结构的生成式人体测量模型GNM Head；
2. 训练数据集融合大规模高分辨率3D扫描库与艺术家制作的高精度解剖结构定制样本；
3. 架构拆分眼部、口内结构为专用子模型独立建模，强化精细结构的表达能力。
### 关键结果
在3D人脸扫描拟合任务上性能达到SOTA，全套框架已完全开源供社区使用。
