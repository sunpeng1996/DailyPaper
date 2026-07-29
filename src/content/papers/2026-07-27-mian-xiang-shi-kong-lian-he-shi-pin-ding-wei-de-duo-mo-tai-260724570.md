---
title: 'The Visual Bottleneck: Sparse-Frame Adaptation of MLLMs for Joint Spatial-Temporal
  Video Grounding'
title_zh: 面向时空联合视频定位的多模态大模型稀疏帧适配方法
authors:
- Jiameng Zhang
- Srikanth Madikeri
affiliations:
- University of Zurich
arxiv_id: '2607.24570'
url: https://arxiv.org/abs/2607.24570
pdf_url: https://arxiv.org/pdf/2607.24570
published: '2026-07-27'
collected: '2026-07-29'
category: Multimodal
direction: 多模态大模型 · 稀疏帧视频处理
tags:
- MLLM
- Video Grounding
- Sparse Frame
- ViT Fine-tuning
- Multimodal Processing
one_liner: 通过微调ViT末三层与边界感知采样策略，解决MLLM稀疏帧输入时空视频定位性能暴跌问题
practical_value: '- 电商短视频审核、商品卖点片段定位场景可直接复用仅微调ViT末3层的方案，仅4%参数量即可大幅提升稀疏帧输入下的性能，兼顾成本与效果

  - 高吞吐量短视频处理场景可采用Hybrid16边界感知采样替代均匀采样，在有事件边界先验时可提升26点temporal mIoU，大幅降低推理成本

  - 稀疏输入的多模态任务无需盲目堆叠大模型，微调后的小模型性能远超零-shot大模型，可显著降低部署算力开销'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
工业级视频平台需支撑海量上传内容的时空定位（如违规内容审核），受限于吞吐量仅能输入8-16帧稀疏采样，而SOTA MLLM预训练使用数百帧稠密序列，训练部署 mismatch 导致性能暴跌：Qwen3-VL 8B输入16帧时temporal mIoU从56.0%跌至22.3%，相对下降60.2%。
### 方法关键点
1. 定位稀疏帧输入下核心瓶颈为视觉特征提取模块，仅微调ViT末三层（占总参数量4%），语言模型微调无收益甚至负向；
2. 提出边界感知采样策略Hybrid16，适配有事件边界先验的场景。
### 关键结果
- 仅微调ViT末三层的方案temporal mIoU达68.8%，比稠密输入的零-shot 8B模型高12.8个点；
- Hybrid16相比均匀采样提升26点temporal mIoU；
- 微调后的2B模型性能始终优于零-shot 8B模型，无论是否使用稠密帧输入。
