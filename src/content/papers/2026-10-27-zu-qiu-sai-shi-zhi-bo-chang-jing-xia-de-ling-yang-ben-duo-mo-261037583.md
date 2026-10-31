---
title: Zero-Shot Multimodal Event Spotting in Soccer Broadcasts
title_zh: 足球赛事直播场景下的零样本多模态事件识别与定位
authors:
- Sadia Kamal
- Mahmudul Hasan
- Tony Braskich
affiliations:
- University of Maryland Baltimore County
- Comcast Applied AI
- Comcast
arxiv_id: '2610.37583'
url: https://arxiv.org/abs/2610.37583
pdf_url: https://arxiv.org/pdf/2610.37583
published: '2026-10-27'
collected: '2026-10-31'
category: Multimodal
direction: 多模态大模型 · 零样本时序事件定位
tags:
- Zero-Shot Learning
- Multimodal LLM
- Event Spotting
- Temporal Localization
- Video Understanding
one_liner: 无需领域标注训练，结合赛事分镜与解说实现足球直播事件零样本检测与时序定位
practical_value: '- 长视频时序定位场景可复用「重叠分段+关键帧分镜压缩」方案，大幅降低多模态模型推理成本，适合电商直播高光切片、商品片段识别等落地场景

  - 垂类内容理解任务可复用「视觉压缩表示+对齐文本联合输入通用MLLM」的零样本架构，无需领域标注即可快速上线

  - 内容排序环节可借鉴证据链支撑的评分逻辑，给输出结果附自然语言解释，提升直播内容推荐、高光推送的可解释性'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有足球赛事事件定位方法高度依赖领域标注数据集与专项模型训练，泛化能力弱、落地成本高，难以快速适配无标注的垂类直播场景。
### 方法关键点
1. 将整场赛事切分为重叠片段，每个片段输出紧凑视觉分镜+对齐的解说转录文本，输入通用多模态模型联合处理，无需任务专项参数训练；
2. 新增证据支撑的兴奋度打分阶段，对检测到的事件排序同时输出自然语言解释，可直接支撑高光片段筛选。
### 关键结果
在3场手动标注共130个事件的测试集上，最优配置F1@5s达72.0%，跨数据集效果优于SoccerNet训练的CALF、NetVLAD++；分镜表示相比单帧输入推理成本降低72%。
