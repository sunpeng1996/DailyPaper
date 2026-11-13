---
title: 'AROMA: Adaptive Representation-Oriented Multimodal Actuation for Vision-Language
  Model Control'
title_zh: AROMA：面向自适应表征的视觉语言模型多模态控制框架
authors:
- Zhaoning Zhang
affiliations:
- University of Toronto
arxiv_id: '2611.15041'
url: https://arxiv.org/abs/2611.15041
pdf_url: https://arxiv.org/pdf/2611.15041
published: '2026-11-11'
collected: '2026-11-13'
category: Multimodal
direction: 多模态大模型 · VLM推理控制
tags:
- VLM
- Model Steering
- Cross-Attention
- Frozen Model
- Multimodal Control
one_liner: 提出解耦6个控制环节的冻结VLM驱动框架AROMA，大幅提升VLM受控输出准确率
practical_value: '- 可复用 magnitude-normalized 因果子空间驱动方法，优化电商多模态商品理解、库存盘点类Agent任务的输出准确率

  - 迭代Minimal-Effort Actuation（MEA）策略可迁移至多模态生成式推荐的输出对齐场景，在低干预成本下提升目标达成率

  - 解耦干预位置、增益、目标、触发时机的控制框架，可直接复用给Agent的VLM工具调用输出对齐模块'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有VLM机械定位方法无法实现有效可控输出，存在因果敏感度与激活能量不匹配、局部方向在有限尺度下失效、可达数值目标错误三类问题，难以支撑计数等需要精确感知的多模态任务。
### 方法关键点
提出冻结VLM控制框架AROMA，解耦干预位置、几何与增益选择、目标达成路径、目标选择、触发时机6个独立控制环节，核心包含量级归一化因果子空间驱动、迭代最小努力驱动（MEA）两个模块。
### 关键结果
- 在Llama-3.2-11B-Vision-Instruct上，精确计数准确率提升8.00pp
- 同等步长预算下MEA的oracle目标达成率达81.25%，远超基线的15.18%
- 自然场景任务准确率从34.444%提升至38.730%，全量7992样本仅需干预63个输入即可实现准确率正向提升
