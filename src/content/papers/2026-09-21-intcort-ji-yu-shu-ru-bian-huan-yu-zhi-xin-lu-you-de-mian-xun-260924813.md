---
title: 'INTCORT: Training-Free Spatial Reasoning Enhancement for Vision-Language Models
  via Input Transformations and Confidence Routing'
title_zh: INTCORT：基于输入变换与置信路由的免训练VLM空间推理增强框架
authors:
- Haoran Sun
- Jingqi Xu
- Yanhui Li
- Enci Liu
- Kaidi Xu
- Yanwei Liu
affiliations:
- The University of Hong Kong
- University of Southern California
- China Telecom
- Columbia University
- City University of Hong Kong
arxiv_id: '2609.24813'
url: https://arxiv.org/abs/2609.24813
pdf_url: https://arxiv.org/pdf/2609.24813
published: '2026-09-21'
collected: '2026-09-22'
category: Reasoning
direction: 多模态大模型 · 空间推理增强
tags:
- VLM
- Spatial Reasoning
- Training-Free
- Input Transformation
- Confidence Routing
one_liner: 开发免训练INTCORT框架，通过多视图推理+置信路由提升VLM空间推理能力
practical_value: '- 多模态电商搜索/商品理解场景可直接复用免训练多视图推理思路，无需微调VLM即可提升空间关系判断准确率，避免微调带来的灾难性遗忘

  - 多预测结果聚合可借鉴关系token置信路由策略，无需额外标注即可自动选择最优输出，适配不同基座VLM的成本极低

  - 视觉输入几何变换+query反向变换的组合增强思路，可复用到多模态推荐的训练/推理环节，提升空间语义理解鲁棒性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有VLM空间推理能力弱，训练依赖型增强方案计算成本高、易出现灾难性遗忘，免训练方案易干扰模型内部机制、损伤通用能力。
### 方法关键点
首先验证两个核心假设：合适的图像几何变换+query反转变换可修正错误空间预测；正确预测的关系token置信度显著高于错误预测。INTCORT免训练框架基于上述发现构建，通过输入变换构造多个推理视图，采用关系token置信路由聚合多视图预测结果，全程不修改VLM内部机制。
### 关键结果数字
在多个通用基准、多款主流VLM上平均提升空间推理准确率10.01%，较现有最优方案最高提升25.01%，无通用能力损耗。
