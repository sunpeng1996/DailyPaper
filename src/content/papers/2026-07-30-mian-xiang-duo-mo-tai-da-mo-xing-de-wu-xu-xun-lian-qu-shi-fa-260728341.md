---
title: Capturing Token Tendencies for Training-Free Token Pruning in Multimodal Large
  Language Models
title_zh: 面向多模态大模型的无需训练趋势感知Token剪枝方法
authors:
- Jie Ma
- Zhike Qiu
- Jie Gao
- Jiayi Ji
- Qian Chen
- Xiaoshuai Sun
- Rongrong Ji
affiliations:
- 厦门大学
- 厦门海洋职业技术学院
arxiv_id: '2607.28341'
url: https://arxiv.org/abs/2607.28341
pdf_url: https://arxiv.org/pdf/2607.28341
published: '2026-07-30'
collected: '2026-07-31'
category: Multimodal
direction: 多模态大模型 · 无训练Token剪枝推理优化
tags:
- MLLM
- Token Pruning
- Training-Free
- Inference Acceleration
- Dynamic Pruning
one_liner: 无需训练的趋势感知Token剪枝框架，建模跨层重要性动态，大幅降低MLLM推理成本且性能损失极小
practical_value: '- 电商多模态商品理解/导购Agent场景可直接复用该无训练剪枝框架，处理高分辨率商品图时裁剪70%+视觉token，推理速度提升近2倍，仅损失不到4%性能，无需重新训练MLLM

  - 端侧/边缘端多模态推荐/导购系统部署可参考动态token恢复机制，避免静态剪枝误删商品细粒度特征（如logo、防伪标识、尺码标注等）导致的理解错误

  - 可将趋势感知的动态重要性建模思路迁移到LLM长文本推理场景，对长用户行为序列/长搜索query的token做动态剪枝，降低生成式推荐的推理成本'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有无训练MLLM视觉Token剪枝依赖单层静态注意力得分做不可逆过滤，忽略了Token重要性随模型层级动态演化的特性，导致深层推理所需的关键视觉信息（如细粒度商品特征、OCR文本）常被浅层误删，高剪枝率下性能骤降，成为高分辨率多模态任务推理的核心瓶颈。
### 方法关键点
- 搭建Layer-wise Token Collector，维护最近W层的注意力得分滑动窗口，将剪枝从单时刻决策转化为Token重要性演化轨迹建模问题
- 设计Adaptive Flow Identification，将Token按注意力变化趋势分为上升、波动、下降三类，基于分布统计的自适应阈值筛选潜在高价值Token
- 提出Flow Activation机制，将静态Top-k保留的Token与趋势筛选出的高潜力Token合并作为下一层输入，实现剪枝可逆，避免关键信息丢失
### 关键实验
在LLaVA全系列、Qwen2.5-VL等主流MLLM上验证，对比FastV、PDrop、SparseVLM等SOTA无训练剪枝方法：50%剪枝率下保留98.89%的基准性能，FLOPs降至55.10%；77.8%超高剪枝率下仅保留约23个视觉Token，仍维持96.03%的性能，OCR等细粒度任务得分比静态Top-k剪枝高12.3分。
### 核心结论
Token重要性不是静态常量，而是随模型层级动态演化的过程，剪枝决策既要参考当前注意力得分，也要评估其未来价值趋势
