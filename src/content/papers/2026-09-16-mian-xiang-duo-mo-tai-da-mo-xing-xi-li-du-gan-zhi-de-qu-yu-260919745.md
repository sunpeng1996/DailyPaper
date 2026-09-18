---
title: Region-Level Policy Optimization for Fine-grained MLLM Perception
title_zh: 面向多模态大模型细粒度感知的区域级策略优化
authors:
- Yuheng Shi
- Xiaohuan Pei
- Minjing Dong
- Chang Xu
affiliations:
- University of Sydney
- City University of Hong Kong
arxiv_id: '2609.19745'
url: https://arxiv.org/abs/2609.19745
pdf_url: https://arxiv.org/pdf/2609.19745
published: '2026-09-16'
collected: '2026-09-18'
category: Multimodal
direction: 多模态大模型 · 细粒度视觉感知优化
tags:
- MLLM
- Fine-grained Perception
- Reinforcement Learning
- RoI Localization
- Visual Token Compression
one_liner: 提出无需区域标注的Vision-RL2方法，仅用1/4视觉token即超越MLLM基线最高精度
practical_value: '- 电商多模态搜推的商品图/短视频细粒度理解场景可复用分阶感知策略：先用低分辨率粗定位RoI，再给RoI分配高分辨率token，整体视觉token量降75%还不损失精度，大幅降低编码和KV
  cache开销

  - 轻量多模态模型适配可借鉴冻结大模型做奖励信号的RL优化思路，不需要人工标注区域数据，仅调整轻量proposal网络就能提升感知效果，训练参数量比全量微调低一个数量级

  - 多模态Agent处理高分辨率视觉输入时，可直接复用这套稀疏编码方案，过滤背景无效token，降低推理prefill耗时，提升响应速度'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
MLLM提升细粒度感知通常靠提高输入分辨率，但会大幅增加视觉编码和prefill成本；现有轻量RoI proposal网络存在注意力噪声，且离散区域选择无法用答案忠实度直接监督，缺少标注时训练困难。

### 方法关键点
1. 验证定位任务比识别任务可承受3-4倍更高的token压缩率，因此采用粗视图定位+高分辨率聚焦选中区域的分阶策略；
2. 提出区域级RL方法Vision-RL2，将连贯区域作为动作，用冻结MLLM根据区域移除对答案似然的影响打分，通过加减互补目标抑制干扰、补全缺失证据，无需区域标注、响应采样或推理轨迹，仅更新proposal网络；
3. 基于优化后的候选区域做稀疏编码，放大有效证据、过滤背景token。

### 关键结果数字
覆盖6个细粒度基准、4种MLLM backbone，全token预算区间精度均超过基线；仅用基线1/4的视觉token即可超越基线最高精度；同token限制下性能优于全量微调的SOTA方法，训练参数量低一个数量级。
