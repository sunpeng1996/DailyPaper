---
title: Enhancing In-context Panoramic Generation via Geometric-aware Pretraining
title_zh: 基于几何感知预训练优化上下文全景图像生成
authors:
- Haoran Feng
- Ruiyang Zhang
- Longyi Zhang
- Dizhe Zhang
- Lu Qi
affiliations:
- Insta360 Research
- Tsinghua University
- Beihang University
- Wuhan University
arxiv_id: '2607.08765'
url: https://arxiv.org/abs/2607.08765
pdf_url: https://arxiv.org/pdf/2607.08765
published: '2026-07-08'
collected: '2026-07-10'
category: Multimodal
direction: 多模态生成 · 全景图像生成编辑
tags:
- Panoramic Generation
- In-context Generation
- Geometric-aware Pretraining
- Multimodal Generation
- Dataset Construction
one_liner: 提出两阶段上下文全景生成框架Canvas360及百万级专用数据集，支持多类全景生成编辑任务性能领先
practical_value: '- 做电商VR/虚拟逛店、3D商品全景展示场景时，可复用并行深度生成、velocity循环padding技巧，解决全景生成畸变、几何一致性差的问题

  - 做单框架多任务统一生成的架构设计时，可借鉴token级拼接方案，在统一底座上支持多下游任务，降低多模型部署维护成本

  - 垂直领域生成模型缺乏训练数据时，可参考其构建百万级配对专用数据集的思路，覆盖核心下游场景做监督训练，提升模型泛化性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有上下文全景生成任务缺乏大规模高质量专用训练数据，生成结果普遍存在几何一致性差、全局连贯性不足、物体畸变等问题，且单模型难以同时支持多类全景生成/编辑任务。
### 方法关键点
1. 构建包含100万高质量配对样本的Canvas360Dataset，覆盖风格迁移、补绘、扩绘、编辑等核心上下文生成场景；
2. 两阶段框架Canvas360引入并行深度生成、velocity循环padding、相似度损失正则三大优化，引导模型学习几何感知表示；
3. 基于token级拼接实现单框架统一支持多下游任务，提升任务覆盖度和建模灵活性。
### 关键结果
全景图像保真度显著提升，全景专用FAED指标表现尤为突出，所有上报量化评估指标均达到领先或可比水平，任务覆盖度和灵活性优于此前方案。
