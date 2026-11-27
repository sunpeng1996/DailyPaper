---
title: 'DiaCap: Jointly Learning Who Speaks When for Audiovisual Dialogue Captioning'
title_zh: DiaCap：联合学习说话人与时序的音视频对话字幕生成模型
authors:
- Binfei Ji
- Zhiwen Cao
- Anqi Yang
- Prem Seetharaman
- Shuo Yang
- Ratheesh Kalarot
- Yingyan Celine Lin
- Mingze Xu
affiliations:
- Georgia Tech
- Adobe Research
arxiv_id: '2611.33153'
url: https://arxiv.org/abs/2611.33153
pdf_url: https://arxiv.org/pdf/2611.33153
published: '2026-11-24'
collected: '2026-11-27'
category: Multimodal
direction: 多模态LLM · 音视频对话字幕生成
tags:
- Multimodal-LLM
- Audio-Visual
- Captioning
- Reinforcement-Learning
- Speaker-Diarization
one_liner: 提出两阶段训练的音视频LLM DiaCap，统一生成对话字幕、说话人描述及精准时间戳
practical_value: '- 两阶段训练范式可直接复用：第一阶段用大规模弱/合成标注数据预训练打底，第二阶段用小批量人工标注数据RL精调，大幅降低多模态任务的标注成本

  - 强耦合子任务统一建模思路可迁移到电商直播场景：同时实现直播话术转录、说话人（主播/助理/嘉宾）识别、话术时序对齐，避免多模型级联的累积误差

  - 细粒度反馈RL优化方法可借鉴：针对核心业务指标（如时序准度、实体匹配度）直接设计reward，无需全量端到端标注即可显著提升目标指标表现'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有音视频对话字幕方案无法同时精准定位说话人身份与说话时序，多模型级联误差大，通用多模态LLM时序准度表现糟糕。

### 方法关键点
将对话转录、时间戳生成、说话人视觉描述三个强耦合任务统一到单个音视频LLM中，采用两阶段训练范式：
1. 预训练阶段：用225K带合成标注的视频剪辑训练，覆盖每轮utterance的密集细粒度标注
2. 精调阶段：用2.9K人工校正剪辑做强化学习精调，reward直接对齐时序准度、说话人分组、说话人匹配三个核心目标

### 关键结果数字
在扩展utterance级时间戳、字幕脱敏的DiaDemBench上，DiaCap音视频说话人分割效果与Gemini 4 Argon持平，时序准度远超后者（76.59 vs 42.76 TIME指标），同时在多语言、分钟级长视频上效果稳定，可直接迁移到音视频问答任务。
