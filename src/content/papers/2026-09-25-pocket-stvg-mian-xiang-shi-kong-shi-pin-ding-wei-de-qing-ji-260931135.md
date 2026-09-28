---
title: 'Pocket-STVG: lightweight architecture for Spatio-Temporal Video Grounding'
title_zh: Pocket-STVG：面向时空视频定位的轻量级架构
authors:
- Alberto Presta
- Michal Byra
- Grzegorz Stefański
- Karol Szurkowski
- Eryk Kołodziejczyk
- Krzysztof Arendt
affiliations:
- Samsung AI Center, Warsaw, Poland
- IFTR, Polish Academy of Sciences, Warsaw, Poland
arxiv_id: '2609.31135'
url: https://arxiv.org/abs/2609.31135
pdf_url: https://arxiv.org/pdf/2609.31135
published: '2026-09-25'
collected: '2026-09-28'
category: Multimodal
direction: 多模态 · 轻量时空视频文本定位架构
tags:
- Multimodal
- Video Grounding
- Lightweight Architecture
- Zero-shot
- Weakly Supervised
one_liner: 参数不足90M的轻量级级联STVG架构，性能追平弱监督方案、优于早期零-shot方案
practical_value: '- 多模态短视频搜索/商品定位场景可复用「预计算与查询无关的视频表征」的设计，大幅降低大规模视频库推理延迟，适配电商内容检索需求

  - 采用高效预训练组件级联替代端到端大模型的架构思路，可快速落地资源受限的端侧多模态交互场景，比如端内短视频实时问答

  - 同一框架兼容弱监督/零-shot双设置的设计，可迁移至多模态推荐冷启动场景，减少标注数据依赖'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有Spatio-Temporal Video Grounding (STVG)方案普遍依赖大参数量多模态大模型、训练管线复杂，推理成本高，难以适配大规模视频库或资源受限部署场景。
### 方法关键点
P-STVG采用轻量级级联架构，融合基于MobileViCLIP的时序感知视频编码器、MDETR衍生的空间编解码器、共享对齐文本编码器；时序定位可选轻量1D U-Net或简单阈值策略，同时支持弱监督与零-shot设置；视频表征可独立于查询预计算，天然支持索引，适配大规模视频库高效推理。
### 关键结果
总参数量低于90M，性能与现有弱监督STVG方案持平，零-shot表现优于早期同类方案，内存与计算成本仅为前者的极小部分，在HC-STVG v2数据集上实现了最优性能效率trade-off
