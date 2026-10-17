---
title: 'EVA-Cap: Optimizing Audiovisual Video Captioning via Event-Centric Alignment'
title_zh: EVA-Cap：基于事件中心对齐的音视频字幕生成优化
authors:
- Jiapeng Shi
- Qiuxia Hou
- Jiaqi Leng
- Junke Wang
- Yanhao Zhang
- Haonan Lu
- Ziyi Ye
- Zuxuan Wu
affiliations:
- Fudan University
- OPPO AI Center, OPPO Inc.
arxiv_id: '2610.22186'
url: https://arxiv.org/abs/2610.22186
pdf_url: https://arxiv.org/pdf/2610.22186
published: '2026-10-15'
collected: '2026-10-17'
category: Multimodal
direction: 多模态音视频理解 · 事件对齐字幕生成
tags:
- VideoCaptioning
- MultimodalAlignment
- GRPO
- SFT
- OmniLanguageModel
- EventExtraction
one_liner: 提出事件中心对齐的音视频字幕框架EVA-Cap，在多类基准上获得显著效果提升
practical_value: '- 电商短视频/直播的自动字幕生成、内容语义打标场景可复用事件拆分解构思路，将非结构化字幕监督转化为结构化事件对齐目标，提升打标准确率

  - 多模态内容召回/搜索场景可借鉴GRPO结合三个事件维度的优化目标，强化跨模态语义对齐效果，降低视频内容理解的事实错误

  - 构建自有多模态训练数据集时可参考事件中心的质量控制流程，减少低质标注对模型效果的影响'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有基于Omni Language Models(OLM)的音视频字幕生成方法将任务视为非结构化文本生成，忽略视频固有语义结构，导致细粒度音视频对齐效果欠佳。

### 方法关键点
1. 提出EVA-Cap框架，将字幕拆解为原子音视频事件，把非结构化文本监督转化为事件中心的对齐任务；
2. 基于自建的经过事件中心质量控制的EVA-Data数据集，先后通过Supervised Fine-Tuning(SFT)和Group Relative Policy Optimization(GRPO)训练，GRPO阶段针对全局事件完整性、事件内属性归因、事件间同步性三个目标专项优化。

### 关键结果
事件中心评估基准ChronusAV上平均增益达9.0%，通用音视频字幕基准WorldSense上提升3.3%，效果显著优于现有方法。
