---
title: Muon Makes the First Mixture-of-Experts Layer Harder to Balance
title_zh: Muon优化器会提升MoE模型首层的负载均衡难度
authors:
- Marcos Hernanz
affiliations:
- Universidad Autónoma de Madrid
arxiv_id: '2610.37914'
url: https://arxiv.org/abs/2610.37914
pdf_url: https://arxiv.org/pdf/2610.37914
published: '2026-10-26'
collected: '2026-11-04'
category: Training
direction: MoE大模型训练 · 优化器与负载均衡
tags:
- MoE
- Muon
- Load Balancing
- Optimizer
- LLM Training
one_liner: 量化Muon对MoE首层负载均衡的负面影响，给出3种可落地缓解方案
practical_value: '- 训练用Muon优化的MoE模型时，需单独监控首层MoE的偏置跨度、专家过载倍数，不要仅依赖全局负载均衡指标

  - 遇到首层负载失衡可直接复用3种验证有效的方案：将Muon学习率降至调优值的1/2、路由输入减去批次/滑动均值、调大负载均衡偏置的更新步长到4倍

  - 主干用Muon时路由层也保持用Muon即可，切换为AdamW会增大warmup阶段的负载波动，还会导致loss微涨

  - 自研MoE训练框架时可优先做首层MoE的专项均衡优化，收益远高于全局通用调整'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前主流开源MoE大模型普遍采用Muon替代AdamW作为主干优化器，但不同官方训练配方对路由层是否使用Muon的选择分歧极大，也无公开量化对比数据；现有研究未关注优化器对无辅助损失的偏置式负载均衡的实际影响，而首层MoE的负载失衡易导致训练不稳定、多机通信拖速、显存溢出等问题，具备明确的工程研究价值。
### 方法关键点
- 采用55M/108M激活参的两个Decoder-only MoE模型，在FineWeb-Edu数据集上完成对照实验；
- 提出用同层路由偏置的跨度（最大值减最小值）作为负载均衡难度的量化指标，规避负载本身受偏置调节的干扰；
- 做拆分消融实验，分别控制路由层、主干不同模块的优化器选择，定位Muon影响负载均衡的来源；
- 测试路由输入中心化、降低Muon学习率、调大偏置更新步长三种缓解方案的效果。
### 关键结果
对比AdamW基线，调优学习率下Muon使首层MoE的偏置跨度平均翻倍，warmup后最忙专家负载是公平份额的4~7倍；路由输入减去批次均值可完全消除早期过载，loss波动小于0.003；Muon学习率减半可消除3/4的跨度上涨，还能让loss微降0.008~0.012；路由层切换为AdamW会使warmup阶段负载波动显著增大，loss微涨0.001~0.004。
### 核心结论
用Muon训练MoE时，首层MoE是负载失衡的重灾区，优先针对该层做专项均衡优化的收益远高于全局通用调整。
