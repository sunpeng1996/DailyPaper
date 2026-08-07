---
title: 'UG-UMRE: Uncertainty-Guided Modality Augmentation and Distributional Calibration
  for Unified Multimodal Relation Extraction'
title_zh: 面向统一多模态关系抽取的不确定性引导模态增强与分布校准
authors:
- Bo Kong
- Liruiz Jia
- Yi Liang
- Chao Liu
- Dongfang Han
- Tianwei Yan
- Yuan Liu
- Shengquan Liu
affiliations:
- Xinjiang University
- Chongqing Jiaotong University
arxiv_id: '2608.04949'
url: https://arxiv.org/abs/2608.04949
pdf_url: https://arxiv.org/pdf/2608.04949
published: '2026-08-05'
collected: '2026-08-07'
category: Multimodal
direction: 多模态关系抽取 · 不确定性引导优化
tags:
- Multimodal Relation Extraction
- Uncertainty Estimation
- Contrastive Learning
- Variational Information Bottleneck
- Distribution Alignment
one_liner: 提出含两个可插拔不确定性模块的UG-UMRE，解决多模态关系抽取噪声与对齐问题，性能达SOTA
practical_value: '- 多模态召回/粗排的跨模态对齐场景可复用JAUA模块，基于概率分布一致性构建共享隐空间，降低图文模态分布差异，提升跨模态匹配效果

  - 处理多模态特征噪声可引入UDUA模块，基于变分信息瓶颈将特征建模为高斯分布，搭配不确定性感知对比学习实现降噪，同时保留核心语义信息

  - 两个模块均为可插拔设计，可直接嵌入现有多模态理解、商品内容理解链路，无需大幅重构原有架构，落地成本低'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
统一多模态关系抽取（UMRE）需识别文本实体与视觉对象的模态内、跨模态关联，现有方案存在两类核心缺陷：一是忽略固有偶然不确定性引发噪声传播，二是不同模态分布的深层异质性阻碍跨模态对齐，限制抽取精度。
### 方法关键点
1. 设计不确定性驱动单模态增强（UDUA）模块：基于变分信息瓶颈将特征建模为高斯分布，结合不确定性感知自监督对比学习，在保留语义一致性的同时过滤噪声；
2. 引入联合偶然不确定性对齐（JAUA）模块：作为全局语义预校准机制，利用概率分布一致性构建共享隐空间，通过同步跨模态统计属性消除分布gap，为细粒度交互提供支撑。
### 关键结果
在UMRE、MORE、MNRE三个基准数据集上性能达到SOTA，UDUA、JAUA均为可插拔模块，泛用性强
