---
title: 'Latent-Foresight: End-to-End Learning Predictable Representations for Latent
  World Models'
title_zh: Latent-Foresight：面向隐式世界模型的可预测表征端到端学习
authors:
- Efstathios Karypidis
- Spyros Gidaris
- Nikos Komodakis
affiliations:
- Archimedes, Athena Research Center, Greece
- valeo.ai
- National Technical University of Athens
- University of Crete
- IACM-Forth
arxiv_id: '2610.01942'
url: https://arxiv.org/abs/2610.01942
pdf_url: https://arxiv.org/pdf/2610.01942
published: '2026-09-30'
collected: '2026-10-03'
category: Agent
direction: Agent 世界模型时序表征学习
tags:
- World Model
- Representation Learning
- End-to-End Training
- Temporal Prediction
- Flow-based Generative Model
one_liner: 端到端联合训练隐式分词器与流生成动力学模型，提升世界模型时序表征可预测性
practical_value: '- 做用户行为时序预测/动态兴趣建模时，可参考端到端联合训练表征压缩与时序预测模块的思路，替代传统先预训练Embedding再冻住训预测器的两阶段方案，提升时序一致性

  - 多目标联合优化时可复用文中防止latent collapse、对齐重构与生成目标的trick，解决训练不稳定问题

  - 构建电商场景决策Agent的未来交互预测模块时，可借鉴该框架打造高可预测性的隐式行为表征空间'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有基于Vision Foundation Models (VFM)的世界模型多采用两阶段pipeline，先通过固定降维/独立训练的自编码器压缩VFM特征，再冻住隐空间单独训练预测器，表征学习与时序预测解耦，无法保证隐空间满足动态可预测性要求。

### 方法关键点
Latent-Foresight端到端框架联合训练隐式分词器与流基生成动力学模型，显式约束表征适配时序预测需求；引入多项优化设计避免latent collapse，对齐重构与生成目标保证训练稳定性。

### 关键结果数字
在多类未来场景理解任务、多预测跨度下，性能一致优于两阶段基线，同时省去独立训练阶段，高分辨率适配场景下也保持性能优势
