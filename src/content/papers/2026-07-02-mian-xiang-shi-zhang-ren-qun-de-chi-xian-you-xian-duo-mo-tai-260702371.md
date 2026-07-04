---
title: 'VisionAId: An Offline-First Multimodal Android Assistant for People with Visual
  Impairment, Featuring Personalized Object Retrieval'
title_zh: 面向视障人群的离线优先多模态安卓助手VisionAId 支持个性化物品检索
authors:
- Cristian-Gabriel Florea
- Stelian Spînu
affiliations:
- The Military Technical Academy “Ferdinand I”, Bucharest, Romania
arxiv_id: '2607.02371'
url: https://arxiv.org/abs/2607.02371
pdf_url: https://arxiv.org/pdf/2607.02371
published: '2026-07-02'
collected: '2026-07-04'
category: Agent
direction: 端侧多模态Agent 个性化物品检索
tags:
- Multimodal Agent
- On-device Inference
- Few-shot Retrieval
- INT8 Quantization
- ONNX Runtime
one_liner: 打造端侧优先的视障多模态智能助手，支持少样本个性化物品检索与多模态反馈
practical_value: '- 端侧Agent架构可复用：低延迟高隐私要求的推理（如物品识别、深度估计）优先跑端侧ONNX Runtime，仅非实时需求（如内容生成、标注）调用云端LLM，平衡性能、成本、隐私

  - 少样本个性化检索方案可迁移：电商用户自定义收藏物品的视觉检索、找同款需求，可复用多角度拍摄建embedding库+实时召回的pipeline

  - 端侧模型压缩落地经验：INT8量化可将CV模型延迟压缩至原来的40%左右，移动终端的推荐/检索场景可优先尝试INT8量化兼顾精度和速度'
score: 5
source: arxiv-cs.AI
depth: abstract
---

### 动机
全球超2.85亿视障人群面临避障、寻找私人物品、识别人脸/现金等日常障碍，现有辅助工具仅支持预定义类别识别、严重依赖云端连接，或需要专用硬件，通用性差。

### 方法关键点
1. 端侧优先架构：6个CV模型（单目深度估计、实例分割、视觉/人脸embedding、人脸检测、自定义钞票检测）全在端侧通过ONNX Runtime运行，仅场景描述、自动物品标注可选调用云端Google Gemini Flash；
2. 少样本个性化物品检索pipeline：用户多角度拍摄物品建库，系统可实时定位特定实例，通过AR标记、空间音频、随距离变化的触觉反馈引导用户；
3. 全链路多模态交互，支持语音合成、语音指令、振动反馈。

### 关键结果
三星S21 Ultra上INT8量化将深度估计延迟从~1200ms降至~491ms；自定义钞票检测器mAP@50达0.986；3米内深度估计误差低于1cm。
