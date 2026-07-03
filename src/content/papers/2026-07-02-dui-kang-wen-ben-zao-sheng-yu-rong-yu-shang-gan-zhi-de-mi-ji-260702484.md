---
title: 'Combating Textual Noise and Redundancy: Entropy-Aware Dense Visual Token Pruning'
title_zh: 对抗文本噪声与冗余：熵感知的密集视觉Token剪枝方法
authors:
- Xuehui Wang
- Xuankun Yang
- Wei Shen
affiliations:
- Shanghai Jiao Tong University
arxiv_id: '2607.02484'
url: https://arxiv.org/abs/2607.02484
pdf_url: https://arxiv.org/pdf/2607.02484
published: '2026-07-02'
collected: '2026-07-03'
category: Multimodal
direction: 多模态大模型 · 视觉Token剪枝推理加速
tags:
- VLM
- Token Pruning
- Entropy
- Submodular Maximization
- Multimodal Inference
one_liner: 提出熵感知视觉Token剪枝框架EADP，优化VLM精度效率权衡，低预算下保留细粒度视觉线索
practical_value: '- 电商多模态搜索/商品理解场景可复用熵感知噪声过滤逻辑，提升用户query与商品视觉特征匹配鲁棒性

  - 低算力端多模态Agent推理可借鉴带空间先验的submodular maximization Token选择方法，低预算下保留细粒度商品/场景特征

  - 生成式推荐多模态内容召回排序链路可引入EADP剪枝逻辑，降低VLM推理延迟，平衡效果与吞吐'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有视觉Token剪枝是VLM加速的核心方案，但在密集指令、细粒度查询场景下易丢失关键视觉线索，核心瓶颈有二：一是文本噪声广泛分布破坏跨模态打分一致性，二是标准Token选择存在特征碎片化问题，难以适配低算力部署需求。
### 方法关键点
1. 提出熵感知密集剪枝框架EADP，将剪枝转化为结构化压缩问题：首先用统计熵量化并过滤文本噪声，生成鲁棒的细粒度指令相关性得分。
2. 放弃朴素Top-K选择，将Token选择建模为带空间先验的submodular maximization问题，显式保证视觉表示的整体性与无冗余性。
### 关键结果
严格Token预算下可稳定保留细粒度视觉线索，在多个高难度多模态基准上达到SOTA性能，大幅优化VLM精度与效率的权衡比
