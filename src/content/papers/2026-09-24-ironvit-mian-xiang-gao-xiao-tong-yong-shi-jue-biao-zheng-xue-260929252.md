---
title: 'IronViT: Toward Efficient Generalist Visual Representation Learning'
title_zh: IronViT：面向高效通用视觉表征学习
authors:
- Jiaxi Huang
- Yueqi Hu
- Xin Zhu
- Xiaopeng Zhang
- Huiting Qiao
- Yanglin Zhang
- Zefeng Ji
- Rongxue Li
- Yifei Xu
- Huiying Yu
affiliations:
- Xpeng Inc. Robotics Foundation Model Team
arxiv_id: '2609.29252'
url: https://arxiv.org/abs/2609.29252
pdf_url: https://arxiv.org/pdf/2609.29252
published: '2026-09-24'
collected: '2026-09-25'
category: Other
direction: 通用视觉表征学习 · 高效ViT蒸馏
tags:
- ViT
- Knowledge Distillation
- Visual Representation
- Efficient Encoder
- Multimodal
one_liner: 提出两阶段蒸馏范式，构建兼顾多任务能力与高分辨率效率的通用视觉编码器IronViT
practical_value: '- 多模态电商推荐场景下，高分辨率商品图特征提取可复用IronViT混合注意力架构，降低推理延迟，适配大流量生产环境

  - 两阶段多教师蒸馏策略（先整合异构能力再轻量化迁移）可用于跨域推荐、多模态召回模型的蒸馏优化，避免能力退化

  - 高信息密度、广域覆盖的蒸馏语料构建方法，可迁移到多模态推荐训练数据集的清洗、去重、采样流程'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有基于softmax attention的通用视觉backbone高分辨率输入下推理成本极高，直接将多专家教师蒸馏到轻量化架构时，学生模型需同时适配异构能力与不同token混合架构，会严重降低表征质量。
### 方法关键点
1. 遵循「先整合能力再约束计算」原则，采用两阶段蒸馏：先将多个互补专家模型蒸馏到softmax attention能力桥整合异构能力，再逐步迁移到混合softmax-线性注意力的轻量化编码器
2. 定制化数据管线，筛选高信息密度、多域覆盖的蒸馏语料，提升蒸馏效率
### 关键结果
在识别、检索、密集预测、多模态理解、机器人学习5类任务上性能与SOTA专用/通用视觉encoder持平；混合编码器效率优势随输入分辨率提升放大，高分辨率场景推理成本远低于传统softmax注意力架构
