---
title: 'LoopDVR: Looped Transformer for Efficient Dense Visual Recognition'
title_zh: LoopDVR：面向高效密集视觉识别的循环Transformer框架
authors:
- Sirui Liang
- Xuanlong Yu
- Longfei Liu
- Xiaodong Cun
- Xi Shen
affiliations:
- GVC Lab, Great Bay University
- Intellindust AI Lab
arxiv_id: '2611.32067'
url: https://arxiv.org/abs/2611.32067
pdf_url: https://arxiv.org/pdf/2611.32067
published: '2026-11-23'
collected: '2026-11-25'
category: Other
direction: 高效视觉Transformer · 参数压缩
tags:
- Transformer
- Model Compression
- Visual Recognition
- Parameter Efficiency
- Adapter
one_liner: 通过分层复用Transformer块与独立适配层设计，实现密集视觉识别模型28%参数量压缩且精度持平
practical_value: '- 大模型参数压缩可参考分层分组复用Transformer块的思路，按层表示相似性划分共享组，避免直接共享参数的效果损失

  - 复用参数时可搭配每层独立的轻量Adapter，保留不同深度的特征变换特性，平衡压缩率与推理效果

  - 微调复用模块时可优先加载组内最后一层的预训练权重，配合知识蒸馏进一步减少精度损失'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
Transformer-based密集视觉识别模型参量过高，直接裁剪宽度/深度易破坏原有计算结构、损失精度，亟需兼顾压缩率与效果的优化方案。
### 方法关键点
1. 按层间表示差异度划分ViT backbone与Decoder的Transformer块共享组，仅保留backbone最后1层独立用于多尺度特征构建
2. 共享块采用所属组终端层预训练权重初始化，每层新增独立Loop Adapter保留深度专属特征变换能力
3. 结合知识蒸馏训练循环主干与循环解码器，适配下游任务
### 关键结果
相比基准模型参数量降低约28%且精度持平；LoopDet-S仅用7.0M参数达到50.9 box AP，在目标检测、实例分割、人体姿态估计三类任务上均实现最优精度-参数tradeoff。
