---
title: Evaluating Visual Realism of AI-Generated Videos with Eye Tracking
title_zh: 利用眼动追踪评估AI生成视频的视觉真实感
authors:
- Danqing Shi
- Lan Jiang
- Jake Lyons
- Miri Zilka
affiliations:
- Lund University
- University of Cambridge
arxiv_id: '2610.38825'
url: https://arxiv.org/abs/2610.38825
pdf_url: https://arxiv.org/pdf/2610.38825
published: '2026-10-28'
collected: '2026-11-01'
category: Eval
direction: 生成式内容评估 · 眼动追踪
tags:
- Eye Tracking
- AIGC Evaluation
- Human Feedback
- Video Generation
- Gaze Pattern
one_liner: 提出眼动追踪作为AI生成视频评估补充信号，构建GazeEval实现71.3%视觉真实感预测准确率
practical_value: '- 电商广告/商品短视频的生成效果评估可引入眼动追踪作为显式用户评分的补充信号，解决用户打分随意、反馈粒度粗的问题

  - 生成式内容质量评估pipeline可复用「两次观看+眼动数据建模」的范式，提升对AI生成素材真实感、吸引力的评估准确率

  - 可将用户在直播间、商品详情页的注视行为数据作为隐式反馈，补充现有点击、转化信号，优化内容排序策略'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有AI生成视频评估依赖显式人类反馈（如评分、判断），仅能捕获用户最终结论，无法支撑感知到决策的过程归因，缺乏细粒度隐式评估信号。

### 方法关键点
1. 开展两轮Visual Turing Test（VTT）实验，招募90名参与者观看438条SOTA模型生成的视频，每条视频观看2次后提交反馈，累计收集4286条有效眼动追踪trial；
2. 验证注视模式与显式反馈的一致性，提出首个基于眼动数据预测视觉真实感的计算方法GazeEval。

### 关键结果
GazeEval的视觉真实感预测准确率达71.3%，证明眼动数据包含有效用户评估信号，相关数据集已开源供后续研究使用。
