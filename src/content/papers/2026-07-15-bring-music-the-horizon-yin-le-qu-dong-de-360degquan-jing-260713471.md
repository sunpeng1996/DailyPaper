---
title: 'Bring Music The Horizon: Music-Driven 360$^\circ$ Video Generation'
title_zh: Bring Music The Horizon：音乐驱动的360°全景视频生成框架
authors:
- Kai Hsu Tsai
- Yong Wei Fu
- Hung I Yang
- Yu-Chih Chen
affiliations:
- Department of Computer Science, National Yang Ming Chiao Tung University
arxiv_id: '2607.13471'
url: https://arxiv.org/abs/2607.13471
pdf_url: https://arxiv.org/pdf/2607.13471
published: '2026-07-15'
collected: '2026-07-18'
category: Multimodal
direction: 多模态生成 · 音频转360°全景视频
tags:
- Music Visualization
- 360° Video Generation
- Multimodal Generation
- Music Emotion Recognition
one_liner: 提出情绪感知的音乐驱动360°全景视频生成pipeline，适配无歌词器乐类音乐
practical_value: '- 可复用「按固定时间粒度拆分提取音频情绪轨迹」的方法，用于电商音乐类商品配套短视频自动生成，提升内容沉浸感

  - 情绪向量转视觉引导的思路可迁移到直播背景自动生成场景，根据直播BGM情绪动态切换360°全景背景

  - 关键帧生成+图生视频的多阶段生成pipeline可借鉴到商品短视频批量生产流程，提升生成内容语义可控性'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有音乐可视化方法要么重度依赖歌词，无法适配纯器乐类内容，要么生成平面非沉浸视频，难以传递音乐的连续情绪动态，也无法提供沉浸式视听体验。

### 方法关键点
1. 以每4小节为粒度预测音乐的valence-arousal值，生成连续的音乐情绪轨迹；
2. 通过EmotiCrafter将情绪值转换为情绪感知视觉引导向量，再通过SEGA框架实现关键帧生成的细粒度语义控制；
3. 基于生成的关键帧调用图生视频模型，生成时间连续的360°全景视频。

### 关键结果
可兼容不同曲风音乐，生成匹配音乐情绪递进与时序结构的360°音乐可视化视频，定性效果优于基线方法From-Sound-To-Sight，支持无歌词器乐类内容的可视化生成。
