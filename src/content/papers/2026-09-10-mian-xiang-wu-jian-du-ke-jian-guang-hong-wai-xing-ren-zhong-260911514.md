---
title: 'Prototype Matters: Modality-unified Prototype Self-distillation for Unsupervised
  Visible-infrared Person Re-identification'
title_zh: 面向无监督可见光-红外行人重识别的模态统一原型自蒸馏方法
authors:
- Menglin Wang
- Xiaojin Gong
affiliations:
- Nanjing Normal University
- Zhejiang University
arxiv_id: '2609.11514'
url: https://arxiv.org/abs/2609.11514
pdf_url: https://arxiv.org/pdf/2609.11514
published: '2026-09-10'
collected: '2026-09-12'
category: Multimodal
direction: 跨模态表征学习 · 原型自蒸馏
tags:
- Cross-Modal Learning
- Self-Distillation
- Prototype Learning
- Unsupervised Learning
- Person ReID
one_liner: 提出模态统一原型对比与原型自蒸馏结合的无监督跨模态行人重识别框架
practical_value: '- 多模态商品检索、图文匹配等跨模态召回场景，可复用模态统一原型对比方法，同时约束模态内+跨模态相似度，替代仅做跨模态对比的损失设计，提升特征对齐效果

  - 无标注跨模态数据训练时，可采用原型作为稳定教师做自蒸馏，缓解聚类噪声导致的硬标签误差，降低标注成本

  - 多模态检索的端侧轻量优化可借鉴自原型蒸馏思路，无需额外大模型作为教师，降低部署复杂度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
无监督可见光-红外行人重识别任务中，现有基于最优传输的跨模态关联方法存在硬标签分配刚性缺陷，未考虑聚类噪声影响；仅约束跨模态对比损失无法同时优化模态内、跨模态的相似度关系，性能存在瓶颈。
### 方法关键点
1. 设计模态统一原型对比学习策略，同步优化模态内、跨模态的相似度约束，提升特征的模态不变性
2. 引入原型引导的自蒸馏机制，将自原型作为稳定教师信号，在线修正实例与原型的关联关系，缓解聚类噪声干扰
两个模块端到端联合训练，架构轻量易实现。
### 关键结果
在标准VI-ReID基准集上性能全面优于现有无监督基线方法，相关代码已开源可复现。
