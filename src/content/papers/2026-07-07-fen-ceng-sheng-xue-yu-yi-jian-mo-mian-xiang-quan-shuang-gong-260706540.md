---
title: 'Hierarchical Acoustic-Semantic Modeling: Modality Separation and Semantic
  Coherence for Full-Duplex SLMs'
title_zh: 分层声学-语义建模：面向全双工SLM的模态分离与语义一致性
authors:
- Zhenyu Liu
- Yunxin Li
- Xuanyu Zhang
- Qixun Teng
- Shenyuan Jiang
- Haolan Chen
- Minjun Zhao
- Fanbo Meng
- Yu Xu
- Yancheng He
affiliations:
- 哈尔滨工业大学（深圳）计算机科学与技术学院
- 深圳环路区域研究院语言与智能机器中心
- 香港中文大学（深圳）人工智能学院
arxiv_id: '2607.06540'
url: https://arxiv.org/abs/2607.06540
pdf_url: https://arxiv.org/pdf/2607.06540
published: '2026-07-07'
collected: '2026-07-08'
category: Multimodal
direction: 多模态大模型 · 全双工口语交互
tags:
- SLM
- Multimodal Alignment
- Full-Duplex Interaction
- Gradient Conflict
- Parameter Decoupling
one_liner: 提出分层参数分离策略解决全双工SLM模态干扰，大幅提升问答精度与交互流畅度
practical_value: '- 语音交互类电商导购/客服Agent可直接集成Lychee-FD框架，快速提升全双工交互流畅度与语音问答准确率

  - 多模态Agent训练时可复用分层参数分离方案，解决不同模态共享参数导致的梯度冲突、性能退化问题

  - 跨模态对齐场景可新增专用语义对齐通道，在模态参数解耦的同时保证语义一致性，不牺牲推理效率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有原生全双工SLM存在严重模态干扰问题，导致知识退化、语义完整性受损，交互体验生硬不自然，此前未明确其根本原因。
### 方法关键点
1. 通过细粒度模型优化动态分析，定位模态干扰根源为声学、语义建模共享深层参数空间时的固有梯度冲突；
2. 提出Lychee-FD端到端全双工框架，采用分层参数分离策略，在深层网络解耦冲突模态，同时通过专用语义对齐通道保留跨模态一致性。
### 关键结果数字
在多个全双工基准测试中达到SOTA，口语问答任务准确率提升7.4%，全双工交互流畅度提升28.5%，无推理效率损失。
