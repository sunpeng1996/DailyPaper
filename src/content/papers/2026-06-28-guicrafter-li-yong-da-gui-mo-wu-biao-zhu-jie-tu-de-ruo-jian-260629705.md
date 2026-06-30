---
title: 'GUICrafter: Weakly-Supervised GUI Agent Leveraging Massive Unannotated Screenshots'
title_zh: GUICrafter：利用大规模无标注截图的弱监督GUI智能体
authors:
- Sunqi Fan
- Lingshan Chen
- Runqi Yin
- Qingle Liu
- Yongming Rao
- Meng-Hao Guo
- Shi-Min Hu
affiliations:
- Tsinghua University
- Tencent Hunyuan
arxiv_id: '2606.29705'
url: https://arxiv.org/abs/2606.29705
pdf_url: https://arxiv.org/pdf/2606.29705
published: '2026-06-28'
collected: '2026-06-30'
category: Agent
direction: GUI Agent · 弱监督训练
tags:
- GUI Agent
- Weakly Supervised Learning
- Curriculum Learning
- Reinforcement Learning
- Visual Grounding
one_liner: 提出两阶段弱监督训练方案，仅用0.1%标注数据即可达到SOTA级GUI Agent性能
practical_value: '- 对于标注成本高的Agent任务，可复用「大规模无标注预训练+小样本RL校准」的两阶段方案，大幅降低数据成本

  - 交互类Agent可直接挖掘无标注界面自带的上下文交互信号做自监督学习，无需额外人工标注

  - 面向多端电商/网页的交互Agent，该方案可提升跨设备泛化能力，适配不同屏幕的UI元素定位'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
GUI Agent领域难以从互联网批量获取标注数据，大规模人工标注成本极高，现有模型普遍存在跨设备泛化能力差、细粒度GUI元素视觉定位能力不足的问题。
### 方法关键点
提出弱监督训练框架GUICrafter，采用两阶段课程学习方案：第一阶段从大规模无标注截图、网页中挖掘GUI交互自带的上下文信号，学习视觉定位能力，全程无需人工标注；第二阶段用少量高质量标注数据，通过强化学习完成模型校准。
### 关键结果
仅使用SOTA模型UI-TARS的0.1%标注数据，就取得了媲美甚至超越UI-TARS的性能；在同等标注数据量下，性能超过GUI-R1等所有现有方法
