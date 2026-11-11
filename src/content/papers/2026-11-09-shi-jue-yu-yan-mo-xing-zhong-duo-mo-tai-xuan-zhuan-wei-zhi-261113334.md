---
title: Disentangling Multimodal Rotary Positional Embedding in Vision-Language Models
title_zh: 视觉语言模型中多模态旋转位置嵌入（MRoPE）的解耦分析
authors:
- Zhaoyi Liu
- Haichuan Zhang
- Xiaochuan Gong
- Yancheng Zhu
- Bowei Tian
- Wanghao Ye
- Yufan Zhang
- Ang Li
affiliations:
- University of Maryland, College Park
- University of Utah
arxiv_id: '2611.13334'
url: https://arxiv.org/abs/2611.13334
pdf_url: https://arxiv.org/pdf/2611.13334
published: '2026-11-09'
collected: '2026-11-11'
category: Multimodal
direction: 多模态大模型 · 位置嵌入优化
tags:
- MRoPE
- RoPE
- Vision-Language Model
- Positional Embedding
- Multimodal
- Attention
one_liner: 解耦MRoPE的视觉内编码与跨模态空间效应，验证后者无增益甚至损害性能
practical_value: '- 多模态搜广推的内容理解模块优化时，可去掉给文本token分配宽高坐标的逻辑，消除跨模态空间噪声提升多模态匹配精度

  - 多模态VLM落地时，仅保留视觉token的内空间编码即可满足细粒度grounding需求，无需额外设计跨模态空间关联规则

  - 多模态Agent感知模块开发可直接复用该结论简化位置嵌入实现，降低工程调试成本'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有视觉语言模型广泛使用的MRoPE会为无固有空间结构的文本token分配宽高坐标，引入跨模态空间效应，其对跨模态交互的价值业界存在矛盾认知。
### 方法关键点
将MRoPE的视觉内空间编码能力与跨模态空间效应解耦，突破共享坐标布局下无法同时消除跨模态效应、保留视觉内编码的约束，设计受控实验独立度量两类模块的贡献。
### 关键结果
覆盖多模型规模、多MRoPE变体、多基准测试的实验表明：跨模态空间效应作为空间参考几乎无额外增益，甚至会损害模型性能；视觉内空间编码对细粒度定位任务仍有显著正向作用。
