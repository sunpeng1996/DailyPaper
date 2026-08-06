---
title: 'Better, Stronger, Faster, and Broader: Structured All-Mask Prediction for
  MLLM-Based Segmentation'
title_zh: 更优更强更快更广：面向MLLM分割的结构化全掩码预测
authors:
- Jiazhen Liu
- Mingkuan Feng
- Long Chen
arxiv_id: '2608.02791'
url: https://arxiv.org/abs/2608.02791
pdf_url: https://arxiv.org/pdf/2608.02791
published: '2026-08-02'
collected: '2026-08-06'
category: Multimodal
direction: 多模态大模型 · 图像分割优化
tags:
- MLLM
- Image Segmentation
- Non-autoregressive Inference
- Multimodal Grounding
- Open-vocabulary Recognition
one_liner: 提出结构化全掩码预测STAMPlus，解决MLLM分割的性能、对话能力、推理速度三重困境
practical_value: '- 多模态Agent做电商商品图拆分、场景识别等视觉理解任务时，可借鉴自回归对话+非自回归任务预测的解耦架构，兼顾交互能力和任务执行速度

  - 多目标视觉识别场景可复用「显式ID绑定多类别空间+单次并行预测」的设计，避免重复推理降低延迟

  - 高分辨率商品图细粒度识别场景，可参考高分辨率mask token缩放方法保留空间细节，提升识别精度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
MLLM-based 分割存在三重困境：高分割性能、保留对话能力、快速推理三者难以兼顾；传统嵌入预测方法会破坏语言建模能力，next-token 生成稠密掩码的推理效率极低；单目标二值掩码预测需要多次重复推理才能输出多类别结果，效率差。

### 方法关键点
1. 提出全掩码预测范式，解耦自回归对话流程和非自回归掩码预测任务，二值版本STAMP通过<SEG>触发符触发掩码预测，融合图像对齐的mask token与patch特征，混合注意力单步完成前后景分类；
2. 升级为结构化全掩码预测STAMPlus，先生成带显式ID和可选框的目标列表，将ID绑定共享多类别掩码空间，单步非自回归并行预测所有目标，支持高分辨率mask token缩放保留细节。

### 关键结果
STAMPlus在开放词汇语义、实例感知、遥感小目标分割等任务达到SOTA，保留通用多模态指令跟随能力，12类别推理latency从STAMP的13.50s降至5.16s。
