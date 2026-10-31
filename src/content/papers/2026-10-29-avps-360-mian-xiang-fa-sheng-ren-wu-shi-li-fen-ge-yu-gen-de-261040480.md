---
title: 'AVPS-360: A Spatial Audio-Visual Benchmark for Instance Segmentation and Tracking
  of Sound-Producing Persons'
title_zh: AVPS-360：面向发声人物实例分割与跟踪的空间视听基准
authors:
- Yifu Sun
- Parthasaarathy Sudarsanam
- Tuomas Virtanen
- Archontis Politis
affiliations:
- Audio Research Group, Tampere University
arxiv_id: '2610.40480'
url: https://arxiv.org/abs/2610.40480
pdf_url: https://arxiv.org/pdf/2610.40480
published: '2026-10-29'
collected: '2026-10-31'
category: Multimodal
direction: 多模态视听 · 实例分割跟踪基准
tags:
- Multimodal Learning
- Audio-Visual Segmentation
- Benchmark Dataset
- Instance Tracking
- Spatial Audio
one_liner: 发布含10.5小时空间音频+360°视频的发声人物分割跟踪基准及性能更优的基线模型
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视听实例分割（AVIS）基准普遍采用单声道音频，缺乏通道间空间线索区分并发声源，也无全景视觉上下文支撑广域场景的声源定位跟踪。
### 方法关键点
1. 基于STARSS23构建AVPS-360基准，匹配一阶Ambisonics空间音频与同步360°视频，覆盖230条共10.5小时真实录制内容，单条平均时长164秒；
2. 提供31678条人工校验的实例掩码，关联声源身份与声事件标签（含语音、笑声、鼓掌、脚步声等间歇发声场景）；
3. 提出融合空间音频与视觉特征的基线模型，支持帧级分割与跨帧身份关联。
### 关键结果
现有AVIS方法在长时录制、声源间歇发声场景下的检测与身份关联表现较差，所提基线在两类任务上均实现显著性能提升。
