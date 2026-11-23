---
title: 'DiTraR: Diverse Scorers and Transcript-Guided Re-ranking for Video Corpus
  Moment Retrieval'
title_zh: DiTraR：融合多打分器与字幕引导重排的视频语料片段检索
authors:
- Mohammad Alijanpour Shalmani
- Alale Rezvani Boroujeni
- Ali Amini
affiliations:
- University of Central Florida
- Kaunas University of Technology
arxiv_id: '2611.27931'
url: https://arxiv.org/abs/2611.27931
pdf_url: https://arxiv.org/pdf/2611.27931
published: '2026-11-20'
collected: '2026-11-23'
category: Multimodal
direction: 多模态检索 · 视频片段定位重排
tags:
- Cross-Modal Retrieval
- Model Ensemble
- Re-ranking
- LLM
- Video Retrieval
one_liner: 提出多独立打分器集成与字幕验证重排的VCMR框架，显著提升跨模态视频片段检索精度
practical_value: '- 多独立打分器能量平均集成的思路可迁移到推荐/搜索排序阶段，无需重新训练基线即可提升泛化效果

  - 冻结大模型做文本侧（商品介绍/评论/字幕等）验证重排的方案，可低成本引入电商多模态搜索场景

  - 先做错误归因定位核心问题的思路可复用在业务优化链路，避免无效迭代边缘问题'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
视频语料片段检索（VCMR）任务中，现有强基线的Top排序错误主要来自选错视频，而非片段边界定位不准，仅重加权已有特征无法解决该问题。
### 方法关键点
1. 设计witness-interval打分器，将query拆分为探针逐候选片段精准打分；
2. 采用多独立训练打分器的能量平均集成，在全量检索前融合结果；
3. 引入冻结大模型作为字幕验证器，读取高排名视频的时间戳对话内容做重排，不调整片段边界。
### 关键结果
在TVR验证集上，IoU=0.5时R@1达24.36，IoU=0.7时R@1达13.55；集成方案优化视觉类query效果，验证器优化对话类query效果，二者收益可叠加。
