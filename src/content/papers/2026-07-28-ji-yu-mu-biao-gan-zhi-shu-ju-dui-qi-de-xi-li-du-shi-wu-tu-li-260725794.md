---
title: Fine-Grained Food Image Understanding via Target-Aware Data Alignment
title_zh: 基于目标感知数据对齐的细粒度食物图像理解
authors:
- Jui-Feng Chi
- Wei-Lun Chu
- Bruce Coburn
- Jinge Ma
- Fengqing Zhu
affiliations:
- Purdue University
- Elmore Family School of Electrical and Computer Engineering
arxiv_id: '2607.25794'
url: https://arxiv.org/abs/2607.25794
pdf_url: https://arxiv.org/pdf/2607.25794
published: '2026-07-28'
collected: '2026-07-30'
category: Multimodal
direction: 多模态细粒度图文理解 · 数据对齐
tags:
- Multimodal
- CLIP
- VLM
- Data Curation
- Image-Text Retrieval
- Fine-grained Recognition
one_liner: 提出数据中心多模态对齐方案，优化细粒度食物图文理解，兼顾检索性能与推理效率
practical_value: '- 餐饮外卖、生鲜电商等垂类多模态商品理解/检索场景，可复用「目标感知数据筛选+VLM caption精修」流程，清洗爬取的异构图文数据，提升垂类模型性能

  - 多模型融合落地时可参考分层决策策略：仅轻量小模型结果不一致时调用大VLM，大幅降低推理成本的同时保障效果

  - 垂类多模态模型训练可复用「先提纯训练数据→训练多个互补小模型→分层融合」架构，无需全量依赖大VLM，落地性价比更高'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
CLIP类VLM落地细粒度垂类图文理解时，网页爬取的异构图文对存在域偏移、跨模态对齐差问题（caption噪点多、与视觉内容弱关联），模型性能受限。
### 方法关键点
1. 目标感知数据筛选：提取和目标分布视觉匹配的训练子集
2. VLM caption精修：生成视觉对齐、符合目标风格的高质量描述
3. 分层多专家融合：训练多个互补CLIP类检索专家，仅专家决策不一致时调用大VLM，平衡效果与成本
### 关键结果
- 仅VLM caption精修步骤就带来平均19%的检索性能提升
- 全方法检索分数是纯VLM检索方案的2倍以上，推理效率显著更高
