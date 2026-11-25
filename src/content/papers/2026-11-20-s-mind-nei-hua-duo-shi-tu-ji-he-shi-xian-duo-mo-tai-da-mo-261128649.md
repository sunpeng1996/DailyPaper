---
title: 'S-Mind: Internalizing Multi-View Geometry for Spatial Intelligence'
title_zh: S-Mind：内化多视图几何实现多模态大模型空间智能
authors:
- Muxin Fu
- Peike Yu
- Guibin Zhang
- Wenrui Zhou
- Runze Liu
- Lang Feng
- Fuchao Yang
- Feng Chen
- Yixuan Li
- Mengao Zhang
affiliations:
- The Hong Kong University of Science and Technology
- Nanyang Technological University
- National University of Singapore
- Tongji University
arxiv_id: '2611.28649'
url: https://arxiv.org/abs/2611.28649
pdf_url: https://arxiv.org/pdf/2611.28649
published: '2026-11-20'
collected: '2026-11-25'
category: Multimodal
direction: 多模态大模型 · 空间推理能力增强
tags:
- Multimodal LLM
- Spatial Reasoning
- Multi-view Geometry
- Token Injection
- Inference Acceleration
one_liner: 通过可训练空间token将多视图几何内化到MLLM，大幅提升空间推理精度与推理效率
practical_value: '- 可借鉴空间token注入范式，为AR商品选品、3D家居场景推荐等多模态推荐场景注入空间感知能力，替代低效的外部3D工具调用

  - 训练时注入领域专属token、推理时可移除的设计，可复用在垂域LLM能力注入中，不增加推理开销即可强化垂域效果

  - 多视图信息融合后统一表征的思路，可优化多模态搜索中多视角商品的召回排序特征对齐效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前多模态大模型（MLLM）落地物理世界场景时，普遍缺乏多视图3D场景融合、视角转换推理两大核心空间能力，即使经过空间微调效果依然不佳，工具调用式Agent推理效率极低。
### 方法关键点
提出S-Mind框架，通过一组紧凑的空间token将多视图几何规则内化到MLLM中；训练时监督空间token编码融合后的3D场景信息，推理时可根据需求从任意视角重新生成场景表征；空间能力通过训练内化到主干模型，推理时无需保留空间token即可生效。
### 关键结果
在4个空间基准上，基于Qwen3.5的S-Mind较基线最高提升22.26个点，平均精度超越GPT-6-Astra（+0.45）、Kimi-K3.1-Pro（+1.97）、GLM-5.3-Flash（+7.80）；场景融合准确率达65.11%（基线最高16.02%），视角转换准确率达82.17%（基线最高37.28%）；推理速度较同主干的工具调用Agent快约100倍。
