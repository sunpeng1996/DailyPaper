---
title: Uncertainty-Aware Cross-Modal Remote Sensing Image-Text Retrieval via Evidential
  Learning
title_zh: 基于证据学习的不确定性感知跨模态遥感图文检索方法
authors:
- Zhuoyue Wang
- Xueqian Wang
- Gang Li
- Chengxi Li
- Yongpan Liu
- Yifang Ban
arxiv_id: '2607.06032'
url: https://arxiv.org/abs/2607.06032
pdf_url: https://arxiv.org/pdf/2607.06032
published: '2026-07-07'
collected: '2026-07-11'
category: Other
direction: 跨模态图文检索 · 不确定性感知优化
tags:
- Cross-Modal Retrieval
- Evidential Learning
- Uncertainty Estimation
- Test-Time Augmentation
- Knowledge Distillation
one_liner: 采用证据学习建模跨模态匹配不确定性，提升非理想条件下遥感图文检索鲁棒性
practical_value: '- 电商跨模态检索（文本搜商品、图搜图）场景可借鉴EDL建模匹配结果不确定性，区分不同query置信度，对低置信度结果走兜底策略提升业务稳定性

  - 可复用不确定性-正确性对齐（UCL）训练目标，让模型输出的不确定性与实际匹配准确率正相关，可用于bad case触发后的干预流程

  - 测试阶段可对高不确定性query采用场景感知的test-time augmentation优化，无需重新训练即可提升非理想输入下的检索鲁棒性

  - 预训练导师编码器的模态内相似性蒸馏trick可用于小模型跨模态检索优化，提升小模型匹配分布的区分度'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
跨模态遥感图文检索测试阶段常存在图像降质、文本词汇异构等非理想输入，现有方法默认所有查询置信度一致，易输出不可靠检索结果。
### 方法关键点
1. 训练阶段引入证据学习（EDL）将图文跨模态匹配关系建模为Dirichlet分布，直接输出每个查询的匹配不确定性；
2. 新增不确定性-正确性对齐（UCL）训练目标，让估计的不确定性与检索实际正误对齐：正确检索对应低不确定性，错误检索对应高不确定性；
3. 加入模态内关系学习，从预训练导师编码器蒸馏模态内相似结构，提升Dirichlet分布的区分度；
4. 测试阶段按固定拒识比例设阈值，低不确定性结果直接返回，高不确定性结果采用场景感知的测试时增强优化。
### 关键结果
与现有SOTA跨模态遥感图文检索方法性能相当，在图像扰动、文本词汇异构等非理想条件下鲁棒性显著提升。
