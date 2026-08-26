---
title: Linear Probing Provides Robust and Efficient Detection of Machine-Generated
  Text
title_zh: 基于线性探针的鲁棒高效机器生成文本检测方法
authors:
- Gerrit Quaremba
- Hanqi Yan
- Elizabeth Black
- Denny Vrandecic
- Elena Simperl
affiliations:
- King's College London
- Wikimedia Foundation
arxiv_id: '2608.24780'
url: https://arxiv.org/abs/2608.24780
pdf_url: https://arxiv.org/pdf/2608.24780
published: '2026-08-25'
collected: '2026-08-26'
category: LLM
direction: LLM 机器生成文本检测
tags:
- Machine-Generated-Text
- Linear-Probing
- Out-of-Domain
- Text-Classification
- LLM-Evaluation
one_liner: 基于线性探针实现高效鲁棒机器生成文本检测，跨域AUC提升11且仅需不足100训练样本
practical_value: '- 电商场景下UGC/AI生成的商品评论、营销文案真伪检测可直接复用线性探针方案，仅需少量标注样本即可上线，性能优于现有复杂检测器

  - Agent交互生成内容的合规校验场景，可基于线性探针提取的连续machineness分值做细粒度风险分级，无需大量标注数据

  - 跨域小样本文本分类任务可借鉴本研究思路，优先验证低维隐空间线性可分性，用线性探针降低建模成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
机器生成文本（MGT）滥用风险凸显，现有监督检测方法跨域（OOD）性能衰减严重，且依赖大规模标注训练集。
### 方法关键点
1. 验证MGT与人类写作文本（HWT）的隐层表示在低维空间存在线性可分性，核心差异来自二者表示质量的系统性区别
2. 基于上述发现训练两种线性探针变体，捕获隐空间中通用的MGT特征方向
### 关键结果
在4个基准数据集上对比16个基线方法，OOD检测AUC平均提升11；仅需<100个训练样本即可达到接近峰值性能；探针输出的特征向量可计算连续「机器度」分值，支持AI编辑文本的细粒度识别
