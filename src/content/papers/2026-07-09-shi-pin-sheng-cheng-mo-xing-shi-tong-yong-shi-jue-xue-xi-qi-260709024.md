---
title: Video Generation Models are General-Purpose Vision Learners
title_zh: 视频生成模型是通用视觉学习器
authors:
- Letian Wang
- Chuhan Zhang
- Rishabh Kabra
- Jasper Uijlings
- Steven Waslander
- Andrew Zisserman
- Joao Carreira
- Kaiming He
- Misha Andriluka
- Eduard Gabriel Bazavan
affiliations:
- Google DeepMind
- University of Toronto
- University College London
- University of Oxford
- MIT
arxiv_id: '2607.09024'
url: https://arxiv.org/abs/2607.09024
pdf_url: https://arxiv.org/pdf/2607.09024
published: '2026-07-09'
collected: '2026-07-13'
category: Other
direction: 通用视觉预训练 · 视频生成范式
tags:
- Video Generation
- Pre-training
- Diffusion Model
- General Vision
- Multimodal Alignment
one_liner: 提出基于视频生成预训练的通用视觉框架GenCeption，性能超专用模型，数据效率提升7至500倍
practical_value: '- 可借鉴生成式预训练思路优化多模态推荐的视觉特征提取器，用短视频生成预训练替代传统图像预训练，提升商品短视频跨模态召回准确率

  - 高数据效率的预训练思路可复用在电商小样本商品分类、素材理解场景，大幅降低素材标注成本

  - 文本指令驱动的多任务视觉感知能力可直接集成到电商Agent的直播/短视频理解模块，同时支撑商品识别、违规检测、卖点提取等多任务需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
NLP领域通过next-token预测预训练实现了从专用模型到通用基础模型的跃迁，而CV领域尚未找到能支撑通用视觉智能的对等预训练范式，缺乏同时具备时空先验、视觉-语言对齐能力、可扩展性的预训练方案。
### 方法关键点
提出GenCeption框架，基于大规模文本到视频生成的diffusion预训练backbone，构建文本指令驱动的前馈感知模型，可无需微调适配多类视觉任务。
### 关键结果
- 在深度估计、表面法向量估计、语义分割、3D关键点预测等任务上达到SOTA，性能匹配或超越DepthAnything3、SAM3等专用模型
- 同等配置下表现优于V-JEPA、Video MAE等主流预训练范式
- 仅需1/7~1/500的训练数据即可达到D4RT、VGGT-Omega等头部模型同等性能
- 仅用合成人类视频训练的模型可泛化到真实场景及动物、机器人等分布外类别
