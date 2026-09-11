---
title: 'Spot-the-shift: Evaluating Grounded Image Difference Captioning of Long-term
  Changes'
title_zh: Spot-the-shift：面向长期场景变化的可定位图像差异描述评测基准
authors:
- Benedetta Liberatori
- Nermin Samet
- Paolo Rota
- Matthieu Cord
- Elisa Ricci
- Andrei Bursuc
- Monika Wysoczańska
affiliations:
- University of Trento
- valeo.ai
- Fondazione Bruno Kessler
- Sorbonne Université
arxiv_id: '2609.10356'
url: https://arxiv.org/abs/2609.10356
pdf_url: https://arxiv.org/pdf/2609.10356
published: '2026-09-09'
collected: '2026-09-11'
category: Multimodal
direction: 多模态大模型 · 视觉变化理解评测
tags:
- MLLM
- Change Detection
- Benchmark
- Synthetic Data
- Visual Grounding
one_liner: 发布真实驾驶场景长期图像变化评测基准，配套人工验证的评估协议与合成数据增强pipeline
practical_value: '- 电商商品巡检、广告素材合规比对等多模态差异识别场景，可复用「结构化变化描述+空间掩码」的标注范式，提升垂类MLLM的识别准确率

  - 垂类多模态任务性能不足时，可借鉴其合成数据生成pipeline，在不损失模型通用能力的前提下实现定向性能提升

  - 多模态Agent的环境感知、动态变化识别能力评测，可参考其人工校准的评估协议，降低纯自动评测的结果偏差'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有图像变化理解方法仅覆盖像素级预测或纯文本差异描述两类任务，缺少同时支持定位、自然语言描述的长期真实场景变化评测方案，无法准确度量MLLM的跨时序多图像对比识别能力。
### 方法关键点
1. 构建人工验证的SPOT-THE-SHIFT基准，覆盖全球多城市驾驶场景下跨度数年的图像对，每个结构变化对应标注自然语言描述+分割掩码
2. 设计经人类实验验证的评估协议，可客观衡量模型的差异描述准确度与定位一致性
3. 提出轻量化合成数据生成pipeline，可定向增强MLLM的变化识别能力
### 关键结果
对SOTA MLLM的基准测试显示，当前模型普遍无法满足任务要求的细粒度多图像空间对比能力；使用提出的合成数据pipeline微调后，现成MLLM的任务性能显著提升且无通用能力衰减
