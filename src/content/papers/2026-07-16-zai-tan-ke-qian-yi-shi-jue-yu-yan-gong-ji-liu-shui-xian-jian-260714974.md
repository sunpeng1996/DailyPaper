---
title: 'On Success and Simplicity: A Second Look at Transferable Vision-Language Attack
  Pipeline'
title_zh: 再探可迁移视觉语言攻击流水线：简化方案反而效果更优
authors:
- Yuchen Ren
- Zhengyu Zhao
- Chenhao Lin
- Bo Yang
- Chao Shen
affiliations:
- 西安交通大学网络空间安全学院
- 信息工程大学数学工程与先进计算国家重点实验室
arxiv_id: '2607.14974'
url: https://arxiv.org/abs/2607.14974
pdf_url: https://arxiv.org/pdf/2607.14974
published: '2026-07-16'
collected: '2026-07-20'
category: Multimodal
direction: 多模态预训练模型对抗攻击优化
tags:
- VLPM
- Adversarial Attack
- Cross-modal Interaction
- Transferability
- Efficiency Optimization
one_liner: 提出极简视觉语言攻击流水线SimVLA，大幅提升迁移性同时显著降低算力开销
practical_value: '- 电商多模态检索（图文搜、以图搜品）场景做鲁棒性评估时，可直接复用SimVLA流水线生成对抗样本，验证系统抗攻击能力

  - 多模态推荐/搜索模型迭代时，可参考核心结论，避免盲目堆叠复杂损失、多阶段流程，优先基于领域知识优化跨模态交互模块，兼顾效果与算力效率

  - 资源受限的端侧多模态模型部署场景，可借鉴SimVLA轻量化设计思路，裁剪冗余操作降低显存、耗时开销'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视觉语言预训练模型（VLPM）的可迁移攻击流水线普遍依赖复杂损失函数、多阶段分步攻击，冗余操作多，性能和效率存在明显短板。
### 方法关键点
定位三类由不合理跨模态交互、过度操作导致的性能瓶颈，提出极简SimVLA流水线，引入跨模态词识别等领域知识优化攻击逻辑，完全去除冗余的复杂设计。
### 关键结果
在4个数据集、3个下游任务上验证性能优势：Flickr30k图文检索任务上，R@1迁移性比SOTA基线高8.01%~14.71%，耗时仅为基线的35.73%，峰值显存占用仅为46.26%。
