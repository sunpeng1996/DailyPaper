---
title: Few-Shot Video Recognition via Hierarchical Metric Learning
title_zh: 基于分层度量学习的少样本视频识别方法
authors:
- Jiaxin Zhang
- Haoran Gao
- Xizhan Gao
- Zihao Dong
- Tingwei Wang
- Sijie Niu
affiliations:
- School of Information Science and Engineering, University of Jinan
arxiv_id: '2609.05242'
url: https://arxiv.org/abs/2609.05242
pdf_url: https://arxiv.org/pdf/2609.05242
published: '2026-09-04'
collected: '2026-09-08'
category: Other
direction: 少样本学习 · 视频动作识别
tags:
- Few-shot Learning
- Action Recognition
- Metric Learning
- Spatial-temporal Feature
- Video Understanding
one_liner: 提出融合空间增强模块与分层多阶段度量约束的少样本动作识别框架，提升类原型泛化与抗噪能力
practical_value: '- 少样本场景下的分层度量学习策略可复用在短视频推荐冷启动类目/行为识别任务，通过渐进式多阶段约束提升小样本下特征区分度

  - 空间增强+时空特征融合模块可迁移到电商短视频/直播内容的商品/行为识别pipeline，优化跨帧全局信息提取效果

  - 多度量互补约束思路可用于用户行为序列特征学习，提升冷启动用户兴趣表征的鲁棒性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有少样本动作识别仅在输出层施加单原型监督，中间层度量约束为并行结构，未沿特征链路做渐进式监督，无法充分利用跨帧全局空间信息，类原型泛化能力受限。
### 方法关键点
1. 设计空间增强模块捕捉跨帧全局空间表征，结合时序MHA、异质对齐、时空特征融合、字典学习模块搭建完整特征处理链路
2. 嵌入分层度量学习策略，包含中心、对齐、对比、字典、原型5种度量，从帧级表征到最终类原型施加渐进式多阶段互补约束，同步优化特征紧凑性、时空对齐度、类间区分性、抗噪鲁棒性
### 关键结果
在5个行业通用少样本动作识别数据集上验证，效果显著优于现有基线方案。
