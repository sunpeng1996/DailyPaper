---
title: 'SPDMX: Large-Scale Open Stem Audio From Symbolic Music'
title_zh: SPDMX：基于符号音乐的大规模开源分轨音频数据集
authors:
- Phillip Long
- Eduardo Escoto
- Julian McAuley
- Zachary Novack
affiliations:
- University of California, San Diego Computer Science and Engineering Department
arxiv_id: '2611.09140'
url: https://arxiv.org/abs/2611.09140
pdf_url: https://arxiv.org/pdf/2611.09140
published: '2026-11-06'
collected: '2026-11-12'
category: Other
direction: 音乐多模态数据集构建与开放
tags:
- Audio Dataset
- Music Processing
- Multimodal
- Open Source
- Synthetic Data
one_liner: 构建目前已知规模最大的开源许可合成多轨音乐分轨数据集，配套开放渲染管线
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有音乐数据集受版权限制无法公开分发，且多数仅提供混合音频而非独立分轨；已有的多轨资源无法同时兼顾真实度、规模、开源许可要求，合成方案要么依赖专有VST工具，要么原生渲染的分轨质量较差。
### 方法关键点
基于公共领域PDMX乐谱，采用听觉引导的渲染管线，生成带对齐乐谱的开源分轨语料，同时开放全套渲染流程、元数据。
### 关键结果数字
- 数据集包含253982首歌曲、490159条单声道分轨，总时长5469小时，采样率44.1kHz，采用CC BY 4.0开源协议
- 34.8%共88403首歌曲提供多轨监督，是目前已知按时长统计规模最大的开源许可合成多轨子集
- 可支撑音源分离、分轨条件生成、MIDI转音频、符号-音频联合建模等多类音乐AI任务
