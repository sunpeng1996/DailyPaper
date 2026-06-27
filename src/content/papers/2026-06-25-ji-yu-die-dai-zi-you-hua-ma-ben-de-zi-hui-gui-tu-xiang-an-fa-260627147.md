---
title: Safe Autoregressive Image Generation with Iterative Self-Improving Codebooks
title_zh: 基于迭代自优化码本的自回归图像安全生成方法
authors:
- Yunqi Xue
- Zhijiang Li
- Philip Torr
- Jindong Gu
affiliations:
- School of Information Management, Wuhan University
- Torr Vision Group, University of Oxford
arxiv_id: '2606.27147'
url: https://arxiv.org/abs/2606.27147
pdf_url: https://arxiv.org/pdf/2606.27147
published: '2026-06-25'
collected: '2026-06-27'
category: Multimodal
direction: 多模态生成 · 自回归图像安全优化
tags:
- Autoregressive Generation
- Codebook
- Multimodal Safety
- Text-to-Image
- Self-Improving
one_liner: 无需人工标注，利用多模态模型自识别不安全内容迭代优化码本，提升自回归图像生成安全性
practical_value: '- 电商营销素材、商品展示图的自回归生成场景，可复用无标注自校验的迭代优化框架，降低色情、暴力等违规内容生成风险，减少内容审核成本

  - 涉及离散codebook的生成式推荐任务（如Semantic ID生成、多模态召回向量量化），可借鉴「有害空间过滤+无害空间微调」的两步码本优化思路，平衡合规性与业务效果

  - 多模态Agent的内容输出合规模块，可复用模型自身能力做闭环迭代优化，减少对第三方审核接口、人工标注数据集的依赖'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
自回归多模态文生图模型通过码本映射的离散视觉token生成内容，现有安全管控多依赖外部标注/后处理，缺乏针对自回归生成链路的原生安全优化方案，成本高且易影响生成质量。

### 方法关键点
1. 无需人工标注与外部反馈，直接利用多模态模型自身的理解判断能力识别不安全生成结果，构建有害/安全图文对，映射生成有害空间指导码本更新，消除有害token映射关系；
2. 在无害空间内基于安全图文对做码本自适应微调，保证生成内容的质量与语义对齐度；
3. 两步循环迭代直到性能无进一步提升，输出安全增强的模型码本。

### 关键结果
无需额外外部标注，迭代优化后模型有害内容生成概率大幅下降，同时文生图的质量、语义匹配度无显著损耗。
