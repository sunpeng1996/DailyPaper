---
title: Towards Closing the Performance Gap in Cross-Modal Place Recognition
title_zh: 缩小跨模态地点识别性能差距的方法研究
authors:
- Ofer Idan
- Dan Badur
- Yoli Shavit
affiliations:
- Bar-Ilan University, Israel
arxiv_id: '2611.34877'
url: https://arxiv.org/abs/2611.34877
pdf_url: https://arxiv.org/pdf/2611.34877
published: '2026-11-25'
collected: '2026-11-27'
category: Multimodal
direction: 跨模态图文匹配 · 地点识别
tags:
- Cross-Modal Retrieval
- Place Recognition
- DINOv2
- BGE
- Reranking
one_liner: 提出两阶段跨模态地点识别框架CrossPlace，大幅提升图文匹配精度，缩小与单模态方法的性能差距
practical_value: '- 多模态检索业务可复用「全局粗排+细粒度token级交叉注意力精排」的两阶段架构，平衡大规模召回的效率与精度

  - 图文匹配任务优化可优先提升视觉token粒度，搭配强通用文本编码器（如BGE系列）做渐进式微调，可获得最大性能收益

  - 多模态系统评测可扩展不同极端场景、大库规模的测试集，提前验证方案上线后的鲁棒性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
跨模态地点识别（CMPR）可实现自然语言描述到地理标记图像库的匹配，支撑无视觉查询的定位与语言引导导航，但现有视觉语言模型即使经过任务适配，性能仍远低于单模态视觉地点识别（VPR）基线，核心瓶颈是难以捕捉图像区域与文本细节的细粒度对应关系。
### 方法关键点
提出两阶段CrossPlace框架：第一阶段用联合对齐的DINOv2-B/14视觉骨干，搭配渐进式微调的BGE-Large文本编码器做全局粗召回；第二阶段用轻量token级交叉注意力重排器优化Top候选。消融实验验证视觉token密度是性能提升最大驱动因素，文本编码器容量、任务微调可提供互补增益。
### 关键结果
在所有已有及新增的城市级、极端天气/光照场景基准上，Recall@1较此前跨模态方法实现两位数提升，追平齐单模态文本检索性能，大幅缩小与单模态VPR的性能差距。
