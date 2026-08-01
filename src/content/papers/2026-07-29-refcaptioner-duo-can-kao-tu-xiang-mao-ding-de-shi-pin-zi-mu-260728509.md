---
title: 'RefCaptioner: Multi-Reference Image-Grounded Video Captioning'
title_zh: RefCaptioner：多参考图像锚定的视频字幕生成方法
authors:
- Tengfei Liu
- Yang Shi
- Yuran Wang
- Xiaohan Zhang
- Yuqing Wen
- Yuqi Tang
- Qixun Wang
- Zhuoran Zhang
- Xuanyu Zhu
- Weihong Lin
affiliations:
- PKU
- Kling Team
- NUS
- NJU
- HKUST(GZ)
arxiv_id: '2607.28509'
url: https://arxiv.org/abs/2607.28509
pdf_url: https://arxiv.org/pdf/2607.28509
published: '2026-07-29'
collected: '2026-08-01'
category: Multimodal
direction: 多模态生成 · 视频字幕事实锚定
tags:
- Video Captioning
- Multimodal Generation
- SFT
- GRPO
- Benchmark
one_liner: 提出多参考图像锚定的视频字幕新任务、两阶段训练框架RefCaptioner及配套评测基准
practical_value: '- 多源参考锚定的训练范式可迁移到电商商品短视频生成场景，解决生成内容与商品原图不一致的幻觉问题

  - 混合数据SFT+分层覆盖折扣GRPO的两阶段后训练组合，可复用在多模态生成任务中，兼顾通用能力与特定任务对齐效果

  - 短语级事实绑定的评测思路可用于生成式电商内容（商品文案、短视频脚本）的自动化事实校验'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有视频字幕模型仅能生成通用内容描述，无法将局部视觉元素与多参考图像显式锚定，存在事实偏差，难以满足内容溯源、保真要求高的落地场景。
### 方法关键点
1. 定义多参考图像锚定的视频字幕生成新任务，要求输出带短语级参考对齐的事实性描述
2. 提出两阶段后训练框架RefCaptioner，结合混合数据SFT与分层覆盖折扣GRPO，同步优化参考选择、短语绑定、干扰项过滤、跨参考一致性，保留通用字幕能力
3. 构建含20000条视频、171354张参考图的训练语料，推出MRVBench评测基准
### 关键结果
开源模型中整体性能最优，标准视频字幕基准表现具备竞争力，人工评估字幕偏好度更高，支撑生成的视频源忠实度显著提升
