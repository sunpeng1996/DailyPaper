---
title: 'CV-OPD: Contrastive Vision On-policy Distillation'
title_zh: CV-OPD：对比视觉在线策略蒸馏方法
authors:
- Haowei Wang
- Hao Lin
- Qi Zhu
- Jiayi Ji
- Deyi Ji
- Liujuan Cao
- Rongrong Ji
affiliations:
- 厦门大学多媒体可信感知与高效计算教育部重点实验室
- Moxin Technology
arxiv_id: '2610.13264'
url: https://arxiv.org/abs/2610.13264
pdf_url: https://arxiv.org/pdf/2610.13264
published: '2026-10-09'
collected: '2026-10-13'
category: Training
direction: 多模态大模型 · 视觉蒸馏训练优化
tags:
- On-policy Distillation
- VLM
- Contrastive Learning
- Knowledge Distillation
- Visual Reasoning
one_liner: 提出带对比约束与差异门控的VLM蒸馏方法，解决蒸馏过程不依赖视觉证据的捷径问题
practical_value: '- 做多模态推荐/商品理解VLM蒸馏时，可复用CV-OPD的Contrastive Divergence Loss（CDL），规避模型只依赖文本语义不看视觉内容的捷径问题，提升商品属性识别、主图质检准确率

  - 可借鉴Discrepancy Aware Gate（DAG）的token级/样本级差异筛选机制，优化多模态Agent的视觉注意力分配，降低无效特征计算开销

  - 做VLM小模型蒸馏部署时，可引入该方法保证小模型视觉推理能力不退化，适配端侧多模态搜索/推荐场景'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
On-policy distillation（OPD）是VLM post-training的常用高效方案，但观测到经OPD蒸馏的VLM存在严重捷径问题：即使相关视觉区域被掩码或替换为噪声，模型仍能准确回答问题，本质是蒸馏过程缺乏视觉约束，模型未真正学习依赖视觉证据完成推理。
### 方法关键点
1. 提出CV-OPD框架，引入与答案无关的负例teacher，设计Contrastive Divergence Loss（CDL），通过对比正负teacher的输出分布约束学生特征分布，修正学生对视觉区域的利用逻辑；2. 新增Discrepancy Aware Gate（DAG），基于token级、样本级差异筛选视觉相关token参与优化，引导学生注意力聚焦有效视觉内容。
### 关键结果
在多类细粒度视觉基准测试中，CV-OPD大幅缓解蒸馏捷径问题，现有VLM的视觉推理能力实现一致性提升。
