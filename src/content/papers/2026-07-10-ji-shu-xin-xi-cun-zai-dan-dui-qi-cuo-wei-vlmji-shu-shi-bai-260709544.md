---
title: 'The Count Is There, but Misaligned: Understanding and Correcting Counting
  Failures in VLMs'
title_zh: 计数信息存在但对齐错位：VLM计数失败问题的解析与修正
authors:
- Ahmed Oumar El-Shangiti
- Abzal Nurgazy
- Hilal AlQuabeh
- Nikolai Rozanov
- Kentaro Inui
affiliations:
- MBZUAI
- DataBayt.AI Labs
- Imperial College London
arxiv_id: '2607.09544'
url: https://arxiv.org/abs/2607.09544
pdf_url: https://arxiv.org/pdf/2607.09544
published: '2026-07-10'
collected: '2026-07-13'
category: Multimodal
direction: 多模态模型 · 推理能力优化
tags:
- VLM
- object counting
- activation probing
- inference-time optimization
- self-correction
one_liner: 通过激活探针定位VLM内部计数信息对齐错位问题，提出推理时无参数自修正方法，最高提准确率15.6个百分点
practical_value: '- 电商多模态搜索/商品审核场景可复用激活探针思路检测VLM数值类推理错误，无需重训即可提升商品件数、包装规格等识别准确率

  - 仅对探针检测到的错误样本重prompt的策略，可在几乎不增加推理开销的前提下提升效果，可迁移到所有支持错误探针检测的LLM/VLM任务

  - 内部表征错位而非知识缺失的结论，可指导多模态推荐场景下VLM优化，优先做推理时对齐而非全量重训'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
VLM在图像captioning、VQA等多模态任务表现优异，但基础物体计数能力存在明显缺陷，此前无法明确问题根源是内部知识缺失，还是内部表征与输出的对齐存在gap。
### 方法关键点
1. 基于4款主流VLM、5个计数数据集的激活值训练简单探针，验证非线性探针可稳定检测计数错误，证明VLM常正确编码计数信息但输出错误；
2. 通过SVCCA分析确认，真值计数探针与模型输出探针共享部分激活子空间，但读取方向存在错位；
3. 提出检测器引导的自修正推理方案，仅当内部错误检测器预测推理失败时触发重prompt，无参数更新。
### 关键结果
该推理时干预方案可将计数准确率最高提升15.6个绝对百分点，仅增加极少量额外推理成本。
