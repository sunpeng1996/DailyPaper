---
title: 'Align-RAG: Alignment Is All You Need for TSFM In-Context Learning'
title_zh: Align-RAG：面向时序基础模型上下文学习的免训练对齐方法
authors:
- Mohammad Asadi
- Soheil Hor
- Bardiya Akhbari
- Jack W. O'Sullivan
- Tahoura Nedaee
- Layne C. Price
- Raviteja Anantha
- Euan Ashley
- Ehsan Adeli
affiliations:
- Stanford University
- Amazon
arxiv_id: '2608.05571'
url: https://arxiv.org/abs/2608.05571
pdf_url: https://arxiv.org/pdf/2608.05571
published: '2026-08-06'
collected: '2026-08-07'
category: RAG
direction: 检索增强生成 · 免训练对齐优化
tags:
- RAG
- Time Series
- Foundation Model
- In-Context Learning
- Zero-Shot
one_liner: 提出免训练检索样本对齐方法Align-RAG，无需适配模块即可提升冻住时序大模型检索增强预测效果
practical_value: '- 电商销量、流量、库存等时序预测场景，可直接复用Align-RAG的幅度重缩放+相位偏移对齐逻辑，无需额外训练适配器即可提升冻住时序大模型的预测效果，节省训练与部署成本

  - 搭建RAG系统时，不要默认叠加训练式融合模块，可先验证无参数的Query与检索样本分布/特征对齐方案的收益，显著降低系统复杂度

  - 大模型零样本适配业务场景时，可优先尝试闭域对齐trick替代LoRA等轻量微调方案，尤其适合小流量冷启动场景下的快速落地'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有检索增强时序预测方案默认冻住的时序基础模型（TSFM）无法动态融合检索上下文，需要额外训练融合适配器，部署成本高、适配周期长。
### 方法关键点
无训练参数的Align-RAG对检索到的过去-未来窗口对，先做逐对闭式幅度重缩放、整数延迟相位偏移，再送入冻住TSFM的上下文窗口即可，无需任何模型微调或适配模块训练。
### 关键结果
在7个标准基准数据集上，冻住Chronos-Bolt上的表现优于SOTA训练式检索适配器，平均MSE降低3.75%；额外在4种不同架构的冻住TSFM上，零样本MSE提升2.5%~13.7%，无需针对单模型做任何调优。
