---
title: 'EgoCARBS: Egocentric Video Meets Active Acoustics for Kitchen Action Understanding'
title_zh: EgoCARBS：第一人称视觉结合主动声学的厨房行为理解
authors:
- Saif Mahmud
- Vineet Parikh
- Bharath Hariharan
- Cheng Zhang
affiliations:
- Cornell University
- Amazon
arxiv_id: '2611.33565'
url: https://arxiv.org/abs/2611.33565
pdf_url: https://arxiv.org/pdf/2611.33565
published: '2026-11-25'
collected: '2026-11-27'
category: Multimodal
direction: 多模态行为理解 · 主动声学传感
tags:
- Multimodal Dataset
- Egocentric Video
- Active Acoustics
- Action Recognition
- Wearable Sensing
one_liner: 发布配对第一人称视频与主动声学的厨房行为数据集，验证声学对视觉盲区的补全效果
practical_value: '- 开发家用场景智能Agent（如烹饪助手、厨房导购）时，可引入智能手表主动声学信号补全第一人称视觉盲区，无需额外部署摄像头降低落地成本

  - 跨模态融合任务中优先选择对用户分布变化鲁棒的模态：主动声学相比外置摄像头对新用户泛化性更好，可提升跨用户场景效果

  - 行为识别任务遇到样本分布偏移（如新用户、视觉遮挡）时，补充低环境依赖的传感模态可快速提升效果'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
第一人称视频常出现手部出框、肢体动作丢失问题，外置中心摄像头需预先部署适配场景成本高，主动声学可通过穿戴设备补全动作信息，但此前无公开配对第一人称视频与主动声学的标注数据集。
### 方法关键点
1. 构建EgoCARBS多模态基准数据集：招募15名参与者在自有厨房完成无脚本烹饪，同步采集眼镜端第一人称视频、眼镜+智能手表主动声学信号、手表IMU与音频、外置摄像头视频，标注4019个动词-名词动作对，总时长11.4小时
2. 量化对比不同模态组合对厨房动作识别任务的增益
### 关键结果
动词识别任务上，穿戴设备信号增益与外置摄像头相当；新用户场景下增益比外置摄像头高20%+，其中80%以上增益来自主动声学，尤其在视觉无法捕捉手部时效果提升最显著
