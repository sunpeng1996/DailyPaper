---
title: 'SyncRA: Learning Temporal Correspondence in Omni-Modal Models'
title_zh: SyncRA：全模态模型的时序对应关系学习方法
authors:
- Zelong Xu
- Yan Li
- Wenhe Hu
- Xiyang Hu
affiliations:
- University of Wisconsin–Madison
- University of Alberta
- Arizona State University
arxiv_id: '2609.34363'
url: https://arxiv.org/abs/2609.34363
pdf_url: https://arxiv.org/pdf/2609.34363
published: '2026-09-28'
collected: '2026-10-04'
category: Multimodal
direction: 全模态模型 · 视听时序对齐
tags:
- Multimodal
- Representation Alignment
- Temporal Modeling
- Contrastive Learning
- Video Understanding
one_liner: 提出无额外标注的轻量同步引导表示对齐方案，提升全模态模型视听时序匹配能力
practical_value: '- 短视频带货多模态内容理解场景，可复用SyncRA无额外标注的时序对齐trick，提升音视频内容匹配准确性，减少虚假宣传相关的召回错误

  - 多模态RAG的视频素材索引环节，可引入中间层表征对比对齐方案，无需修改推理逻辑就能提升时序感知能力，降低跨模态检索错配率

  - 直播互动Agent的实时音视频理解模块，可借鉴该轻量对齐方法，在不增加推理开销的前提下提升话术与画面的匹配判断精度'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有全模态模型视听时序对应能力薄弱，易将语音提示与错误视觉场景关联，输出看似合理但基于错误音视配对的结果，现有优化方案普遍需要额外标注、改动推理逻辑。

### 方法关键点
提出轻量Synchrony-Guided Representation Alignment（SyncRA）方法：对单视频内的中间层视听表征做对比学习，对齐同时刻跨模态表征、分离错配时刻表征，捕获全局上下文下的局部时序对应关系；监督信号直接取自输入自带的时序信息，无需额外标注，推理流程完全无改动。

### 关键结果
在4种不同架构、不同规模的开源全模态模型、5个公开视频基准上测试，所有模型-基准组合表现均优于仅答案微调方案，受控测试中视听配对跟踪能力实现大幅提升。
