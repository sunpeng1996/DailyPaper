---
title: 'The Missing Temporal Link: Temporal Context Routing for Script-Driven Audio-Video
  Generation'
title_zh: 面向脚本驱动音视频生成的时间上下文路由方法
authors:
- Yichen Liu
- Quanwei Zhang
- Haozhe Wang
- Donghao Zhou
- Xiaojie Li
- Yang Shi
- Jiaming Liu
- Ruihua Huang
- Yingtian Zou
- Daquan Zhou
affiliations:
- PKU
- Qwen Applications
- HKUST
- CUHK
- SJTU
arxiv_id: '2609.02367'
url: https://arxiv.org/abs/2609.02367
pdf_url: https://arxiv.org/pdf/2609.02367
published: '2026-09-01'
collected: '2026-09-05'
category: Multimodal
direction: 多模态音视频生成 · 时序路由对齐
tags:
- Temporal Alignment
- Multimodal Generation
- Context Routing
- Script-to-Video
- Audio-Video Sync
one_liner: 提出TCR模块对齐脚本时序与音视频生成共享时序轴，大幅提升脚本驱动生成的时序准确度
practical_value: '- 电商广告脚本自动生成视频场景可复用TCR框架，实现脚本指定的镜头切换、台词播报时间精准控制，降低后期剪辑成本

  - 生成式内容推荐场景中，若需按用户行为时序生成多模态内容（如时序化商品展示短视频），可借鉴时序映射路由的思路对齐用户需求时序与生成内容时序

  - Agent辅助内容生产工作流中，可集成TCR模块作为时序控制层，解决多模态生成内容与结构化指令时序不匹配的问题'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有音视频联合生成模型仅能保证音画同步，无法对齐脚本指定的镜头切换、台词播报的精确时序，时序误差会破坏叙事连贯性，限制脚本驱动内容生成的落地。
### 方法关键点
提出Temporal Context Routing (TCR)模块，将结构化脚本中的时序信息映射到音视频生成的共享时间轴上，把每个prompt的引导信号路由到两个模态对应的生成位置，将时序对齐范围从音视频之间拓展到包含结构化脚本。
### 关键结果
在200条测试脚本上对比基线，Shot Boundary MAE降低96%（从1.11s降至0.042s），Dialogue Acc@0.5s从28.3%提升至84.1%，同时保留与基线相当的视觉质量与音画同步效果，用户调研5个维度均更受偏好。
