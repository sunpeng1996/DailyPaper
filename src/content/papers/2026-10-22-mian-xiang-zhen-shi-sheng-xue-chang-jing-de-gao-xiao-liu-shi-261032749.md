---
title: Efficient Streaming Audio-Visual Target Speaker Extraction for Real-World Acoustic
  Scenes
title_zh: 面向真实声学场景的高效流式音视频目标说话人提取
authors:
- Wendi Sang
- Kai Li
- Yifan Li
- Jianqiang Huang
- Xiaolin Hu
affiliations:
- Qinghai University
- Tsinghua University
- Intelligent Computing and Application Laboratory of Qinghai Province
- Chinese Institute for Brain Research (CIBR)
arxiv_id: '2610.32749'
url: https://arxiv.org/abs/2610.32749
pdf_url: https://arxiv.org/pdf/2610.32749
published: '2026-10-22'
collected: '2026-10-29'
category: Other
direction: 音视频语音处理 · 流式低延迟推理
tags:
- AVTSE
- Streaming Inference
- Low-Latency
- Speech Extraction
- Benchmark
one_liner: 发布真实场景AVTSE基准RealSSA，提出轻量因果模型Falcon实现SOTA且大幅降低参数量与推理延迟
practical_value: '- 开发语音交互类Agent（如直播智能助理、语音导购、语音搜索入口）时，可复用Falcon轻量流式提取方案，降低边缘端语音降噪、目标人声提取的延迟与算力开销

  - 训练多模态模型时，可借鉴编码器空间对比损失的设计思路，在训练阶段注入约束，实现零推理成本的无关信号抑制，不额外增加线上开销

  - 构建业务场景专属评估基准时，可参考RealSSA的构建逻辑，同时产出可控模拟调参集与真实场景验证集，兼顾算法迭代效率与落地效果可信度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
流式音视频目标说话人提取（AVTSE）是低延迟交互场景的核心技术，现有方案存在两大痛点：一是通用基准仅固定2说话人设置，未覆盖真实场景的远近场干扰、混响、突发噪声；二是高性能因果架构参数量过大不适合边缘部署，轻量方案需重复调用分离器反而抵消了算力收益。
### 方法关键点
1. 发布RealSSA真实场景AVTSE基准，包含可控模拟集RealSSA-Sim（支持1-5个近场、10-15个远场干扰的动态场景）与真实录制测试集RealSSA-Real；
2. 提出Falcon轻量因果AVTSE模型，分离器单次编解码 pass 即可完成多尺度时频分离，搭配编码器空间说话人对比损失，零推理成本抑制近场信号泄露，该损失可跨骨干迁移。
### 关键结果
在RealSSA-Sim、LRS2-2Mix等4个数据集上取得SOTA提取效果；相比AV-TFGridNet基线，参数量降低91.9%，计算量减少20.2倍，GPU推理 latency 降低11.1倍
