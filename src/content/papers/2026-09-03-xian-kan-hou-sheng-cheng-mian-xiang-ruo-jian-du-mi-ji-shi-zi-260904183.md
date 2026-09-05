---
title: 'Seeing Before Synthesizing: VLM-Guided Transition Event Discovery for Weakly-Supervised
  Dense Video Captioning'
title_zh: 先看后生成：面向弱监督密集视频字幕的VLM引导过渡事件发现
authors:
- Ye-Chan Kim
- Seunghee Choi
- SeungJu Cha
- Si-Woo Kim
- Hwiseon Kim
- Hyungee Kim
- Dong-Jin Kim
affiliations:
- Hanyang University, South Korea
arxiv_id: '2609.04183'
url: https://arxiv.org/abs/2609.04183
pdf_url: https://arxiv.org/pdf/2609.04183
published: '2026-09-03'
collected: '2026-09-05'
category: Multimodal
direction: 多模态 · 弱监督视频字幕生成
tags:
- VLM
- Weakly Supervised Learning
- Dense Video Captioning
- Vision-Language Alignment
- Temporal Localization
one_liner: 用VLM检测视频帧语义变化，自适应生成有视觉依据的过渡字幕，提升弱监督密集视频字幕性能
practical_value: '- 电商短视频自动打标签场景可复用VLM帧级语义变化检测逻辑，自动定位片段过渡点，降低人工标注成本

  - 生成多模态辅助标注时，可参考「先做视觉语义校验再生成文本」的范式，避免LLM生成文本无视觉支撑的幻觉问题

  - 时序事件定位任务可借鉴「融合时间中点与语义变化点、最大化跨模态对齐选最优宽度」的mask优化方法，提升时序边界准确率'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
弱监督密集视频字幕（WSDVC）仅需视频对应有序事件级字幕即可训练，可大幅降低标注成本，但现有方法通过LLM生成的过渡辅助字幕无视觉grounding，还会刚性分配给所有事件间隙，存在幻觉、冗余问题，效果受限。
### 方法关键点
1. 提出SBS框架，先调用VLM生成事件间隙的帧级叙事，通过跨帧语义差异识别有效过渡点，仅对真实过渡生成辅助字幕，避免冗余与幻觉；
2. 融合时间中点与语义变化点优化过渡段时序mask，选择最大化vision-language alignment的宽度作为最终过渡区间。
### 关键结果
在ActivityNet Captions、YouCook2两个公开基准数据集上，字幕生成与时序定位指标均达到SOTA。
