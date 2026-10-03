---
title: 'Where-OPD: Spatially Guided On-Policy Self-Distillation of MLLMs with Synthetic
  Scenes'
title_zh: Where-OPD：空间引导的多模态大模型合成场景在策略自蒸馏
authors:
- Sophia Sirko-Galouchenko
- Monika Wysoczanska
- Andrei Bursuc
- Nicolas Thome
- Spyros Gidaris
affiliations:
- Valeo.ai
- Sorbonne Université
- CNRS
- Institut universitaire de France (IUF)
- ILLS Montreal
arxiv_id: '2610.02117'
url: https://arxiv.org/abs/2610.02117
pdf_url: https://arxiv.org/pdf/2610.02117
published: '2026-09-30'
collected: '2026-10-03'
category: Training
direction: 多模态大模型 · 自蒸馏训练优化
tags:
- MLLM
- self-distillation
- on-policy-training
- synthetic-data
- spatial-guidance
one_liner: 提出空间引导的MLLM在策略自蒸馏方法，用无标注合成数据实现合成到真实的感知能力迁移
practical_value: '- 多模态商品理解/属性识别场景可复用空间引导自蒸馏思路，用低成本合成的带空间标注的商品场景数据finetune MLLM，大幅降低标注成本

  - 小模型蒸馏优化可复用on-policy自蒸馏框架，给teacher模型喂额外特权信息（如空间坐标、属性标注），引导student模型隐式习得细粒度感知能力，无需引入外部teacher

  - 跨域迁移场景可复用合成数据预训练+真实数据微调的范式，合成数据训练的能力可稳定迁移到真实场景，可低成本扩充多模态训练数据集'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有MLLM在策略自蒸馏相关探索较少，已有方法依赖人工标注grounding数据或外部教师模型，收益仅局限于视觉放大类任务，泛化性差。
### 方法关键点
1. 提出Where-OPD空间引导自蒸馏框架，给教师模型输入查询相关视觉元素的文本化空间坐标特权信息，无需额外人工标注；
2. 采用程序生成的带自动物体ID、空间坐标的合成场景作为训练数据，实现可扩展的无标注后训练；
3. 教师模型用空间引导定位整合多区域证据，学生模型仅从原始图像和问题学习复现教师的推理行为。
### 关键结果
仅用合成场景完成后训练，在CVBench、V*、ZoomBench等6个真实感知基准上平均性能提升3.23点，在计数、文档/图表理解任务上均有稳定提升，能力可跨任务、跨分布迁移到真实场景。
