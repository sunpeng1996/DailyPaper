---
title: 'Falcon Perception-HD: High Density Perception via Reinforcement Learning'
title_zh: Falcon Perception-HD：基于强化学习的高密度感知模型
authors:
- Sofian Chaybouti
- Yasser Dahou
- Ngoc Dung Huynh
- Reda Alami
- Hilde Kuehne
affiliations:
- Technology Innovation Institute, Abu Dhabi, UAE
- Tübingen AI Center / University of Tübingen
- MIT-IBM Watson AI Lab
arxiv_id: '2608.18881'
url: https://arxiv.org/abs/2608.18881
pdf_url: https://arxiv.org/pdf/2608.18881
published: '2026-08-19'
collected: '2026-08-20'
category: Multimodal
direction: 多模态感知 · RL目标对齐优化
tags:
- GRPO
- Reinforcement Learning
- Open-Vocabulary Perception
- Dense Scene Perception
- Self-Annotation
one_liner: 采用GRPO强化学习对齐感知指标，实现高密度场景感知SOTA，消除对NMS等后处理的依赖
practical_value: '- 生成式推荐/多模态Agent输出集合类结果（如多Item召回、多标签生成）时，可采用GRPO直接对齐precision/recall等业务指标，替代MLE损失减少结果重复

  - 多输出去重场景可参考惩罚假阳/假阴的极简reward设计，替代NMS、规则去重等后处理步骤，降低超参数调优成本

  - 高密度商品识别、长尾Query理解等稀缺标注场景，可复用两类混合自标注pipeline，低成本生成RL后训所需数据'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
开放词汇自回归感知模型普遍采用SFT+MLE训练，逐token交叉熵的代理优化目标与precision、recall等真实感知指标存在对齐偏差，高密度场景下性能骤降，且依赖NMS等后处理去重，调参成本高。

### 方法关键点
基于Falcon Perception底座，采用GRPO强化学习做后训，针对集合结构输出设计惩罚假阳/假阴的极简reward，新增多头采样控制适配感知任务；配套开发面向难例指代表达、高密度场景的两类混合自标注pipeline生成训练数据。

### 关键结果
单场景最多支持500个对象检测，性能达SOTA；几乎完全消除掩码重复问题，无需NMS与坐标去重；PBench、SACO-Gold上全难度指代表达分割指标全面提升；无需负样本训练即可保留对象存在性判断能力，MCC指标表现优异。
