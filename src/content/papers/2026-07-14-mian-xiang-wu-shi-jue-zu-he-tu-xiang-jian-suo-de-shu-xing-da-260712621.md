---
title: 'Towards Vision-Free CIR: Attribute-Augmented Scoring and LLM-Based Reranking
  for Zero-Shot Composed Image Retrieval'
title_zh: 面向无视觉组合图像检索的属性增强打分与LLM重排序方案
authors:
- Ryotaro Shimada
- Yu-Chieh Lin
- Yuji Nozawa
- Youyang Ng
- Osamu Torii
- Yusuke Matsui
arxiv_id: '2607.12621'
url: https://arxiv.org/abs/2607.12621
pdf_url: https://arxiv.org/pdf/2607.12621
published: '2026-07-14'
collected: '2026-07-15'
category: RecSys
direction: 多模态零样本商品检索优化
tags:
- CIR
- Zero-Shot
- Attribute Matching
- Reranking
- LLM
- Multimodal Retrieval
one_liner: 提出属性增强打分+LLM重排序的无视觉CIR框架，零样本下CIRR数据集R@1提升8.79%
practical_value: '- 电商服饰、家居等多模态商品检索场景可直接复用属性增强打分方案，补充文本表征图像损失的细粒度信息，无需额外训练视觉模型可降低部署成本

  - 检索链路顶层可新增轻量LLM重排模块，验证Top候选与用户组合查询的语义一致性，零样本场景下能稳定提升召回准确率

  - 零样本CIR落地可参考FashionIQ实验结论，提前适配语义推理能力与细粒度视觉匹配精度的权衡方案'
score: 8
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有无视觉（将图像转为文本表征）检索方案在组合图像检索（CIR）任务中存在文本描述丢失视觉细节的缺陷，零样本场景下效果较差，无法适配电商等实际多模态检索需求。
### 方法关键点
1. 设计属性增强混合打分模块，通过显式属性匹配补充文本表征丢失的细粒度视觉信息；
2. 新增LLM重排层，验证Top检索候选与用户组合查询的语义一致性，过滤不符合要求的结果。
### 关键结果
在公开CIRR数据集上优于现有零样本CIR方法，R@1达44.04%，相对提升8.79%；FashionIQ数据集实验明确了语义推理与细粒度视觉匹配的权衡关系，消融实验验证两个核心模块均能稳定带来效果提升。
