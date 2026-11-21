---
title: 'PSM-WSM: Predictively Sufficient Multimodal World Social Modeling'
title_zh: PSM-WM：基于预测充分性的多模态社交世界建模框架
authors:
- Chunlei Meng
- Zhenyu Yu
- Pengbin Feng
- Jacqueline J. Pang
- Jiabin Luo
- Chih-Ting Liao
- Zhaolu Kang
- Chun Ouyang
- Zhongxue Gan
affiliations:
- Fudan University
- University of Southern California
- Cornell University
- Peking University
- University of New South Wales
arxiv_id: '2611.25835'
url: https://arxiv.org/abs/2611.25835
pdf_url: https://arxiv.org/pdf/2611.25835
published: '2026-11-19'
collected: '2026-11-21'
category: Multimodal
direction: 多模态世界建模 · 预测性隐状态学习
tags:
- Multimodal World Model
- Predictive State
- Latent Representation
- Temporal Modeling
- State Evaluation
one_liner: 基于预测充分性原则构建多模态预测隐状态，提升时序建模效果与鲁棒性
practical_value: '- 多模态用户行为建模可复用预测充分性原则，过滤历史行为冗余信息，仅保留对未来点击/转化预测有用的特征，降低特征冗余提升推理效率

  - Agent交互时序建模可直接复用事件条件转移+多步一致性优化的训练范式，提升长时序预测的鲁棒性，减少长对话/长路径决策的偏差

  - 隐状态质量评估可复用预测闭合度、历史剩余增益、未来语义对齐三个指标，替代单纯的预测精度指标，更全面衡量序列建模的泛化能力'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
多模态交互系统现有隐状态学习仅优化当前语义理解或直接预测效果，未明确定义隐状态需保留的未来相关信息，相同当前语义可能对应完全不同的未来演化趋势，无法支撑长时序推理需求。

### 方法关键点
基于预测充分性原则的PSM-WM框架，通过概率状态推断、事件条件转移、多步一致性优化三个核心模块，联合学习预测性隐状态及其随机时序演化规律；同时提出三个以状态为核心的评估指标：预测闭合度、历史剩余增益、未来语义对齐，衡量隐状态的预测属性。

### 关键结果
在Hi-EF、IEMOCAP、MELD、Ego4D四个公开数据集上，未来多模态交互建模效果显著优于基线，隐状态预测属性与鲁棒性均有提升，验证了预测充分性原则对未来导向多模态状态构建的有效性。
