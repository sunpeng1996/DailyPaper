---
title: 'UMM-JEPA: Generative Pretraining via Masked Next-Scale Representation Prediction
  for Unified Multimodal Models'
title_zh: UMM-JEPA：基于掩码下尺度表征预测的统一多模态生成预训练
authors:
- Yucheng Zhou
- Yunjia Xi
- Di Yin
- Jianbing Shen
affiliations:
- University of Macau
- Tencent Youtu Lab
arxiv_id: '2611.18668'
url: https://arxiv.org/abs/2611.18668
pdf_url: https://arxiv.org/pdf/2611.18668
published: '2026-10-25'
collected: '2026-11-17'
category: Multimodal
direction: 多模态大模型预训练 · 表征对齐优化
tags:
- Multimodal LLM
- Pretraining
- Representation Learning
- JEPA
- Vision-Language
one_liner: 提出UMM-JEPA预训练框架，生成任务直接监督感知表征，同步提升多模态理解与生成性能
practical_value: '- 多模态商品表征预训练场景可复用核心思路：放弃离散视觉code预训练目标，直接用连续理解型表征作为生成任务的监督信号，降低跨模态表征对齐成本

  - 商品文案/海报等多模态生成场景可采用「多尺度表征预训练+渲染层解耦」架构，预训练阶段无需优化像素生成任务，大幅降低预训练算力消耗

  - 跨模态商品召回/匹配场景可直接采用该预训练范式得到的多模态表征，其更丰富的物体、空间结构信息可显著提升图文匹配准确率'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有统一多模态模型的生成训练目标仅优化合成导向空间（如离散视觉code、生成隐空间），与理解任务依赖的感知表征存在匹配gap，导致生成训练无法反哺理解能力。
### 方法关键点
1. 重定义生成任务为连续视觉理解表征的渐进式预测，构建从粗到细的多尺度表征层级；
2. 像素渲染模块与表征预训练完全解耦，预训练阶段不参与，仅在下游生成任务部署前挂载；
3. 采用掩码下尺度表征预测作为预训练目标，直接监督理解任务消费的感知表征。
### 关键结果
1. 16项视觉基准平均得分达51.71，较纯理解的Qwen-VL基线提升5.35分，文本指标同步上涨；
2. 相比离散code、隐流生成目标，感知表征预测对理解任务的迁移效果更强更稳定；
3. 预训练得到的表征包含更丰富的物体、空间结构信息，对图像独有信息的利用率更高
