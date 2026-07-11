---
title: 'VEGAS: Human-Aligned Video Caption Evaluation via Gaze'
title_zh: VEGAS：基于眼动信号的人类对齐视频字幕评估方法
authors:
- Shenghui Chen
- Po-han Li
- Ximeng Sun
- Shijia Yang
- Emad Barsoum
- Zicheng Liu
- Sandeep Chinchali
- Ufuk Topcu
affiliations:
- The University of Texas at Austin
- AMD
arxiv_id: '2607.08489'
url: https://arxiv.org/abs/2607.08489
pdf_url: https://arxiv.org/pdf/2607.08489
published: '2026-07-09'
collected: '2026-07-11'
category: Multimodal
direction: 多模态内容评估 · 眼动对齐
tags:
- Video Captioning
- Gaze Alignment
- Training-free Metric
- Cross-modal
- Multimodal Evaluation
one_liner: 提出无需训练的眼动驱动视频字幕评估指标VEGAS，实现个性化注意力对齐的字幕筛选
practical_value: '- 内容推荐场景可复用「无需重训模型、仅在测试时用用户注意力信号做生成结果后筛选」的思路，用点击、停留等隐式注意力替代眼动信号，即可低成本提升内容个性化匹配度

  - 短视频/直播带货的自动字幕生成、商品解说文案匹配场景，可引入用户注意力信号设计对齐指标，筛选更符合用户当前关注重点的文案，提升转化

  - 跨模态商品检索业务可借鉴该思路，用用户交互产生的注意力信号修正索引文本权重，降低无关内容干扰，提升检索召回准确率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：现有视觉语言模型生成的视频字幕通常为全局语义正确的通用内容，未考虑不同用户的个性化注意力差异，在内容匹配、跨模态检索等下游任务中易出现匹配度不足的问题。
**方法关键点**：1. 训练无关的跨模态信息论指标VEGAS，利用测试阶段采集的用户眼动数据，量化候选字幕与用户注意力焦点的匹配程度；2. 基于拒绝采样策略，直接用VEGAS打分筛选最优字幕，无需微调基础视觉语言模型；3. 构建同步标注眼动数据、参考标注的第一人称活动、教学幻灯片双数据集用于验证。
**关键结果**：VEGAS筛选的字幕与人类注意力的对齐度显著优于基线，下游字幕到视频检索任务效果获得明确提升，验证了推理阶段引入用户注意力信号的实用价值。
