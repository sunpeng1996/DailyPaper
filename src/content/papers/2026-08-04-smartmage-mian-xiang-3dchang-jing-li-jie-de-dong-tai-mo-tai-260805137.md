---
title: 'SmartMage: Dynamic Modality Orchestration for 3D Scene Understanding'
title_zh: SmartMage：面向3D场景理解的动态模态编排框架
authors:
- Yue Zhang
- Yingzhao Jian
- Yunqiu Xu
- Xiaoxiao Sun
- Hehe Fan
affiliations:
- Zhejiang University
- Stanford University
arxiv_id: '2608.05137'
url: https://arxiv.org/abs/2608.05137
pdf_url: https://arxiv.org/pdf/2608.05137
published: '2026-08-04'
collected: '2026-08-07'
category: Multimodal
direction: 多模态大模型 · 动态模态调度优化
tags:
- MLLM
- Multimodal Orchestration
- 3D Scene Understanding
- Adaptive Routing
- MoE Gating
one_liner: 提出支持动态模态编排的统一多模态大模型，实现3D场景理解性能SOTA
practical_value: '- 多模态Agent（如电商实景导购、3D家装推荐Agent）可复用SMART模块逻辑，根据用户query语义动态选择调用图像/点云/深度等模态输入，减少无关模态噪声同时降低算力开销

  - 多模态生成式推荐系统可借鉴MAGE模态感知门控专家设计，给不同模态数据分配对应专长的LoRA/MoE专家，提升多模态特征融合推理效率

  - 3D商品/场景理解类业务（如AR试穿、家居搭配推荐）可参考其模态-语义偏好分析范式，提前给不同语义类query配置最优模态组合做预路由优化'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
3D场景理解是具身智能核心能力，需联合视觉、几何等多模态异质信息推理，现有MLLM采用固定模态组合，未匹配不同query的模态需求，易引入无关模态噪声、浪费算力同时稀释推理效果。

### 方法关键点
核心包含两个模块：
1. Semantic-guided Modality Adaptive RouTng（SMART）模块，结合语义先验、文本-模态对齐度、模态质量三个维度动态筛选任务相关模态；
2. Modality-Aware Gating Expert（MAGE）模块，基于模态先验引导MoE专家激活，实现多模态推理的自适应专业化。

### 关键结果
在5个3D场景理解基准集上取得SOTA性能，在纯RGB视频理解基准上达到竞争力水平，自研细粒度诊断基准ScanFacet验证了模态-语义匹配模式的有效性。
