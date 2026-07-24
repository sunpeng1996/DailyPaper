---
title: 3D-Aware VLMs with Implicit and Explicit Geometries
title_zh: 融合隐式与显式几何信息的3D感知视觉语言模型
authors:
- Wenhao Li
- Xueying Jiang
- Quanhao Qian
- Deli Zhao
- Ran Xu
- Shijian Lu
- Gongjie Zhang
affiliations:
- Nanyang Technological University
- DAMO Academy, Alibaba Group
- HuPan Lab
- Alibaba Group
arxiv_id: '2607.21595'
url: https://arxiv.org/abs/2607.21595
pdf_url: https://arxiv.org/pdf/2607.21595
published: '2026-07-23'
collected: '2026-07-24'
category: Multimodal
direction: 多模态大模型 · 3D感知能力增强
tags:
- VLM
- 3D Perception
- Implicit Geometry
- Explicit Geometry
- Adapter
one_liner: 仅用RGB输入通过融合隐式显式几何token提升VLM的3D空间理解与推理性能
practical_value: '- 电商3D商品展示/AR试穿场景可复用仅RGB输入生成几何token的方法，无需点云等3D数据即可建模空间信息，大幅降低3D内容制作成本

  - 多模态召回/生成式推荐的跨模态特征融合模块，可借鉴「显式+隐式双特征token + 轻量adapter」的架构设计，提升多源特征融合效果

  - 电商导购Agent的空间交互场景（如用户询问「货架左数第三件商品参数」）可集成该3D感知VLM，提升空间推理准确率'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有基于2D输入的VLM在需细粒度空间理解的3D任务上表现较差，依赖额外3D传感器输入的方案落地成本高，难以适配大规模通用场景。

### 方法关键点
提出VLM-IE3D统一框架，仅用RGB视频作为输入：1）设计Implicit Geometry Tokens（IGTs）捕获输入视频的高层几何先验；2）设计Explicit Geometry Tokens（EGTs）编码重建3D属性的细粒度几何结构；3）新增3D感知adapter融合两类几何表征与2D视觉线索，注入强3D归纳偏置。

### 关键结果
在3D视频检测、3D视觉grounding、3D密集字幕、空间推理等多类3D任务上性能全面优于现有方案，已开源代码与预训练模型。
