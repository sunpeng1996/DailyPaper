---
title: 'Agile-WAM: An Agile Tactile World Action Model for Contact-Rich Robot Control'
title_zh: Agile-WAM：面向多接触机器人控制的轻量化触觉世界动作模型
authors:
- Hanchu Zhou
- Brendan Lynch
- Raman Goyal
- Dechen Gao
- Begum Kasap
- Boqi Zhao
- Junshan Zhang
affiliations:
- University of California, Davis
- Analog Devices
arxiv_id: '2609.20761'
url: https://arxiv.org/abs/2609.20761
pdf_url: https://arxiv.org/pdf/2609.20761
published: '2026-09-17'
collected: '2026-09-20'
category: Other
direction: 多模态世界模型 · 机器人控制
tags:
- World Action Model
- Multimodal Fusion
- Flow Matching
- Latent Representation
- Efficient Inference
one_liner: 基于多模态不同时间尺度设计轻量化WAM，兼顾机器人控制成功率与极低推理延迟
practical_value: '- 多模态融合任务可复用「差异化时间尺度预测」思路：对变化慢的特征（如用户画像、商品静态属性）用长预测窗口，变化快的特征（如实时点击、交互信号）用短预测窗口，平衡效果与效率；

  - 端到端生成任务可参考flow matching替代扩散类backbone，能大幅降低推理延迟，适配推荐/广告高吞吐低延迟的线上要求；

  - 多模态输入共享隐层的架构设计可复用在跨域特征（如文本/图像/行为）的统一表征学习，减少冗余计算'
score: 3
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有触觉WAM依赖大参数量预训练生成backbone，推理效率低、部署灵活性差，无法适配高频率机器人控制需求。
### 方法关键点
1. 将视觉、触觉观测编码为共享隐层，基于flow matching实现端到端视触觉到动作的映射，可同时生成动作块隐层与未来视触觉隐层表征；
2. 针对视觉、触觉信号演化的时间尺度差异，引入多时间尺度多模态预测机制：视觉隐层预测大时间偏移结果，触觉隐层仅预测下一帧结果，兼顾全局趋势与细粒度接触动态捕捉。
### 关键结果数字
9个仿真、5个真实世界多接触操作任务上成功率优于最优基线；真实任务整体成功率相对提升29.4%，推理latency仅11.9ms
