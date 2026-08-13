---
title: Learning from Multimodal Pseudo-Labels for Robust Open-Vocabulary Instance
  and Panoptic Segmentation
title_zh: 基于多模态伪标签的鲁棒开放词汇实例与全景分割方法
authors:
- Duy Tran Thanh
- Yeejin Lee
- Byeongkeun Kang
affiliations:
- Seoul National University of Science and Technology
- Chung-Ang University
arxiv_id: '2608.11681'
url: https://arxiv.org/abs/2608.11681
pdf_url: https://arxiv.org/pdf/2608.11681
published: '2026-08-12'
collected: '2026-08-13'
category: Multimodal
direction: 多模态语义对齐 · 伪标签自动生成
tags:
- Multimodal
- Pseudo-Label
- Open-Vocabulary
- CLIP
- Vision-Language Alignment
one_liner: 利用预训练多模态模型自动生成伪标签，提升开放词汇实例与全景分割的鲁棒性
practical_value: '- 可借鉴CLIP引导同义词过滤+GPT caption重建的方案，优化电商商品图文语义对齐，解决同品异名、OOV长尾词匹配问题

  - 伪标签自动生成pipeline可复用到垂类商品分割标注场景，无需人工标注即可低成本扩充商品分割训练数据

  - 语义一致性损失+扩展grounding损失的组合训练思路，可迁移到多模态召回模型的微调环节，提升跨模态匹配鲁棒性'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
开放词汇实例分割（OVIS）、开放集全景分割（OSPS）现有方案存在伪掩码噪声大、图文对齐能力弱、同义词/OOV词处理效果差的问题，依赖大量人工标注成本极高，难以落地到长尾品类场景。

### 方法关键点
1. 提出无人工标注的多模态伪标签生成框架，基于Grounded SAM生成伪分割掩码、LLaVA生成描述性caption、CLIP生成语义对齐同义词集，提供多模态监督信号；
2. 引入三个互补训练目标优化图文对齐：融合视觉grounded同义词的扩展grounding损失、语义一致性损失、生成式caption重建损失，强化跨模态语义匹配能力。

### 关键结果
在COCO数据集上，相比此前SOTA方案，在OVIS、OSPS两大基准测试中均实现稳定大幅性能提升，标注成本降为0的同时超过有监督方案的泛化表现。
