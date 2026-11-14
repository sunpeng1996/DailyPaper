---
title: 'K2V: Generative Keyframing For Physically Plausible Video Generation'
title_zh: K2V：面向物理可信视频生成的生成式关键帧方法
authors:
- Felix O'Mahony
- Daniel Olmeda Reino
- Roberto Cipolla
- Ayush Tewari
affiliations:
- University of Cambridge, UK
- Toyota Motor Europe, Belgium
arxiv_id: '2611.17324'
url: https://arxiv.org/abs/2611.17324
pdf_url: https://arxiv.org/pdf/2611.17324
published: '2026-11-12'
collected: '2026-11-14'
category: Multimodal
direction: 物理可信视频生成 · 关键帧引导生成
tags:
- Video Diffusion
- LLM
- Keyframe Generation
- Physical Plausibility
- Multimodal Generation
one_liner: 用LLM驱动的关键帧生成模块分担物理推理任务，大幅提升视频生成的物理合理性
practical_value: '- 任务拆分思路可迁移到电商营销视频生成：先用LLM规划产品展示的核心关键帧（如外观、功能、场景节点），再用视频模型补全过渡，避免产品变形、场景穿帮等物理错误，提升生成内容质量

  - 「关键节点锚定+中间插值填充」的生成范式可复用至文案生成、推荐理由生成等场景：先规划核心卖点/逻辑节点，再补全流畅内容，降低生成模型的逻辑推理压力，提升输出一致性

  - 对需高可控性的生成场景（如直播切片、种草短视频生成），可采用关键帧锚定方法，保证核心信息不偏离业务要求'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视频diffusion模型可生成高画质、高纹理质量的内容，但输出普遍存在严重物理逻辑错误，核心原因是所有物理推理任务都需要在diffusion过程中同步完成，任务难度过高。
### 方法关键点
1. 拆分物理推理职责，交由LLM驱动的关键帧生成模块完成，通过自然语言做显式物理逻辑推理，输出视频关键时间节点的物理合规关键帧；
2. 下游视频diffusion模型仅需要基于关键帧做中间帧插值补全，无需从头推理完整视频序列，大幅降低diffusion模型的任务负担。
### 关键结果
在Physics-IQ Verified、PhyGenBench两个物理合理性基准上达到SOTA，性能显著优于Wan2.2、CogVideoX、Hunyuan Video 1.5等主流视频生成模型。
