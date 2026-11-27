---
title: 'RAPID: Codec-Aware Video Decoding for Efficient Long-Video Understanding'
title_zh: RAPID：面向高效长视频理解的编码感知视频解码方法
authors:
- Yuna Lee
- Yulhwa Kim
affiliations:
- Sungkyunkwan University
arxiv_id: '2611.30557'
url: https://arxiv.org/abs/2611.30557
pdf_url: https://arxiv.org/pdf/2611.30557
published: '2026-11-23'
collected: '2026-11-27'
category: Multimodal
direction: 多模态大模型 · 长视频理解效率优化
tags:
- VLM
- Long Video Understanding
- Inference Optimization
- Video Codec
- TTFT
one_liner: 提出编码感知的长视频解码框架RAPID，大幅降低解码与帧选择开销，提升VLM推理效率
practical_value: '- 短视频/直播电商内容理解场景可复用RAPID编码感知解码思路，直接利用H.264等压缩码流的参考帧、关键帧信息跳过冗余帧解码，大幅降低视频预处理时延

  - 长视频（如商家直播回放、用户晒单长视频）帧选择环节可复用RAPID-Sel的关键帧代表方案，无需逐帧解码打分，预处理速度提升3倍且不损失精度

  - 多模态Agent推理优化时可参考该框架的优化优先级，优先优化占比更高的预处理（如视频解码）环节，而非仅聚焦LLM推理本身'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有长视频VLM推理中，视频解码耗时甚至超过LLM prefill，现有效率优化方案普遍忽略解码环节，帧选择需逐帧解码打分进一步拉高预处理时延。
### 方法关键点
RAPID为编码感知解码框架，包含两个核心模块：
1. RAPID-Dec：利用压缩码流的参考帧、随机接入点信息跳过不必要帧，并行解码保留帧，完全保留目标帧重建精度
2. RAPID-Sel：用关键帧作为视频段粗粒度代表，避免现有帧选择方法的稠密候选解码打分开销
### 关键结果
- H.264/AVC视频解码速度较最快基线最高提升3.7x
- 预处理速度最高提升3.0x且精度与基准方案相当
- 小时级长视频场景下，TTFT较SOTA帧选择方法提升4.9x
